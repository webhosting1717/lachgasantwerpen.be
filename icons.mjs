import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const [svgPath, outDir] = process.argv.slice(2);
const svg = fs.readFileSync(svgPath,'utf8');
const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const size of [32, 48, 180, 192, 512]) {
  const ctx = await browser.newContext({viewport:{width:size,height:size}, deviceScaleFactor:1});
  const page = await ctx.newPage();
  await page.setContent(`<html><body style="margin:0;background:transparent">${svg.replace('<svg ', `<svg width="${size}" height="${size}" `)}</body></html>`);
  await page.screenshot({path:`${outDir}/icon-${size}.png`, omitBackground:true, clip:{x:0,y:0,width:size,height:size}});
  await ctx.close();
}
await browser.close();
