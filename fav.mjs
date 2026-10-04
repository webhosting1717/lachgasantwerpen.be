import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p = await b.newPage({viewport:{width:360,height:170}});
const u='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI+PHJlY3Qgd2lkdGg9IjY0IiBoZWlnaHQ9IjY0IiByeD0iMTQiIGZpbGw9IiMxZDRlZDgiLz48cGF0aCBkPSJNMjEuOCAxNmg4LjN2MjVoMTQuMXY3SDIxLjh6IiBmaWxsPSIjZmZmIi8+PC9zdmc+Cg==';
await p.setContent('<body style="margin:0;background:#fff;display:flex;gap:28px;align-items:center;padding:20px"><img src="'+u+'" width="128" height="128"><img src="'+u+'" width="48" height="48"><img src="'+u+'" width="32" height="32"><img src="'+u+'" width="16" height="16"></body>');
await p.waitForTimeout(300); await p.screenshot({path:'fav_rotterdam.png'}); await b.close();
