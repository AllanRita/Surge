// UnlockDetection V2.5
// Author: AllanRita
// Platform: Surge
// Global & Regional Streaming Detection
// 12 Streaming Services
// Follow existing Surge routing rules
// Reference: RegionRestrictionCheck

(function () {

  const UA =
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

  const ok = c => '☑' + (c || '');
  const partial = c => '△' + (c || '');
  const no = c => '☒' + (c || '');
  const unknown = '?';

  const geo =
    /unsupported_country|forbidden-location|app-unavailable-in-region|GEO_BLOCKED|GEO_CHECK_FAIL|not available in your (?:country|region|location)|not currently available in your (?:country|region|location)|日本国外からはご利用|僅限台灣地區/i;

  const challenge =
    /cf-chl-|challenge-platform|just a moment\.\.\.|captcha challenge|verify you are human|access denied/i;

  function cc(value) {

    const s = String(value || '')
      .trim()
      .toUpperCase();

    if (s === 'UK') return 'GB';

    return /^[A-Z]{2}$/.test(s) &&
      !['EN', 'XX', 'ZZ'].includes(s)
      ? s
      : '';

  }

  function json(r) {
    try {
      return JSON.parse(r.text);
    } catch (_) {
      return {};
    }
  }

  function field(s, key) {

    const m = s.match(
      new RegExp(
        '"' + key + '"\\s*:\\s*"([^"\\r\\n]+)"',
        'i'
      )
    );

    return m ? m[1] : '';

  }

  function flag(s, key) {

    const m = s.match(
      new RegExp(
        '"' + key + '"\\s*:\\s*(true|false)',
        'i'
      )
    );

    return m ? m[1].toLowerCase() : '';

  }

  // ==================================
  // HTTP Request
  // No fixed proxy or policy group
  // ==================================

  function request(url, opt) {

    opt = opt || {};

    return new Promise(resolve => {

      const options = {

        url,

        timeout: 8,

        'auto-redirect': false,

        'auto-cookie': false,

        headers: Object.assign({

          'User-Agent': UA,

          'Accept-Language': 'en-US,en;q=0.9',

          'Cache-Control': 'no-cache',

          'Accept': '*/*'

        }, opt.headers || {})

      };

      if (opt.body !== undefined) {
        options.body = opt.body;
      }

      const method = opt.method || 'get';

      try {

        $httpClient[method](
          options,
          (error, response, data) => {

            const headers = {};

            Object.keys(
              (response && response.headers) || {}
            ).forEach(k => {

              headers[k.toLowerCase()] =
                String(response.headers[k]);

            });

            const result = {

              status: error || !response
                ? 0
                : Number(response.status),

              text: typeof data === 'string'
                ? data
                : '',

              headers,

              url

            };

            console.log(
              'HTTP ' + result.status +
              ' | ' + url.split('?')[0]
            );

            resolve(result);

          }
        );

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

  // ==================================
  // Redirect & Regional Identification
  // ==================================

  function host(url) {

    return (
      (String(url).match(
        /^https:\/\/([a-z0-9.-]+)(?:[/?#]|$)/i
      ) || [])[1] || ''
    ).toLowerCase();

  }

  function allowed(url, domains) {

    const h = host(url);

    return domains.some(d =>
      h === d || h.endsWith('.' + d)
    );

  }

  function nextURL(r) {

    let l = r.headers.location || '';

    if (/^\/\//.test(l)) {
      l = 'https:' + l;
    }

    if (/^\/(?!\/)/.test(l)) {
      l = 'https://' + host(r.url) + l;
    }

    return /^https:\/\//i.test(l)
      ? l
      : '';

  }

  async function page(url, domains) {

    let r = await request(url);

    const redirects = [];
    const cookies = [];

    for (let i = 0; i < 3; i++) {

      if (r.headers['set-cookie']) {

        cookies.push(
          r.headers['set-cookie']
        );

      }

      if (
        r.status < 300 ||
        r.status >= 400
      ) {
        break;
      }

      const loc = nextURL(r);

      if (!loc) break;

      redirects.push(loc);

      if (

        !allowed(loc, domains) ||

        geo.test(loc) ||

        /\/(?:no-service|restricted|restrict|unavailable)(?:[/?#]|$)/i.test(loc) ||

        loc === r.url

      ) {
        break;
      }

      r = await request(loc);

    }

    if (r.headers['set-cookie']) {

      cookies.push(
        r.headers['set-cookie']
      );

    }

    r.redirects = redirects;
    r.cookies = cookies.join('\n');

    return r;

  }

  function links(r) {

    return [

      r.url,

      r.headers.location || '',

      ...(r.redirects || [])

    ].join(' ');

  }

  function usable(r) {

    return r.status >= 200 &&
      r.status < 300 &&
      !challenge.test(r.text);

  }

  function restricted(r) {

    if (r.status === 451) {
      return true;
    }

    if (geo.test(links(r))) {
      return true;
    }

    if (

      /\/(?:no-service|restricted|restrict|unavailable)(?:[/?#\s]|$)/i
        .test(links(r))

    ) {
      return true;
    }

    if (

      !challenge.test(r.text) &&
      r.text.length < 20000 &&
      geo.test(r.text)

    ) {
      return true;
    }

    return false;

  }

  function basic(r) {

    if (restricted(r)) return no();

    if (usable(r)) return partial();

    return unknown;

  }

  function localeRegion(r, order) {

    const urls = [

      r.url,

      ...(r.redirects || []).slice().reverse()

    ];

    for (const u of urls) {

      const m = u.match(

        /^https:\/\/[^/]+\/([a-z]{2})-([a-z]{2})(?:[/?#]|$)/i

      );

      if (m) {

        const c = cc(
          order === 'language-country'
            ? m[2]
            : m[1]
        );

        if (c) return c;

      }

    }

    return '';

  }

  function pathRegion(r) {

    const urls = [

      r.url,

      ...(r.redirects || []).slice().reverse()

    ];

    for (const u of urls) {

      const m = u.match(

        /^https:\/\/[^/]+\/([a-z]{2})(?:[/?#]|$)/i

      );

      if (m && cc(m[1])) {
        return cc(m[1]);
      }

    }

    return '';

  }

  // ==================================
  // 01. YouTube Premium
  // Global
  // ==================================

  async function youtube() {

    const r = await page(

      'https://www.youtube.com/premium',

      ['youtube.com']

    );

    if (restricted(r)) return no();

    if (!usable(r)) return unknown;

    const c = cc(

      field(r.text, 'INNERTUBE_CONTEXT_GL')

    );

    if (

      /Premium is not available in your country/i
        .test(r.text)

    ) {

      return no(c);

    }

    if (c && /ad-free/i.test(r.text)) {

      return ok(c);

    }

    return partial(c);

  }

  // ==================================
  // 02. Netflix
  // Global catalog cross-check
  // ==================================

  async function netflix() {

    const results = await Promise.all([

      page(

        'https://www.netflix.com/title/81280792',

        ['netflix.com']

      ),

      page(

        'https://www.netflix.com/title/70143836',

        ['netflix.com']

      ),

      page(

        'https://www.netflix.com/title/80018499',

        ['netflix.com']

      )

    ]);

    function region(r) {

      const m = r.text.match(

        /"requestCountry"\s*:\s*\{\s*"id"\s*:\s*"([A-Z]{2})"/i

      );

      return cc(m && m[1]) ||

        localeRegion(r, 'country-language') ||

        pathRegion(r);

    }

    function titleAvailable(r) {

      return usable(r) &&

        !/Oh no!|title is not available/i.test(r.text) &&

        /"@type"\s*:\s*"(?:TVSeries|Movie|VideoObject)"/i
          .test(r.text);

    }

    const codes = [...new Set(

      results.map(region).filter(Boolean)

    )];

    if (codes.length > 1) return unknown;

    const c = codes[0] || '';

    const licensed = results.slice(0, 2);

    if (

      licensed.some(titleAvailable) && c

    ) {

      return ok(c);

    }

    if (titleAvailable(results[2])) {

      return partial(c);

    }

    if (results.every(restricted)) {

      return no(c);

    }

    return results.some(usable)
      ? partial(c)
      : unknown;

  }

  // ==================================
  // 03. Disney+
  // Global
  // ==================================

  async function disney() {

    const r = await page(

      'https://www.disneyplus.com/',

      ['disneyplus.com']

    );

    if (restricted(r)) return no();

    const c =

      localeRegion(r, 'language-country') ||

      cc(r.headers['x-country-code']);

    if (

      /\/preview(?:[/?#\s]|$)/i
        .test(links(r))

    ) {

      return partial(c);

    }

    if (!usable(r)) return unknown;

    // Explicit service availability field only.

    const m = r.text.match(

      /"inSupportedLocation"\s*:\s*(true|false)/gi

    ) || [];

    const states = [...new Set(

      m.map(s =>
        s.split(':').pop().trim().toLowerCase()
      )

    )];

    if (

      states.length === 1 &&
      states[0] === 'false'

    ) {

      return no(c);

    }

    if (

      states.length === 1 &&
      states[0] === 'true' &&
      c

    ) {

      return ok(c);

    }

    return partial(c);

  }

  // ==================================
  // 04. HBO Max
  // Global
  // Do not use arbitrary HTML countryCode
  // ==================================

  async function hbo() {

    const r = await page(

      'https://www.hbomax.com/',

      ['hbomax.com', 'max.com']

    );

    if (restricted(r)) return no();

    const cookie = r.cookies || '';

    const matches = cookie.match(

      /(?:^|[\s,;])countryCode=[A-Z]{2}(?=[\s,;]|$)/gi

    ) || [];

    const codes = [...new Set(

      matches.map(s =>
        cc(s.split('=').pop())
      ).filter(Boolean)

    )];

    const m = r.url.match(

      /^https:\/\/[^/]+\/([a-z]{2})\/[a-z]{2}(?:[/?#]|$)/i

    );

    const route = cc(m && m[1]);

    if (codes.length > 1) return unknown;

    const c = codes[0] || route;

    if (

      codes[0] && route &&
      codes[0] !== route

    ) {

      return unknown;

    }

    if (!usable(r)) return unknown;

    return partial(c);

  }

  // ==================================
  // 05. Hulu
  // USA & Japan
  // Display one region only
  // ==================================

  async function huluUS() {

    const r = await page(

      'https://www.hulu.com/',

      ['hulu.com']

    );

    if (restricted(r)) return no();

    if (!usable(r)) return unknown;

    const c = cc(

      r.headers['x-country-code']

    );

    return partial(c === 'US' ? c : '');

  }

  async function huluJP() {

    const r = await page(

      'https://id.hulu.jp/',

      ['hulu.jp']

    );

    if (restricted(r)) return no();

    if (!usable(r)) return unknown;

    const c = cc(

      r.headers['x-country-code']

    );

    // Login page access is not proof of playback.

    return partial(c === 'JP' ? c : '');

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

    const regions = [...new Set(

      results.filter(
        s => /^△[A-Z]{2}$/.test(s)
      )

    )];

    if (regions.length === 1) {

      return regions[0];

    }

    if (regions.length > 1) {

      return unknown;

    }

    if (results.every(s => s.startsWith('☒'))) {

      return no();

    }

    if (

      results[0] === partial() &&
      results[1].startsWith('☒')

    ) {

      return partial('US');

    }

    if (

      results[1] === partial() &&
      results[0].startsWith('☒')

    ) {

      return partial('JP');

    }

    return results.some(
      s => s.startsWith('△')
    ) ? partial() : unknown;

  }

  // ==================================
  // 06. Prime Video
  // Global
  // ==================================

  async function prime() {

    const r = await page(

      'https://www.primevideo.com/',

      ['primevideo.com']

    );

    if (restricted(r)) return no();

    if (!usable(r)) return unknown;

    const c = cc(

      field(r.text, 'currentTerritory')

    );

    const state = flag(

      r.text, 'isServiceRestricted'

    );

    if (state === 'true') {

      return no(c);

    }

    if (state === 'false' && c) {

      return ok(c);

    }

    return partial(c);

  }

  // ==================================
  // 07. Spotify
  // Global country-selector endpoint
  // ==================================

  async function spotify() {

    const r = await request(

      'https://www.spotify.com/api/content/v1/country-selector'

    );

    if (restricted(r)) return no();

    const loc = r.headers.location || '';

    const m = loc.match(

      /\/([a-z]{2})(?:-[a-z]{2})?\/(?:api\/|$)/i

    );

    const d = json(r);

    const c =

      cc(d.countryCode) ||

      cc(d.country) ||

      cc(m && m[1]);

    if (

      d.is_country_launched === false

    ) {

      return no(c);

    }

    if (

      d.is_country_launched === true &&
      c

    ) {

      return ok(c);

    }

    if (c) return partial(c);

    const web = await page(

      'https://www.spotify.com/',

      ['spotify.com']

    );

    if (restricted(web)) return no();

    if (!usable(web)) return unknown;

    return partial(

      localeRegion(web, 'country-language') ||

      pathRegion(web)

    );

  }

  // ==================================
  // 08. Paramount+
  // Global
  // No fixed country or country whitelist
  // ==================================

  async function paramount() {

    const r = await page(

      'https://www.paramountplus.com/',

      ['paramountplus.com']

    );

    if (

      restricted(r) ||

      /\/intl(?:[/?#\s]|$)/i.test(links(r))

    ) {

      return no();

    }

    if (!usable(r)) return unknown;

    const c =

      cc(r.headers['x-country-code']) ||

      localeRegion(r, 'language-country') ||

      pathRegion(r);

    const state = flag(

      r.text, 'isServiceRestricted'

    );

    const available = flag(

      r.text, 'inSupportedLocation'

    );

    if (

      state === 'true' ||
      available === 'false'

    ) {

      return no(c);

    }

    if (

      c &&

      (state === 'false' ||
       available === 'true')

    ) {

      return ok(c);

    }

    return partial(c);

  }

  // ==================================
  // 09. Viu
  // Multi-region
  // ==================================

  async function viu() {

    const r = await page(

      'https://www.viu.com/',

      ['viu.com']

    );

    if (restricted(r)) return no();

    if (!usable(r)) return unknown;

    const m = r.url.match(

      /\/ott\/([a-z]{2})(?:[/?#]|$)/i

    );

    const c = cc(m && m[1]);

    // Regional landing page is a location
    // signal, not complete playback proof.

    return partial(c);

  }

  // ==================================
  // 10. ABEMA
  // Japan & overseas
  // ==================================

  async function abema() {

    const r = await request(

      'https://api.abema.io/v1/ip/check?device=android',

      {

        headers: {

          'Accept': 'application/json',

          'User-Agent':
            'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 Chrome/131.0.0.0 Mobile Safari/537.36'

        }

      }

    );

    if (restricted(r)) return no();

    if (!usable(r)) return unknown;

    const d = json(r);

    const c = cc(d.isoCountryCode);

    if (d.isAllowed === false) {

      return no(c);

    }

    if (c === 'JP') {

      return ok(c);

    }

    return c ? partial(c) : unknown;

  }

  // ==================================
  // 11. U-NEXT
  // Playback validation
  // ==================================

  async function unext() {

    const query =

      'query cosmo_getPlaylistUrl($code: String, $playMode: String, $bitrateLow: Int, $bitrateHigh: Int, $validationOnly: Boolean) { webfront_playlistUrl(code: $code, playMode: $playMode, bitrateLow: $bitrateLow, bitrateHigh: $bitrateHigh, validationOnly: $validationOnly) { resultStatus result { errorCode errorMessage } } }';

    const r = await request(

      'https://cc.unext.jp',

      {

        method: 'post',

        headers: {

          'Content-Type': 'application/json',

          'Origin': 'https://video.unext.jp',

          'Referer': 'https://video.unext.jp/'

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

    if (restricted(r)) return no();

    if (!usable(r)) return unknown;

    const d = json(r);

    const result =

      d.data &&
      d.data.webfront_playlistUrl;

    if (!result) {

      console.log('U-NEXT: invalid response');

      return unknown;

    }

    const status = Number(

      result.resultStatus

    );

    console.log(

      'U-NEXT resultStatus: ' + status

    );

    if (status === 467) return no();

    if (status === 200) return ok('JP');

    if (status === 475) return partial('JP');

    return unknown;

  }

  // ==================================
  // 12. Bahamut Anime
  // Regional catalog eligibility
  // ==================================

  async function bahamut() {

    const web = await page(

      'https://ani.gamer.com.tw/',

      ['gamer.com.tw']

    );

    if (restricted(web)) return no();

    if (!usable(web)) return unknown;

    const m = web.text.match(

      /data-geo="([a-z]{2})"/i

    );

    const c = cc(m && m[1]);

    const device = await request(

      'https://ani.gamer.com.tw/ajax/getdeviceid.php'

    );

    if (!usable(device)) {

      return partial(c);

    }

    const d = json(device);

    if (!d.deviceid) {

      return partial(c);

    }

    const cookies =

      (device.headers['set-cookie'] || '')

        .split(/,(?=\s*[^;,=\s]+=[^;,]*)/)

        .map(s => s.trim().split(';')[0])

        .filter(Boolean)

        .join('; ');

    const test = await request(

      'https://ani.gamer.com.tw/ajax/token.php?adID=89422&sn=37783&device=' +

      encodeURIComponent(d.deviceid),

      {

        headers: cookies

          ? {'Cookie': cookies}

          : {}

      }

    );

    if (restricted(test)) {

      return no(c);

    }

    const token = json(test);

    if (usable(test) && token.animeSn && c) {

      return ok(c);

    }

    return partial(c);

  }

  // ==================================
  // Services
  // ==================================

  const services = [

    ['YouTube Premium', youtube],

    ['Netflix', netflix],

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

    clearTimeout(timer);

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

      content,

      icon: 'lock.open.display',

      'icon-color': '#007AFF'

    });

  }

  // ==================================
  // Concurrent Detection
  // ==================================

  const timer = setTimeout(

    finish,

    40000

  );

  Promise.all(

    services.map(s =>

      Promise.resolve()

        .then(s[1])

        .then(v => {

          values[s[0]] = v;

          console.log(

            s[0] + ': ' + v

          );

        })

        .catch(e => {

          values[s[0]] = unknown;

          console.log(

            s[0] + ': ' + String(e)

          );

        })

    )

  ).then(finish);

})();
