# App-level rule overlap report

Generated: 2026-11-27 09:57 UTC

- Rule files scanned: 853
- App/scenario candidate groups across categories: 11
- High-overlap cross-App pairs for manual review: 19

## Same App candidates across categories

Grouped by normalized app-folder name and scenario. A match is a review candidate, not permission to merge. Standard and Resolve are analyzed separately.

### abema (standard)
- Categories: Abema, AbemaTV
- Exact shared rule lines: 29; union: 29
- Same full rule set: yes
- Exact shared domain rules: 27; domain union: 27
- File: Rule/Upstream/Abema/Abema.list (29 total rules; 27 domain rules)
- File: Rule/Upstream/AbemaTV/AbemaTV.list (29 total rules; 27 domain rules)

### assassinscreedodyssey (resolve)
- Categories: Assassin'sCreed, Game
- Exact shared rule lines: 15; union: 15
- Same full rule set: yes
- Exact shared domain rules: 0; domain union: 0
- File: Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list (15 total rules; 0 domain rules)
- File: Rule/Upstream/Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey_Resolve.list (15 total rules; 0 domain rules)

### assassinscreedodyssey (standard)
- Categories: Assassin'sCreed, Game
- Exact shared rule lines: 15; union: 15
- Same full rule set: yes
- Exact shared domain rules: 0; domain union: 0
- File: Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list (15 total rules; 0 domain rules)
- File: Rule/Upstream/Game/Assassin'sCreed-Odyssey/Assassin'sCreed-Odyssey.list (15 total rules; 0 domain rules)

### assassinscreedorigins (resolve)
- Categories: Assassin'sCreed, Game
- Exact shared rule lines: 16; union: 16
- Same full rule set: yes
- Exact shared domain rules: 0; domain union: 0
- File: Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list (16 total rules; 0 domain rules)
- File: Rule/Upstream/Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins_Resolve.list (16 total rules; 0 domain rules)

### assassinscreedorigins (standard)
- Categories: Assassin'sCreed, Game
- Exact shared rule lines: 16; union: 16
- Same full rule set: yes
- Exact shared domain rules: 0; domain union: 0
- File: Rule/Upstream/Assassin'sCreed/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list (16 total rules; 0 domain rules)
- File: Rule/Upstream/Game/Assassin'sCreed-Origins/Assassin'sCreed-Origins.list (16 total rules; 0 domain rules)

### direct (standard)
- Categories: AdGuardSDNSFilter, Direct
- Exact shared rule lines: 4; union: 413
- Same full rule set: no
- Exact shared domain rules: 4; domain union: 340
- File: Rule/Upstream/AdGuardSDNSFilter/Direct/Direct.list (149 total rules; 149 domain rules)
- File: Rule/Upstream/Direct/Direct.list (268 total rules; 195 domain rules)
- Only in Rule/Upstream/AdGuardSDNSFilter/Direct/Direct.list: 145
  - DOMAIN,5471782.fls.doubleclick.net
  - DOMAIN,79423.analytics.edgekey.net
  - DOMAIN,a.adwolf.ru
  - DOMAIN,a.sellpoint.net
  - DOMAIN,ac.ebis.ne.jp
  - DOMAIN,acs-m.daraz.com.bd
  - DOMAIN,acs-m.daraz.pk
  - DOMAIN,action.metaffiliation.com
  - DOMAIN,ad.abchina.com
  - DOMAIN,ad.kazakinfo.com
  - DOMAIN,ad.ourgame.com
  - DOMAIN,adcdn.pingan.com
- Only in Rule/Upstream/Direct/Direct.list: 264
  - DOMAIN,ad.12306.cn
  - DOMAIN,ain.bgm.tv
  - DOMAIN,alt1-mtalk.google.com
  - DOMAIN,alt2-mtalk.google.com
  - DOMAIN,alt3-mtalk.google.com
  - DOMAIN,alt4-mtalk.google.com
  - DOMAIN,alt5-mtalk.google.com
  - DOMAIN,alt6-mtalk.google.com
  - DOMAIN,alt7-mtalk.google.com
  - DOMAIN,alt8-mtalk.google.com
  - DOMAIN,analytics.95516.com
  - DOMAIN,analytics.strava.com

### dns (standard)
- Categories: Block, DNS
- Exact shared rule lines: 0; union: 172
- Same full rule set: no
- Exact shared domain rules: 0; domain union: 125
- File: Rule/Upstream/Block/DNS/DNS.list (53 total rules; 32 domain rules)
- File: Rule/Upstream/DNS/DNS.list (119 total rules; 93 domain rules)
- Only in Rule/Upstream/Block/DNS/DNS.list: 53
  - DOMAIN,3dns-1.adobe.com
  - DOMAIN,3dns-2.adobe.com
  - DOMAIN,3dns-3.adobe.com
  - DOMAIN,3dns-4.adobe.com
  - DOMAIN,adobe-dns-1.adobe.com
  - DOMAIN,adobe-dns-2.adobe.com
  - DOMAIN,adobe-dns-3.adobe.com
  - DOMAIN,adobe-dns-4.adobe.com
  - DOMAIN,adobe-dns.adobe.com
  - DOMAIN,dns.jd.com
  - DOMAIN,dns.weibo.cn
  - DOMAIN,dns.weixin.qq.com
- Only in Rule/Upstream/DNS/DNS.list: 119
  - DOMAIN,1dot1dot1dot1.cloudflare-dns.com
  - DOMAIN,8888.google
  - DOMAIN,adblock.mydns.network
  - DOMAIN,applied-privacy.net
  - DOMAIN,cdn-doh.ssnm.xyz
  - DOMAIN,chrome.cloudflare-dns.com
  - DOMAIN,cloudflare-dns.com
  - DOMAIN,dns-family.adguard.com
  - DOMAIN,dns-nyc.aaflalo.me
  - DOMAIN,dns-tls.qis.io
  - DOMAIN,dns-unfiltered.adguard.com
  - DOMAIN,dns.aa.net.uk

### gemini (standard)
- Categories: BardAI, Gemini
- Exact shared rule lines: 14; union: 14
- Same full rule set: yes
- Exact shared domain rules: 11; domain union: 11
- File: Rule/Upstream/BardAI/BardAI.list (14 total rules; 11 domain rules)
- File: Rule/Upstream/Gemini/Gemini.list (14 total rules; 11 domain rules)

### globalscholar (standard)
- Categories: GlobalScholar, Scholar
- Exact shared rule lines: 231; union: 231
- Same full rule set: yes
- Exact shared domain rules: 231; domain union: 231
- File: Rule/Upstream/GlobalScholar/GlobalScholar.list (231 total rules; 231 domain rules)
- File: Rule/Upstream/Scholar/Scholar.list (231 total rules; 231 domain rules)

### pchome (standard)
- Categories: PChome, PChomeTW
- Exact shared rule lines: 5; union: 5
- Same full rule set: yes
- Exact shared domain rules: 5; domain union: 5
- File: Rule/Upstream/PChome/PChome.list (5 total rules; 5 domain rules)
- File: Rule/Upstream/PChomeTW/PChomeTW.list (5 total rules; 5 domain rules)

### youtube (standard)
- Categories: Block, YouTube
- Exact shared rule lines: 0; union: 205
- Same full rule set: no
- Exact shared domain rules: 0; domain union: 179
- File: Rule/Upstream/Block/YouTube/YouTube.list (15 total rules; 0 domain rules)
- File: Rule/Upstream/YouTube/YouTube.list (190 total rules; 179 domain rules)
- Only in Rule/Upstream/Block/YouTube/YouTube.list: 15
  - URL-REGEX,^https?://(www|s).youtube.com/(pagead|ptracking)
  - URL-REGEX,^https?://(www|s).youtube.com/api/stats/ads
  - URL-REGEX,^https?://.+.youtube.com/api/stats/.+adformat
  - URL-REGEX,^https?://.+.youtube.com/api/stats/ads
  - URL-REGEX,^https?://.+.youtube.com/get_midroll
  - URL-REGEX,^https?://.+.youtube.com/get_midroll_
  - URL-REGEX,^https?://.+.youtube.com/pagead/
  - URL-REGEX,^https?://.+.youtube.com/ptracking
  - URL-REGEX,^https?://.+.youtube.com/ptracking\?
  - URL-REGEX,^https?://[\w-]+.googlevideo.com/((?!(dclk_video_ads|videoplayback)).)+&(oad|ctier)
  - URL-REGEX,^https?://premiumyva.appspot.com/vmclickstoadvertisersite
  - URL-REGEX,^https?://s.youtube.com/api/stats/qoe?.*adformat
- Only in Rule/Upstream/YouTube/YouTube.list: 190
  - DOMAIN-KEYWORD,youtube
  - DOMAIN-SUFFIX,ggpht.cn
  - DOMAIN-SUFFIX,ggpht.com
  - DOMAIN-SUFFIX,googlevideo.com
  - DOMAIN-SUFFIX,gvt1.com
  - DOMAIN-SUFFIX,gvt2.com
  - DOMAIN-SUFFIX,video.google.com
  - DOMAIN-SUFFIX,wide-youtube.l.google.com
  - DOMAIN-SUFFIX,withyoutube.com
  - DOMAIN-SUFFIX,youtu.be
  - DOMAIN-SUFFIX,youtube
  - DOMAIN-SUFFIX,youtube-nocookie.com

## High-overlap cross-App candidates

Shared domains may be CDNs, identity providers, analytics, or other common infrastructure. Do not merge these lists solely because of overlap.

### Hulu vs HuluUSA
- Files: Rule/Upstream/Hulu/Hulu.list and Rule/Upstream/HuluUSA/HuluUSA.list
- Shared exact domain rules: 52; Jaccard: 0.90; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,112263.com, DOMAIN-SUFFIX,assetshuluimcom-a.akamaihd.net, DOMAIN-SUFFIX,callhulu.com, DOMAIN-SUFFIX,cws-hulu.conviva.com, DOMAIN-SUFFIX,findyourlimits.com, DOMAIN-SUFFIX,freehulu.com, DOMAIN-SUFFIX,hooloo.tv, DOMAIN-SUFFIX,hoolu.com

### DuoWan vs HuanJu
- Files: Rule/Upstream/DuoWan/DuoWan.list and Rule/Upstream/HuanJu/HuanJu.list
- Shared exact domain rules: 20; Jaccard: 0.74; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,5253.com, DOMAIN-SUFFIX,blogchina.org, DOMAIN-SUFFIX,c19ce66ff87253fdda68740edcb7ce3b.v.smtcdns.net, DOMAIN-SUFFIX,chinaduo.com, DOMAIN-SUFFIX,duowan.cn, DOMAIN-SUFFIX,duowan.com, DOMAIN-SUFFIX,duowan.com.cn, DOMAIN-SUFFIX,dwstatic.com

### Wikimedia vs Wikipedia
- Files: Rule/Upstream/Wikimedia/Wikimedia.list and Rule/Upstream/Wikipedia/Wikipedia.list
- Shared exact domain rules: 12; Jaccard: 0.60; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,mediawiki.org, DOMAIN-SUFFIX,wikibooks.org, DOMAIN-SUFFIX,wikidata.org, DOMAIN-SUFFIX,wikileaks.org, DOMAIN-SUFFIX,wikimedia.org, DOMAIN-SUFFIX,wikinews.org, DOMAIN-SUFFIX,wikipedia.org, DOMAIN-SUFFIX,wikiquote.org

### Copilot vs OpenAI
- Files: Rule/Upstream/Copilot/Copilot.list and Rule/Upstream/OpenAI/OpenAI.list
- Shared exact domain rules: 28; Jaccard: 0.57; smaller-set coverage: 0.90
- Examples: DOMAIN,browser-intake-datadoghq.com, DOMAIN,chat.openai.com.cdn.cloudflare.net, DOMAIN,openai-api.arkoselabs.com, DOMAIN,openaicomproductionae4b.blob.core.windows.net, DOMAIN,production-openaicom-storage.azureedge.net, DOMAIN,static.cloudflareinsights.com, DOMAIN-SUFFIX,algolia.net, DOMAIN-SUFFIX,auth0.com

### HBO vs HBOHK
- Files: Rule/Upstream/HBO/HBO.list and Rule/Upstream/HBOHK/HBOHK.list
- Shared exact domain rules: 23; Jaccard: 0.48; smaller-set coverage: 0.96
- Examples: DOMAIN-SUFFIX,hboasia.com, DOMAIN-SUFFIX,hboasia1-i.akamaihd.net, DOMAIN-SUFFIX,hboasia2-i.akamaihd.net, DOMAIN-SUFFIX,hboasia3-i.akamaihd.net, DOMAIN-SUFFIX,hboasia4-i.akamaihd.net, DOMAIN-SUFFIX,hboasia5-i.akamaihd.net, DOMAIN-SUFFIX,hboasialive.akamaized.net, DOMAIN-SUFFIX,hbogo.co.th

### BiliBili vs ChinaMedia
- Files: Rule/Upstream/BiliBili/BiliBili.list and Rule/Upstream/ChinaMedia/ChinaMedia.list
- Shared exact domain rules: 111; Jaccard: 0.34; smaller-set coverage: 0.97
- Examples: DOMAIN,0gr4uqmtt8y41hcjsgrzdrc31.ourdvsss.com, DOMAIN,0gr4uqmtt8y41hcjsgrzdrc3s.ourdvsss.com, DOMAIN,0gr4uqmtt8y41hcjsgrzdrc3z.ourdvsss.com, DOMAIN,0gr4uqmtt8y41hcjsgrzdrctt.ourdvsss.com, DOMAIN,0gr4uqmtt8y41hcjsgrzdrctu.ourdvsss.com, DOMAIN,0gr4uqmtt8y41hcjz8yzdnc31.ourdvsss.com, DOMAIN,0gr4uqmtt8y41hcjz8yzdnc3t.ourdvsss.com, DOMAIN,0gr4uqmtt8y41hcjzgazdrpba.ourdvsss.com

### Cloudflare vs Cloudflarecn
- Files: Rule/Upstream/Cloudflare/Cloudflare.list and Rule/Upstream/Cloudflarecn/Cloudflarecn.list
- Shared exact domain rules: 14; Jaccard: 0.33; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,cf-ns.com, DOMAIN-SUFFIX,cf-ns.net, DOMAIN-SUFFIX,cf-ns.site, DOMAIN-SUFFIX,cf-ns.tech, DOMAIN-SUFFIX,cftest5.cn, DOMAIN-SUFFIX,cftest6.cn, DOMAIN-SUFFIX,cftest7.com, DOMAIN-SUFFIX,cftest8.com

### Line vs Naver
- Files: Rule/Upstream/Line/Line.list and Rule/Upstream/Naver/Naver.list
- Shared exact domain rules: 8; Jaccard: 0.31; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,lin.ee, DOMAIN-SUFFIX,line-apps.com, DOMAIN-SUFFIX,line-cdn.net, DOMAIN-SUFFIX,line-scdn.net, DOMAIN-SUFFIX,line.me, DOMAIN-SUFFIX,linecorp.com, DOMAIN-SUFFIX,naver.jp, DOMAIN-SUFFIX,nhncorp.jp

### BritboxUK vs UKMedia
- Files: Rule/Upstream/BritboxUK/BritboxUK.list and Rule/Upstream/UKMedia/UKMedia.list
- Shared exact domain rules: 8; Jaccard: 0.29; smaller-set coverage: 1.00
- Examples: DOMAIN,itvpnp.live.ott.irdeto.com, DOMAIN,itvpnp.stage.ott.irdeto.com, DOMAIN-SUFFIX,bb-static.com, DOMAIN-SUFFIX,bbc.co.uk, DOMAIN-SUFFIX,britbox.co.uk, DOMAIN-SUFFIX,britbox.com, DOMAIN-SUFFIX,itv.com, DOMAIN-SUFFIX,massive-itv.com

### CCTV vs ChinaMedia
- Files: Rule/Upstream/CCTV/CCTV.list and Rule/Upstream/ChinaMedia/ChinaMedia.list
- Shared exact domain rules: 37; Jaccard: 0.12; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,cctv.cn, DOMAIN-SUFFIX,cctv.com, DOMAIN-SUFFIX,cctvlib.cn, DOMAIN-SUFFIX,cctvlib.com.cn, DOMAIN-SUFFIX,cctvlibrary.cn, DOMAIN-SUFFIX,cctvlibrary.com.cn, DOMAIN-SUFFIX,cctvpic.com, DOMAIN-SUFFIX,cctvpro.cn

### ChinaMedia vs Youku
- Files: Rule/Upstream/ChinaMedia/ChinaMedia.list and Rule/Upstream/Youku/Youku.list
- Shared exact domain rules: 34; Jaccard: 0.11; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,0co3geye.cn, DOMAIN-SUFFIX,2isbbess.cn, DOMAIN-SUFFIX,33lwhaoinc.cn, DOMAIN-SUFFIX,52mtkvideo.cn, DOMAIN-SUFFIX,9xsecndns.cn, DOMAIN-SUFFIX,b82yxres.cn, DOMAIN-SUFFIX,e8h2ty.tdum.alibaba.com, DOMAIN-SUFFIX,gamenow.club

### ChinaMedia vs iQIYI
- Files: Rule/Upstream/ChinaMedia/ChinaMedia.list and Rule/Upstream/iQIYI/iQIYI.list
- Shared exact domain rules: 34; Jaccard: 0.11; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,71.am, DOMAIN-SUFFIX,71.am.com, DOMAIN-SUFFIX,71edge.com, DOMAIN-SUFFIX,71edge.net, DOMAIN-SUFFIX,aianno.cn, DOMAIN-SUFFIX,aianno.com, DOMAIN-SUFFIX,aiqiyicloud-mgmt.com, DOMAIN-SUFFIX,aiqiyicloud.com

### Hulu vs HuluJP
- Files: Rule/Upstream/Hulu/Hulu.list and Rule/Upstream/HuluJP/HuluJP.list
- Shared exact domain rules: 5; Jaccard: 0.09; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,happyon.jp, DOMAIN-SUFFIX,hjholdings.jp, DOMAIN-SUFFIX,hulu.jp, DOMAIN-SUFFIX,streaks.jp, DOMAIN-SUFFIX,yb.uncn.jp

### ChinaMedia vs TencentVideo
- Files: Rule/Upstream/ChinaMedia/ChinaMedia.list and Rule/Upstream/TencentVideo/TencentVideo.list
- Shared exact domain rules: 19; Jaccard: 0.06; smaller-set coverage: 1.00
- Examples: DOMAIN,00713915daab0be43def5c338c02c80b.dlied1.cdntips.net, DOMAIN,17caa75e77d31e1f5a7841e0b3374569.dlied1.cdntips.net, DOMAIN,apd-pcdnvodstat.teg.tencent-cloud.net, DOMAIN,dldir1.qq.com, DOMAIN,iacc.qq.com, DOMAIN,ins-eeww7kom.ias.tencent-cloud.net, DOMAIN,ios.video.mpush.qq.com, DOMAIN,rdelivery.qq.com

### Microsoft vs Xbox
- Files: Rule/Upstream/Microsoft/Microsoft.list and Rule/Upstream/Xbox/Xbox.list
- Shared exact domain rules: 36; Jaccard: 0.05; smaller-set coverage: 0.86
- Examples: DOMAIN-SUFFIX,beth.games, DOMAIN-SUFFIX,bethesda.net, DOMAIN-SUFFIX,bethesdagamestudios.com, DOMAIN-SUFFIX,bethsoft.com, DOMAIN-SUFFIX,callersbane.com, DOMAIN-SUFFIX,forzamotorsport.net, DOMAIN-SUFFIX,forzaracingchampionship.com, DOMAIN-SUFFIX,forzarc.com

### ByteDance vs LianMeng
- Files: Rule/Upstream/ByteDance/ByteDance.list and Rule/Upstream/LianMeng/LianMeng.list
- Shared exact domain rules: 13; Jaccard: 0.04; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,2333333333333.com, DOMAIN-SUFFIX,bqtalk.com, DOMAIN-SUFFIX,faceu.com, DOMAIN-SUFFIX,faceu.com.cn, DOMAIN-SUFFIX,faceu.mobi, DOMAIN-SUFFIX,faceu.net, DOMAIN-SUFFIX,heycan.com, DOMAIN-SUFFIX,qmoji.mobi

### Baidu vs TaiheMusic
- Files: Rule/Upstream/Baidu/Baidu.list and Rule/Upstream/TaiheMusic/TaiheMusic.list
- Shared exact domain rules: 7; Jaccard: 0.03; smaller-set coverage: 0.88
- Examples: DOMAIN-SUFFIX,dmhmusic.com, DOMAIN-SUFFIX,qianqian.com, DOMAIN-SUFFIX,submusic.cn, DOMAIN-SUFFIX,taihe.com, DOMAIN-SUFFIX,ttplayer.com, DOMAIN-SUFFIX,youyou.com, DOMAIN-SUFFIX,youyou001.com

### ChinaMedia vs HunanTV
- Files: Rule/Upstream/ChinaMedia/ChinaMedia.list and Rule/Upstream/HunanTV/HunanTV.list
- Shared exact domain rules: 7; Jaccard: 0.02; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,hifuntv.com, DOMAIN-SUFFIX,hitv.com, DOMAIN-SUFFIX,hunaniptv.com, DOMAIN-SUFFIX,hunantv.com, DOMAIN-SUFFIX,imgo.tv, DOMAIN-SUFFIX,mgtv.com, DOMAIN-SUFFIX,tazai.com

### Bing vs Microsoft
- Files: Rule/Upstream/Bing/Bing.list and Rule/Upstream/Microsoft/Microsoft.list
- Shared exact domain rules: 9; Jaccard: 0.01; smaller-set coverage: 1.00
- Examples: DOMAIN-SUFFIX,bing.com, DOMAIN-SUFFIX,bing.com.cn, DOMAIN-SUFFIX,bing.net, DOMAIN-SUFFIX,bingads.com, DOMAIN-SUFFIX,bingagencyawards.com, DOMAIN-SUFFIX,bingapistatistics.com, DOMAIN-SUFFIX,bingsandbox.com, DOMAIN-SUFFIX,bingvisualsearch.com

## Safety and scope
- No rule files are deleted, rewritten, or merged by this report generator.
- Aggregate, All, Domain-only, and No-Resolve variants are not collapsed into standard app lists.
- Domain overlap is not proof that two apps are the same; shared infrastructure can produce false positives.
- Personal rules are outside this scan and must remain separate.
