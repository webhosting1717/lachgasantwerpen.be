import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [port, prefix, ...paths] = process.argv.slice(2);
const out='/tmp/claude-0/-home-user-lachgasantwerpen-be/67fc4ab1-ced0-522e-b4aa-cfe5831e8c00/scratchpad/';
const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const [w,h,dev] of [[390,844,'m'],[1280,900,'d']]) {
  const ctx = await browser.newContext({viewport:{width:w,height:h}}); const page = await ctx.newPage();
  const errs=[]; page.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); }); page.on('pageerror',e=>errs.push('PAGEERR '+e.message));
  for (const p of paths) {
    await page.goto(`http://127.0.0.1:${port}${p}`,{waitUntil:'load'}).catch(e=>errs.push('NAV '+p+' '+e.message));
    await page.waitForTimeout(300);
    const sw = await page.evaluate(()=>document.documentElement.scrollWidth);
    if (sw>w) errs.push('HSCROLL '+p+' '+sw);
    const name = p.replace(/\//g,'_')||'_root';
    await page.screenshot({path:`${out}${prefix}${name}-${dev}.png`, fullPage:true});
  }
  console.log(dev, 'errors:', errs.filter(e=>!e.includes('fonts.g')));
  await ctx.close();
}
await browser.close();
