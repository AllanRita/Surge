# Surge manual review notes

Generated: 2026-11-27
Repository: AllanRita/Surge

## Scope

This file records manual interpretation of the static audit. It does not replace a live Surge subscription import or device-level traffic test. No subscription files or personal rules were deleted or rewritten during this review.

## Single-label suffix audit

- Static broad-domain matches: 912 rows across rule files and scenario variants.
- Distinct single-label suffix values: 79.
- Present in the current IANA delegated TLD list: 78 values, 895 rows.
- Absent from the current IANA delegated TLD list: `xihuan`, 17 rows.
- IANA list checked: `https://data.iana.org/TLD/tlds-alpha-by-domain.txt`, version `2026112503`, updated 2026-11-26 UTC.

Interpretation:
- A one-label suffix is not automatically malformed. Most values in this snapshot are real delegated TLDs, including brand TLDs and IDN/punycode TLDs.
- These rules are still broad in scope: for example, `DOMAIN-SUFFIX,cn` matches the entire `.cn` namespace. Whether that is correct depends on the intended scenario and policy.
- `DOMAIN-SUFFIX,xihuan` is not in the current delegated root list. It is retained and flagged for review; it has not been automatically removed.

## Financial-domain audit

- 238 upstream financial-domain review matches.
- 1 personal financial-rule match in `Rule/Personal/PayPay.list`.
- 29 distinct domain values across the report.
- The personal PayPay file remains unchanged.

Important interpretation:
- Matches in advertising, privacy, or AdGuard-native lists may represent tracking, telemetry, email, or measurement endpoints; they do not by themselves prove that payment or checkout traffic is blocked.
- Broad service rules such as `alipay.com`, `unionpay.com`, `paypal.com`, `visa.com`, and `stripe.com` need to be interpreted in the context of their category and the user's policy. They were not deleted or rewritten automatically.
- Keep the PayPay personal rule separate from upstream blocklists. Do not remove it as an audit cleanup.

## Identical-content candidates

The audit reports 8 groups:
- 3 same-app scenario pairs: `All` and `All_No_Resolve` variants. These are intentionally kept separate because their resolution behavior differs.
- 5 cross-category exact-content candidates. The Assassin's Creed Odyssey and Origins rule bodies, and the PChome/PChomeTW rule bodies, were checked and are identical in the paired paths (rule payloads match; metadata timestamps can differ).

No cross-category file was deleted. Keeping both paths avoids silently breaking any existing raw-file subscription URL. Consolidation to one canonical subscription path requires a separate compatibility/redirect plan.

## Current validation limits

- The latest workflow run validates and publishes a static snapshot and audit artifact.
- It does not prove live DNS resolution, actual routing decisions, payment completion, or real-device Surge subscription behavior.
- Device-level regression must verify the intended policy for Alipay, UnionPay, PayPal, Visa, Stripe, and PayPay before any payment-related rule is changed.

## Safety decision

No broad-domain or financial-domain rule was automatically deleted. Keep potentially useful rules pending scenario-aware and live behavior verification.
