// Iconen en OG-afbeelding voor lachgasbrabant.nl renderen met Chromium
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'node:fs';
const out = process.argv[2];
const svg = fs.readFileSync(process.argv[3], 'utf8');
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p = await b.newPage();
for (const [name,size] of [['icon-512',512],['icon-192',192],['apple-touch-icon',180],['favicon-48',48],['favicon-32',32],['favicon-16',16]]) {
  await p.setViewportSize({width:size,height:size});
  await p.setContent(`<body style="margin:0;background:transparent"><img src="data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}" width="${size}" height="${size}" style="display:block"></body>`);
  await p.screenshot({path:`${out}/${name}.png`, omitBackground:true, clip:{x:0,y:0,width:size,height:size}});
}
await p.setViewportSize({width:1200,height:630});
await p.setContent(`<body style="margin:0;width:1200px;height:630px;background:#1c1917;font-family:system-ui,sans-serif;color:#fff;position:relative;overflow:hidden">
<div style="position:absolute;right:-120px;top:-120px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(226,86,42,.55),transparent 70%)"></div>
<div style="position:absolute;left:80px;top:90px;display:flex;align-items:center;gap:18px"><div style="width:72px;height:72px;border-radius:18px;background:#b4350f;display:grid;place-items:center;font-weight:800;font-size:38px">L</div><div style="font-size:34px;font-weight:800">Lachgas <span style="color:#e2562a">Brabant</span></div></div>
<div style="position:absolute;left:80px;top:230px;font-size:64px;font-weight:800;line-height:1.08;letter-spacing:-.01em;max-width:900px">Lachgas bestellen in heel Noord-Brabant</div>
<div style="position:absolute;left:80px;top:420px;font-size:28px;color:rgba(255,255,255,.75)">24/7 via WhatsApp &middot; verzegeld bezorgd &middot; uitsluitend 18+</div>
<div style="position:absolute;left:80px;bottom:60px;display:flex;gap:14px"><span style="padding:12px 22px;border-radius:999px;background:#15803d;font-weight:700;font-size:22px">WhatsApp ons</span><span style="padding:12px 22px;border-radius:999px;border:2px solid rgba(255,255,255,.3);font-size:22px">lachgasbrabant.nl</span></div>
</body>`);
await p.screenshot({path:`${out}/og-lachgas-brabant.png`});
await b.close(); console.log('assets ok');
