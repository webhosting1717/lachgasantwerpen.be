import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [port, out, path, sel, w] = process.argv.slice(2);
const browser = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const page = await browser.newPage({viewport:{width:+w,height:900}});
await page.goto(`http://127.0.0.1:${port}${path}`,{waitUntil:'load'}); await page.waitForTimeout(300);
const el = await page.locator(sel).first(); await el.screenshot({path:out});
await browser.close();
