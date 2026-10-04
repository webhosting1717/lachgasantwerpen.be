import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const out='/tmp/claude-0/-home-user-lachgasantwerpen-be/67fc4ab1-ced0-522e-b4aa-cfe5831e8c00/scratchpad/';
const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const shots=[['/', 'home2'],['/bezorggebied/amsterdam-noord/','noord2'],['/lachgas-informatie/veilig-gebruik/','veilig2']];
for (const [w,h,tag] of [[390,844,'m'],[1280,900,'d']]) {
  const ctx = await browser.newContext({viewport:{width:w,height:h}});
  const page = await ctx.newPage();
  const errs=[]; page.on('console',m=>{ if(m.type()==='error') errs.push(m.text()); }); page.on('requestfailed',r=>errs.push('REQFAIL '+r.url()));
  for (const [p,name] of shots){
    await page.goto('http://127.0.0.1:8766'+p,{waitUntil:'networkidle'});
    const sw = await page.evaluate(()=>document.documentElement.scrollWidth);
    if (sw>w) errs.push('HORIZONTAL SCROLL '+p+' '+sw);
    await page.screenshot({path:out+name+'-'+tag+'.png', fullPage:false});
    if (name!=='home2') await page.screenshot({path:out+name+'-'+tag+'-full.png', fullPage:true});
  }
  console.log(tag,'errors:',errs);
  await ctx.close();
}
await browser.close();
