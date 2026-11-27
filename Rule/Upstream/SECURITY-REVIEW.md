# Security reputation review

Generated: 2026-11-27 12:41 UTC

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
- Classification: shared cloud infrastructure / AWS; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,azurefd.net
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Microsoft/Microsoft.list
- Matched feed host examples: 35ctt56wc6hcja27hkpd-d4g3a2apa2g2ergs.z03.azurefd.net
- Classification: Azure Front Door shared CDN; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,azurewebsites.net
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Microsoft/Microsoft.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: forrit-tb-csmr-prod-dev-02.azurewebsites.net
- Classification: Azure App Service hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,blogspot.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Google/Google.list, Google/Google_Resolve.list
- Matched feed host examples: instagram-baittouts-login.blogspot.com
- Classification: Blogger shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,cloudfront.net
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Amazon/Amazon.list, Amazon/Amazon_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, GlobalMedia/GlobalMedia_All.list, GlobalMedia/GlobalMedia_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, ProxyLite/ProxyLite.list, ProxyLite/ProxyLite_Resolve.list
- Matched feed host examples: d33wubrfki0l68.cloudfront.net
- Classification: shared CDN / Amazon CloudFront; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,duckdns.org
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, NaSDDNS/NaSDDNS.list, NaSDDNS/NaSDDNS_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: hizliyapiyoruzherseyi.duckdns.org
- Classification: dynamic DNS; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,eu.org
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: wisayq9065.embih.eu.org
- Classification: subdomain hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,gitbook.io
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: GitBook/GitBook.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: matumasklogie.gitbook.io
- Classification: shared documentation hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,github.io
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: GitHub/GitHub.list, Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: zhouxiaoka.github.io
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
- Matched feed host examples: y5uf3y31k3-4746176-jbmorw-lnwfs-3htbp6e.pages.dev
- Classification: Cloudflare Pages shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,trycloudflare.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Cloudflare/Cloudflare.list, Cloudflare/Cloudflare_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: drainage-possess-unavailable-focal.trycloudflare.com
- Classification: Cloudflare temporary tunnel; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,vercel.app
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, Vercel/Vercel.list
- Matched feed host examples: ore45.vercel.app
- Classification: Vercel shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,weebly.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: www.xhdfh7hfnrrjjjff.weebly.com
- Classification: Weebly shared website hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,workers.dev
- Scope: app_or_routing
- Feed(s): OpenPhish
- Rule files: Cloudflare/Cloudflare.list, Cloudflare/Cloudflare_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: substantiating-proof-f2d1.63186834.workers.dev
- Classification: Cloudflare Workers shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.


## Known shared-hosting suffixes in the rule library

The curated suffix scan covers all upstream rule files, not only threat-feed matches. These are broad multi-tenant or shared-platform namespaces; presence is not proof of maliciousness and no rule is automatically removed.

| Suffix | Classification | Rule occurrences | Folders |
|---|---|---:|---|
| amazonaws.com | shared cloud infrastructure / AWS | 10 | Amazon, Global, GlobalMedia, Proxy, ProxyLite |
| appspot.com | Google App Engine hosting | 6 | Global, Google, Proxy |
| azureedge.net | Azure CDN | 5 | Global, Microsoft, Proxy |
| azurefd.net | Azure Front Door shared CDN | 3 | Global, Microsoft |
| azurestaticapps.net | Azure Static Web Apps | 2 | Global |
| azurewebsites.net | Azure App Service hosting | 5 | Global, Microsoft, Proxy |
| bit.ly | URL shortener | 6 | Global, Proxy, ProxyLite |
| bitbucket.io | Bitbucket Pages hosting | 2 | Global |
| blogspot.com | Blogger shared hosting | 4 | Global, Google |
| cloudapp.net | Azure Cloud Services | 3 | Global, Microsoft |
| cloudfront.net | shared CDN / Amazon CloudFront | 10 | Amazon, Global, GlobalMedia, Proxy, ProxyLite |
| cutt.ly | URL shortener | 2 | Global |
| duckdns.org | dynamic DNS | 6 | Global, NaSDDNS, Proxy |
| dynu.net | Dynu dynamic DNS | 5 | Dynu, Global, Proxy |
| eu.org | subdomain hosting | 2 | Global |
| firebaseapp.com | Firebase Hosting | 4 | Global, Google |
| fly.dev | Fly.io shared hosting | 2 | Global |
| gitbook.io | shared documentation hosting | 5 | GitBook, Global, Proxy |
| github.io | GitHub Pages shared hosting | 3 | GitHub, Global |
| gitlab.io | GitLab Pages shared hosting | 7 | Developer, Global, Proxy, ProxyLite |
| herokuapp.com | Heroku shared hosting | 6 | Global, Heroku, Proxy, Salesforce |
| is.gd | URL shortener | 6 | Global, Proxy, ProxyLite |
| linktr.ee | link-in-bio / redirect platform | 4 | Global, Proxy |
| netlify.app | Netlify shared hosting | 4 | Global, Proxy |
| no-ip.org | dynamic DNS | 4 | Global, Proxy |
| pages.dev | Cloudflare Pages shared hosting | 6 | Cloudflare, Global, Proxy |
| shorturl.at | URL shortener | 2 | Global |
| t.co | URL shortener | 8 | Global, Proxy, ProxyLite, Twitter |
| tinyurl.com | URL shortener | 4 | Global, Proxy |
| trycloudflare.com | Cloudflare temporary tunnel | 4 | Cloudflare, Global |
| vercel.app | Vercel shared hosting | 5 | Global, Proxy, Vercel |
| web.app | Firebase Hosting | 4 | Global, Google |
| weebly.com | Weebly shared website hosting | 4 | Global, Proxy |
| workers.dev | Cloudflare Workers shared hosting | 6 | Cloudflare, Global, Proxy |
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
