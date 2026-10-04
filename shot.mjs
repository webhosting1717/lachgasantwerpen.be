import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const out='/tmp/claude-0/-home-user-lachgasantwerpen-be/67fc4ab1-ced0-522e-b4aa-cfe5831e8c00/scratchpad/';
const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(async e=>{console.log('fallback launch',e.message); return chromium.launch();});
const shots=[['/', 'home'],['/bezorggebied/amsterdam-noord/','noord'],['/lachgas-tanks/2kg/','tank2kg'],['/lachgas-informatie/veilig-gebruik/','veilig']];
for (const [w,h,tag] of [[390,844,'m'],[1280,900,'d']]) {
  const ctx = await browser.newContext({viewport:{width:w,height:h}, deviceScaleFactor:1});
  const page = await ctx.newPage();
  const errs=[]; page.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); }); page.on('requestfailed',r=>errs.push('REQFAIL '+r.url()));
  for (const [p,name] of shots){
    await page.goto('http://127.0.0.1:8765'+p,{waitUntil:'networkidle'});
    await page.screenshot({path:out+name+'-'+tag+'.png', fullPage: tag==='m' && name==='home' ? false : (name!=='home')});
  }
  console.log(tag,'errors:',errs);
  await ctx.close();
}
await browser.close();
