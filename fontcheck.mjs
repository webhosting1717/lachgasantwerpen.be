import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const u = new URL(process.env.HTTPS_PROXY);
const proxy = {server: u.protocol+'//'+u.host}; if (u.username) { proxy.username=decodeURIComponent(u.username); proxy.password=decodeURIComponent(u.password); }
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium', proxy, args:['--ignore-certificate-errors']});
const ctx = await b.newContext({viewport:{width:1280,height:700}, ignoreHTTPSErrors:true}); const p = await ctx.newPage();
const ev=[]; p.on('response', r=>{ if(/gstatic|googleapis/.test(r.url())) ev.push(r.status()+' '+r.url().slice(0,80)); }); p.on('requestfailed', r=>{ if(/gstatic|googleapis/.test(r.url())) ev.push('FAIL '+r.failure()?.errorText+' '+r.url().slice(0,60)); });
await p.goto(process.argv[2], {waitUntil:'load'}); await p.waitForTimeout(2000);
const used = await p.evaluate(async()=>{ await document.fonts.ready; return [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight); });
console.log('events:', ev); console.log('loaded:', used);
await p.screenshot({path:process.argv[3]}); await b.close();
