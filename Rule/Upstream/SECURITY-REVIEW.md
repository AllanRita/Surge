# Security reputation review

Generated: 2026-11-27 11:13 UTC

This report compares current domain rules against public threat-intelligence feeds. A feed match is a review signal, not proof that the rule's parent domain is malicious. No rules are automatically removed.

- URLhaus domains loaded: 0
- OpenPhish domains loaded: 278
- Rule-to-feed matches: 61 (up to 500 retained in the JSON report)
- Scope counts: {'app_or_routing': 61}

- URLhaus feed unavailable in this run; OpenPhish was used for the phishing cross-check.

## Matched rules

### DOMAIN-SUFFIX,blogspot.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Google/Google.list, Google/Google_Resolve.list
- Matched feed host examples: www.lazada0277.blogspot.com
- Classification: Blogger shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,cloudfront.net
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Amazon/Amazon.list, Amazon/Amazon_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, GlobalMedia/GlobalMedia_All.list, GlobalMedia/GlobalMedia_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, ProxyLite/ProxyLite.list, ProxyLite/ProxyLite_Resolve.list
- Matched feed host examples: d33wubrfki0l68.cloudfront.net
- Classification: Amazon CloudFront shared CDN; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,duckdns.org
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, NaSDDNS/NaSDDNS.list, NaSDDNS/NaSDDNS_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: www.112acil112acil112acil.duckdns.org
- Classification: DuckDNS dynamic DNS; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,eu.org
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: five.seafn.eu.org
- Classification: EU.org subdomain hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,gitbook.io
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: GitBook/GitBook.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: metamasiuklogin.gitbook.io
- Classification: GitBook hosted content; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,github.io
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: GitHub/GitHub.list, Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: dank1ngzzz.github.io
- Classification: GitHub Pages shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,is.gd
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, ProxyLite/ProxyLite.list, ProxyLite/ProxyLite_Resolve.list
- Matched feed host examples: is.gd
- Classification: URL shortener; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,netlify.app
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: ingprsonasvrtal.netlify.app
- Classification: Netlify shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,pages.dev
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Cloudflare/Cloudflare.list, Cloudflare/Cloudflare_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: 02796960-nmc6bvvpedys-tabefjvb-prs8y9b-v25qyixzuz5.pages.dev
- Classification: Cloudflare Pages shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,vercel.app
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, Vercel/Vercel.list
- Matched feed host examples: dataserver-kappa.vercel.app
- Classification: Vercel shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,web.app
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Google/Google.list, Google/Google_Resolve.list
- Matched feed host examples: netflix-bobby.web.app
- Classification: Firebase Hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,workers.dev
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Cloudflare/Cloudflare.list, Cloudflare/Cloudflare_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: supplemental-insert-259e.andrew-andrew23.workers.dev
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
