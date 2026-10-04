import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [port,tag]=process.argv.slice(2); const out='/tmp/claude-0/-home-user-lachgasantwerpen-be/67fc4ab1-ced0-522e-b4aa-cfe5831e8c00/scratchpad/';
const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const res={};
for (const p of ['/','/lachgas-bestellen/noord.html','/faq.html','/contact.html']) for (const [w,h,dev] of [[390,844,'m'],[1280,900,'d']]) {
  const ctx = await browser.newContext({viewport:{width:w,height:h}}); const page = await ctx.newPage();
  await page.goto(`http://127.0.0.1:${port}${p}`,{waitUntil:'networkidle'}); await page.waitForTimeout(400);
  res[p+'@'+dev] = await page.evaluate(()=>[...document.querySelectorAll('body *')].filter(e=>e.offsetParent!==null||e.tagName==='IMG').map(e=>{const r=e.getBoundingClientRect();return e.tagName+(e.className&&typeof e.className==='string'?'.'+e.className.split(' ')[0]:'')+':'+Math.round(r.x)+','+Math.round(r.y)+','+Math.round(r.width)+','+Math.round(r.height)}).join('\n'));
  if (p==='/') await page.screenshot({path:`${out}lsa-${tag}-${dev}.png`});
  await ctx.close();
}
await browser.close();
import('fs').then(fs=>fs.writeFileSync(out+'boxes-'+tag+'.json', JSON.stringify(res)));
