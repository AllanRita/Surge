#!/usr/bin/env python3
"""Offline self-tests for Surge batch maintenance, cached-source merge and rollback backups."""
import importlib.util
import json
import sys
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

    def test_urlhaus_hostfile_first_column(self):
        with tempfile.TemporaryDirectory() as td:
            feed = Path(td) / "urlhaus.txt"
            feed.write_text("evil.example CNAME . ; malware download\n", encoding="utf-8")
            self.assertEqual(MAINTAIN.feed_hosts(str(feed)), {"evil.example"})

if __name__ == "__main__":
    unittest.main(verbosity=2)
