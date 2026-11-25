// ABEMA UnlockDetection
// Author: AllanRita
// Version: 1.1.0

$httpClient.get({
  url: "https://api.abema.io/v1/ip/check?device=android",
  timeout: 10,
  headers: {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13)",
    "Accept": "application/json",
    "Cache-Control": "no-cache"
  }
}, (error, response, data) => {

  if (error || !response) {
    return finish("?");
  }

  const status = response.status;

  if (status === 403 || status === 451) {
    return finish("☒");
  }

  if (status !== 200) {
    return finish("?");
  }

  try {
    const result = JSON.parse(data);
    const region = result.isoCountryCode || "";

    if (result.isAllowed === false) {
      return finish("☒" + region);
    }

    if (region === "JP") {
      return finish("☑JP");
    }

    if (region) {
      return finish("△" + region);
    }

    return finish("?");

  } catch (e) {
    return finish("?");
  }
});

function finish(result) {
  const now = new Date();
  const hh = ("0" + now.getHours()).slice(-2);
  const mm = ("0" + now.getMinutes()).slice(-2);

  $done({
    title: "UnlockDetection | " + hh + ":" + mm,
    content: "ABEMA: " + result,
    icon: "lock.open.display",
    "icon-color": "#007AFF"
  });
}
