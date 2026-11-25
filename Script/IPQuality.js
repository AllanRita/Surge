// IPQuality V1.0
// Author: AllanRita
// Platform: Surge
// Global IP Quality Detection
// Data Source: IPQuery
// https://ipquery.io/

(function () {

  const API =
    'https://api.ipquery.io/?format=json';

  const POLICY =
    typeof $argument === 'string'
      ? $argument.trim()
      : 'AUTO';

  const options = {
    url: API,
    timeout: 12,
    'auto-redirect': false,
    'auto-cookie': false,
    headers: {
      'Accept': 'application/json',
      'Cache-Control': 'no-cache'
    }
  };

  // AUTO follows existing Surge rules.
  // Other values use an existing policy.

  if (POLICY && POLICY !== 'AUTO') {
    options.policy = POLICY;
  }

  let complete = false;

  function time() {

    const d = new Date();
    const pad = n => ('0' + n).slice(-2);

    return pad(d.getHours()) +
      ':' + pad(d.getMinutes());

  }

  function finish(content, color) {

    if (complete) return;

    complete = true;

    $done({
      title: 'IPQuality | ' + time(),
      content: content,
      icon: 'checkmark.shield.fill',
      'icon-color': color
    });

  }

  function text(v) {

    return v === undefined ||
      v === null ||
      v === ''
      ? '未知'
      : String(v);

  }

  // Country Flag

  function flag(code) {

    const c = String(code || '')
      .toUpperCase();

    if (!/^[A-Z]{2}$/.test(c)) {
      return '';
    }

    return String.fromCodePoint(
      ...c.split('').map(
        x => x.charCodeAt(0) + 127397
      )
    );

  }

  // Detection Status

  function state(v) {

    if (v === true) return '已识别';

    if (v === false) return '未识别';

    return '未知';

  }

  // Network Classification

  function ipType(risk) {

    if (risk.is_datacenter === true) {
      return '数据中心 / 机房';
    }

    if (risk.is_mobile === true) {
      return '移动网络';
    }

    if (risk.is_datacenter === false) {
      return '非机房（住宅待确认）';
    }

    return '未知';

  }

  // Risk Score

  function scoreOf(risk) {

    const n = risk.risk_score;

    if (
      typeof n !== 'number' ||
      !Number.isFinite(n) ||
      n < 0 ||
      n > 100
    ) {
      return null;
    }

    return n;

  }

  function riskLevel(score) {

    if (score === null) return '未知';

    if (score < 25) return '较低';

    if (score < 50) return '中等';

    if (score < 75) return '较高';

    return '高';

  }

  function errorPanel(message) {

    finish(
      '检测失败：' + message +
      '\n请检查网络及分流规则',
      '#8E8E93'
    );

  }

  // Main Request

  try {

    $httpClient.get(
      options,
      function (error, response, data) {

        if (error || !response) {

          return errorPanel(
            '网络连接异常'
          );

        }

        if (response.status !== 200) {

          return errorPanel(
            'HTTP ' + response.status
          );

        }

        let result;

        try {

          result = JSON.parse(data);

        } catch (_) {

          return errorPanel(
            '接口解析异常'
          );

        }

        if (
          !result ||
          typeof result.ip !== 'string' ||
          !result.ip
        ) {

          return errorPanel(
            '未返回有效IP'
          );

        }

        const location =
          result.location || {};

        const isp =
          result.isp || {};

        const risk =
          result.risk || {};

        const ip = result.ip;

        const country = String(
          location.country_code || ''
        ).toUpperCase();

        const city =
          location.city || '';

        const region = [
          flag(country),
          country || '未知',
          city ? '· ' + city : ''
        ].filter(Boolean).join(' ');

        const provider =
          isp.isp ||
          isp.org ||
          '未知';

        const asn = text(isp.asn);

        const type = ipType(risk);

        const score = scoreOf(risk);

        const level = riskLevel(score);

        const scoreText =
          score === null
            ? '未知'
            : score + '/100 · ' + level;

        const content = [

          'IP：' + ip,

          '地区：' + region,

          '运营商：' + provider,

          'ASN：' + asn,

          'IP类型：' + type,

          '风险评分：' + scoreText,

          'VPN：' + state(risk.is_vpn) +
            ' | Proxy：' + state(risk.is_proxy),

          'Tor：' + state(risk.is_tor),

          '线路：' +
            (
              !POLICY || POLICY === 'AUTO'
                ? '按分流规则'
                : POLICY
            )

        ].join('\n');

        finish(content, '#34C759');

      }
    );

  } catch (_) {

    errorPanel('脚本执行异常');

  }

})();
