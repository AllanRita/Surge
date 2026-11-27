# Security reputation review

Generated: 2026-11-27 12:28 UTC

This report compares current domain rules against public threat-intelligence feeds. A feed match is a review signal, not proof that the rule's parent domain is malicious. No rules are automatically removed.

- URLhaus domains loaded: 0
- OpenPhish domains loaded: 280
- Rule-to-feed matches: 77 (up to 500 retained in the JSON report)
- Scope counts: {'app_or_routing': 77}

- URLhaus hostfile not loaded: the current export requires an Auth-Key. Configure the GitHub Actions secret URLHAUS_AUTH_KEY to enable authenticated checks; OpenPhish was used for this run.

## Matched rules

### DOMAIN-SUFFIX,amazonaws.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Amazon/Amazon.list, Amazon/Amazon_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, GlobalMedia/GlobalMedia_All.list, GlobalMedia/GlobalMedia_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, ProxyLite/ProxyLite.list, ProxyLite/ProxyLite_Resolve.list
- Matched feed host examples: n8turz.s3.us-east-1.amazonaws.com
- Classification: app/routing match; verify that the domain is genuinely required by the App and is not an overly broad shared service.

### DOMAIN-SUFFIX,azurefd.net
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Microsoft/Microsoft.list
- Matched feed host examples: 35ctt56wc6hcja27hkpd-d4g3a2apa2g2ergs.z03.azurefd.net
- Classification: app/routing match; verify that the domain is genuinely required by the App and is not an overly broad shared service.

### DOMAIN-SUFFIX,azurewebsites.net
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Microsoft/Microsoft.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: forrit-tb-csmr-prod-dev-02.azurewebsites.net
- Classification: app/routing match; verify that the domain is genuinely required by the App and is not an overly broad shared service.

### DOMAIN-SUFFIX,blogspot.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Google/Google.list, Google/Google_Resolve.list
- Matched feed host examples: rejekishopee23.blogspot.com
- Classification: Blogger shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,cloudfront.net
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Amazon/Amazon.list, Amazon/Amazon_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, GlobalMedia/GlobalMedia_All.list, GlobalMedia/GlobalMedia_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, ProxyLite/ProxyLite.list, ProxyLite/ProxyLite_Resolve.list
- Matched feed host examples: d1by761p31t71v.cloudfront.net
- Classification: Amazon CloudFront shared CDN; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,duckdns.org
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, NaSDDNS/NaSDDNS.list, NaSDDNS/NaSDDNS_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: hizliyapiyoruzherseyi.duckdns.org
- Classification: DuckDNS dynamic DNS; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,eu.org
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: wisayq9065.embih.eu.org
- Classification: EU.org subdomain hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,gitbook.io
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: GitBook/GitBook.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: matumasklogie.gitbook.io
- Classification: GitBook hosted content; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,github.io
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: GitHub/GitHub.list, Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: wargreymon9.github.io
- Classification: GitHub Pages shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,netlify.app
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: boisterous-sprite-d1fe49.netlify.app
- Classification: Netlify shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,pages.dev
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Cloudflare/Cloudflare.list, Cloudflare/Cloudflare_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: brige-traezor-io.pages.dev
- Classification: Cloudflare Pages shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,trycloudflare.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Cloudflare/Cloudflare.list, Cloudflare/Cloudflare_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: drainage-possess-unavailable-focal.trycloudflare.com
- Classification: app/routing match; verify that the domain is genuinely required by the App and is not an overly broad shared service.

### DOMAIN-SUFFIX,vercel.app
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, Vercel/Vercel.list
- Matched feed host examples: www.vakifbank.vercel.app
- Classification: Vercel shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,weebly.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: www.xhdfh7hfnrrjjjff.weebly.com
- Classification: app/routing match; verify that the domain is genuinely required by the App and is not an overly broad shared service.

### DOMAIN-SUFFIX,workers.dev
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Cloudflare/Cloudflare.list, Cloudflare/Cloudflare_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: substantiating-proof-f2d1.63186834.workers.dev
- Classification: Cloudflare Workers shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

## Stale/private single-label suffixes

- None detected or IANA TLD feed unavailable.

## Financial-service domains

- Financial-domain rule matches found: 238
- These are retained. The user's rule is to remove dedicated bank/payment App folders only, not payment-related domains embedded in other App or block/filter lists.
- Rule/Personal was not modified.

## Interpretation
- OpenPhish/URLhaus matches under a shared CDN or hosting suffix are not direct evidence that the App rule itself is malicious.
- Shared hosting suffixes can match unrelated tenants. Review broad suffixes before assigning them to an App-specific policy group.
- No automatic deletion or rewriting is performed by this report.
