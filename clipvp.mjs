import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const [port, out, path, w, h] = process.argv.slice(2);
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p = await b.newPage({viewport:{width:+w,height:+h}});
await p.goto(`http://127.0.0.1:${port}${path}`,{waitUntil:'load'}); await p.waitForTimeout(300);
await p.screenshot({path:out}); await b.close();
