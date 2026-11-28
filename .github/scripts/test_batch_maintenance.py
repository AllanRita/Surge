#!/usr/bin/env python3
"""Offline self-tests for Surge batch maintenance, cached-source merge and rollback backups."""
import importlib.util
import json
import sys
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

BASE = Path(__file__).resolve().parent

def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, BASE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

MERGE = load_module("merge_cached_sources", "merge_cached_sources.py")
MAINTAIN = load_module("batch_maintain", "batch_maintain.py")
PREFLIGHT = load_module("batch_preflight", "batch_preflight.py")
FORMAT = load_module("audit_format_parity", "audit_format_parity.py")
APP_AUDIT = load_module("audit_app_completeness", "audit_app_completeness.py")
VERIFY = load_module("verify_batch_integrity", "verify_batch_integrity.py")

class SurgeMaintenanceTests(unittest.TestCase):
    def test_domain_suffix_semantic_coverage(self):
        parent = [MERGE.parse_rule("DOMAIN-SUFFIX,example.com")]
        self.assertTrue(MERGE.is_covered(MERGE.parse_rule("DOMAIN,api.example.com"), parent))
        self.assertTrue(MERGE.is_covered(MERGE.parse_rule("DOMAIN-SUFFIX,sub.example.com"), parent))
        self.assertFalse(MERGE.is_covered(MERGE.parse_rule("DOMAIN-SUFFIX,example.com"), [MERGE.parse_rule("DOMAIN,example.com")]))

    def test_ip_network_containment_respects_no_resolve(self):
        broader = [MERGE.parse_rule("IP-CIDR,10.0.0.0/8,no-resolve")]
        different_mode = [MERGE.parse_rule("IP-CIDR,10.0.0.0/8")]
        self.assertTrue(MERGE.is_covered(MERGE.parse_rule("IP-CIDR,10.1.0.0/16,no-resolve"), broader))
        self.assertFalse(MERGE.is_covered(MERGE.parse_rule("IP-CIDR,10.1.0.0/16,no-resolve"), different_mode))
        self.assertFalse(MERGE.is_covered(MERGE.parse_rule("IP-CIDR6,2001:db8::/32,no-resolve"), broader))

    def test_resolve_format_adaptation(self):
        standard = MERGE.adapt_for_target("IP-CIDR,192.0.2.0/24", "Example/Example.list", "IP-CIDR,198.51.100.0/24,no-resolve\n")
        resolve = MERGE.adapt_for_target("IP-CIDR,192.0.2.0/24,no-resolve", "Example/Example_Resolve.list", "IP-CIDR,198.51.100.0/24\n")
        self.assertEqual(standard, "IP-CIDR,192.0.2.0/24,no-resolve")
        self.assertEqual(resolve, "IP-CIDR,192.0.2.0/24")

    def test_cached_merge_is_idempotent_and_creates_backup(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "Rule" / "Upstream"
            personal = Path(td) / "Rule" / "Personal"
            manifest = Path(td) / ".github" / "explicit-rule-exclusions.json"
            out = Path(td) / "out"
            backup = Path(td) / "backup"
            personal.mkdir(parents=True)
            (personal / "private.list").write_text("DOMAIN,personal.example\n", encoding="utf-8")
            manifest.parent.mkdir(parents=True)
            manifest.write_text(json.dumps({"exclusions": []}), encoding="utf-8")
            for targets in MERGE.SOURCES.values():
                for rel in targets:
                    p = root / rel
                    p.parent.mkdir(parents=True, exist_ok=True)
                    if not p.exists():
                        p.write_text("# NAME: test\n", encoding="utf-8")
            for source_file in MERGE.SOURCES:
                p = root / "SourceMetadata" / source_file
                p.parent.mkdir(parents=True, exist_ok=True)
                rules = ["DOMAIN,unique-cache-test.example"] if source_file == "Aoang-OneDrive.json" else []
                p.write_text(json.dumps({"source": "test-source", "commit": "test-commit", "license": "MIT", "rules": rules}), encoding="utf-8")
            target = root / "OneDrive" / "OneDrive.list"
            original = "# NAME: OneDrive\nDOMAIN-SUFFIX,unrelated.example\n"
            target.write_text(original, encoding="utf-8")
            argv = ["merge_cached_sources.py", "--batch", "1", "--batch-size", "100", "--output-dir", str(out), "--backup-dir", str(backup)]
            with patch.object(MERGE, "ROOT", root), patch.object(MERGE, "PERSONAL", personal), patch.object(MERGE, "MANIFEST", manifest), patch.object(sys, "argv", argv):
                MERGE.main()
            self.assertIn("DOMAIN,unique-cache-test.example", target.read_text(encoding="utf-8"))
            saved = backup / "batch-001" / "OneDrive" / "OneDrive.list"
            self.assertTrue(saved.is_file())
            self.assertEqual(saved.read_text(encoding="utf-8"), original)
            with patch.object(MERGE, "ROOT", root), patch.object(MERGE, "PERSONAL", personal), patch.object(MERGE, "MANIFEST", manifest), patch.object(sys, "argv", argv):
                MERGE.main()
            report = json.loads((out / "batch-001-cached-sources.json").read_text(encoding="utf-8"))
            self.assertEqual(report["summary"]["added"], 0)
            self.assertEqual(target.read_text(encoding="utf-8").count("DOMAIN,unique-cache-test.example"), 1)
            self.assertTrue(report["personal_unchanged"])

    def test_deterministic_cleanup_creates_backup(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "Rule" / "Upstream"
            personal = Path(td) / "Rule" / "Personal"
            manifest = Path(td) / ".github" / "explicit-rule-exclusions.json"
            out = Path(td) / "out"
            backup = Path(td) / "backup"
            folder = root / "TestApp"
            folder.mkdir(parents=True)
            personal.mkdir(parents=True)
            (personal / "private.list").write_text("DOMAIN,personal.example\n", encoding="utf-8")
            manifest.parent.mkdir(parents=True)
            manifest.write_text(json.dumps({"exclusions": []}), encoding="utf-8")
            target = folder / "TestApp.list"
            original = "# NAME: TestApp\nDOMAIN,example.com\nDOMAIN,example.com\n"
            target.write_text(original, encoding="utf-8")
            argv = ["batch_maintain.py", "--batch", "1", "--batch-size", "100", "--output-dir", str(out), "--backup-dir", str(backup)]
            with patch.object(MAINTAIN, "ROOT", root), patch.object(MAINTAIN, "PERSONAL", personal), patch.object(MAINTAIN, "MANIFEST", manifest), patch.object(sys, "argv", argv):
                MAINTAIN.main()
            self.assertEqual(target.read_text(encoding="utf-8").count("DOMAIN,example.com"), 1)
            saved = backup / "batch-001" / "TestApp" / "TestApp.list"
            self.assertTrue(saved.is_file())
            self.assertEqual(saved.read_text(encoding="utf-8"), original)


    def test_format_duplicates_are_scoped_to_app_directory(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            files = [
                root / "CloudCN" / "CloudCN.list",
                root / "CloudCN" / "CloudCN_Resolve.list",
                root / "AmazonCloud" / "AmazonCloud.list",
                root / "AmazonCloud" / "AmazonCloud_Resolve.list",
            ]
            duplicates = PREFLIGHT.duplicate_formats_by_directory(files)
            self.assertEqual(duplicates, [])
            files.extend([
                root / "CloudCN" / "CloudCN_All.list",
                root / "CloudCN" / "CloudCN_Extra_All.list",
            ])
            duplicates = PREFLIGHT.duplicate_formats_by_directory(files)
            self.assertEqual(len(duplicates), 1)
            self.assertEqual(duplicates[0][1], ["all"])

    def test_iana_delegated_tld_is_not_flagged_as_unregistered(self):
        with tempfile.TemporaryDirectory() as td:
            ref = Path(td) / "tlds-alpha-by-domain.txt"
            ref.write_text("# Version 2026112700, Last Updated Fri Nov 27 07:07:01 2026 UTC\nCN\nALIBABA\nALIPAY\nXN--1QQW23A\n", encoding="utf-8")
            tlds, version = PREFLIGHT.load_iana_tlds(str(ref))
            self.assertEqual(version, "Version 2026112700, Last Updated Fri Nov 27 07:07:01 2026 UTC")
            self.assertTrue({"cn", "alibaba", "alipay", "xn--1qqw23a"}.issubset(tlds))
            self.assertNotIn("xihuan", tlds)


    def test_format_parity_ignores_only_no_resolve(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            folder = root / "Example"
            folder.mkdir()
            standard = folder / "Example.list"
            resolve = folder / "Example_Resolve.list"
            standard.write_text("# standard\nDOMAIN,api.example.com\nIP-CIDR,10.0.0.0/8,no-resolve\n", encoding="utf-8")
            resolve.write_text("# resolve\nDOMAIN,api.example.com\nIP-CIDR,10.0.0.0/8\n", encoding="utf-8")
            with patch.object(FORMAT, "ROOT", root):
                result = FORMAT.compare_files(standard, resolve, "Standard vs Resolve")
            self.assertEqual(result["status"], "MATCH")
            self.assertEqual(result["left_only_count"], 0)
            self.assertEqual(result["right_only_count"], 0)
            self.assertEqual(result["resolution_option_difference_count"], 1)

    def test_format_parity_keeps_non_resolution_options_significant(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            folder = root / "Example"
            folder.mkdir()
            standard = folder / "Example.list"
            resolve = folder / "Example_Resolve.list"
            standard.write_text("DOMAIN,api.example.com,policy=Proxy\n", encoding="utf-8")
            resolve.write_text("DOMAIN,api.example.com,policy=Direct\n", encoding="utf-8")
            with patch.object(FORMAT, "ROOT", root):
                result = FORMAT.compare_files(standard, resolve, "Standard vs Resolve")
            self.assertEqual(result["status"], "REVIEW")
            self.assertEqual(result["left_only_count"], 1)
            self.assertEqual(result["right_only_count"], 1)

    def test_format_suffix_classification(self):
        self.assertEqual(FORMAT.classify(Path("App/App_All_No_Resolve.list")), ("App", "all_no_resolve"))
        self.assertEqual(FORMAT.classify(Path("App/App_Resolve.list")), ("App", "resolve"))
        self.assertEqual(FORMAT.classify(Path("App/App.list")), ("App", "standard"))
    def test_no_ipv6_format_only_omits_ipv6_rules(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            folder = root / "Example"
            folder.mkdir()
            standard = folder / "Example.list"
            no_ipv6 = folder / "Example_No_IPv6.list"
            standard.write_text("DOMAIN,api.example.com\nIP-CIDR,10.0.0.0/8\nIP-CIDR6,2001:db8::/32\n", encoding="utf-8")
            no_ipv6.write_text("DOMAIN,api.example.com\nIP-CIDR,10.0.0.0/8\n", encoding="utf-8")
            with patch.object(FORMAT, "ROOT", root):
                result = FORMAT.compare_files(standard, no_ipv6, "Standard vs No_IPv6", ignore_ipv6_left=True)
            self.assertEqual(result["status"], "MATCH")
            self.assertEqual(result["left_only_count"], 0)
            self.assertEqual(result["right_only_count"], 0)

    def test_no_ipv6_pair_does_not_hide_missing_ipv4_rules(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            folder = root / "Example"
            folder.mkdir()
            standard = folder / "Example.list"
            no_ipv6 = folder / "Example_No_IPv6.list"
            standard.write_text("DOMAIN,api.example.com\nIP-CIDR,10.0.0.0/8\nIP-CIDR6,2001:db8::/32\n", encoding="utf-8")
            no_ipv6.write_text("DOMAIN,api.example.com\n", encoding="utf-8")
            with patch.object(FORMAT, "ROOT", root):
                result = FORMAT.compare_files(standard, no_ipv6, "Standard vs No_IPv6", ignore_ipv6_left=True)
            self.assertEqual(result["status"], "REVIEW")
            self.assertEqual(result["left_only_count"], 1)
            self.assertEqual(result["left_only_examples"][0]["rule"], "IP-CIDR,10.0.0.0/8")
    def test_dual_feed_deletes_exact_domain_only_and_preserves_parent_and_blocklist(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root = base / "Rule" / "Upstream"
            personal = base / "Rule" / "Personal"
            manifest = base / ".github" / "explicit-rule-exclusions.json"
            out = base / "out"
            backup = base / "backup"
            threat = root / "ThreatApp"
            block = root / "BlockApp"
            threat.mkdir(parents=True)
            block.mkdir(parents=True)
            personal.mkdir(parents=True)
            manifest.parent.mkdir(parents=True)
            manifest.write_text(json.dumps({"exclusions": []}), encoding="utf-8")
            personal_file = personal / "private.list"
            personal_file.write_text("DOMAIN,private.example\n", encoding="utf-8")
            target = threat / "ThreatApp.list"
            original = "DOMAIN,evil.example\nDOMAIN-SUFFIX,evil.example\nDOMAIN,one-feed.example\n"
            target.write_text(original, encoding="utf-8")
            block_file = block / "BlockApp.list"
            block_file.write_text("DOMAIN,evil.example\n", encoding="utf-8")
            openphish = base / "openphish.txt"
            openphish.write_text("https://evil.example/malware\nhttps://one-feed.example/login\n", encoding="utf-8")
            urlhaus = base / "urlhaus.txt"
            urlhaus.write_text("evil.example CNAME . ; Malware download\n", encoding="utf-8")
            argv = ["batch_maintain.py", "--batch", "1", "--batch-size", "100", "--openphish", str(openphish), "--urlhaus", str(urlhaus), "--output-dir", str(out), "--backup-dir", str(backup)]
            with patch.object(MAINTAIN, "ROOT", root), patch.object(MAINTAIN, "PERSONAL", personal), patch.object(MAINTAIN, "MANIFEST", manifest), patch.object(sys, "argv", argv):
                MAINTAIN.main()
            self.assertNotIn("DOMAIN,evil.example", target.read_text(encoding="utf-8").splitlines())
            self.assertIn("DOMAIN-SUFFIX,evil.example", target.read_text(encoding="utf-8").splitlines())
            self.assertIn("DOMAIN,one-feed.example", target.read_text(encoding="utf-8").splitlines())
            self.assertIn("DOMAIN,evil.example", block_file.read_text(encoding="utf-8").splitlines())
            report = json.loads((out / "batch-001-maintenance.json").read_text(encoding="utf-8"))
            self.assertEqual(report["summary"]["threats_removed"], 1)
            self.assertTrue(report["security_coverage_complete"])
            self.assertTrue(report["personal_unchanged"])
            self.assertEqual(personal_file.read_text(encoding="utf-8"), "DOMAIN,private.example\n")
            self.assertEqual((backup / "batch-001" / "ThreatApp" / "ThreatApp.list").read_text(encoding="utf-8"), original)

    def test_single_feed_match_is_review_only(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root = base / "Rule" / "Upstream"
            personal = base / "Rule" / "Personal"
            manifest = base / ".github" / "explicit-rule-exclusions.json"
            out = base / "out"
            (root / "ThreatApp").mkdir(parents=True)
            personal.mkdir(parents=True)
            manifest.parent.mkdir(parents=True)
            manifest.write_text(json.dumps({"exclusions": []}), encoding="utf-8")
            target = root / "ThreatApp" / "ThreatApp.list"
            target.write_text("DOMAIN,only-one.example\n", encoding="utf-8")
            openphish = base / "openphish.txt"
            openphish.write_text("https://only-one.example/login\n", encoding="utf-8")
            argv = ["batch_maintain.py", "--batch", "1", "--batch-size", "100", "--openphish", str(openphish), "--output-dir", str(out)]
            with patch.object(MAINTAIN, "ROOT", root), patch.object(MAINTAIN, "PERSONAL", personal), patch.object(MAINTAIN, "MANIFEST", manifest), patch.object(sys, "argv", argv):
                MAINTAIN.main()
            self.assertEqual(target.read_text(encoding="utf-8"), "DOMAIN,only-one.example\n")
            report = json.loads((out / "batch-001-maintenance.json").read_text(encoding="utf-8"))
            self.assertEqual(report["summary"].get("threats_removed", 0), 0)
            self.assertFalse(report["security_coverage_complete"])
            self.assertEqual(len(report["review_findings"]), 1)
    def test_app_completeness_matrix_distinguishes_mapped_and_unmapped_sources(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root = base / 'Rule' / 'Upstream'
            source_root = root / 'SourceMetadata'
            source_root.mkdir(parents=True)
            mapped = root / 'Apple'
            unmapped = root / 'UnmappedApp'
            mapped.mkdir()
            unmapped.mkdir()
            (mapped / 'README.md').write_text('Apple scope', encoding='utf-8')
            (mapped / 'Apple.list').write_text('DOMAIN-SUFFIX,apple.com\n||ads.example^\napi.example.com\n', encoding='utf-8')
            (unmapped / 'UnmappedApp.list').write_text('DOMAIN,api.example.com\n', encoding='utf-8')
            (source_root / 'Apple.json').write_text('{}', encoding='utf-8')
            source_map = {'Apple.json': ['Apple/Apple.list']}
            report = APP_AUDIT.inventory(root, source_root, source_map)
            self.assertEqual(report['folder_count'], 2)
            self.assertEqual(report['folders_with_cached_source_mapping'], 1)
            self.assertEqual(report['folders_not_verifiable_from_cached_sources'], 1)
            by_name = {row['folder']: row for row in report['folders']}
            self.assertEqual(by_name['Apple']['author_source_coverage'], 'CACHED_SOURCE_COMPARISON_CONFIGURED')
            self.assertEqual(by_name['UnmappedApp']['author_source_coverage'], 'NOT_VERIFIABLE_FROM_CACHED_SOURCES')
            self.assertTrue(by_name['Apple']['readme_present'])
            self.assertEqual(report['rule_entry_count'], 4)
            self.assertEqual(report['surge_rule_entry_count'], 2)
            self.assertEqual(report['native_filter_entry_count'], 1)
            self.assertEqual(report['native_domain_entry_count'], 1)
    def test_urlhaus_hostfile_accepts_domain_first_and_ip_prefixed_rows(self):
        with tempfile.TemporaryDirectory() as td:
            feed = Path(td) / "urlhaus.txt"
            feed.write_text(
                "evil.example CNAME . ; malware download\n"
                "127.0.0.1 prefixed.example\n"
                "https://url.example/path\n",
                encoding="utf-8"
            )
            self.assertEqual(MAINTAIN.feed_hosts(str(feed)), {"evil.example", "prefixed.example", "url.example"})

    def test_parent_suffix_single_feed_hits_are_review_only_for_domain_and_host_suffix(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            root = base / "Rule" / "Upstream"
            personal = base / "Rule" / "Personal"
            manifest = base / ".github" / "explicit-rule-exclusions.json"
            out = base / "out"
            folder = root / "ThreatApp"
            folder.mkdir(parents=True)
            personal.mkdir(parents=True)
            manifest.parent.mkdir(parents=True)
            manifest.write_text(json.dumps({"exclusions": []}), encoding="utf-8")
            target = folder / "ThreatApp.list"
            original = "DOMAIN-SUFFIX,shared.example\nHOST-SUFFIX,shared.example\n"
            target.write_text(original, encoding="utf-8")
            openphish = base / "openphish.txt"
            openphish.write_text("https://tenant.shared.example/path\n", encoding="utf-8")
            argv = ["batch_maintain.py", "--batch", "1", "--batch-size", "100", "--openphish", str(openphish), "--output-dir", str(out)]
            with patch.object(MAINTAIN, "ROOT", root), patch.object(MAINTAIN, "PERSONAL", personal), patch.object(MAINTAIN, "MANIFEST", manifest), patch.object(sys, "argv", argv):
                MAINTAIN.main()
            self.assertEqual(target.read_text(encoding="utf-8"), original)
            report = json.loads((out / "batch-001-maintenance.json").read_text(encoding="utf-8"))
            self.assertEqual(report["summary"].get("threats_removed", 0), 0)
            self.assertEqual(len(report["review_findings"]), 2)
            self.assertEqual({x["rule"] for x in report["review_findings"]}, {"DOMAIN-SUFFIX,shared.example", "HOST-SUFFIX,shared.example"})

    def test_block_filter_paths_are_excluded_from_threat_deletion(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            with patch.object(MAINTAIN, "ROOT", root):
                for rel in (
                    "Block/DNS/DNS.list",
                    "Advertising/Advertising.list",
                    "AdvertisingTest/AdvertisingTest.list",
                    "Privacy/Privacy.list",
                    "EasyPrivacy/EasyPrivacy.list",
                    "AdGuardSDNSFilter/AdGuardSDNSFilter_All.list",
                    "Hijacking/Hijacking.list",
                ):
                    self.assertTrue(MAINTAIN.is_blocklist_path(root / rel), rel)
                self.assertFalse(MAINTAIN.is_blocklist_path(root / "Apple/Apple.list"))

    def test_prechange_backup_is_preserved_across_multiple_stages(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            source = base / "App.list"
            backup = base / "backups" / "batch-001" / "App.list"
            source.write_bytes(b"original before any maintenance")
            MAINTAIN.write_backup_once(backup, source)
            source.write_bytes(b"after deterministic cleanup")
            MERGE.write_backup_once(backup, source)
            self.assertEqual(backup.read_bytes(), b"original before any maintenance")

    def test_batch_integrity_rejects_out_of_batch_and_file_deletion(self):
        self.assertTrue(VERIFY.validate_change_records([("M", "Rule/Upstream/Apple/Apple.list")], {"Apple"}))
        with self.assertRaises(ValueError):
            VERIFY.validate_change_records([("M", "Rule/Upstream/Microsoft/Microsoft.list")], {"Apple"})
        with self.assertRaises(ValueError):
            VERIFY.validate_change_records([("D", "Rule/Upstream/Apple/Apple.list")], {"Apple"})


    def test_batch_integrity_verifies_backup_and_git_rollback_in_isolated_repo(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            subprocess.run(["git", "init", "-q"], cwd=base, check=True)
            subprocess.run(["git", "config", "user.name", "Surge Test"], cwd=base, check=True)
            subprocess.run(["git", "config", "user.email", "surge-test@example.invalid"], cwd=base, check=True)
            target = base / "Rule" / "Upstream" / "Apple" / "Apple.list"
            target.parent.mkdir(parents=True)
            target.write_text("DOMAIN,original.example\\n", encoding="utf-8")
            subprocess.run(["git", "add", "Rule/Upstream/Apple/Apple.list"], cwd=base, check=True)
            subprocess.run(["git", "commit", "-qm", "fixture baseline"], cwd=base, check=True)

            out = base / "batch-output"
            backup_root = out / "backups"
            backup = backup_root / "batch-001" / "Apple" / "Apple.list"
            backup.parent.mkdir(parents=True)
            backup.write_text("DOMAIN,original.example\\n", encoding="utf-8")
            target.write_text("DOMAIN,repaired.example\\n", encoding="utf-8")

            selected = ["Apple"]
            preflight = {"batch": 1, "batch_size": 100, "selected_folders": selected,
                         "selected_folder_count": 1, "total_eligible_top_level_folders": 1,
                         "summary": {"blockers": 0}, "personal_tree_unchanged": True}
            maintenance = {"batch": 1, "batch_size": 100, "selected_folders": selected,
                           "personal_unchanged": True}
            cached = {"batch": 1, "batch_size": 100, "selected_folders": selected,
                      "personal_unchanged": True, "cached_sources_expected": 15,
                      "cached_sources_processed": 15}
            out.mkdir(exist_ok=True)
            (out / "batch-001.json").write_text(json.dumps(preflight), encoding="utf-8")
            (out / "batch-001-maintenance.json").write_text(json.dumps(maintenance), encoding="utf-8")
            (out / "batch-001-cached-sources.json").write_text(json.dumps(cached), encoding="utf-8")

            # Run the verifier's Git inspection against this isolated fixture repository.
            original_git_bytes = VERIFY.git_bytes
            VERIFY.git_bytes = lambda args: subprocess.run(["git", *args], cwd=base, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout
            try:
                result = VERIFY.verify_batch(1, out, backup_root)
                self.assertEqual(result["changed_files"], 1)
                backup.unlink()
                with self.assertRaisesRegex(RuntimeError, "Missing pre-change backup"):
                    VERIFY.verify_batch(1, out, backup_root)
                subprocess.run(["git", "checkout", "--", "Rule/Upstream/Apple/Apple.list"], cwd=base, check=True)
                self.assertEqual(target.read_text(encoding="utf-8"), "DOMAIN,original.example\\n")
            finally:
                VERIFY.git_bytes = original_git_bytes


if __name__ == "__main__":
    unittest.main(verbosity=2)
