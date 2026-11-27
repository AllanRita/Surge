# Security reputation review

Generated: 2026-11-27 11:10 UTC

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
- Matched feed host examples: metamask173.blogspot.com
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
- Matched feed host examples: cripthcomlogin.gitbook.io
- Classification: GitBook hosted content; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,github.io
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: GitHub/GitHub.list, Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: meenakshi-cse.github.io
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
- Matched feed host examples: b41382317-e93d-48f1-8e5b-812d31bf809d.netlify.app
- Classification: Netlify shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,pages.dev
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Cloudflare/Cloudflare.list, Cloudflare/Cloudflare_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: xfm31-z75-urmp-7tlst-07-10-2026-hh.pages.dev
- Classification: Cloudflare Pages shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,vercel.app
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, Vercel/Vercel.list
- Matched feed host examples: www.zimbra-auth-adm-old.vercel.app
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
- Matched feed host examples: taskorynex-velnoryx-371c.s2504191-f02.workers.dev
- Classification: Cloudflare Workers shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

## Stale/private single-label suffixes

- ChinaMax/ChinaMax.list:30: DOMAIN-SUFFIX,xihuan
- ChinaMax/ChinaMax_All.list:97388: DOMAIN-SUFFIX,xihuan
- ChinaMax/ChinaMax_All_No_Resolve.list:97388: DOMAIN-SUFFIX,xihuan
- ChinaMax/ChinaMax_No_IPv6.list:30: DOMAIN-SUFFIX,xihuan
- ChinaMax/ChinaMax_No_IPv6_Resolve.list:30: DOMAIN-SUFFIX,xihuan
- ChinaMax/ChinaMax_Resolve.list:30: DOMAIN-SUFFIX,xihuan
- ChinaMaxNoIP/ChinaMaxNoIP.list:23: DOMAIN-SUFFIX,xihuan
- ChinaMaxNoIP/ChinaMaxNoIP_All.list:97063: DOMAIN-SUFFIX,xihuan
- ChinaMaxNoIP/ChinaMaxNoIP_All_No_Resolve.list:97063: DOMAIN-SUFFIX,xihuan
- ChinaMaxNoMedia/ChinaMaxNoMedia.list:26: DOMAIN-SUFFIX,xihuan
- ChinaMaxNoMedia/ChinaMaxNoMedia_All.list:96972: DOMAIN-SUFFIX,xihuan
- ChinaMaxNoMedia/ChinaMaxNoMedia_All_No_Resolve.list:96972: DOMAIN-SUFFIX,xihuan
- ChinaMaxNoMedia/ChinaMaxNoMedia_Resolve.list:26: DOMAIN-SUFFIX,xihuan
- ChinaTest/ChinaTest.list:28: DOMAIN-SUFFIX,xihuan
- ChinaTest/ChinaTest_All.list:97997: DOMAIN-SUFFIX,xihuan
- ChinaTest/ChinaTest_All_No_Resolve.list:97997: DOMAIN-SUFFIX,xihuan
- ChinaTest/ChinaTest_Resolve.list:28: DOMAIN-SUFFIX,xihuan

## Financial-service domains

- Financial-domain rule matches found: 238
- These are retained. The user's rule is to remove dedicated bank/payment App folders only, not payment-related domains embedded in other App or block/filter lists.
- Rule/Personal was not modified.

## Interpretation
- OpenPhish/URLhaus matches under a shared CDN or hosting suffix are not direct evidence that the App rule itself is malicious.
- Shared hosting suffixes can match unrelated tenants. Review broad suffixes before assigning them to an App-specific policy group.
- No automatic deletion or rewriting is performed by this report.
