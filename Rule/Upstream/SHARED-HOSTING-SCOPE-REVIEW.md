# Shared-hosting and multi-tenant suffix scope review

Generated from CLEANUP-INVENTORY.json (2026-11-27 13:46 UTC).

## Executive result

- 42 curated shared-hosting, CDN, dynamic-DNS, and URL-shortener suffixes were checked against the rule library.
- 34 suffixes are present in 159 rule occurrences.
- 21 suffixes occur in App/service folders; the inventory records 33 App/service-folder occurrences and 126 aggregate-folder occurrences.
- Aggregate folders in this report: Global, GlobalMedia, Proxy, and ProxyLite.
- No rules were removed or rewritten. Shared-hosting suffixes are never automatically deleted based on a feed match.

## Suffix inventory

| Suffix | Classification | Occurrences | Scope | App/service folders | Aggregate folders |
|---|---|---:|---|---|---|
| amazonaws.com | shared cloud infrastructure / AWS | 10 | App/service folder present | Amazon | Global, GlobalMedia, Proxy, ProxyLite |
| appspot.com | Google App Engine hosting | 6 | App/service folder present | Google | Global, Proxy |
| azureedge.net | Azure CDN | 5 | App/service folder present | Microsoft | Global, Proxy |
| azurefd.net | Azure Front Door shared CDN | 3 | App/service folder present | Microsoft | Global |
| azurestaticapps.net | Azure Static Web Apps | 2 | Aggregate-only | — | Global |
| azurewebsites.net | Azure App Service hosting | 5 | App/service folder present | Microsoft | Global, Proxy |
| bit.ly | URL shortener | 6 | Aggregate-only | — | Global, Proxy, ProxyLite |
| bitbucket.io | Bitbucket Pages hosting | 2 | Aggregate-only | — | Global |
| blogspot.com | Blogger shared hosting | 4 | App/service folder present | Google | Global |
| cloudapp.net | Azure Cloud Services | 3 | App/service folder present | Microsoft | Global |
| cloudfront.net | shared CDN / Amazon CloudFront | 10 | App/service folder present | Amazon | Global, GlobalMedia, Proxy, ProxyLite |
| cutt.ly | URL shortener | 2 | Aggregate-only | — | Global |
| duckdns.org | dynamic DNS | 6 | App/service folder present | NaSDDNS | Global, Proxy |
| dynu.net | Dynu dynamic DNS | 5 | App/service folder present | Dynu | Global, Proxy |
| eu.org | subdomain hosting | 2 | Aggregate-only | — | Global |
| firebaseapp.com | Firebase Hosting | 4 | App/service folder present | Google | Global |
| fly.dev | Fly.io shared hosting | 2 | Aggregate-only | — | Global |
| gitbook.io | shared documentation hosting | 5 | App/service folder present | GitBook | Global, Proxy |
| github.io | GitHub Pages shared hosting | 3 | App/service folder present | GitHub | Global |
| gitlab.io | GitLab Pages shared hosting | 7 | App/service folder present | Developer | Global, Proxy, ProxyLite |
| herokuapp.com | Heroku shared hosting | 6 | App/service folder present | Heroku, Salesforce | Global, Proxy |
| is.gd | URL shortener | 6 | Aggregate-only | — | Global, Proxy, ProxyLite |
| linktr.ee | link-in-bio / redirect platform | 4 | Aggregate-only | — | Global, Proxy |
| netlify.app | Netlify shared hosting | 4 | Aggregate-only | — | Global, Proxy |
| no-ip.org | dynamic DNS | 4 | Aggregate-only | — | Global, Proxy |
| pages.dev | Cloudflare Pages shared hosting | 6 | App/service folder present | Cloudflare | Global, Proxy |
| shorturl.at | URL shortener | 2 | Aggregate-only | — | Global |
| t.co | URL shortener | 8 | App/service folder present | Twitter | Global, Proxy, ProxyLite |
| tinyurl.com | URL shortener | 4 | Aggregate-only | — | Global, Proxy |
| trycloudflare.com | Cloudflare temporary tunnel | 4 | App/service folder present | Cloudflare | Global |
| vercel.app | Vercel shared hosting | 5 | App/service folder present | Vercel | Global, Proxy |
| web.app | Firebase Hosting | 4 | App/service folder present | Google | Global |
| weebly.com | Weebly shared website hosting | 4 | Aggregate-only | — | Global, Proxy |
| workers.dev | Cloudflare Workers shared hosting | 6 | App/service folder present | Cloudflare | Global, Proxy |

## Threat-feed interpretation

- The current OpenPhish comparison found 77 rule-to-feed match records in the inventory snapshot.
- All recorded matches are parent-suffix matches: a listed host exists beneath a broader shared-hosting suffix. This does not mean the parent suffix itself is malicious.
- URLhaus was not loaded in the inventory snapshot because URLHAUS_AUTH_KEY was missing or the authenticated feed download failed. This is incomplete coverage, not a clean result.
- No exact-domain dual-feed confirmation was available, so threat-based automatic deletion remained disabled.

## Handling decision

1. Keep shared CDN/hosting suffixes review-only. A broad suffix can route unrelated tenants and customers.
2. Review App-specific placements such as Amazon, Cloudflare, Google, Microsoft, Vercel, and other providers in the context of the App policy group's intended traffic.
3. Review aggregate placements in Global, GlobalMedia, Proxy, and ProxyLite separately; they serve different routing scopes and must not be merged into individual App rules.
4. Do not remove a parent suffix because an OpenPhish host appears beneath it. Only an exact hostname corroborated by both OpenPhish and URLhaus may qualify for the existing narrow threat-deletion rule, and block/filter lists remain excluded.
5. Keep URLhaus-dependent threat deletion disabled until the authenticated feed is successfully loaded.

## Source and limitations

- Source inventory: Rule/Upstream/CLEANUP-INVENTORY.json.
- Detailed feed examples: Rule/Upstream/SECURITY-REVIEW.md.
- This is a scope review, not a benign/malicious verdict for every tenant beneath each suffix.
