# Brief voor contentmodules (fase 3) — lees volledig voordat je schrijft

Je schrijft een Python-contentmodule (UTF-8, eerste regel `# -*- coding: utf-8 -*-`, alleen data: geen imports, geen functies) met letterlijke Nederlandse teksten voor een statische website van een lachgas-bezorgservice. Het bestand moet importeerbaar zijn (`python3 -c "import <naam>"`).

## Harde regels (afwijken = afgekeurd)
- Uitsluitend voor 18+. Geen gebruiksinstructies, geen dosering, geen aantallen ballonnen, niets dat gebruik aanmoedigt of verheerlijkt. Nooit "onschuldig", "veilig middel", "legaal voor recreatief gebruik".
- GEEN prijzen of bedragen, geen "goedkoopst", geen telefoonnummer, geen "bel ons". Wel: "prijs vooraf bevestigd via WhatsApp", "betalen bij levering".
- Levertijden altijd met "meestal" en als indicatie, nooit als garantie. Gebruik de levertijd die per pagina is opgegeven.
- Geen verzonnen reviews, cijfers over klanten, keurmerken, bedrijfsgeschiedenis, namen van medewerkers. Geen concurrentnamen.
- Feiten over plaatsen (wijken, stations, wegen, afstanden) moeten kloppen; bij twijfel weglaten. Wetgeving voorzichtig formuleren en naar een officiële bron verwijzen.
- Teksten moeten natuurlijk en zakelijk klinken, geen marketingkreten, geen herhaling van de plaatsnaam in elke zin, geen opsommingen van loze beloften. Elke pagina volledig uniek: hergebruik geen zinnen tussen pagina's (ook niet licht aangepast).
- HTML in teksten beperkt tot <a href="..."> en <strong>. Alleen links uit de toegestane lijst (zie site-brief). Maximaal 2 links per alinea. Gebruik echte apostrofs (’ of ') en geen HTML-entities.
- Lengtes: title ≤ 60 tekens; description 120–155 tekens; h1 kort; lead 1–2 zinnen (max 180 tekens); intro-alinea's 60–110 woorden.

## Schema: gebied (AREAS)
{"slug": "...", "name": "...", "kind": "stad|gemeente|dorp|wijk", "title": "...", "description": "...", "h1": "...", "lead": "...",
 "intro": ["alinea 1: ligging, buurten/kernen, hoe bestellen", "alinea 2: route vanuit de stad, OV, waarom deze levertijd", "alinea 3: situaties, tankkeuze met link naar assortiment, betalen, 18+, link veilig gebruik"],
 "wijken": "6–10 echte wijken/buurten/kernen/plekken, komma-gescheiden, zonder punt", "levertijd": "meestal binnen X tot Y minuten",
 "faq": [["Vraag?", "Antwoord 1–3 zinnen, max 1 link"], ["...", "..."], ["...", "..."]],   # precies 3, lokaal en uniek
 "nearby": ["slug", "slug", "slug"],   # precies 3 slugs uit de lijst in de site-brief
 "lat": 51.5, "lon": 4.7}

## Schema: artikel (ARTICLES) en servicepagina (SERVICE_PAGES)
{"slug": "...", "label": "Gezondheid|Praktisch|Regels|Achtergrond|Service|...", "title": "...", "description": "...", "h1": "...", "lead": "...",
 "sections": [{"h2": "...", "paragraphs": ["60–120 woorden", "..."], "bullets": ["optioneel", "..."]}, ...],   # artikel 4–6 secties (600–900 woorden), service 3–5 secties (400–650 woorden)
 "note": "Let-op-tekst (1–3 zinnen)", "related": ["slug", "slug"],   # 2–4 slugs van artikelen/servicepagina's uit de site-brief
 "faq": [["V?", "A"], ["V?", "A"], ["V?", "A"]]}   # alleen bij SERVICE_PAGES: precies 3

## Schema: FAQ-thema (FAQ_TOPICS)
{"slug": "bestellen", "title": "...", "description": "...", "h1": "Vragen over bestellen", "lead": "...", "intro": ["1 alinea 50–90 woorden"],
 "items": [["Vraag?", "Antwoord 2–4 zinnen, max 1 link"], ...],   # 8–12 items per thema, uniek, geen overlap met andere thema's
 "related": ["slug", "slug"]}

## Schema: regio-hub (HUBS)
{"slug": "west-brabant", "name": "West-Brabant", "title": "...", "description": "...", "h1": "...", "lead": "...",
 "intro": ["3 alinea's 60–110 woorden: wat de regio is, hoe levertijd met afstand samenhangt, hoe bestellen"],
 "groups": [{"h2": "Deelgebied", "text": "1 zin", "slugs": ["slug", ...]}, ...],
 "faq": [["V?", "A"], ["V?", "A"], ["V?", "A"], ["V?", "A"], ["V?", "A"]]}

## Schema: productpagina (PRODUCTS) — bestaande URL /product/<slug>/ wordt herschreven
{"slug": "lachgas-tank-2kg", "title": "...", "description": "...", "h1": "Lachgastank 2KG", "lead": "...",
 "facts": [["Inhoud", "2 kilo N2O"], ["Levering", "Verzegeld, aan de deur"], ["Levertijd", "..."], ["Betalen", "..."], ["Leeftijd", "Uitsluitend 18+"], ["Prijs", "Op aanvraag via WhatsApp"]],
 "sections": [3–4 secties, totaal 400–650 woorden: voor wie dit formaat past, hoe de levering gaat, bewaren/vervoeren, verantwoord omgaan (zonder gebruiksinstructies of ballonaantallen)],
 "note": "...", "faq": [["V?", "A"], ["V?", "A"], ["V?", "A"]], "related": ["slug", ...]}

## Schema: over ons (ABOUT) — herschrijft /over-ons/
{"title": "...", "description": "...", "h1": "...", "lead": "...", "sections": [4–5 secties, 450–700 woorden: wie wij zijn (zonder verzonnen geschiedenis of namen), hoe wij werken, werkgebied, waar wij voor staan (18+, verzegeld, eerlijke informatie), contact], "note": "..."}

## Schema: SITE_TEXTS (dict) — unieke gedeelde blokken per site
{"home_title": "≤60", "home_description": "120–155", "home_h1": "platte tekst met de stadsnaam erin, max 70 tekens", "home_hero_lead": "2–3 zinnen, max 320 tekens, mag 1 <a>",
 "home_why_h2": "...", "home_why": [[kop, 1 zin] ×4], "home_areas_text": "1–2 zinnen onder 'Lachgas bezorgd in heel <Stad>'",
 "home_faq": [[vraag, antwoord 2–4 zinnen, max 1 link] ×6],
 "why_h2": "kop van het 'waarom wij'-blok op alle subpagina's", "why": [[kop, 1 zin] ×4] — het 4e item MOET beginnen met "Snelle levering" als kop en als tekst "In <Stad> meestal binnen 20 tot 30 minuten." (wordt per gebied automatisch gelokaliseerd),
 "cta_h2": "...", "cta_text": "1 zin",
 "assortiment": {"lead": "1–2 zinnen voor de paginakop van /assortiment/", "intro": ["2 alinea's van 60–100 woorden"]},
 "footer_links": [[ankerregel, nieuwe regel], ...] — laat leeg: wordt door de generator ingevuld}

## Schema: FAQ_INDEX (dict) — hub /veelgestelde-vragen/ (Rotterdam: /faq/)
{"title": "≤60", "description": "120–155", "intro": ["1 alinea 50–90 woorden met uitleg van de thema's"]}

## Schema: PAGES_EXTRA (dict) — unieke teksten voor assortiment, bezorggebied-index, informatie-index en contact
{"assortiment": {"title": "≤60", "description": "120–155", "h1": "...", "lead": "1–2 zinnen", "intro": ["2 alinea's 60–100 woorden"],
                 "sections": [3 secties van 80–140 woorden: welk formaat past bij welke situatie (zonder ballonaantallen), cracker en slagroompatronen uitgelegd (wat, waarvoor, veilig bewaren; geen gebruiksinstructie), hoe bestellen en bezorgen gaat], "note": "...", "faq": [4 paren]},
 "areas_index": {"title": "≤60", "description": "120–155", "lead": "1–2 zinnen", "h2": "kop boven de intro", "intro": ["2 alinea's 60–100 woorden"]},
 "info_index": {"title": "≤60", "description": "120–155", "lead": "1–2 zinnen", "intro": ["1–2 alinea's 50–90 woorden"]},
 "contact": {"title": "≤60", "description": "120–155", "lead": "1–2 zinnen", "intro": ["2 alinea's 50–90 woorden: WhatsApp als hoofdkanaal, wat je in je eerste bericht zet, e-mail voor niet-dringende vragen; noem geen nummer of e-mailadres"]}}
