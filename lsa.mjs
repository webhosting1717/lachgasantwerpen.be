import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const out='/tmp/claude-0/-home-user-lachgasantwerpen-be/67fc4ab1-ced0-522e-b4aa-cfe5831e8c00/scratchpad/';
const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const [port,tag] of [[8771,'voor'],[8772,'na']]) {
  for (const [w,h,dev] of [[390,844,'m'],[1280,900,'d']]) {
    const ctx = await browser.newContext({viewport:{width:w,height:h}});
    const page = await ctx.newPage();
    await page.goto(`http://127.0.0.1:${port}/`,{waitUntil:'networkidle'}).catch(e=>console.log('err',e.message));
    await page.waitForTimeout(500);
    await page.screenshot({path:`${out}lsa-${tag}-${dev}.png`, fullPage:false});
    await page.screenshot({path:`${out}lsa-${tag}-${dev}-full.png`, fullPage:true});
    await ctx.close();
  }
}
await browser.close();
