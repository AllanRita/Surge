# Surge rule cleanup inventory and security audit

Generated: 2026-11-27 13:02 UTC

Scope: existing rule files and cached source metadata only. No new rule authors or rule lists were fetched. This report is read-only and does not alter rule files.

## Inventory

- Rule files: **828**
- App/category folders: **663**
- Top-level folders: **640**
- Rule data size: **116,049,942 bytes**
- Folders with multiple files/formats: **107**
- Exact byte-identical file groups: **2**
- Identical rule-payload groups (headers ignored): **3**
- Duplicate rule lines inside files: **0**
- Personal files inspected but not modified: **3**

## Bank/payment App folders

This classifies dedicated App folders by folder name only. Financial-service domains inside other App or aggregate lists are not removed.
- No dedicated bank/payment App folders found under Rule/Upstream. Rule/Personal/PayPay.list remains untouched.

## Other finance/trading/crypto folders — review only

These folders are not automatically classified as bank/payment Apps. They are listed for manual classification only; no rule files are deleted or modified.

| Folder | Classification | Rule files | Rule entries | Status |
|---|---|---:|---:|---|
| Binance | crypto exchange | 1 | 12 | Review only |
| Crypto | cryptocurrency category list (not a single App) | 1 | 201 | Review only |
| Cryptocurrency | cryptocurrency category list (not a single App) | 1 | 43 | Review only |
| EastMoney | securities brokerage / investment platform | 1 | 33 | Review only |
| OKX | crypto exchange | 1 | 3 | Review only |
| TigerFintech | securities brokerage / investment platform | 1 | 19 | Review only |

## Same-App / regional alias candidates

### Abema
- Candidate folders: AbemaTV
- Present aliases: none
- Rationale: Same service under former/alternate name; prior union verified.
### Gemini
- Candidate folders: BardAI
- Present aliases: none
- Rationale: Same Google assistant service after renaming; prior union verified.
### PChome
- Candidate folders: PChomeTW
- Present aliases: none
- Rationale: Same PChome Online service; prior union verified.
### GlobalScholar
- Candidate folders: Scholar
- Present aliases: none
- Rationale: GlobalScholar README explicitly says Scholar is included; prior union adds cnki.net.
### BiliBili
- Candidate folders: BiliBiliIntl
- Present aliases: none
- Rationale: Same Bilibili service family with international variant.
### iQIYI
- Candidate folders: iQIYIIntl
- Present aliases: none
- Rationale: Same iQIYI service family with international variant.
### Hulu
- Candidate folders: HuluUSA, HuluJP
- Present aliases: none
- Rationale: Same Hulu app/service with US and Japan regional domains.
### Telegram
- Candidate folders: TelegramNL, TelegramSG, TelegramUS
- Present aliases: none
- Rationale: Same Telegram app; regional files are IP-range subsets.
### Amazon
- Candidate folders: AmazonCN
- Present aliases: none
- Rationale: Same Amazon service family with China-region domains.
### HBO
- Candidate folders: HBOAsia, HBOHK, HBOUSA
- Present aliases: none
- Rationale: Same HBO/Max service family with regional rules.
### Cloudflare
- Candidate folders: Cloudflarecn
- Present aliases: none
- Rationale: Same Cloudflare service with China-specific domain subset.
### Steam
- Candidate folders: SteamCN
- Present aliases: none
- Rationale: Same Steam service family with China-region domains.
### Assassin'sCreed/Assassin'sCreed-Odyssey
- Candidate folders: Game/Assassin'sCreed-Odyssey
- Present aliases: none
- Rationale: Same game duplicated under two categories; Standard and Resolve stay separate.
### Assassin'sCreed/Assassin'sCreed-Origins
- Candidate folders: Game/Assassin'sCreed-Origins
- Present aliases: none
- Rationale: Same game duplicated under two categories; Standard and Resolve stay separate.

## Known shared-hosting, dynamic-DNS, and URL-shortener suffixes

This curated scan checks exact DOMAIN-SUFFIX / HOST-SUFFIX rules across all upstream lists. It is a review inventory, not an automatic deletion list; a platform suffix may be intentional in a particular scenario.

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

## Cached author-source coverage

- Cached source snapshots compared: **15**
- Source rule entries checked: **300**
- Missing source rules: **0**
- Scope limitation: only cached author snapshots are compared. This does not establish that every App has been compared against every author. No new authors or rule lists were fetched.

| Cached source | Target | Source rules | Exact | Parent suffix | IP covered | Missing |
|---|---|---:|---:|---:|---:|---:|
| Aoang-Apple | Apple/Apple.list + Apple/Apple_Domain.list | 69 | 12 | 57 | 0 | 0 |
| Aoang-DNS | Block/DNS/DNS.list | 53 | 53 | 0 | 0 | 0 |
| Aoang-OneDrive | OneDrive/OneDrive.list | 4 | 3 | 1 | 0 | 0 |
| Aoang-Other | Block/Other/Other.list | 1 | 1 | 0 | 0 | 0 |
| Aoang-Parallels | Block/Parallels/Parallels.list | 12 | 12 | 0 | 0 | 0 |
| Aoang-Process | Process/Process/Process.list | 23 | 23 | 0 | 0 | 0 |
| Aoang-Teams | Teams/Teams.list | 4 | 4 | 0 | 0 | 0 |
| Aoang-Unavailable | Process/Unavailable/Unavailable.list | 1 | 1 | 0 | 0 | 0 |
| Aoang-YouTube | Block/YouTube/YouTube.list | 15 | 15 | 0 | 0 | 0 |
| Apple | Apple/Apple.list + Apple/Apple_Domain.list | 16 | 16 | 0 | 0 | 0 |
| BiliBiliIntl | BiliBili/BiliBili.list | 5 | 4 | 1 | 0 | 0 |
| GitLab | GitLab/GitLab.list | 1 | 1 | 0 | 0 | 0 |
| Microsoft | Microsoft/Microsoft.list | 80 | 80 | 0 | 0 | 0 |
| NetEaseMusic | NetEaseMusic/NetEaseMusic.list | 2 | 2 | 0 | 0 | 0 |
| Telegram | Telegram/Telegram.list | 14 | 14 | 0 | 0 | 0 |

### Cached source coverage by available routing format

- Every available same-App format in the mapped folder (including Standard, Resolve, All, All_No_Resolve, and Domain when present) is checked separately; this does not imply that every App has a cached author snapshot.

| Cached source | Format | Target | Source rules | Missing |
|---|---|---|---:|---:|
| Aoang-Apple | standard | Apple/Apple.list + Apple/Apple_Domain.list | 69 | 0 |
| Aoang-Apple | resolve | Apple/Apple_Resolve.list + Apple/Apple_Domain.list | 69 | 0 |
| Aoang-Apple | all | Apple/Apple_All.list | 69 | 0 |
| Aoang-Apple | all_no_resolve | Apple/Apple_All_No_Resolve.list | 69 | 0 |
| Aoang-DNS | standard | Block/DNS/DNS.list | 53 | 0 |
| Aoang-OneDrive | standard | OneDrive/OneDrive.list | 4 | 0 |
| Aoang-Other | standard | Block/Other/Other.list | 1 | 0 |
| Aoang-Parallels | standard | Block/Parallels/Parallels.list | 12 | 0 |
| Aoang-Process | standard | Process/Process/Process.list | 23 | 0 |
| Aoang-Teams | standard | Teams/Teams.list | 4 | 0 |
| Aoang-Unavailable | standard | Process/Unavailable/Unavailable.list | 1 | 0 |
| Aoang-YouTube | standard | Block/YouTube/YouTube.list | 15 | 0 |
| Apple | standard | Apple/Apple.list + Apple/Apple_Domain.list | 16 | 0 |
| Apple | resolve | Apple/Apple_Resolve.list + Apple/Apple_Domain.list | 16 | 0 |
| Apple | all | Apple/Apple_All.list | 16 | 0 |
| Apple | all_no_resolve | Apple/Apple_All_No_Resolve.list | 16 | 0 |
| BiliBiliIntl | standard | BiliBili/BiliBili.list | 5 | 0 |
| BiliBiliIntl | resolve | BiliBili/BiliBili_Resolve.list | 5 | 0 |
| GitLab | standard | GitLab/GitLab.list | 1 | 0 |
| Microsoft | standard | Microsoft/Microsoft.list | 80 | 0 |
| NetEaseMusic | standard | NetEaseMusic/NetEaseMusic.list | 2 | 0 |
| NetEaseMusic | resolve | NetEaseMusic/NetEaseMusic_Resolve.list | 2 | 0 |
| Telegram | standard | Telegram/Telegram.list | 14 | 0 |
| Telegram | resolve | Telegram/Telegram_Resolve.list | 14 | 0 |

## Static security checks

- catch_all_network: 0
- duplicate_rule_lines: 0
- hidden_control: 0
- invalid_domain: 0
- invalid_native_filter: 0
- invalid_network: 0
- ip_family_mismatch: 0
- recognized_native_domain: 1330757
- recognized_native_filter: 0
- recognized_native_regex: 0
- single_label_suffix: 894
- stale_or_private_root_suffix: 0
- unsupported_or_missing_operand: 0

- Detailed threat-feed and broad shared-hosting review: see SECURITY-REVIEW.md.
- Financial-domain matches: 238 (review only; not deleted)
- URLhaus domains loaded: 0
- URLhaus status: not loaded; URLHAUS_AUTH_KEY is missing or download failed
- OpenPhish domains loaded: 280
- OpenPhish status: loaded
- Reputation matches shown: 77 (max 500); scope counts: {'app_or_routing': 77}
- Reputation-feed matches are review flags, not automatic deletions. Matches in block/filter lists may be intentional; app/routing matches need manual review.

- Feed coverage is incomplete; zero matches must not be interpreted as clean.
ChinaMaxNoIP/ChinaMaxNoIP_All.list, ChinaMaxNoIP/ChinaMaxNoIP_All_No_Resolve.list
EasyPrivacy/EasyPrivacy_All.list, EasyPrivacy/EasyPrivacy_All_No_Resolve.list

## Identical rule payloads with headers ignored

AdGuardSDNSFilter/AdGuardSDNSFilter_All.list, AdGuardSDNSFilter/AdGuardSDNSFilter_All_No_Resolve.list
ChinaMaxNoIP/ChinaMaxNoIP_All.list, ChinaMaxNoIP/ChinaMaxNoIP_All_No_Resolve.list
EasyPrivacy/EasyPrivacy_All.list, EasyPrivacy/EasyPrivacy_All_No_Resolve.list

## Multi-format folders

Format labels are inferred from filename suffixes; distinct formats are preserved unless explicitly approved after content comparison.

- AdGuardSDNSFilter: all, all_no_resolve, domain_only (3 files)
- AdobeActivation: resolve, standard (2 files)
- Advertising: all, all_no_resolve, domain_only, resolve, standard (5 files)
- AdvertisingLite: all, all_no_resolve, domain_only, resolve, standard (5 files)
- AdvertisingTest: all, all_no_resolve, domain_only, resolve, standard (5 files)
- Alibaba: all, all_no_resolve, domain_only, resolve, standard (5 files)
- Amazon: resolve, standard (2 files)
- AmazonIP: resolve, standard (2 files)
- Apple: all, all_no_resolve, domain_only, resolve, standard (5 files)
- AsianMedia: resolve, standard (2 files)
- Assassin'sCreed/Assassin'sCreed-Odyssey: resolve, standard (2 files)
- Assassin'sCreed/Assassin'sCreed-Origins: resolve, standard (2 files)
- BiliBili: resolve, standard (2 files)
- Blizzard: resolve, standard (2 files)
- BlockHttpDNS: resolve, standard (2 files)
- ByteDance: resolve, standard (2 files)
- China: all, all_no_resolve, domain_only, resolve, standard (5 files)
- ChinaASN: resolve, standard (2 files)
- ChinaDNS: resolve, standard (2 files)
- ChinaIPs: no_ipv6, no_ipv6_resolve, resolve, standard (4 files)
- ChinaIPs/ChinaIPsTest: no_ipv6, no_ipv6_resolve, resolve, standard (4 files)
- ChinaIPsBGP: resolve, standard (2 files)
- ChinaMax: all, all_no_resolve, domain_only, no_ipv6, no_ipv6_resolve, resolve, standard (7 files)
- ChinaMaxNoIP: all, all_no_resolve, domain_only, standard (4 files)
- ChinaMaxNoMedia: all, all_no_resolve, domain_only, resolve, standard (5 files)
- ChinaMedia: resolve, standard (2 files)
- ChinaMobile: resolve, standard (2 files)
- ChinaNoMedia: all, all_no_resolve, domain_only, resolve, standard (5 files)
- ChinaTest: all, all_no_resolve, domain_only, resolve, standard (5 files)
- ChinaUnicom: resolve, standard (2 files)
- Cloud/360Cloud: resolve, standard (2 files)
- Cloud/AkamaiCloud: resolve, standard (2 files)
- Cloud/AmazonCloud: resolve, standard (2 files)
- Cloud/BaiduCloud: resolve, standard (2 files)
- Cloud/CloudCN: resolve, standard (2 files)
- Cloud/CloudGlobal: resolve, standard (2 files)
- Cloud/HiNet: resolve, standard (2 files)
- Cloud/HuaweiCloud: resolve, standard (2 files)
- Cloud/JingDongCloud: resolve, standard (2 files)
- Cloud/KingsoftCloud: resolve, standard (2 files)
- Cloud/NeteaseCloud: resolve, standard (2 files)
- Cloud/TencentCloud: resolve, standard (2 files)
- Cloudflare: resolve, standard (2 files)
- ClubhouseIP: resolve, standard (2 files)
- Copilot: resolve, standard (2 files)
- DMM: resolve, standard (2 files)
- DNS: resolve, standard (2 files)
- DiabloIII: resolve, standard (2 files)
- EHGallery: resolve, standard (2 files)
- EasyPrivacy: all, all_no_resolve, domain_only (3 files)
- Facebook: resolve, standard (2 files)
- Game: resolve, standard (2 files)
- Game/Nikke: resolve, standard (2 files)
- Global: all, all_no_resolve, domain_only, resolve, standard (5 files)
- GlobalMedia: all, all_no_resolve, domain_only, resolve, standard (5 files)
- Google: resolve, standard (2 files)
- GoogleFCM: resolve, standard (2 files)
- Hearthstone: resolve, standard (2 files)
- HeroesoftheStorm: resolve, standard (2 files)
- Hijacking: resolve, standard (2 files)
- IPTVMainland: resolve, standard (2 files)
- IPTVOther: all, all_no_resolve, domain_only, resolve, standard (5 files)
- JOOX: resolve, standard (2 files)
- KakaoTalk: resolve, standard (2 files)
- KuangShi: resolve, standard (2 files)
- KugouKuwo: resolve, standard (2 files)
- LG: resolve, standard (2 files)
- Lan: resolve, standard (2 files)
- Line: resolve, standard (2 files)
- MEGA: resolve, standard (2 files)
- NaSDDNS: resolve, standard (2 files)
- Naver: resolve, standard (2 files)
- NetEase: resolve, standard (2 files)
- NetEaseMusic: resolve, standard (2 files)
- Netflix: resolve, standard (2 files)
- Nintendo: resolve, standard (2 files)
- OpenAI: resolve, standard (2 files)
- Opera: resolve, standard (2 files)
- Overwatch: resolve, standard (2 files)
- PotatoChat: resolve, standard (2 files)
- Privacy: all, all_no_resolve, domain_only, resolve, standard (5 files)
- PrivateTracker: resolve, standard (2 files)
- Proxy: all, all_no_resolve, domain_only, resolve, standard (5 files)
- ProxyLite: resolve, standard (2 files)
- Qobuz: resolve, standard (2 files)
- STUN: resolve, standard (2 files)
- Spotify: resolve, standard (2 files)
- StarCraftII: resolve, standard (2 files)
- Steam: resolve, standard (2 files)
- Supercell: resolve, standard (2 files)
- TeamViewer: resolve, standard (2 files)
- Telegram: resolve, standard (2 files)
- Tencent: all, all_no_resolve, domain_only, resolve, standard (5 files)
- TencentVideo: resolve, standard (2 files)
- Twitch: resolve, standard (2 files)
- Twitter: resolve, standard (2 files)
- WeChat: resolve, standard (2 files)
- WeTV: resolve, standard (2 files)
- Whatsapp: resolve, standard (2 files)
- WorldofWarcraft: resolve, standard (2 files)
- XiaoMi: resolve, standard (2 files)
- Yandex: resolve, standard (2 files)
- YouTube: resolve, standard (2 files)
- Youku: resolve, standard (2 files)
- Zhihu: resolve, standard (2 files)
- ZhihuAds: resolve, standard (2 files)
- iQIYI: resolve, standard (2 files)

## Safety boundaries
- No rule files or personal files are deleted, renamed, or rewritten by this audit.
- Bank/payment classification applies to dedicated App folders only; domains embedded in other Apps remain untouched.
- Regional variants are candidates for consolidation into one App policy group; country selection belongs in the Surge policy group, not separate rule folders.
- Resolve / non-Resolve and other distinct formats are compared and preserved separately.
- Similarity, shared CDN domains, or parent-company ownership alone never authorizes cross-App merging.
