# Security reputation review

Generated: 2026-11-27 13:22 UTC

This report compares current domain rules against public threat-intelligence feeds. A feed match is a review signal, not proof that the rule's parent domain is malicious. No rules are automatically removed.

- URLhaus domains loaded: 0
- OpenPhish domains loaded: 280
- Rule-to-feed matches: 77 (up to 500 retained in the JSON report)
- Scope counts: {'app_or_routing': 77}
- Exact-domain matches: 0
- Parent-suffix coverage matches: 77
- A parent-suffix hit means a feed-listed host exists beneath a broad suffix; it does not mean the suffix root itself is malicious.

- URLhaus status: not loaded; URLHAUS_AUTH_KEY is missing or download failed.
- Feed coverage is incomplete; zero matches must not be interpreted as clean.

## Matched rules

### DOMAIN-SUFFIX,amazonaws.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Amazon/Amazon.list, Amazon/Amazon_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, GlobalMedia/GlobalMedia_All.list, GlobalMedia/GlobalMedia_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, ProxyLite/ProxyLite.list, ProxyLite/ProxyLite_Resolve.list
- Matched feed host examples: n8turz.s3.us-east-1.amazonaws.com
- Classification: shared cloud infrastructure / AWS; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,azurefd.net
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Microsoft/Microsoft.list
- Matched feed host examples: jqtwxeuajdx7rhx43etm-enc3ewbnatfudeba.z03.azurefd.net
- Classification: Azure Front Door shared CDN; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,azurewebsites.net
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Microsoft/Microsoft.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: forrit-tb-csmr-prod-dev-02.azurewebsites.net
- Classification: Azure App Service hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,blogspot.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Google/Google.list, Google/Google_Resolve.list
- Matched feed host examples: shopee1647.blogspot.com
- Classification: Blogger shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,cloudfront.net
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Amazon/Amazon.list, Amazon/Amazon_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, GlobalMedia/GlobalMedia_All.list, GlobalMedia/GlobalMedia_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, ProxyLite/ProxyLite.list, ProxyLite/ProxyLite_Resolve.list
- Matched feed host examples: d33wubrfki0l68.cloudfront.net
- Classification: shared CDN / Amazon CloudFront; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,duckdns.org
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, NaSDDNS/NaSDDNS.list, NaSDDNS/NaSDDNS_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: hizliyapiyoruzherseyi.duckdns.org
- Classification: dynamic DNS; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,eu.org
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: wisayq9065.embih.eu.org
- Classification: subdomain hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,gitbook.io
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: GitBook/GitBook.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: kucinlogn16.gitbook.io
- Classification: shared documentation hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,github.io
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: GitHub/GitHub.list, Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: wildpigger.github.io
- Classification: GitHub Pages shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,netlify.app
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: connexion-mabanquebnpparibas.netlify.app
- Classification: Netlify shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,pages.dev
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Cloudflare/Cloudflare.list, Cloudflare/Cloudflare_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: kynsy-9re-hz3l-wds1k-04-10-2026-hh.pages.dev
- Classification: Cloudflare Pages shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,trycloudflare.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Cloudflare/Cloudflare.list, Cloudflare/Cloudflare_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list
- Matched feed host examples: drainage-possess-unavailable-focal.trycloudflare.com
- Classification: Cloudflare temporary tunnel; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,vercel.app
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list, Vercel/Vercel.list
- Matched feed host examples: www.vansh-net-clone.vercel.app
- Classification: Vercel shared hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,weebly.com
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: www.xhdfh7hfnrrjjjff.weebly.com
- Classification: Weebly shared website hosting; this is a shared-hosting suffix, not an App-exclusive domain. Review whether it belongs in this App policy group.

### DOMAIN-SUFFIX,workers.dev
- Scope: app_or_routing
- Feed(s): OpenPhish
- Match type(s): parent_suffix
- Rule files: Cloudflare/Cloudflare.list, Cloudflare/Cloudflare_Resolve.list, Global/Global_All.list, Global/Global_All_No_Resolve.list, Proxy/Proxy_All.list, Proxy/Proxy_All_No_Resolve.list
- Matched feed host examples: taskorynex-velnoryx-371c.s2504191-f02.workers.dev
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

## Bare IANA public-TLD suffix rules

- Rule occurrences: 894 across 78 distinct TLD suffixes.
- These operands are valid IANA top-level domains, but a suffix rule at the TLD root can match every domain beneath that TLD. They are review-only; no rules are automatically removed.

| TLD suffix | Rule occurrences | Folders |
|---|---:|---|
| alibaba | 21 | Alibaba, ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| alipay | 10 | ChinaMax, ChinaTest |
| amazon | 2 | Amazon |
| anquan | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| aws | 2 | Amazon |
| azure | 1 | Microsoft |
| baidu | 10 | ChinaMax, ChinaTest |
| bbc | 2 | BBC, UKMedia |
| bing | 1 | Microsoft |
| bmw | 1 | BMW |
| cisco | 1 | Cisco |
| citic | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| cn | 25 | China, ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaNoMedia, ChinaTest |
| fox | 1 | Fox |
| google | 2 | ProxyLite |
| hotmail | 1 | Microsoft |
| ibm | 1 | IBM |
| icbc | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| imdb | 2 | Amazon |
| java | 1 | Oracle |
| kindle | 2 | Amazon |
| microsoft | 1 | Microsoft |
| mini | 1 | BMW |
| mit | 1 | GlobalScholar |
| ms | 25 | China, ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaNoMedia, ChinaTest |
| office | 1 | Microsoft |
| oracle | 1 | Oracle |
| shouji | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| sina | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| skype | 1 | Microsoft |
| sohu | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| taobao | 14 | Alibaba, ChinaMax, ChinaTest |
| tmall | 21 | Alibaba, ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| unicom | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| wang | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| weatherchannel | 1 | IBM |
| weibo | 10 | ChinaMax, ChinaTest |
| windows | 1 | Microsoft |
| xn--1qqw23a | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--3bst00m | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--3ds443g | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--55qw42g | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--55qx5d | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--5tzm5g | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--6frz82g | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--6qq986b3xl | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--8y0a063a | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--9et52u | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--9krt00a | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--cckwcxetd | 2 | Amazon |
| xn--czr694b | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--czrs0t | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--czru2d | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--fiq228c5hs | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--fiq64b | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--fiqs8s | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--fiqz9s | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--fjq720a | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--g2xx48c | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--hxt814e | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--imr513n | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--io0a7i | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--jlq480n2rg | 2 | Amazon |
| xn--kput3i | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--nyqy26a | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--otu796d | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--rhqv96g | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--ses554g | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--unup4y | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--vhquv | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--vuq861b | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--xhq521b | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--zfr164b | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| yamaxun | 2 | Amazon |
| yandex | 2 | Yandex |
| youtube | 6 | GlobalMedia, YouTube |
| yun | 17 | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| zappos | 2 | Amazon |

## Stale/private single-label suffixes

- None detected or IANA TLD feed unavailable.

## Financial-service domains

- Financial-domain rule matches found: 238
- Dedicated bank/payment, crypto-exchange, cryptocurrency-category, securities-brokerage, and stock-investment folders were removed per user direction. Financial-service domains embedded in unrelated App, aggregate, advertising, privacy, or filter lists remain unchanged.
- Rule/Personal was not modified.

## Interpretation
- OpenPhish/URLhaus matches under a shared CDN or hosting suffix are not direct evidence that the App rule itself is malicious.
- Shared hosting suffixes can match unrelated tenants. Review broad suffixes before assigning them to an App-specific policy group.
- No automatic deletion or rewriting is performed by this report.
