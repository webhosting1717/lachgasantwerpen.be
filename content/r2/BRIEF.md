# Brief: content voor lachgasrotterdam.nl (fase 2, uitbreiding Zuid-Holland)

Je schrijft een Python-contentmodule (UTF-8, `# -*- coding: utf-8 -*-` als eerste regel) met letterlijke Nederlandse teksten voor de statische website lachgasrotterdam.nl (merk "Lachgas Rotterdam", bezorgservice voor lachgastanks, bestellen via WhatsApp +31 6 17341812, e-mail info@lachgasrotterdam.nl). Aanspreekvorm "je". Het bestand moet importeerbaar zijn (`python3 -c "import x"`) en ALLEEN data bevatten (geen functies, geen imports).

## Harde regels (afwijken = afgekeurd)
- Uitsluitend voor 18+. Geen gebruiksinstructies, geen dosering, niets dat gebruik aanmoedigt. Lachgas = tanks met N2O voor volwassenen; recreatief gebruik niet verheerlijken. Zeg nooit "lachgas is onschuldig".
- GEEN prijzen, geen euro-bedragen, geen "goedkoopste". Wel: "prijs vooraf bevestigd via WhatsApp", "betalen bij levering, contant of via Tikkie".
- Levertijd: Rotterdam zelf "meestal binnen 20 tot 30 minuten"; buurgemeenten "meestal binnen 25 tot 40 minuten"; verder weg (Dordrecht, Gouda, Zoetermeer, Hellevoetsluis, Naaldwijk, Oud-Beijerland) "meestal binnen 35 tot 50 minuten". Altijd "meestal", nooit garantie.
- 24/7 bereikbaar via WhatsApp, ook 's nachts en in het weekend. GEEN telefoonnummer noemen, geen "bel ons".
- Wet: lachgas staat sinds 1 januari 2023 op lijst II van de Opiumwet; verkoop/bezit voor recreatief gebruik is verboden, met uitzonderingen voor medisch, technisch en voedingsgebruik. Formuleer altijd voorzichtig en verwijs naar rijksoverheid.nl. Nooit beweren dat recreatief gebruik legaal is.
- Geen verzonnen reviews, geen verzonnen cijfers over klanten, geen namen van concurrenten.
- Producten: lachgastanks 2KG, 4KG en 10KG (schrijf exact zo: "2KG"), verzegeld geleverd. Geen patronen/crackers (die verkopen we niet).
- Interne links die je mag gebruiken (relatief, exact): /lachgas-tanks/, /veilig-gebruik/, /lachgas-nachtbezorging/, /lachgas-feest-evenement/, /werkwijze/, /voordelen/, /faq/, /contact/, /bezorggebieden/, /lachgas-informatie/, /lachgas-informatie/wat-is-lachgas/, /lachgas-informatie/lachgas-en-vitamine-b12/, /lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/, /lachgas-informatie/is-lachgas-legaal-in-nederland/, /lachgas-informatie/lachgas-in-het-verkeer/, en /lachgas-bestellen/<slug>/ voor elk bestaand gebied (lijst hieronder). Externe links alleen: https://www.drugsinfo.nl, https://www.rijksoverheid.nl, https://www.trimbos.nl. Maximaal 2 links per alinea. HTML in teksten beperkt tot <a href="..."> en <strong>. Geen andere HTML, geen markdown.
- Gebruik gewone rechte aanhalingstekens in HTML-attributen; in Python-strings dubbele quotes escapen of enkele quotes gebruiken. Gebruik de echte apostrof ' (bijv. 's nachts) en geen HTML-entities.
- Lengtes: title max 60 tekens (incl. spaties), description 120 tot 155 tekens. h1 kort. lead 1 tot 2 zinnen. intro-alinea's 60 tot 110 woorden elk, concreet en lokaal (echte wijknamen, straten, pleinen, stations, uitvalswegen vanuit Rotterdam), geen opsommingen van loze kreten. Elke pagina uniek: geen zinnen hergebruiken tussen pagina's.
- Feiten over plaatsen moeten kloppen (wijken, metro/trein, snelwegen). Twijfel je, laat het weg.

## Bestaande gebiedsslugs (voor "nearby")
Rotterdamse gebieden: centrum, noord, kralingen-crooswijk, delfshaven, feijenoord, ijsselmonde, charlois, prins-alexander, hillegersberg-schiebroek, overschie, hoogvliet, hoek-van-holland.
Regio (bestaand): schiedam, vlaardingen, capelle-aan-den-ijssel, spijkenisse, barendrecht, ridderkerk, berkel-en-rodenrijs.
Nieuw in deze ronde (mogen ook in nearby): maassluis, delft, zoetermeer, krimpen-aan-den-ijssel, nieuwerkerk-aan-den-ijssel, rhoon, hellevoetsluis, brielle, rozenburg, dordrecht, zwijndrecht, gouda, pijnacker, bergschenhoek, bleiswijk, hendrik-ido-ambacht, naaldwijk, oud-beijerland, nesselande, ommoord, zevenkamp, kop-van-zuid, blijdorp, pernis, lombardijen.

## Schema voor een gebied (AREAS = [ {...}, ... ])
{
 "slug": "maassluis", "name": "Maassluis", "kind": "stad",   # kind: "stad" | "gemeente" | "dorp" | "wijk"
 "title": "Lachgas Maassluis | 24/7 bezorgd via WhatsApp",   # <= 60 tekens
 "description": "...",                                       # 120-155 tekens, begint met "Lachgas bestellen in <Naam>?"
 "h1": "Lachgas Maassluis",                                  # voor Rotterdamse wijken: "Lachgas <Wijk>" (zonder "Rotterdam")
 "lead": "Snel en discreet bezorgd in Maassluis, besteld via WhatsApp. 24/7 bereikbaar.",
 "intro": ["alinea 1 (ligging, wijken, hoe bestellen)", "alinea 2 (route vanuit Rotterdam, OV, waarom levertijd)", "alinea 3 (situaties, tankkeuze met link /lachgas-tanks/, betalen, 18+, link /veilig-gebruik/)"],
 "wijken": "Kern, Wijk A, Wijk B, ...",                      # 6-10 echte wijken/buurten, komma-gescheiden, zonder punt
 "levertijd": "meestal binnen 25 tot 40 minuten",
 "faq": [["Vraag?", "Antwoord (1-3 zinnen, mag 1 link bevatten)."], ["...", "..."], ["...", "..."]],   # precies 3, lokaal en uniek
 "nearby": ["slug", "slug", "slug"],                         # 3 slugs uit de lijst hierboven, geografisch logisch
 "lat": 51.92, "lon": 4.25,
}
