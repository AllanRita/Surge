# Broad public-TLD suffix scope review

Generated from the current `CLEANUP-INVENTORY.json` snapshot (`2026-11-27 13:46 UTC`). This is a **report-only routing-scope review**: no rule file was modified, removed, merged, or restored.

## Summary

| Scope | Distinct suffixes | Rule occurrences |
|---|---:|---:|
| Aggregate-only | 45 | 767 |
| Mixed aggregate + App | 5 | 85 |
| App/service-only | 28 | 44 |

Total: **78 distinct IANA-delegated bare public-TLD suffixes**, **896 rule occurrences**. Counts include format variants and therefore are rule occurrences, not unique semantic rules.

The six aggregate containers used for classification are: `China`, `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaNoMedia`, and `ChinaTest`. Classification describes where a suffix occurs; it does not label the rule as wrong or malicious.

## Aggregate-only

### `cn` — 25 occurrences

- Folders: `China`, `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaNoMedia`, `ChinaTest`
- Example rules:
  - `China/China.list:12: DOMAIN-SUFFIX,cn`
  - `China/China_All.list:969: DOMAIN-SUFFIX,cn`
  - `China/China_All_No_Resolve.list:969: DOMAIN-SUFFIX,cn`
  - `China/China_Resolve.list:12: DOMAIN-SUFFIX,cn`

### `ms` — 25 occurrences

- Folders: `China`, `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaNoMedia`, `ChinaTest`
- Example rules:
  - `China/China.list:13: DOMAIN-SUFFIX,ms`
  - `China/China_All.list:2373: DOMAIN-SUFFIX,ms`
  - `China/China_All_No_Resolve.list:2373: DOMAIN-SUFFIX,ms`
  - `China/China_Resolve.list:13: DOMAIN-SUFFIX,ms`

### `anquan` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:18: DOMAIN-SUFFIX,anquan`
  - `ChinaMax/ChinaMax_All.list:15483: DOMAIN-SUFFIX,anquan`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:15483: DOMAIN-SUFFIX,anquan`
  - `ChinaMax/ChinaMax_No_IPv6.list:17: DOMAIN-SUFFIX,anquan`

### `citic` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:20: DOMAIN-SUFFIX,citic`
  - `ChinaMax/ChinaMax_All.list:25444: DOMAIN-SUFFIX,citic`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:25444: DOMAIN-SUFFIX,citic`
  - `ChinaMax/ChinaMax_No_IPv6.list:19: DOMAIN-SUFFIX,citic`

### `shouji` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:22: DOMAIN-SUFFIX,shouji`
  - `ChinaMax/ChinaMax_All.list:80872: DOMAIN-SUFFIX,shouji`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:80872: DOMAIN-SUFFIX,shouji`
  - `ChinaMax/ChinaMax_No_IPv6.list:21: DOMAIN-SUFFIX,shouji`

### `sina` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:23: DOMAIN-SUFFIX,sina`
  - `ChinaMax/ChinaMax_All.list:81739: DOMAIN-SUFFIX,sina`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:81739: DOMAIN-SUFFIX,sina`
  - `ChinaMax/ChinaMax_No_IPv6.list:22: DOMAIN-SUFFIX,sina`

### `sohu` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:24: DOMAIN-SUFFIX,sohu`
  - `ChinaMax/ChinaMax_All.list:82857: DOMAIN-SUFFIX,sohu`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:82857: DOMAIN-SUFFIX,sohu`
  - `ChinaMax/ChinaMax_No_IPv6.list:23: DOMAIN-SUFFIX,sohu`

### `unicom` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:27: DOMAIN-SUFFIX,unicom`
  - `ChinaMax/ChinaMax_All.list:90333: DOMAIN-SUFFIX,unicom`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:90333: DOMAIN-SUFFIX,unicom`
  - `ChinaMax/ChinaMax_No_IPv6.list:26: DOMAIN-SUFFIX,unicom`

### `wang` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:28: DOMAIN-SUFFIX,wang`
  - `ChinaMax/ChinaMax_All.list:92173: DOMAIN-SUFFIX,wang`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:92173: DOMAIN-SUFFIX,wang`
  - `ChinaMax/ChinaMax_No_IPv6.list:27: DOMAIN-SUFFIX,wang`

### `xn--1qqw23a` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:30: DOMAIN-SUFFIX,xn--1qqw23a`
  - `ChinaMax/ChinaMax_All.list:98585: DOMAIN-SUFFIX,xn--1qqw23a`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98585: DOMAIN-SUFFIX,xn--1qqw23a`
  - `ChinaMax/ChinaMax_No_IPv6.list:29: DOMAIN-SUFFIX,xn--1qqw23a`

### `xn--3bst00m` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:31: DOMAIN-SUFFIX,xn--3bst00m`
  - `ChinaMax/ChinaMax_All.list:98594: DOMAIN-SUFFIX,xn--3bst00m`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98594: DOMAIN-SUFFIX,xn--3bst00m`
  - `ChinaMax/ChinaMax_No_IPv6.list:30: DOMAIN-SUFFIX,xn--3bst00m`

### `xn--3ds443g` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:32: DOMAIN-SUFFIX,xn--3ds443g`
  - `ChinaMax/ChinaMax_All.list:98597: DOMAIN-SUFFIX,xn--3ds443g`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98597: DOMAIN-SUFFIX,xn--3ds443g`
  - `ChinaMax/ChinaMax_No_IPv6.list:31: DOMAIN-SUFFIX,xn--3ds443g`

### `xn--55qw42g` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:33: DOMAIN-SUFFIX,xn--55qw42g`
  - `ChinaMax/ChinaMax_All.list:98607: DOMAIN-SUFFIX,xn--55qw42g`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98607: DOMAIN-SUFFIX,xn--55qw42g`
  - `ChinaMax/ChinaMax_No_IPv6.list:32: DOMAIN-SUFFIX,xn--55qw42g`

### `xn--55qx5d` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:34: DOMAIN-SUFFIX,xn--55qx5d`
  - `ChinaMax/ChinaMax_All.list:98610: DOMAIN-SUFFIX,xn--55qx5d`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98610: DOMAIN-SUFFIX,xn--55qx5d`
  - `ChinaMax/ChinaMax_No_IPv6.list:33: DOMAIN-SUFFIX,xn--55qx5d`

### `xn--5tzm5g` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:35: DOMAIN-SUFFIX,xn--5tzm5g`
  - `ChinaMax/ChinaMax_All.list:98613: DOMAIN-SUFFIX,xn--5tzm5g`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98613: DOMAIN-SUFFIX,xn--5tzm5g`
  - `ChinaMax/ChinaMax_No_IPv6.list:34: DOMAIN-SUFFIX,xn--5tzm5g`

### `xn--6frz82g` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:36: DOMAIN-SUFFIX,xn--6frz82g`
  - `ChinaMax/ChinaMax_All.list:98616: DOMAIN-SUFFIX,xn--6frz82g`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98616: DOMAIN-SUFFIX,xn--6frz82g`
  - `ChinaMax/ChinaMax_No_IPv6.list:35: DOMAIN-SUFFIX,xn--6frz82g`

### `xn--6qq986b3xl` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:37: DOMAIN-SUFFIX,xn--6qq986b3xl`
  - `ChinaMax/ChinaMax_All.list:98620: DOMAIN-SUFFIX,xn--6qq986b3xl`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98620: DOMAIN-SUFFIX,xn--6qq986b3xl`
  - `ChinaMax/ChinaMax_No_IPv6.list:36: DOMAIN-SUFFIX,xn--6qq986b3xl`

### `xn--8y0a063a` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:38: DOMAIN-SUFFIX,xn--8y0a063a`
  - `ChinaMax/ChinaMax_All.list:98632: DOMAIN-SUFFIX,xn--8y0a063a`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98632: DOMAIN-SUFFIX,xn--8y0a063a`
  - `ChinaMax/ChinaMax_No_IPv6.list:37: DOMAIN-SUFFIX,xn--8y0a063a`

### `xn--9et52u` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:39: DOMAIN-SUFFIX,xn--9et52u`
  - `ChinaMax/ChinaMax_All.list:98634: DOMAIN-SUFFIX,xn--9et52u`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98634: DOMAIN-SUFFIX,xn--9et52u`
  - `ChinaMax/ChinaMax_No_IPv6.list:38: DOMAIN-SUFFIX,xn--9et52u`

### `xn--9krt00a` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:40: DOMAIN-SUFFIX,xn--9krt00a`
  - `ChinaMax/ChinaMax_All.list:98636: DOMAIN-SUFFIX,xn--9krt00a`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98636: DOMAIN-SUFFIX,xn--9krt00a`
  - `ChinaMax/ChinaMax_No_IPv6.list:39: DOMAIN-SUFFIX,xn--9krt00a`

### `xn--czr694b` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:41: DOMAIN-SUFFIX,xn--czr694b`
  - `ChinaMax/ChinaMax_All.list:98652: DOMAIN-SUFFIX,xn--czr694b`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98652: DOMAIN-SUFFIX,xn--czr694b`
  - `ChinaMax/ChinaMax_No_IPv6.list:40: DOMAIN-SUFFIX,xn--czr694b`

### `xn--czrs0t` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:42: DOMAIN-SUFFIX,xn--czrs0t`
  - `ChinaMax/ChinaMax_All.list:98653: DOMAIN-SUFFIX,xn--czrs0t`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98653: DOMAIN-SUFFIX,xn--czrs0t`
  - `ChinaMax/ChinaMax_No_IPv6.list:41: DOMAIN-SUFFIX,xn--czrs0t`

### `xn--czru2d` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:43: DOMAIN-SUFFIX,xn--czru2d`
  - `ChinaMax/ChinaMax_All.list:98654: DOMAIN-SUFFIX,xn--czru2d`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98654: DOMAIN-SUFFIX,xn--czru2d`
  - `ChinaMax/ChinaMax_No_IPv6.list:42: DOMAIN-SUFFIX,xn--czru2d`

### `xn--fiq228c5hs` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:44: DOMAIN-SUFFIX,xn--fiq228c5hs`
  - `ChinaMax/ChinaMax_All.list:98669: DOMAIN-SUFFIX,xn--fiq228c5hs`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98669: DOMAIN-SUFFIX,xn--fiq228c5hs`
  - `ChinaMax/ChinaMax_No_IPv6.list:43: DOMAIN-SUFFIX,xn--fiq228c5hs`

### `xn--fiq64b` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:45: DOMAIN-SUFFIX,xn--fiq64b`
  - `ChinaMax/ChinaMax_All.list:98671: DOMAIN-SUFFIX,xn--fiq64b`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98671: DOMAIN-SUFFIX,xn--fiq64b`
  - `ChinaMax/ChinaMax_No_IPv6.list:44: DOMAIN-SUFFIX,xn--fiq64b`

### `xn--fiqs8s` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:46: DOMAIN-SUFFIX,xn--fiqs8s`
  - `ChinaMax/ChinaMax_All.list:98675: DOMAIN-SUFFIX,xn--fiqs8s`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98675: DOMAIN-SUFFIX,xn--fiqs8s`
  - `ChinaMax/ChinaMax_No_IPv6.list:45: DOMAIN-SUFFIX,xn--fiqs8s`

### `xn--fiqz9s` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:47: DOMAIN-SUFFIX,xn--fiqz9s`
  - `ChinaMax/ChinaMax_All.list:98680: DOMAIN-SUFFIX,xn--fiqz9s`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98680: DOMAIN-SUFFIX,xn--fiqz9s`
  - `ChinaMax/ChinaMax_No_IPv6.list:46: DOMAIN-SUFFIX,xn--fiqz9s`

### `xn--fjq720a` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:48: DOMAIN-SUFFIX,xn--fjq720a`
  - `ChinaMax/ChinaMax_All.list:98682: DOMAIN-SUFFIX,xn--fjq720a`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98682: DOMAIN-SUFFIX,xn--fjq720a`
  - `ChinaMax/ChinaMax_No_IPv6.list:47: DOMAIN-SUFFIX,xn--fjq720a`

### `xn--g2xx48c` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:49: DOMAIN-SUFFIX,xn--g2xx48c`
  - `ChinaMax/ChinaMax_All.list:98683: DOMAIN-SUFFIX,xn--g2xx48c`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98683: DOMAIN-SUFFIX,xn--g2xx48c`
  - `ChinaMax/ChinaMax_No_IPv6.list:48: DOMAIN-SUFFIX,xn--g2xx48c`

### `xn--hxt814e` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:50: DOMAIN-SUFFIX,xn--hxt814e`
  - `ChinaMax/ChinaMax_All.list:98691: DOMAIN-SUFFIX,xn--hxt814e`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98691: DOMAIN-SUFFIX,xn--hxt814e`
  - `ChinaMax/ChinaMax_No_IPv6.list:49: DOMAIN-SUFFIX,xn--hxt814e`

### `xn--imr513n` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:51: DOMAIN-SUFFIX,xn--imr513n`
  - `ChinaMax/ChinaMax_All.list:98696: DOMAIN-SUFFIX,xn--imr513n`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98696: DOMAIN-SUFFIX,xn--imr513n`
  - `ChinaMax/ChinaMax_No_IPv6.list:50: DOMAIN-SUFFIX,xn--imr513n`

### `xn--io0a7i` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:52: DOMAIN-SUFFIX,xn--io0a7i`
  - `ChinaMax/ChinaMax_All.list:98697: DOMAIN-SUFFIX,xn--io0a7i`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98697: DOMAIN-SUFFIX,xn--io0a7i`
  - `ChinaMax/ChinaMax_No_IPv6.list:51: DOMAIN-SUFFIX,xn--io0a7i`

### `xn--kput3i` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:53: DOMAIN-SUFFIX,xn--kput3i`
  - `ChinaMax/ChinaMax_All.list:98705: DOMAIN-SUFFIX,xn--kput3i`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98705: DOMAIN-SUFFIX,xn--kput3i`
  - `ChinaMax/ChinaMax_No_IPv6.list:52: DOMAIN-SUFFIX,xn--kput3i`

### `xn--nyqy26a` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:54: DOMAIN-SUFFIX,xn--nyqy26a`
  - `ChinaMax/ChinaMax_All.list:98721: DOMAIN-SUFFIX,xn--nyqy26a`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98721: DOMAIN-SUFFIX,xn--nyqy26a`
  - `ChinaMax/ChinaMax_No_IPv6.list:53: DOMAIN-SUFFIX,xn--nyqy26a`

### `xn--otu796d` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:55: DOMAIN-SUFFIX,xn--otu796d`
  - `ChinaMax/ChinaMax_All.list:98723: DOMAIN-SUFFIX,xn--otu796d`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98723: DOMAIN-SUFFIX,xn--otu796d`
  - `ChinaMax/ChinaMax_No_IPv6.list:54: DOMAIN-SUFFIX,xn--otu796d`

### `xn--rhqv96g` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:56: DOMAIN-SUFFIX,xn--rhqv96g`
  - `ChinaMax/ChinaMax_All.list:98732: DOMAIN-SUFFIX,xn--rhqv96g`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98732: DOMAIN-SUFFIX,xn--rhqv96g`
  - `ChinaMax/ChinaMax_No_IPv6.list:55: DOMAIN-SUFFIX,xn--rhqv96g`

### `xn--ses554g` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:57: DOMAIN-SUFFIX,xn--ses554g`
  - `ChinaMax/ChinaMax_All.list:98742: DOMAIN-SUFFIX,xn--ses554g`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98742: DOMAIN-SUFFIX,xn--ses554g`
  - `ChinaMax/ChinaMax_No_IPv6.list:56: DOMAIN-SUFFIX,xn--ses554g`

### `xn--unup4y` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:58: DOMAIN-SUFFIX,xn--unup4y`
  - `ChinaMax/ChinaMax_All.list:98752: DOMAIN-SUFFIX,xn--unup4y`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98752: DOMAIN-SUFFIX,xn--unup4y`
  - `ChinaMax/ChinaMax_No_IPv6.list:57: DOMAIN-SUFFIX,xn--unup4y`

### `xn--vhquv` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:59: DOMAIN-SUFFIX,xn--vhquv`
  - `ChinaMax/ChinaMax_All.list:98761: DOMAIN-SUFFIX,xn--vhquv`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98761: DOMAIN-SUFFIX,xn--vhquv`
  - `ChinaMax/ChinaMax_No_IPv6.list:58: DOMAIN-SUFFIX,xn--vhquv`

### `xn--vuq861b` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:60: DOMAIN-SUFFIX,xn--vuq861b`
  - `ChinaMax/ChinaMax_All.list:98764: DOMAIN-SUFFIX,xn--vuq861b`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98764: DOMAIN-SUFFIX,xn--vuq861b`
  - `ChinaMax/ChinaMax_No_IPv6.list:59: DOMAIN-SUFFIX,xn--vuq861b`

### `xn--xhq521b` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:61: DOMAIN-SUFFIX,xn--xhq521b`
  - `ChinaMax/ChinaMax_All.list:98771: DOMAIN-SUFFIX,xn--xhq521b`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98771: DOMAIN-SUFFIX,xn--xhq521b`
  - `ChinaMax/ChinaMax_No_IPv6.list:60: DOMAIN-SUFFIX,xn--xhq521b`

### `xn--zfr164b` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:62: DOMAIN-SUFFIX,xn--zfr164b`
  - `ChinaMax/ChinaMax_All.list:98789: DOMAIN-SUFFIX,xn--zfr164b`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:98789: DOMAIN-SUFFIX,xn--zfr164b`
  - `ChinaMax/ChinaMax_No_IPv6.list:61: DOMAIN-SUFFIX,xn--zfr164b`

### `yun` — 17 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:63: DOMAIN-SUFFIX,yun`
  - `ChinaMax/ChinaMax_All.list:103700: DOMAIN-SUFFIX,yun`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:103700: DOMAIN-SUFFIX,yun`
  - `ChinaMax/ChinaMax_No_IPv6.list:62: DOMAIN-SUFFIX,yun`

### `baidu` — 10 occurrences

- Folders: `ChinaMax`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:19: DOMAIN-SUFFIX,baidu`
  - `ChinaMax/ChinaMax_All.list:17117: DOMAIN-SUFFIX,baidu`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:17117: DOMAIN-SUFFIX,baidu`
  - `ChinaMax/ChinaMax_No_IPv6.list:18: DOMAIN-SUFFIX,baidu`

### `weibo` — 10 occurrences

- Folders: `ChinaMax`, `ChinaTest`
- Example rules:
  - `ChinaMax/ChinaMax.list:29: DOMAIN-SUFFIX,weibo`
  - `ChinaMax/ChinaMax_All.list:92879: DOMAIN-SUFFIX,weibo`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:92879: DOMAIN-SUFFIX,weibo`
  - `ChinaMax/ChinaMax_No_IPv6.list:28: DOMAIN-SUFFIX,weibo`

## Mixed aggregate + App

### `alibaba` — 21 occurrences

- Folders: `Alibaba`, `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `Alibaba/Alibaba.list:10: DOMAIN-SUFFIX,alibaba`
  - `Alibaba/Alibaba_All.list:34: DOMAIN-SUFFIX,alibaba`
  - `Alibaba/Alibaba_All_No_Resolve.list:34: DOMAIN-SUFFIX,alibaba`
  - `Alibaba/Alibaba_Resolve.list:10: DOMAIN-SUFFIX,alibaba`

### `tmall` — 21 occurrences

- Folders: `Alibaba`, `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`
- Example rules:
  - `Alibaba/Alibaba.list:12: DOMAIN-SUFFIX,tmall`
  - `Alibaba/Alibaba_All.list:1158: DOMAIN-SUFFIX,tmall`
  - `Alibaba/Alibaba_All_No_Resolve.list:1158: DOMAIN-SUFFIX,tmall`
  - `Alibaba/Alibaba_Resolve.list:12: DOMAIN-SUFFIX,tmall`

### `icbc` — 18 occurrences

- Folders: `ChinaMax`, `ChinaMaxNoIP`, `ChinaMaxNoMedia`, `ChinaTest`, `ICBC`
- Example rules:
  - `ChinaMax/ChinaMax.list:21: DOMAIN-SUFFIX,icbc`
  - `ChinaMax/ChinaMax_All.list:50893: DOMAIN-SUFFIX,icbc`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:50893: DOMAIN-SUFFIX,icbc`
  - `ChinaMax/ChinaMax_No_IPv6.list:20: DOMAIN-SUFFIX,icbc`

### `taobao` — 14 occurrences

- Folders: `Alibaba`, `ChinaMax`, `ChinaTest`
- Example rules:
  - `Alibaba/Alibaba.list:11: DOMAIN-SUFFIX,taobao`
  - `Alibaba/Alibaba_All.list:1122: DOMAIN-SUFFIX,taobao`
  - `Alibaba/Alibaba_All_No_Resolve.list:1122: DOMAIN-SUFFIX,taobao`
  - `Alibaba/Alibaba_Resolve.list:11: DOMAIN-SUFFIX,taobao`

### `alipay` — 11 occurrences

- Folders: `AliPay`, `ChinaMax`, `ChinaTest`
- Example rules:
  - `AliPay/AliPay.list:7: DOMAIN-SUFFIX,alipay`
  - `ChinaMax/ChinaMax.list:17: DOMAIN-SUFFIX,alipay`
  - `ChinaMax/ChinaMax_All.list:14885: DOMAIN-SUFFIX,alipay`
  - `ChinaMax/ChinaMax_All_No_Resolve.list:14885: DOMAIN-SUFFIX,alipay`

## App/service-only

### `youtube` — 6 occurrences

- Folders: `GlobalMedia`, `YouTube`
- Example rules:
  - `GlobalMedia/GlobalMedia.list:15: DOMAIN-SUFFIX,youtube`
  - `GlobalMedia/GlobalMedia_All.list:1157: DOMAIN-SUFFIX,youtube`
  - `GlobalMedia/GlobalMedia_All_No_Resolve.list:1157: DOMAIN-SUFFIX,youtube`
  - `GlobalMedia/GlobalMedia_Resolve.list:15: DOMAIN-SUFFIX,youtube`

### `amazon` — 2 occurrences

- Folders: `Amazon`
- Example rules:
  - `Amazon/Amazon.list:37: DOMAIN-SUFFIX,amazon`
  - `Amazon/Amazon_Resolve.list:37: DOMAIN-SUFFIX,amazon`

### `aws` — 2 occurrences

- Folders: `Amazon`
- Example rules:
  - `Amazon/Amazon.list:119: DOMAIN-SUFFIX,aws`
  - `Amazon/Amazon_Resolve.list:119: DOMAIN-SUFFIX,aws`

### `bbc` — 2 occurrences

- Folders: `BBC`, `UKMedia`
- Example rules:
  - `BBC/BBC.list:21: DOMAIN-SUFFIX,bbc`
  - `UKMedia/UKMedia.list:17: DOMAIN-SUFFIX,bbc`

### `google` — 2 occurrences

- Folders: `ProxyLite`
- Example rules:
  - `ProxyLite/ProxyLite.list:320: DOMAIN-SUFFIX,google`
  - `ProxyLite/ProxyLite_Resolve.list:320: DOMAIN-SUFFIX,google`

### `imdb` — 2 occurrences

- Folders: `Amazon`
- Example rules:
  - `Amazon/Amazon.list:146: DOMAIN-SUFFIX,imdb`
  - `Amazon/Amazon_Resolve.list:146: DOMAIN-SUFFIX,imdb`

### `kindle` — 2 occurrences

- Folders: `Amazon`
- Example rules:
  - `Amazon/Amazon.list:149: DOMAIN-SUFFIX,kindle`
  - `Amazon/Amazon_Resolve.list:149: DOMAIN-SUFFIX,kindle`

### `xn--cckwcxetd` — 2 occurrences

- Folders: `Amazon`
- Example rules:
  - `Amazon/Amazon.list:194: DOMAIN-SUFFIX,xn--cckwcxetd`
  - `Amazon/Amazon_Resolve.list:194: DOMAIN-SUFFIX,xn--cckwcxetd`

### `xn--jlq480n2rg` — 2 occurrences

- Folders: `Amazon`
- Example rules:
  - `Amazon/Amazon.list:195: DOMAIN-SUFFIX,xn--jlq480n2rg`
  - `Amazon/Amazon_Resolve.list:195: DOMAIN-SUFFIX,xn--jlq480n2rg`

### `yamaxun` — 2 occurrences

- Folders: `Amazon`
- Example rules:
  - `Amazon/Amazon.list:196: DOMAIN-SUFFIX,yamaxun`
  - `Amazon/Amazon_Resolve.list:196: DOMAIN-SUFFIX,yamaxun`

### `yandex` — 2 occurrences

- Folders: `Yandex`
- Example rules:
  - `Yandex/Yandex.list:12: DOMAIN-SUFFIX,yandex`
  - `Yandex/Yandex_Resolve.list:12: DOMAIN-SUFFIX,yandex`

### `zappos` — 2 occurrences

- Folders: `Amazon`
- Example rules:
  - `Amazon/Amazon.list:200: DOMAIN-SUFFIX,zappos`
  - `Amazon/Amazon_Resolve.list:200: DOMAIN-SUFFIX,zappos`

### `azure` — 1 occurrences

- Folders: `Microsoft`
- Example rules:
  - `Microsoft/Microsoft.list:46: DOMAIN-SUFFIX,azure`

### `bing` — 1 occurrences

- Folders: `Microsoft`
- Example rules:
  - `Microsoft/Microsoft.list:117: DOMAIN-SUFFIX,bing`

### `bmw` — 1 occurrences

- Folders: `BMW`
- Example rules:
  - `BMW/BMW.list:77: DOMAIN-SUFFIX,bmw`

### `cisco` — 1 occurrences

- Folders: `Cisco`
- Example rules:
  - `Cisco/Cisco.list:20: DOMAIN-SUFFIX,cisco`

### `fox` — 1 occurrences

- Folders: `Fox`
- Example rules:
  - `Fox/Fox.list:16: DOMAIN-SUFFIX,fox`

### `hotmail` — 1 occurrences

- Folders: `Microsoft`
- Example rules:
  - `Microsoft/Microsoft.list:222: DOMAIN-SUFFIX,hotmail`

### `ibm` — 1 occurrences

- Folders: `IBM`
- Example rules:
  - `IBM/IBM.list:10: DOMAIN-SUFFIX,ibm`

### `java` — 1 occurrences

- Folders: `Oracle`
- Example rules:
  - `Oracle/Oracle.list:21: DOMAIN-SUFFIX,java`

### `microsoft` — 1 occurrences

- Folders: `Microsoft`
- Example rules:
  - `Microsoft/Microsoft.list:276: DOMAIN-SUFFIX,microsoft`

### `mini` — 1 occurrences

- Folders: `BMW`
- Example rules:
  - `BMW/BMW.list:494: DOMAIN-SUFFIX,mini`

### `mit` — 1 occurrences

- Folders: `GlobalScholar`
- Example rules:
  - `GlobalScholar/GlobalScholar.list:136: DOMAIN-SUFFIX,mit`

### `office` — 1 occurrences

- Folders: `Microsoft`
- Example rules:
  - `Microsoft/Microsoft.list:491: DOMAIN-SUFFIX,office`

### `oracle` — 1 occurrences

- Folders: `Oracle`
- Example rules:
  - `Oracle/Oracle.list:24: DOMAIN-SUFFIX,oracle`

### `skype` — 1 occurrences

- Folders: `Microsoft`
- Example rules:
  - `Microsoft/Microsoft.list:564: DOMAIN-SUFFIX,skype`

### `weatherchannel` — 1 occurrences

- Folders: `IBM`
- Example rules:
  - `IBM/IBM.list:18: DOMAIN-SUFFIX,weatherchannel`

### `windows` — 1 occurrences

- Folders: `Microsoft`
- Example rules:
  - `Microsoft/Microsoft.list:622: DOMAIN-SUFFIX,windows`

## Review guidance

1. **Aggregate-only** entries are the first priority for scenario review because a single-label suffix may intentionally route a broad public-TLD namespace in country/region aggregate lists. Confirm the intended region and traffic scope before any change.
2. **Mixed** entries require checking both the dedicated App folder and aggregate routing behavior. A rule in `AliPay` or `ICBC` must not be inferred to be redundant merely because the same suffix appears in `ChinaMax`.
3. **App/service-only** entries are still broad matches, but their effect is limited to the named App/service list. Validate ownership and actual service use before changing them.
4. Do not delete or narrow any suffix automatically. A delegated TLD is syntactically valid, but validity does not prove that routing the entire namespace is intended.
5. Preserve Standard, Resolve, All, No_IPv6, and other distinct variants. Compare within the same App only.


## OpenPhish correlation for the broad cn suffix (workflow run #45, 2026-11-27)

The batch security review identified **25 occurrences** of DOMAIN-SUFFIX,cn across the six aggregate folders China, ChinaMax, ChinaMaxNoIP, ChinaMaxNoMedia, ChinaNoMedia, and ChinaTest. These occurrences are the intended format/aggregate variants, not 25 unique domains.

OpenPhish contained three matched hostnames beneath the suffix:

- 6s8.aolade.cn
- gea.aolade.cn
- www.scxkjx.cn

All 25 records matched OpenPhish only. URLhaus remained unavailable (0 parsed hostnames), so this is incomplete threat-intelligence coverage, not dual-feed confirmation. The parent .cn suffix is review-only: no rule was deleted, narrowed, or rewritten. Do not infer that the entire .cn namespace is malicious from these three tenant/host matches.
