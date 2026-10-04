import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const [w,h,dev] of [[390,844,'mobile'],[1280,900,'desktop']]) {
  const ctx = await browser.newContext({viewport:{width:w,height:h}});
  const page = await ctx.newPage();
  const reqs=[]; page.on('response', async r=>{ try{ const b=await r.body(); reqs.push({url:r.url().replace('http://127.0.0.1:8776',''), type:r.request().resourceType(), bytes:b.length}); }catch(e){} });
  await page.addInitScript(()=>{ window.__cls=0; window.__lcp=null; new PerformanceObserver(l=>{for(const e of l.getEntries()){ if(!e.hadRecentInput) window.__cls+=e.value; }}).observe({type:'layout-shift',buffered:true}); new PerformanceObserver(l=>{const e=l.getEntries().pop(); if(e) window.__lcp={t:e.startTime, el:(e.element&&(e.element.tagName+'.'+e.element.className+' '+(e.element.currentSrc||''))), size:e.size};}).observe({type:'largest-contentful-paint',buffered:true}); });
  await page.goto('http://127.0.0.1:8776/',{waitUntil:'networkidle'});
  await page.waitForTimeout(1500);
  const m = await page.evaluate(()=>({cls:window.__cls, lcp:window.__lcp, fonts:[...document.fonts].map(f=>f.family+' '+f.status).filter((v,i,a)=>a.indexOf(v)===i), blocking:[...document.querySelectorAll('head link[rel=stylesheet], head script:not([async]):not([defer]):not([type="application/ld+json"])')].map(e=>e.outerHTML.slice(0,120)), imgsNoDim:[...document.images].filter(i=>!i.getAttribute('width')||!i.getAttribute('height')).map(i=>i.getAttribute('src')), lazy:[...document.images].map(i=>(i.loading||'eager')+' '+i.getAttribute('src')).slice(0,12), domNodes:document.querySelectorAll('*').length}));
  const total=reqs.reduce((a,r)=>a+r.bytes,0);
  console.log(`== ${dev}: requests=${reqs.length} total=${(total/1024).toFixed(0)}KB CLS=${m.cls.toFixed(3)} LCP=${m.lcp?Math.round(m.lcp.t)+'ms '+m.lcp.el:'n/a'} DOM=${m.domNodes}`);
  console.log('blocking:', m.blocking); console.log('fonts:', m.fonts); console.log('img no dims:', m.imgsNoDim); console.log('lazy:', m.lazy);
  console.log('largest:', reqs.sort((a,b)=>b.bytes-a.bytes).slice(0,8).map(r=>`${(r.bytes/1024).toFixed(0)}KB ${r.type} ${r.url}`));
  await ctx.close();
}
await browser.close();
