// Meet navigatie-prestaties met netwerk-throttling (4G-achtig) via CDP, incl. tweede navigatie (warme cache).
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [port, ...paths] = process.argv.slice(2);
const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const ctx = await browser.newContext({viewport:{width:390,height:844}, userAgent:'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Mobile Safari/537.36'});
const page = await ctx.newPage();
const cdp = await ctx.newCDPSession(page);
await cdp.send('Network.enable');
await cdp.send('Network.emulateNetworkConditions', {offline:false, latency:150, downloadThroughput:1.6*1024*1024/8, uploadThroughput:750*1024/8});
await cdp.send('Emulation.setCPUThrottlingRate', {rate:4});
const rows=[];
for (const p of paths) {
  const reqs=[]; let bytes=0;
  const onReq = r => reqs.push(r.url());
  const onResp = async r => { try { const h=r.headers(); bytes += parseInt(h['content-length']||'0',10); } catch{} };
  page.on('request', onReq); page.on('response', onResp);
  const t0=Date.now();
  await page.goto(`http://127.0.0.1:${port}${p}`, {waitUntil:'load'});
  const loadMs=Date.now()-t0;
  const m = await page.evaluate(() => new Promise(res => {
    const nav = performance.getEntriesByType('navigation')[0];
    const paint = performance.getEntriesByType('paint');
    const fcp = paint.find(x=>x.name==='first-contentful-paint')?.startTime;
    let lcp=0; const po=new PerformanceObserver(l=>{for(const e of l.getEntries()) lcp=e.startTime;}); po.observe({type:'largest-contentful-paint', buffered:true});
    let cls=0; const po2=new PerformanceObserver(l=>{for(const e of l.getEntries()) if(!e.hadRecentInput) cls+=e.value;}); po2.observe({type:'layout-shift', buffered:true});
    setTimeout(()=>res({ttfb:nav.responseStart, dcl:nav.domContentLoadedEventEnd, load:nav.loadEventEnd, fcp, lcp, cls, transfer: performance.getEntriesByType('resource').reduce((s,r)=>s+(r.transferSize||0), nav.transferSize||0), res: performance.getEntriesByType('resource').length+1, fonts: performance.getEntriesByType('resource').filter(r=>/font|gstatic|googleapis/.test(r.name)).length}), 600);
  }));
  page.off('request', onReq); page.off('response', onResp);
  rows.push({path:p, ...Object.fromEntries(Object.entries(m).map(([k,v])=>[k, typeof v==='number'? Math.round(v*(k==='cls'?1000:1))/(k==='cls'?1000:1):v]))});
}
console.table(rows);
await browser.close();
