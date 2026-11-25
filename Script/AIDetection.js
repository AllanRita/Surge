// AI Detection V2.4
// Author: AllanRita
// Platform: Surge
// ChatGPT | Claude | Gemini
// Global Region Detection

(function () {

  const UA =
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';

  const ok = c => '☑' + (c || '');
  const partial = c => '△' + (c || '');
  const no = c => '☒' + (c || '');
  const unknown = '?';

  // Region Restriction

  const geo =
    /unsupported_country|app-unavailable-in-region|unsupported.country.region.territory|not available in your (?:country|region|location)|not (?:currently )?supported in your (?:country|region|location)|目前不支持你所在的|目前不支援你所在的/i;

  const challenge =
    /cf-chl-|challenge-platform|just a moment\.\.\.|captcha challenge|verify you are human/i;

  // ISO 3166 Country Code Conversion
  // Gemini: ISO-3 -> ISO-2

  const isoData = `
ABWAW AFGAF AGOAO AIAAI ALAAX ALBAL ANDAD AREAE
ARGAR ARMAM ASMAS ATAAQ ATFTF ATGAG AUSAU AUTAT
AZEAZ BDIBI BELBE BENBJ BESBQ BFABF BGDBD BGRBG
BHRBH BHSBS BIHBA BLMBL BLRBY BLZBZ BMUBM BOLBO
BRABR BRBBB BRNBN BTNBT BVTBV BWABW CAFCF CANCA
CCKCC CHECH CHLCL CHNCN CIVCI CMRCM CODCD COGCG
COKCK COLCO COMKM CPVCV CRICR CUBCU CUWCW CXRCX
CYMKY CYPCY CZECZ DEUDE DJIDJ DMADM DNKDK DOMDO
DZADZ ECUEC EGYEG ERIER ESHEH ESPES ESTEE ETHET
FINFI FJIFJ FLKFK FRAFR FROFO FSMFM GABGA GBRGB
GEOGE GGYGG GHAGH GIBGI GINGN GLPGP GMBGM GNBGW
GNQGQ GRCGR GRDGD GRLGL GTMGT GUFGF GUMGU GUYGY
HKGHK HMDHM HNDHN HRVHR HTIHT HUNHU IDNID IMNIM
INDIN IOTIO IRLIE IRNIR IRQIQ ISLIS ISRIL ITAIT
JAMJM JEYJE JORJO JPNJP KAZKZ KENKE KGZKG KHMKH
KIRKI KNAKN KORKR KWTKW LAOLA LBNLB LBRLR LBYLY
LCALC LIELI LKALK LSOLS LTULT LUXLU LVALV MACMO
MAFMF MARMA MCOMC MDAMD MDGMG MDVMV MEXMX MHLMH
MKDMK MLIML MLTMT MMRMM MNEME MNGMN MNPMP MOZMZ
MRTMR MSRMS MTQMQ MUSMU MWIMW MYSMY MYTYT NAMNA
NCLNC NERNE NFKNF NGANG NICNI NIUNU NLDNL NORNO
NPLNP NRUNR NZLNZ OMNOM PAKPK PANPA PCNPN PERPE
PHLPH PLWPW PNGPG POLPL PRIPR PRKKP PRTPT PRYPY
PSEPS PYFPF QATQA REURE ROURO RUSRU RWARW SAUSA
SDNSD SENSN SGPSG SGSGS SHNSH SJMSJ SLBSB SLESL
SLVSV SMRSM SOMSO SPMPM SRBRS SSDSS STPST SURSR
SVKSK SVNSI SWESE SWZSZ SXMSX SYCSC SYRSY TCATC
TCDTD TGOTG THATH TJKTJ TKLTK TKMTM TLSTL TONTO
TTOTT TUNTN TURTR TUVTV TWNTW TZATZ UGAUG UKRUA
UMIUM URYUY USAUS UZBUZ VATVA VCTVC VENVE VGBVG
VIRVI VNMVN VUTVU WLFWF WSMWS YEMYE ZAFZA ZMBZM
ZWEZW
`;

  const ISO = {};
  const ISO2 = new Set();

  isoData.trim().split(/\s+/).forEach(item => {
    ISO[item.slice(0, 3)] = item.slice(3);
    ISO2.add(item.slice(3));
  });

  function cc(value) {

    const s = String(value || '')
      .trim()
      .toUpperCase();

    if (s === 'UK') return 'GB';

    if (ISO2.has(s)) return s;

    return ISO[s] || '';

  }

  // HTTP Request
  // Follow existing Surge routing rules.
  // No fixed proxy policy.

  function request(url, opt) {

    opt = opt || {};

    return new Promise(resolve => {

      const options = {

        url: url,

        timeout: 7,

        'auto-redirect': false,

        'auto-cookie': false,

        headers: Object.assign({

          'User-Agent': UA,

          'Accept-Language': 'en-US,en;q=0.9',

          'Cache-Control': 'no-cache',

          'Accept':
            'text/html,application/json,text/plain,*/*'

        }, opt.headers || {})

      };

      try {

        $httpClient.get(
          options,
          (error, response, data) => {

            const headers = {};

            Object.keys(
              (response && response.headers) || {}
            ).forEach(k => {

              headers[k.toLowerCase()] =
                String(response.headers[k]);

            });

            resolve({

              status:
                error || !response
                  ? 0
                  : Number(response.status),

              text:
                typeof data === 'string'
                  ? data
                  : '',

              headers: headers,

              url: url

            });

          }
        );

      } catch (_) {

        resolve({
          status: 0,
          text: '',
          headers: {},
          url: url
        });

      }

    });

  }

  // Common Status Detection

  function restricted(r) {

    if (!r.status) return false;

    const loc = r.headers.location || '';

    if (r.status === 451 || geo.test(loc)) {
      return true;
    }

    if (challenge.test(r.text)) {
      return false;
    }

    return geo.test(r.text);

  }

  function usable(r) {

    return r.status >= 200 &&
      r.status < 300 &&
      !challenge.test(r.text) &&
      !restricted(r);

  }

  // Same-domain Redirect

  function nextURL(r, domain) {

    let loc = r.headers.location || '';

    if (!loc) return '';

    if (/^\/\//.test(loc)) {
      loc = 'https:' + loc;
    }

    if (/^\/(?!\/)/.test(loc)) {
      loc = 'https://' + domain + loc;
    }

    const m = loc.match(
      /^https:\/\/([^/]+)(?:\/|$)/i
    );

    if (!m) return '';

    if (m[1].toLowerCase() !== domain) {
      return '';
    }

    return loc;

  }

  async function page(url, domain) {

    let r = await request(url);

    for (let i = 0; i < 2; i++) {

      if (
        r.status < 300 ||
        r.status >= 400 ||
        restricted(r)
      ) {
        break;
      }

      const loc = nextURL(r, domain);

      if (!loc || loc === r.url) break;

      r = await request(loc);

    }

    return r;

  }

  // Cloudflare Region Detection

  function traceRegion(r) {

    if (!usable(r)) return '';

    const m = r.text.match(
      /^loc=([A-Z]{2})\s*$/im
    );

    return m ? cc(m[1]) : '';

  }

  // ==================================
  // 01. ChatGPT
  // ==================================

  async function chatgpt() {

    const results = await Promise.all([

      request(
        'https://chatgpt.com/cdn-cgi/trace'
      ),

      request(
        'https://chatgpt.com/backend-anon/models',
        {
          headers: {
            'Accept': 'application/json'
          }
        }
      ),

      page(
        'https://chatgpt.com/',
        'chatgpt.com'
      )

    ]);

    const trace = results[0];

    const models = results[1];

    const web = results[2];

    const c = traceRegion(trace);

    if (
      restricted(models) ||
      restricted(web)
    ) {

      return no(c);

    }

    if (usable(models)) {

      try {

        const data = JSON.parse(models.text);

        if (
          c &&
          Array.isArray(data.models) &&
          data.models.length > 0
        ) {

          return ok(c);

        }

      } catch (_) {}

    }

    if (c) return partial(c);

    if (usable(web)) return partial();

    return unknown;

  }

  // ==================================
  // 02. Claude
  // ==================================

  async function claude() {

    const results = await Promise.all([

      request(
        'https://claude.ai/cdn-cgi/trace'
      ),

      page(
        'https://claude.ai/',
        'claude.ai'
      )

    ]);

    const trace = results[0];

    const web = results[1];

    const c = traceRegion(trace);

    if (
      restricted(trace) ||
      restricted(web)
    ) {

      return no(c);

    }

    // Trace confirms the network region,
    // not authenticated account access.

    if (c) return partial(c);

    if (usable(web)) return partial();

    return unknown;

  }

  // ==================================
  // 03. Gemini
  // ==================================

  async function gemini() {

    const results = await Promise.all([

      page(
        'https://gemini.google.com/',
        'gemini.google.com'
      ),

      page(
        'https://gemini.google.com/app',
        'gemini.google.com'
      )

    ]);

    const regions = [];

    for (const r of results) {

      if (!usable(r)) continue;

      const body = r.text.replace(/\\"/g, '"');

      const matches = body.matchAll(
        /,\s*2,\s*1,\s*200,\s*"([A-Z]{3})"/g
      );

      for (const m of matches) {

        const c = cc(m[1]);

        if (c) regions.push(c);

      }

    }

    const unique = [...new Set(regions)];

    const c =
      unique.length === 1
        ? unique[0]
        : '';

    if (results.some(restricted)) {

      return no(c);

    }

    // Conflicting regions are not guessed.

    if (unique.length > 1) {
      return unknown;
    }

    // Region signal detected directly
    // from Gemini's own page.

    if (c) return partial(c);

    if (results.some(usable)) {

      return partial();

    }

    return unknown;

  }

  // ==================================
  // AI Services
  // ==================================

  const services = [

    ['ChatGPT', chatgpt],

    ['Claude', claude],

    ['Gemini', gemini]

  ];

  const values = {};

  services.forEach(s => {
    values[s[0]] = unknown;
  });

  let complete = false;

  // ==================================
  // Panel Layout
  // ==================================

  function result(name) {

    return name + ': ' +
      (values[name] || unknown);

  }

  function finish() {

    if (complete) return;

    complete = true;

    clearTimeout(timer);

    const d = new Date();

    const pad = n =>
      ('0' + n).slice(-2);

    const content = [

      result('ChatGPT') +
        ' | ' +
        result('Claude'),

      result('Gemini')

    ].join('\n');

    $done({

      title:
        'AI Detection | ' +
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

  const timer = setTimeout(
    finish,
    24000
  );

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
