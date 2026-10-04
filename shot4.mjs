import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const out='/tmp/claude-0/-home-user-lachgasantwerpen-be/67fc4ab1-ced0-522e-b4aa-cfe5831e8c00/scratchpad/';
const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const [w,h,tag] of [[390,844,'m'],[1280,900,'d']]) {
  const ctx = await browser.newContext({viewport:{width:w,height:h}});
  const page = await ctx.newPage();
  await page.goto('http://127.0.0.1:8768/',{waitUntil:'networkidle'});
  await page.screenshot({path:out+'home4-'+tag+'.png', fullPage:true, clip:{x:0,y:tag==='m'?750:820,width:w,height:tag==='m'?1500:900}});
  await page.goto('http://127.0.0.1:8768/bezorggebied/amsterdam-noord/',{waitUntil:'networkidle'});
  await page.screenshot({path:out+'noord4-'+tag+'.png', fullPage:true, clip:{x:0,y:tag==='m'?900:700,width:w,height:tag==='m'?900:500}});
  await ctx.close();
}
await browser.close();
