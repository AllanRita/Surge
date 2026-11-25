// UnlockDetection V2.4
// Author: AllanRita
// Platform: Surge
// 12 Streaming Services
// Global & Regional Detection

(function () {

  const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

  const ok = c => '☑' + (c || '');
  const partial = c => '△' + (c || '');
  const no = c => '☒' + (c || '');
  const unknown = '?';

  const geo = /unsupported_country|app-unavailable-in-region|GEO_BLOCKED|GEO_CHECK_FAIL|not available in your (?:country|region|location)|not currently available in your (?:country|region|location)|日本国外からはご利用|僅限台灣地區/i;

  const challenge = /cf-chl-|challenge-platform|just a moment\.\.\.|captcha challenge|verify you are human|access denied/i;

  function cc(s) {
    return /^[a-z]{2}$/i.test(String(s || ''))
      ? String(s).toUpperCase()
      : '';
  }

  function field(s, k) {
    const m = s.match(
      new RegExp('"' + k + '"\\s*:\\s*"([^"\\r\\n]+)"', 'i')
    );
    return m ? m[1] : '';
  }

  function flag(s, k) {
    const m = s.match(
      new RegExp('"' + k + '"\\s*:\\s*(true|false)', 'i')
    );
    return m ? m[1].toLowerCase() : '';
  }

  // HTTP Request
  // Follow existing Surge routing rules.

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

      if (opt.body !== undefined) {
        o.body = opt.body;
      }

      const method = opt.method || 'get';

      try {

        $httpClient[method](o, (e, r, d) => {

          const headers = {};

          Object.keys((r && r.headers) || {})
            .forEach(k => {
              headers[k.toLowerCase()] =
                String(r.headers[k]);
            });

          resolve({
            status: e || !r ? 0 : Number(r.status),
            text: typeof d === 'string' ? d : '',
            headers,
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

  // Redirect Detection

  function host(url) {
    return (
      (String(url).match(
        /^https:\/\/([a-z0-9.-]+)(?:[/?#]|$)/i
      ) || [])[1] || ''
    ).toLowerCase();
  }

  function nextURL(r) {

    const l = r.headers.location || '';

    if (/^https:\/\//i.test(l)) return l;

    if (/^\/\//.test(l)) return 'https:' + l;

    if (/^\/(?!\/)/.test(l)) {
      return 'https://' + host(r.url) + l;
    }

    return '';

  }

  function withinDomain(url, domain) {

    const h = host(url);

    return h === domain ||
      h.endsWith('.' + domain);

  }

  async function page(url, domain) {

    let r = await request(url);
    const redirects = [];

    for (let i = 0; i < 2; i++) {

      if (r.status < 300 || r.status >= 400) break;

      const loc = nextURL(r);

      if (!loc) break;

      redirects.push(loc);

      if (
        !withinDomain(loc, domain) ||
        /\/(?:unavailable|no-service|restrict(?:ed)?)(?:[/?#]|$)/i.test(loc) ||
        geo.test(loc)
      ) {
        break;
      }

      r = await request(loc);

    }

    r.redirects = redirects;

    return r;

  }

  // Status Detection

  function basic(r) {

    if (!r.status) return unknown;

    const links = [
      r.url,
      r.headers.location || '',
      ...(r.redirects || [])
    ].join(' ');

    if (
      r.status === 451 ||
      geo.test(links) ||
      /\/(?:no-service|restrict(?:ed)?)(?:[/?#]|$)/i.test(links)
    ) {
      return no();
    }

    if (
      challenge.test(r.text) ||
      r.status === 429 ||
      r.status >= 500
    ) {
      return unknown;
    }

    if (geo.test(r.text)) return no();

    if (r.status === 403) return unknown;

    if (r.status >= 200 && r.status < 300) {
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

  function detectedRegion(r) {

    return cc(field(r.text, 'countryCode')) ||
      cc(field(r.text, 'country_code')) ||
      cc(field(r.text, 'isoCountryCode')) ||
      cc(field(r.text, 'geoCountryCode'));

  }

  function redirectRegion(r) {

    const urls = [
      r.url,
      ...(r.redirects || []).slice().reverse()
    ];

    for (const u of urls) {

      const c = pathRegion(u);

      if (c) return c;

    }

    return '';

  }

  // ==================================
  // Global Streaming Services
  // ==================================

  // 01. YouTube Premium

  async function yt() {

    const r = await page(
      'https://www.youtube.com/premium',
      'youtube.com'
    );

    const b = basic(r);

    if (b !== partial()) return b;

    const c = cc(
      field(r.text, 'INNERTUBE_CONTEXT_GL')
    );

    return c && /ad-free/i.test(r.text)
      ? ok(c)
      : partial(c);

  }

  // 02. Netflix
  // Regional catalog detection

  async function nf() {

    const results = await Promise.all([

      page(
        'https://www.netflix.com/title/81280792',
        'netflix.com'
      ),

      page(
        'https://www.netflix.com/title/80018499',
        'netflix.com'
      )

    ]);

    const a = results[0];
    const b = results[1];

    if (basic(a) === no() &&
        basic(b) === no()) {
      return no();
    }

    const countries = results.map(r =>
      detectedRegion(r) ||
      redirectRegion(r)
    ).filter(Boolean);

    const unique = [...new Set(countries)];

    if (unique.length > 1) return unknown;

    const c = unique[0] || '';

    if (results.some(usable)) {
      return partial(c);
    }

    return unknown;

  }

  // 03. Disney+

  async function disney() {

    const r = await page(
      'https://www.disneyplus.com/',
      'disneyplus.com'
    );

    const b = basic(r);

    if (b === no()) return b;

    const c = detectedRegion(r) ||
      redirectRegion(r);

    const available = flag(
      r.text, 'inSupportedLocation'
    );

    if (available === 'false') return no(c);

    if (
      usable(r) &&
      available === 'true' &&
      c
    ) {
      return ok(c);
    }

    return b === partial()
      ? partial(c)
      : unknown;

  }

  // 04. HBO Max

  async function hbo() {

    const r = await page(
      'https://www.hbomax.com/',
      'hbomax.com'
    );

    const b = basic(r);

    if (b !== partial()) return b;

    const c =
      detectedRegion(r) ||
      cc(
        (String(r.headers['set-cookie'] || '')
          .match(/countryCode=([A-Z]{2})/i)
          || [])[1]
      ) ||
      redirectRegion(r);

    return partial(c);

  }

  // 05. Hulu
  // US and Japan checked independently.
  // Display only one detected region.

  async function huluUS() {

    const r = await page(
      'https://www.hulu.com/',
      'hulu.com'
    );

    const b = basic(r);

    if (b === no()) return no();

    if (b !== partial()) return unknown;

    const c = detectedRegion(r);

    if (
      c === 'US' &&
      flag(r.text, 'isAllowed') === 'true'
    ) {
      return ok('US');
    }

    return partial(c === 'US' ? 'US' : '');

  }

  async function huluJP() {

    const r = await page(
      'https://id.hulu.jp/',
      'hulu.jp'
    );

    const b = basic(r);

    if (b === no()) return no();

    if (
      usable(r) &&
      withinDomain(r.url, 'hulu.jp') &&
      /ログイン|login|sign in/i.test(r.text)
    ) {
      return ok('JP');
    }

    return b === partial()
      ? partial(
          detectedRegion(r) === 'JP' ? 'JP' : ''
        )
      : unknown;

  }

  async function hulu() {

    const results = await Promise.all([
      huluUS(),
      huluJP()
    ]);

    const passed = results.filter(
      s => s.startsWith('☑')
    );

    if (passed.length === 1) {
      return passed[0];
    }

    if (passed.length > 1) {
      return unknown;
    }

    const identified = results.filter(
      s => /^△[A-Z]{2}$/.test(s)
    );

    if (identified.length === 1) {
      return identified[0];
    }

    if (identified.length > 1) {
      return unknown;
    }

    if (results.every(s => s.startsWith('☒'))) {
      return no();
    }

    if (results.some(s => s.startsWith('△'))) {
      return partial();
    }

    return unknown;

  }

  // 06. Prime Video

  async function prime() {

    const r = await page(
      'https://www.primevideo.com/',
      'primevideo.com'
    );

    const b = basic(r);

    if (b === no()) return b;

    const c =
      cc(field(r.text, 'currentTerritory')) ||
      detectedRegion(r);

    const restricted = flag(
      r.text, 'isServiceRestricted'
    );

    if (restricted === 'true') return no(c);

    if (
      usable(r) &&
      c &&
      restricted === 'false'
    ) {
      return ok(c);
    }

    return b === partial()
      ? partial(c)
      : unknown;

  }

  // 07. Spotify

  async function spotify() {

    const r = await page(
      'https://www.spotify.com/',
      'spotify.com'
    );

    const b = basic(r);

    if (b !== partial()) return b;

    const c =
      detectedRegion(r) ||
      redirectRegion(r);

    return partial(c);

  }

  // 08. Paramount+
  // Multi-region detection.
  // No fixed country.

  async function paramount() {

    const r = await page(
      'https://www.paramountplus.com/',
      'paramountplus.com'
    );

    const b = basic(r);

    const c =
      detectedRegion(r) ||
      redirectRegion(r);

    const restricted = flag(
      r.text, 'isServiceRestricted'
    );

    const available = flag(
      r.text, 'inSupportedLocation'
    );

    if (
      b === no() ||
      restricted === 'true' ||
      available === 'false'
    ) {
      return no(c);
    }

    if (
      usable(r) &&
      c &&
      (
        restricted === 'false' ||
        available === 'true'
      )
    ) {
      return ok(c);
    }

    return b === partial()
      ? partial(c)
      : unknown;

  }

  // 09. Viu
  // Detect the actual regional Viu site.
  // Not ViuTV.

  async function viu() {

    const r = await page(
      'https://www.viu.com/',
      'viu.com'
    );

    const urls = [
      r.url,
      ...(r.redirects || []).slice().reverse()
    ];

    if (
      urls.some(u =>
        /\/no-service(?:[/?#]|$)/i.test(u)
      )
    ) {
      return no();
    }

    const b = basic(r);

    if (b === no()) return no();

    let c = detectedRegion(r);

    if (!c) {

      for (const u of urls) {

        const m = u.match(
          /\/ott\/([a-z]{2})(?:[/?#]|$)/i
        );

        if (m) {
          c = cc(m[1]);
          break;
        }

      }

    }

    if (
      usable(r) &&
      c &&
      flag(r.text, 'isAllowed') === 'true'
    ) {
      return ok(c);
    }

    return b === partial()
      ? partial(c)
      : unknown;

  }

  // ==================================
  // Regional Streaming Services
  // ==================================

  // 10. ABEMA

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

    if (d.isAllowed === false) {
      return no(c);
    }

    if (c === 'JP') return ok(c);

    return c ? partial(c) : unknown;

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

    if (m[1] === '467') return no();

    if (m[1] === '200') return ok('JP');

    if (m[1] === '475') return partial('JP');

    return unknown;

  }

  // 12. Bahamut Anime

  async function bahamut() {

    const r = await page(
      'https://ani.gamer.com.tw/',
      'gamer.com.tw'
    );

    const b = basic(r);

    if (b !== partial()) return b;

    const c =
      detectedRegion(r) ||
      cc(
        (r.text.match(
          /data-geo="([a-z]{2})"/i
        ) || [])[1]
      );

    return partial(c);

  }

  // ==================================
  // Services List
  // ==================================

  const services = [

    ['YouTube Premium', yt],
    ['Netflix', nf],
    ['Disney+', disney],
    ['HBO Max', hbo],
    ['Hulu', hulu],
    ['Prime Video', prime],
    ['Spotify', spotify],
    ['Paramount+', paramount],
    ['Viu', viu],

    ['ABEMA', abema],
    ['U-NEXT', unext],
    ['巴哈姆特动画疯', bahamut]

  ];

  const values = {};

  services.forEach(s => {
    values[s[0]] = unknown;
  });

  let complete = false;

  function result(name) {
    return name + ': ' +
      (values[name] || unknown);
  }

  function line(...names) {
    return names.map(result).join(' | ');
  }

  // ==================================
  // Panel Layout
  // ==================================

  function finish() {

    if (complete) return;

    complete = true;

    const d = new Date();

    const pad = n =>
      ('0' + n).slice(-2);

    const content = [

      '🌐 全球流媒体',

      line('YouTube Premium'),

      line('Netflix', 'Disney+'),

      line('HBO Max', 'Hulu'),

      line('Prime Video', 'Spotify'),

      line('Paramount+', 'Viu'),

      '',

      '📍 地区流媒体',

      line('ABEMA', 'U-NEXT'),

      line('巴哈姆特动画疯')

    ].join('\n');

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

  // ==================================
  // Concurrent Detection
  // ==================================

  setTimeout(finish, 24000);

  Promise.all(

    services.map(s =>

      Promise.resolve()

        .then(s[1])

        .then(v => {

          values[s[0]] = v;

          console.log(s[0] + ': ' + v);

        })

        .catch(() => {

          values[s[0]] = unknown;

        })

    )

  ).then(finish);

})();
