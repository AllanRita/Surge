// UnlockDetection V2.3
// Author: AllanRita
// Platform: Surge
// 16 Streaming Services

(function () {

  const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

  const POLICY = '';
  const ok = c => '☑' + (c || '');
  const partial = c => '△' + (c || '');
  const no = c => '☒' + (c || '');
  const unknown = '?';

  const geo = /unsupported_country|app-unavailable-in-region|not available in your (?:country|region|location)|not (?:currently )?available in your (?:country|region|location)|outside (?:the )?(?:united states|us)|GEO_CHECK_FAIL|available (?:only )?in South Korea|このサービスは日本国内|日本国外からはご利用|僅限台灣地區|仅限台湾地区/i;

  const challenge = /cf-chl-|challenge-platform|just a moment\.\.\.|captcha challenge|verify you are human|access denied|security policy has been breached/i;

  const cc = s =>
    /^[a-z]{2}$/i.test(String(s || ''))
      ? String(s).toUpperCase()
      : '';

  const field = (s, k) => {
    const m = s.match(
      new RegExp('"' + k + '"\\s*:\\s*"([^"\\r\\n]+)"', 'i')
    );
    return m ? m[1] : '';
  };

  const flag = (s, k) => {
    const m = s.match(
      new RegExp('"' + k + '"\\s*:\\s*(true|false)', 'i')
    );
    return m ? m[1].toLowerCase() : '';
  };

  // HTTP Request

  function request(url, opt) {
    opt = opt || {};

    return new Promise(resolve => {

      const o = {
        url,
        timeout: 7,
        'auto-redirect': false,
        'auto-cookie': false,
        headers: Object.assign({
          'User-Agent': UA,
          'Accept-Language': 'en-US,en;q=0.9',
          'Cache-Control': 'no-cache'
        }, opt.headers || {})
      };

      if (POLICY) o.policy = POLICY;
      if (opt.body !== undefined) o.body = opt.body;

      const method = opt.method || 'get';

      try {
        $httpClient[method](o, (e, r, d) => {

          const h = {};

          Object.keys((r && r.headers) || {})
            .forEach(k => {
              h[k.toLowerCase()] = String(r.headers[k]);
            });

          resolve({
            status: e || !r ? 0 : Number(r.status),
            text: typeof d === 'string' ? d : '',
            headers: h,
            url
          });

        });
      } catch (_) {
        resolve({
          status: 0,
          text: '',
          headers: {},
          url
        });
      }
    });
  }

  // Redirect Handling

  function nextURL(r) {

    const l = r.headers.location || '';

    if (/^https:\/\//i.test(l)) return l;

    if (/^\/(?!\/)/.test(l)) {
      return r.url.match(/^https:\/\/[^/]+/i)[0] + l;
    }

    return '';
  }

  function sameFamily(a, b) {

    const host = u =>
      ((u.match(/^https:\/\/([a-z0-9.-]+)(?:\/|$)/i)
      || [])[1] || '').toLowerCase();

    const x = host(a);
    const y = host(b);

    return !!x && !!y &&
      (x === y ||
      x.replace(/^www\./, '') ===
      y.replace(/^www\./, ''));
  }

  async function page(url) {

    let r = await request(url);
    let loc = nextURL(r);

    if (
      r.status >= 300 &&
      r.status < 400 &&
      loc &&
      !geo.test(loc) &&
      !/\/(?:unavailable|intl)(?:[/?#]|$)/i.test(loc) &&
      sameFamily(url, loc)
    ) {

      const n = await request(loc);
      n.firstLocation = loc;

      return n;
    }

    return r;
  }

  // Status Detection

  function basic(r) {

    if (!r.status) return unknown;

    if (
      r.status === 451 ||
      geo.test(r.headers.location || '') ||
      (
        r.status < 500 &&
        !challenge.test(r.text) &&
        geo.test(r.text)
      )
    ) {
      return no();
    }

    if (
      challenge.test(r.text) ||
      [403, 429].includes(r.status) ||
      r.status >= 500
    ) {
      return unknown;
    }

    if (r.status >= 200 && r.status < 400) {
      return partial();
    }

    return unknown;
  }

  function usable(r) {

    return r.status >= 200 &&
      r.status < 300 &&
      !challenge.test(r.text);
  }

  function pathRegion(u) {

    const m = String(u || '').match(
      /^https:\/\/[^/]+\/([a-z]{2})(?:-[a-z]{2})?(?:[/?#]|$)/i
    );

    return m ? cc(m[1]) : '';
  }

  // 01. YouTube Premium

  async function yt() {

    const r = await page(
      'https://www.youtube.com/premium'
    );

    const b = basic(r);

    if (b !== partial() || !usable(r)) return b;

    const c = cc(
      field(r.text, 'INNERTUBE_CONTEXT_GL')
    );

    return /ad-free/i.test(r.text) && c
      ? ok(c)
      : partial(c);
  }

  // 02. Netflix

  async function nf() {

    const r = await page(
      'https://www.netflix.com/title/70143836'
    );

    const b = basic(r);

    if (b !== partial()) return b;

    const c =
      cc(field(r.text, 'countryCode')) ||
      pathRegion(r.firstLocation || r.headers.location) ||
      pathRegion(
        (r.text.match(
          /<link[^>]*rel="canonical"[^>]*href="([^"]+)"/i
        ) || [])[1]
      );

    return partial(c);
  }

  // 03. Disney+

  async function disney() {

    const r = await page(
      'https://www.disneyplus.com/'
    );

    const b = basic(r);

    if (b !== partial()) return b;

    const c =
      cc(field(r.text, 'countryCode')) ||
      pathRegion(r.firstLocation || r.headers.location);

    if (
      /\/(?:unavailable|preview)(?:[/?#]|$)/i
        .test(r.headers.location || '')
    ) {
      return partial(c);
    }

    return usable(r) &&
      flag(r.text, 'inSupportedLocation') === 'true' &&
      c
      ? ok(c)
      : partial(c);
  }

  // 04. HBO Max

  async function hbo() {

    const r = await page(
      'https://www.hbomax.com/'
    );

    const b = basic(r);

    if (b !== partial()) return b;

    const c =
      cc(
        (String(r.headers['set-cookie'] || '')
          .match(/countryCode=([A-Z]{2})/i) || [])[1]
      ) ||
      pathRegion(r.firstLocation || r.headers.location);

    return partial(c);
  }

  // 05. Spotify

  async function spotify() {

    const r = await page(
      'https://www.spotify.com/'
    );

    const b = basic(r);

    if (b !== partial()) return b;

    return partial(
      pathRegion(r.firstLocation || r.headers.location)
    );
  }

  // 06. Prime Video

  async function prime() {

    const r = await page(
      'https://www.primevideo.com/'
    );

    const b = basic(r);

    if (b !== partial()) return b;

    const c = cc(
      field(r.text, 'currentTerritory')
    );

    const restricted = flag(
      r.text, 'isServiceRestricted'
    );

    if (restricted === 'true') return no(c);

    return usable(r) &&
      c &&
      restricted === 'false'
      ? ok(c)
      : partial(c);
  }

  // 07. Apple TV

  async function appleTV() {

    return basic(
      await page('https://tv.apple.com/')
    );
  }

  // 08. Paramount+

  async function paramount() {

    const r = await page(
      'https://www.paramountplus.com/'
    );

    const b = basic(r);

    if (b !== partial()) return b;

    return partial(
      pathRegion(r.firstLocation || r.headers.location)
    );
  }

  // 09. ABEMA

  async function abema() {

    const r = await request(
      'https://api.abema.io/v1/ip/check?device=android',
      {
        headers: {
          'User-Agent':
            'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 Chrome/131.0.0.0 Mobile Safari/537.36',
          'Accept': 'application/json'
        }
      }
    );

    if (basic(r) === no()) return no();

    if (!usable(r)) return unknown;

    let d;

    try {
      d = JSON.parse(r.text);
    } catch (_) {
      return unknown;
    }

    const c = cc(d.isoCountryCode);

    if (d.isAllowed === false) return no(c);

    return c === 'JP'
      ? ok(c)
      : c
      ? partial(c)
      : unknown;
  }

  // 10. TVer

  async function tver() {

    return basic(
      await page('https://tver.jp/')
    );
  }

  // 11. U-NEXT

  async function unext() {

    const query =
      'query cosmo_getPlaylistUrl($code: String, $playMode: String, $bitrateLow: Int, $bitrateHigh: Int, $validationOnly: Boolean) { webfront_playlistUrl(code: $code, playMode: $playMode, bitrateLow: $bitrateLow, bitrateHigh: $bitrateHigh, validationOnly: $validationOnly) { resultStatus } }';

    const r = await request(
      'https://cc.unext.jp',
      {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          operationName: 'cosmo_getPlaylistUrl',
          variables: {
            code: 'ED00479780',
            playMode: 'caption',
            bitrateLow: 192,
            bitrateHigh: null,
            validationOnly: true
          },
          query
        })
      }
    );

    if (basic(r) === no()) return no();

    if (!usable(r)) return unknown;

    const m = r.text.match(
      /"resultStatus"\s*:\s*(\d+)/
    );

    if (!m) return unknown;

    return m[1] === '467'
      ? no()
      : m[1] === '200'
      ? ok('JP')
      : m[1] === '475'
      ? partial('JP')
      : unknown;
  }

  // 12. Hulu

  async function hulu() {

    return basic(
      await page('https://www.hulu.com/')
    );
  }

  // 13. Peacock

  async function peacock() {

    return basic(
      await page('https://www.peacocktv.com/')
    );
  }

  // 14. 巴哈姆特动画疯

  async function bahamut() {

    const r = await page(
      'https://ani.gamer.com.tw/'
    );

    const b = basic(r);

    if (b !== partial()) return b;

    const c = cc(
      (r.text.match(
        /data-geo="([a-z]{2})"/i
      ) || [])[1]
    );

    return partial(c);
  }

  // 15. ViuTV

  async function viu() {

    const r = await request(
      'https://api.viu.now.com/p8/3/getLiveURL',
      {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          callerReferenceNo: String(Date.now()),
          contentId: '099',
          contentType: 'Channel',
          channelno: '099',
          mode: 'prod',
          deviceId: 'surge-panel-' + Date.now(),
          deviceType: 'ANDROID_WEB'
        })
      }
    );

    if (basic(r) === no()) return no();

    if (!usable(r)) return unknown;

    const code = field(r.text, 'responseCode');

    return code === 'SUCCESS'
      ? ok('HK')
      : code === 'GEO_CHECK_FAIL'
      ? no()
      : unknown;
  }

  // 16. TVING

  async function tving() {

    return basic(
      await page('https://www.tving.com/')
    );
  }

  // Streaming Services

  const services = [
    ['YouTube Premium', yt],
    ['Netflix', nf],
    ['Disney+', disney],
    ['HBO Max', hbo],
    ['Spotify', spotify],
    ['Prime Video', prime],
    ['Apple TV', appleTV],
    ['Paramount+', paramount],
    ['ABEMA', abema],
    ['TVer', tver],
    ['U-NEXT', unext],
    ['Hulu', hulu],
    ['Peacock', peacock],
    ['巴哈姆特动画疯', bahamut],
    ['ViuTV', viu],
    ['TVING', tving]
  ];

  // Panel Layout

  const rows = [1, 2, 2, 2, 2, 2, 2, 2, 1];

  const values = services.map(() => unknown);

  let complete = false;

  function finish() {

    if (complete) return;

    complete = true;

    const d = new Date();

    const pad = n => ('0' + n).slice(-2);

    let i = 0;

    const content = rows.map(n => {

      const line = services
        .slice(i, i + n)
        .map((s, j) =>
          s[0] + ': ' + values[i + j]
        )
        .join(' | ');

      i += n;

      return line;

    }).join('\n');

    $done({
      title:
        'UnlockDetection | ' +
        pad(d.getHours()) + ':' +
        pad(d.getMinutes()),

      content: content,

      icon: 'lock.open.display',

      'icon-color': '#007AFF'
    });
  }

  // Concurrent Detection

  setTimeout(finish, 24000);

  Promise.all(
    services.map((s, i) =>
      Promise.resolve()
        .then(s[1])
        .then(v => {
          values[i] = v;
          console.log(s[0] + ': ' + v);
        })
        .catch(() => {})
    )
  ).then(finish);

})();
