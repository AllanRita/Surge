// AI Detection V2.1 | AllanRita | Surge
// Independent implementation; public probe references:
// https://github.com/lmc999/RegionRestrictionCheck
// https://manual.nssurge.com/scripting/api.html
// No credentials, MITM, rewrites or proxy changes.
// △ = reachable / region signal only; ☒ = explicit geo restriction; ? = unknown.

(function () {
  const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36';
  const POLICY = '';
  const ok = c => '☑' + (c || '');
  const partial = c => '△' + (c || '');
  const no = c => '☒' + (c || '');
  const unknown = '?';

  const geo = /unsupported_country|app-unavailable-in-region|not available in your (?:country|region|location)|not (?:currently )?available in your (?:country|region|location)|outside (?:the )?(?:united states|us)|GEO_CHECK_FAIL|available (?:only )?in South Korea|このサービスは日本国内|日本国外からはご利用|僅限台灣地區|仅限台湾地区/i;

  const challenge = /cf-chl-|challenge-platform|just a moment\.\.\.|captcha challenge|verify you are human|access denied|security policy has been breached/i;

  const cc = s => /^[a-z]{2}$/i.test(String(s || '')) ? String(s).toUpperCase() : '';

  const field = (s, k) => { const m = s.match(new RegExp('"' + k + '"\\s*:\\s*"([^"\\r\\n]+)"','i')); return m ? m[1] : ''; };

  const flag = (s,k) => { const m=s.match(new RegExp('"'+k+'"\\s*:\\s*(true|false)','i')); return m ? m[1].toLowerCase() : ''; };

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
          'Accept-Language':'en-US,en;q=0.9',
          'Cache-Control':'no-cache'
        },opt.headers || {})
      };

      if (POLICY) o.policy = POLICY;
      if (opt.body !== undefined) o.body = opt.body;
      const method = opt.method || 'get';

      try {
        $httpClient[method](o, (e,r,d) => {
          const h = {};
          Object.keys((r && r.headers) || {}).forEach(k => h[k.toLowerCase()] = String(r.headers[k]));

          resolve({
            status: e || !r ? 0 : Number(r.status),
            text: typeof d === 'string' ? d : '',
            headers:h,
            url
          });
        });
      } catch (_) {
        resolve({status:0,text:'',headers:{},url});
      }
    });
  }

  function nextURL(r) {
    const l=r.headers.location || '';
    if (/^https:\/\//i.test(l)) return l;
    if (/^\/(?!\/)/.test(l)) return r.url.match(/^https:\/\/[^/]+/i)[0]+l;
    return '';
  }

  function sameFamily(a,b) {
    const host=u=>((u.match(/^https:\/\/([a-z0-9.-]+)(?:\/|$)/i)||[])[1]||'').toLowerCase();
    const x=host(a), y=host(b);
    return !!x && !!y && (x===y || x.replace(/^www\./,'')===y.replace(/^www\./,''));
  }

  async function page(url) {
    let r=await request(url);
    let loc=nextURL(r);

    if (r.status>=300 && r.status<400 && loc && !geo.test(loc) && !/\/(?:unavailable|intl)(?:[/?#]|$)/i.test(loc) && sameFamily(url,loc)) {
      const n=await request(loc);
      n.firstLocation=loc;
      return n;
    }
    return r;
  }

  function basic(r) {
    if (!r.status) return unknown;
    if (r.status===451 || geo.test(r.headers.location||'') || (r.status<500 && !challenge.test(r.text) && geo.test(r.text))) return no();
    if (challenge.test(r.text) || [403,429].includes(r.status) || r.status>=500) return unknown;
    if (r.status>=200 && r.status<400) return partial();
    return unknown;
  }

  function usable(r) {
    return r.status>=200 && r.status<300 && !challenge.test(r.text);
  }

  function pathRegion(u) {
    const m=String(u||'').match(/^https:\/\/[^/]+\/([a-z]{2})(?:-[a-z]{2})?(?:[/?#]|$)/i);
    return m?cc(m[1]):'';
  }

  // ChatGPT
  async function gpt() {
    const r=await request('https://chatgpt.com/cdn-cgi/trace');
    const b=basic(r);

    if(b!==partial())return b;

    const c=cc((r.text.match(/^loc=([A-Z]{2})\s*$/m)||[])[1]);

    return c?partial(c):basic(await page('https://chatgpt.com/'));
  }

  // Claude
  async function claude() {
    const r=await page('https://claude.ai/');
    return basic(r);
  }

  // Gemini
  const reach = url => async () => basic(await page(url));

  const services = [
    ['GPT',gpt],
    ['Claude',claude],
    ['Gemini',reach('https://gemini.google.com/')]
  ];

  const rows=[3];
  const values=services.map(()=>unknown);
  let complete=false;

  function finish(){
    if(complete)return;
    complete=true;

    const d=new Date();
    const pad=n=>('0'+n).slice(-2);
    let i=0;

    const content=rows.map(n=>services.slice(i,i+n).map((s,j)=>s[0]+': '+values[i+j]).join(' | ')+(i+=n,'')).join('\n');

    $done({
      title:'AI Detection | '+pad(d.getHours())+':'+pad(d.getMinutes()),
      content,
      icon:'lock.open.display',
      'icon-color':'#007AFF'
    });
  }

  setTimeout(finish, 24*1000);

  Promise.all(services.map((s,i)=>Promise.resolve().then(s[1]).then(v=>{
    values[i]=v;
    console.log(s[0]+': '+v);
  }).catch(()=>{}))).then(finish);

})();
