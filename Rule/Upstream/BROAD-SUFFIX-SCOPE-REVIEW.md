# Broad public-TLD suffix scope review

Generated from CLEANUP-INVENTORY.json (2026-11-27 13:46 UTC UTC).

## Executive result

- 78 distinct single-label DOMAIN-SUFFIX values; all 78 were present in the IANA root-zone list used by the inventory check.
- 896 rule occurrences across files and formats. This is not 896 unique App rules; the same rule may be mirrored across Standard/Resolve/All formats.
- 35 of the 78 values are IDN/punycode TLDs.
- No rule was deleted, rewritten, or quarantined by this review.
- IANA delegation confirms that the suffix exists; it does not establish that using the whole TLD namespace is appropriate for every routing scenario.

## Scope classification

| Scope | Distinct suffixes | Rule occurrences | Interpretation |
|---|---:|---:|---|
| China aggregate only | 45 | 767 | Broad geo/aggregate namespace rules; review intended coverage, not malformed syntax |
| Mixed China aggregate and App folders | 5 | 85 | Shared between aggregate lists and a named App; verify App-specific intent |
| Other App/aggregate folders | 28 | 44 | Mostly brand TLDs or other named service/aggregate scopes |

China aggregate folders used for this classification: China, ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaNoMedia, and ChinaTest.

## Full suffix inventory

| Suffix | Occurrences | Scope | Folders |
|---|---:|---|---|
| alibaba | 21 | Mixed: China aggregate + App | Alibaba, ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| alipay | 11 | Mixed: China aggregate + App | AliPay, ChinaMax, ChinaTest |
| amazon | 2 | Other App/aggregate | Amazon |
| anquan | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| aws | 2 | Other App/aggregate | Amazon |
| azure | 1 | Other App/aggregate | Microsoft |
| baidu | 10 | China aggregate only | ChinaMax, ChinaTest |
| bbc | 2 | Other App/aggregate | BBC, UKMedia |
| bing | 1 | Other App/aggregate | Microsoft |
| bmw | 1 | Other App/aggregate | BMW |
| cisco | 1 | Other App/aggregate | Cisco |
| citic | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| cn | 25 | China aggregate only | China, ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaNoMedia, ChinaTest |
| fox | 1 | Other App/aggregate | Fox |
| google | 2 | Other App/aggregate | ProxyLite |
| hotmail | 1 | Other App/aggregate | Microsoft |
| ibm | 1 | Other App/aggregate | IBM |
| icbc | 18 | Mixed: China aggregate + App | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest, ICBC |
| imdb | 2 | Other App/aggregate | Amazon |
| java | 1 | Other App/aggregate | Oracle |
| kindle | 2 | Other App/aggregate | Amazon |
| microsoft | 1 | Other App/aggregate | Microsoft |
| mini | 1 | Other App/aggregate | BMW |
| mit | 1 | Other App/aggregate | GlobalScholar |
| ms | 25 | China aggregate only | China, ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaNoMedia, ChinaTest |
| office | 1 | Other App/aggregate | Microsoft |
| oracle | 1 | Other App/aggregate | Oracle |
| shouji | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| sina | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| skype | 1 | Other App/aggregate | Microsoft |
| sohu | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| taobao | 14 | Mixed: China aggregate + App | Alibaba, ChinaMax, ChinaTest |
| tmall | 21 | Mixed: China aggregate + App | Alibaba, ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| unicom | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| wang | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| weatherchannel | 1 | Other App/aggregate | IBM |
| weibo | 10 | China aggregate only | ChinaMax, ChinaTest |
| windows | 1 | Other App/aggregate | Microsoft |
| xn--1qqw23a | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--3bst00m | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--3ds443g | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--55qw42g | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--55qx5d | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--5tzm5g | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--6frz82g | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--6qq986b3xl | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--8y0a063a | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--9et52u | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--9krt00a | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--cckwcxetd | 2 | Other App/aggregate | Amazon |
| xn--czr694b | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--czrs0t | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--czru2d | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--fiq228c5hs | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--fiq64b | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--fiqs8s | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--fiqz9s | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--fjq720a | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--g2xx48c | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--hxt814e | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--imr513n | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--io0a7i | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--jlq480n2rg | 2 | Other App/aggregate | Amazon |
| xn--kput3i | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--nyqy26a | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--otu796d | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--rhqv96g | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--ses554g | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--unup4y | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--vhquv | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--vuq861b | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--xhq521b | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| xn--zfr164b | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| yamaxun | 2 | Other App/aggregate | Amazon |
| yandex | 2 | Other App/aggregate | Yandex |
| youtube | 6 | Other App/aggregate | GlobalMedia, YouTube |
| yun | 17 | China aggregate only | ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaTest |
| zappos | 2 | Other App/aggregate | Amazon |

## Handling decision

1. Do not remove these rules solely because the operand has one label. They are valid delegated TLDs in the IANA snapshot.
2. The highest-scope review target is the China aggregate family: .cn, .ms, and the listed brand/IDN TLDs can match every registered name beneath those TLDs.
3. The five mixed entries (alibaba, alipay, icbc, taobao, tmall) appear both in China aggregate folders and named App folders. Do not delete either copy without a scenario-specific decision.
4. Brand TLDs such as .amazon, .bbc, .bmw, .microsoft, .youtube, and .yandex may be appropriate in their corresponding service rules, but still match the entire delegated TLD namespace.
5. Re-run this review whenever the upstream .list files or IANA reference snapshot changes.

## Source and limitations

- Source inventory: Rule/Upstream/CLEANUP-INVENTORY.json.
- The inventory's IANA check found zero stale/private root suffixes.
- This is a routing-scope audit, not a reputation or threat verdict.
- Shared hosting and threat-feed matches are handled separately in SECURITY-REVIEW.md.
