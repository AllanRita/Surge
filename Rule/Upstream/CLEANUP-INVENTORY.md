# Surge rule cleanup inventory and security audit

Generated: 2026-11-27 10:45 UTC

Scope: existing rule files and cached source metadata only. No new rule authors or rule lists were fetched. This report is read-only and does not alter rule files.

## Inventory

- Rule files: **853**
- App/category folders: **682**
- Top-level folders: **657**
- Rule data size: **116,070,619 bytes**
- Folders with multiple files/formats: **113**
- Exact byte-identical file groups: **2**
- Identical rule-payload groups (headers ignored): **11**
- Duplicate rule lines inside files: **0**
- Personal files inspected but not modified: **3**

## Bank/payment App folders

This classifies dedicated App folders by folder name only. Financial-service domains inside other App or aggregate lists are not removed.
- No dedicated bank/payment App folders found under Rule/Upstream. Rule/Personal/PayPay.list remains untouched.

## Same-App / regional alias candidates

### Abema
- Candidate folders: AbemaTV
- Present aliases: AbemaTV
- Rationale: Same service under former/alternate name; prior union verified.
- standard: canonical 29 lines; aliases 29 lines; union 29 unique; new semantic lines 0
### Gemini
- Candidate folders: BardAI
- Present aliases: BardAI
- Rationale: Same Google assistant service after renaming; prior union verified.
- standard: canonical 14 lines; aliases 14 lines; union 14 unique; new semantic lines 0
### PChome
- Candidate folders: PChomeTW
- Present aliases: PChomeTW
- Rationale: Same PChome Online service; prior union verified.
- standard: canonical 5 lines; aliases 5 lines; union 5 unique; new semantic lines 0
### GlobalScholar
- Candidate folders: Scholar
- Present aliases: Scholar
- Rationale: GlobalScholar README explicitly says Scholar is included; prior union adds cnki.net.
- standard: canonical 231 lines; aliases 231 lines; union 231 unique; new semantic lines 0
### BiliBili
- Candidate folders: BiliBiliIntl
- Present aliases: BiliBiliIntl
- Rationale: Same Bilibili service family with international variant.
- standard: canonical 133 lines; aliases 6 lines; union 135 unique; new semantic lines 1
  - PROCESS-NAME,com.bstar.intl
### iQIYI
- Candidate folders: iQIYIIntl
- Present aliases: iQIYIIntl
- Rationale: Same iQIYI service family with international variant.
- resolve: canonical 63 lines; aliases 21 lines; union 80 unique; new semantic lines 11
  - IP-CIDR,104.85.165.17/32
  - IP-CIDR,159.138.102.146/32
  - IP-CIDR,184.51.102.0/24
  - IP-CIDR,203.80.97.203/32
  - IP-CIDR,23.200.145.146/32
  - IP-CIDR,23.210.215.186/32
  - IP-CIDR,23.211.15.0/24
  - IP-CIDR,23.219.172.0/24
  - IP-CIDR,23.59.252.0/24
  - PROCESS-NAME,com.iqiyi.i18n
- standard: canonical 63 lines; aliases 21 lines; union 80 unique; new semantic lines 11
  - IP-CIDR,104.85.165.17/32,no-resolve
  - IP-CIDR,159.138.102.146/32,no-resolve
  - IP-CIDR,184.51.102.0/24,no-resolve
  - IP-CIDR,203.80.97.203/32,no-resolve
  - IP-CIDR,23.200.145.146/32,no-resolve
  - IP-CIDR,23.210.215.186/32,no-resolve
  - IP-CIDR,23.211.15.0/24,no-resolve
  - IP-CIDR,23.219.172.0/24,no-resolve
  - IP-CIDR,23.59.252.0/24,no-resolve
  - PROCESS-NAME,com.iqiyi.i18n
### Hulu
- Candidate folders: HuluUSA, HuluJP
- Present aliases: HuluUSA, HuluJP
- Rationale: Same Hulu app/service with US and Japan regional domains.
- standard: canonical 59 lines; aliases 58 lines; union 59 unique; new semantic lines 0
### Telegram
- Candidate folders: TelegramNL, TelegramSG, TelegramUS
- Present aliases: TelegramNL, TelegramSG, TelegramUS
- Rationale: Same Telegram app; regional files are IP-range subsets.
- resolve: canonical 46 lines; aliases 10 lines; union 53 unique; new semantic lines 0
- standard: canonical 46 lines; aliases 10 lines; union 53 unique; new semantic lines 0
### Amazon
- Candidate folders: AmazonCN
- Present aliases: AmazonCN
- Rationale: Same Amazon service family with China-region domains.
- standard: canonical 206 lines; aliases 47 lines; union 223 unique; new semantic lines 17
  - DOMAIN-SUFFIX,a2z.org.cn
  - DOMAIN-SUFFIX,amazonaws.cn
  - DOMAIN-SUFFIX,amazonwebservices.com.cn
  - DOMAIN-SUFFIX,asfiovnxocqpcry.com.cn
  - DOMAIN-SUFFIX,aws-border.cn
  - DOMAIN-SUFFIX,aws-icp-domain-manager.cn
  - DOMAIN-SUFFIX,awsapps.cn
  - DOMAIN-SUFFIX,awsapps.com.cn
  - DOMAIN-SUFFIX,awsstatic.cn
  - DOMAIN-SUFFIX,cloudfront-test.cn
### HBO
- Candidate folders: HBOAsia, HBOHK, HBOUSA
- Present aliases: HBOAsia, HBOHK, HBOUSA
- Rationale: Same HBO/Max service family with regional rules.
- standard: canonical 50 lines; aliases 56 lines; union 70 unique; new semantic lines 5
  - DOMAIN,s3-ap-southeast-1.amazonaws.com
  - DOMAIN-KEYWORD,.hbogoasia.
  - DOMAIN-SUFFIX,discomax.com
  - DOMAIN-SUFFIX,h264.io
  - USER-AGENT,HBO%20GO%20PROD*
### Cloudflare
- Candidate folders: Cloudflarecn
- Present aliases: Cloudflarecn
- Rationale: Same Cloudflare service with China-specific domain subset.
- standard: canonical 65 lines; aliases 14 lines; union 65 unique; new semantic lines 0
### Steam
- Candidate folders: SteamCN
- Present aliases: SteamCN
- Rationale: Same Steam service family with China-region domains.
- standard: canonical 69 lines; aliases 17 lines; union 86 unique; new semantic lines 5
  - DOMAIN,xz.pphimalayanrt.com
  - DOMAIN-SUFFIX,steamchina.com
  - DOMAIN-SUFFIX,steamcontent.com
  - DOMAIN-SUFFIX,steamserver.net
  - DOMAIN-SUFFIX,steamusercontent.com
### Assassin'sCreed/Assassin'sCreed-Odyssey
- Candidate folders: Game/Assassin'sCreed-Odyssey
- Present aliases: Game/Assassin'sCreed-Odyssey
- Rationale: Same game duplicated under two categories; Standard and Resolve stay separate.
- resolve: canonical 15 lines; aliases 15 lines; union 15 unique; new semantic lines 0
- standard: canonical 15 lines; aliases 15 lines; union 15 unique; new semantic lines 0
### Assassin'sCreed/Assassin'sCreed-Origins
- Candidate folders: Game/Assassin'sCreed-Origins
- Present aliases: Game/Assassin'sCreed-Origins
- Rationale: Same game duplicated under two categories; Standard and Resolve stay separate.
- resolve: canonical 16 lines; aliases 16 lines; union 16 unique; new semantic lines 0
- standard: canonical 16 lines; aliases 16 lines; union 16 unique; new semantic lines 0

## Cached author-source coverage

| Cached source | Target | Source rules | Exact | Parent suffix | IP covered | Missing |
|---|---|---:|---:|---:|---:|---:|
| Aoang-Apple | Apple/Apple.list | 69 | 12 | 57 | 0 | 0 |
| Aoang-DNS | Block/DNS/DNS.list | 53 | 53 | 0 | 0 | 0 |
| Aoang-OneDrive | OneDrive/OneDrive.list | 4 | 3 | 1 | 0 | 0 |
| Aoang-Other | Block/Other/Other.list | 1 | 1 | 0 | 0 | 0 |
| Aoang-Parallels | Block/Parallels/Parallels.list | 12 | 12 | 0 | 0 | 0 |
| Aoang-Process | Process/Process/Process.list | 23 | 23 | 0 | 0 | 0 |
| Aoang-Teams | Teams/Teams.list | 4 | 4 | 0 | 0 | 0 |
| Aoang-Unavailable | Process/Unavailable/Unavailable.list | 1 | 1 | 0 | 0 | 0 |
| Aoang-YouTube | Block/YouTube/YouTube.list | 15 | 15 | 0 | 0 | 0 |
| Apple | Apple/Apple.list | 16 | 16 | 0 | 0 | 0 |
| BiliBiliIntl | BiliBili/BiliBili.list | 5 | 4 | 1 | 0 | 0 |
| GitLab | GitLab/GitLab.list | 1 | 1 | 0 | 0 | 0 |
| Microsoft | Microsoft/Microsoft.list | 80 | 80 | 0 | 0 | 0 |
| NetEaseMusic | NetEaseMusic/NetEaseMusic.list | 2 | 2 | 0 | 0 | 0 |
| Telegram | Telegram/Telegram.list | 14 | 14 | 0 | 0 | 0 |

## Static security checks

- duplicate_rule_lines: 0
- single_label_suffix: 912
- stale_or_private_root_suffix: 17
- unsupported_or_missing_operand: 1330757
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:8: .0.101tubeporn.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:9: .0.code.cotsta.ru
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:10: .0.cosmicnewspulse.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:11: .0.myikas.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:12: .0.net.easyjet.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:13: .0000.5clo0xmbf.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:14: .0000.833enmhob.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:15: .0006.4puuqeh41.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:16: .0012.4puuqeh41.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:17: .0013.79j68qav2.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:18: .0015.cosmicnewspulse.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:19: .0018.5clo0xmbf.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:20: .0019.833enmhob.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:21: .0019x.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:22: .0023.5clo0xmbf.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:23: .0024.seponews.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:24: .0025.4puuqeh41.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:25: .002777.xyz
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:26: .0033.5clo0xmbf.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:27: .0035.bestinterestings.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:28: .0038.79j68qav2.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:29: .0039.k3718qw08.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:30: .003store.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:31: .0040.5clo0xmbf.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:32: .00404850.xyz
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:33: .0041.5clo0xmbf.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:34: .0049.ohhmyoffers.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:35: .0054.4puuqeh41.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:36: .0058.4puuqeh41.com
  - AdGuardSDNSFilter/AdGuardSDNSFilter_Domain.list:37: .0072.4puuqeh41.com

- Financial-domain matches: 160 (review only; not deleted)
- URLhaus domains loaded: 0
- OpenPhish domains loaded: 278
- Reputation matches shown: 61 (max 500); scope counts: {'app_or_routing': 61}
- Reputation-feed matches are review flags, not automatic deletions. Matches in block/filter lists may be intentional; app/routing matches need manual review.

## Exact duplicate files

ChinaMaxNoIP/ChinaMaxNoIP_All.list, ChinaMaxNoIP/ChinaMaxNoIP_All_No_Resolve.list
EasyPrivacy/EasyPrivacy_All.list, EasyPrivacy/EasyPrivacy_All_No_Resolve.list

## Identical rule payloads with headers ignored

Abema/Abema.list, AbemaTV/AbemaTV.list
AdGuardSDNSFilter/AdGuardSDNSFilter_All.list, AdGuardSDNSFilter/AdGuardSDNSFilter_All_No_Resolve.list
Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list, Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list
Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list, Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list
Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list, Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list
Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list, Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list
BardAI/BardAI.list, Gemini/Gemini.list
ChinaMaxNoIP/ChinaMaxNoIP_All.list, ChinaMaxNoIP/ChinaMaxNoIP_All_No_Resolve.list
EasyPrivacy/EasyPrivacy_All.list, EasyPrivacy/EasyPrivacy_All_No_Resolve.list
GlobalScholar/GlobalScholar.list, Scholar/Scholar.list
PChome/PChome.list, PChomeTW/PChomeTW.list

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
- Game/Assassin'sCreed-Odyssey: resolve, standard (2 files)
- Game/Assassin'sCreed-Origins: resolve, standard (2 files)
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
- TelegramNL: resolve, standard (2 files)
- TelegramSG: resolve, standard (2 files)
- TelegramUS: resolve, standard (2 files)
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
- iQIYIIntl: resolve, standard (2 files)

## Safety boundaries
- No rule files or personal files are deleted, renamed, or rewritten by this audit.
- Bank/payment classification applies to dedicated App folders only; domains embedded in other Apps remain untouched.
- Regional variants are candidates for consolidation into one App policy group; country selection belongs in the Surge policy group, not separate rule folders.
- Resolve / non-Resolve and other distinct formats are compared and preserved separately.
- Similarity, shared CDN domains, or parent-company ownership alone never authorizes cross-App merging.
