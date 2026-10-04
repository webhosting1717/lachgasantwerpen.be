# -*- coding: utf-8 -*-
"""Content voor nieuwe subpagina's van lachgasrotterdam.nl.

Toegestane HTML in tekstvelden: strong, em en a (interne paden of drugsinfo.nl / rijksoverheid.nl).
"""

SITE = {"domain": "lachgasrotterdam.nl", "brand": "Lachgas Rotterdam", "city": "Rotterdam", "aanspreek": "je"}

AREAS = [
    {
        "slug": "schiedam", "name": "Schiedam", "kind": "stad",
        "title": "Lachgas Schiedam | 24/7 bezorgd via WhatsApp",
        "description": "Lachgas bestellen in Schiedam? Snel en discreet bezorgd via WhatsApp, van de Lange Haven tot Groenoord en Kethel. 24/7 bereikbaar, alleen voor 18+.",
        "h1": "Lachgas Schiedam",
        "lead": "Snel en discreet bezorgd in Schiedam, besteld via WhatsApp. 24/7 bereikbaar.",
        "intro": [
            """Schiedam grenst direct aan Rotterdam-West en ligt voor onze bezorgers praktisch om de hoek. Wij bezorgen lachgastanks in de hele stad: in de historische binnenstad rond de Lange Haven, de Grote Markt en de Koemarkt, in Nieuwland en Schiedam-Zuid, maar ook in de ruimere wijken Groenoord, Kethel, Spaland en Woudhoek. Je stuurt een bericht via WhatsApp met je adres, de gewenste maat en het tijdstip, wij bevestigen het levermoment en komen langs.""",
            """Vanuit Rotterdam rijden we via de Schiedamseweg door Delfshaven of via de A20 (afslag Schiedam) de stad binnen. Metrolijnen A, B en C stoppen bij Schiedam Centrum, Parkweg, Troelstralaan en Vijfsluizen, dus ook de adressen rond die stations kennen we goed. Omdat de afstand tot Rotterdam-centrum maar een paar kilometer is, verschilt de bezorgtijd in Schiedam nauwelijks van die in de stad zelf.""",
            """Of je nu een verjaardag viert in een bovenwoning aan de Broersvest, een avond met vrienden hebt in Sveaparken of een groter feest organiseert in Kethel: kies de <a href="/lachgas-tanks/">lachgastank</a> die bij je avond past, 2KG, 4KG of 10KG. Je betaalt bij levering, contant of via Tikkie, en we leveren uitsluitend aan personen van 18 jaar en ouder. Lees vooraf onze tips voor <a href="/veilig-gebruik/">veilig gebruik</a>.""",
        ],
        "wijken": "Schiedam Centrum, Lange Haven, Nieuwland, Groenoord, Kethel, Spaland, Woudhoek, Sveaparken, Schiedam-Zuid, Schiedam-West",
        "levertijd": "meestal binnen 20 tot 30 minuten",
        "faq": [
            ["Bezorgen jullie in heel Schiedam of alleen in het centrum?", "In heel Schiedam, van de binnenstad tot Kethel, Spaland en Woudhoek. Stuur je postcode mee in je WhatsApp-bericht, dan bevestigen we direct het levermoment en het totaalbedrag."],
            ["Hoe snel zijn jullie in Schiedam?", "Schiedam ligt direct naast Rotterdam-West, dus meestal binnen 20 tot 30 minuten. Bij grote drukte, bijvoorbeeld in het weekend, kan het iets langer duren; je krijgt vooraf een eerlijke indicatie."],
            ["Kan ik 's nachts bestellen in Schiedam?", """Ja, we zijn 24/7 bereikbaar via WhatsApp, ook 's nachts en in het weekend. Lees meer over <a href="/lachgas-nachtbezorging/">lachgas 's nachts</a>."""],
        ],
        "nearby": ["delfshaven", "vlaardingen", "overschie"],
        "lat": 51.919, "lon": 4.389,
    },
    {
        "slug": "vlaardingen", "name": "Vlaardingen", "kind": "stad",
        "title": "Lachgas Vlaardingen | Snel bezorgd via WhatsApp",
        "description": "Lachgas bestellen in Vlaardingen? Discreet bezorgd via WhatsApp in Centrum, Holy, Westwijk en Ambacht. 24/7 bereikbaar, betalen bij levering, alleen 18+.",
        "h1": "Lachgas Vlaardingen",
        "lead": "Snel en discreet bezorgd in Vlaardingen, besteld via WhatsApp. 24/7 bereikbaar.",
        "intro": [
            """Vlaardingen ligt ten westen van Schiedam aan de Nieuwe Maas en hoort bij ons vaste bezorggebied. We bezorgen lachgastanks in het centrum rond de Westhavenkade en winkelcentrum Liesveld, in de Oostwijk en de Westwijk, in Holy-Noord en Holy-Zuid, in de Babberspolder en Ambacht en in de Indische Buurt. Geen afhaalpunt: je appt je adres, wij bevestigen en komen naar je deur.""",
            """Vanuit Rotterdam nemen we de A20 richting Hoek van Holland en rijden we bij afslag Vlaardingen de stad in, of we komen via de Beneluxtunnel en de A4 als we vanaf Zuid komen. De Hoekse Lijn (metro B) stopt bij Vlaardingen Oost, Vlaardingen Centrum en Vlaardingen West, en ook de adressen rond die stations en langs de Marathonweg kennen we goed. Reken op iets meer reistijd dan in Rotterdam zelf; we geven vooraf een eerlijke indicatie.""",
            """Vlaardingers bestellen bij ons voor een huisfeest in Holy, een verjaardag in de Westwijk of een avond met vrienden bij de Oude Haven. Bekijk de <a href="/lachgas-tanks/">lachgastanks</a> in 2KG, 4KG en 10KG en kies het formaat dat past bij je groep. Verzegeld geleverd, betalen bij levering contant of via Tikkie, en uitsluitend voor 18+. Lees ook onze pagina over <a href="/veilig-gebruik/">veilig gebruik</a>.""",
        ],
        "wijken": "Vlaardingen Centrum, Westhavenkade, Oostwijk, Westwijk, Holy-Noord, Holy-Zuid, Babberspolder, Ambacht, Indische Buurt, Vettenoordsepolder",
        "levertijd": "meestal binnen 25 tot 40 minuten",
        "faq": [
            ["Hoe lang duurt bezorgen in Vlaardingen?", "Meestal binnen 25 tot 40 minuten, afhankelijk van de wijk en de drukte. Holy en de Broekpolder liggen wat verder van de A20 dan het centrum. Je hoort via WhatsApp vooraf hoe laat we er zijn."],
            ["Bezorgen jullie ook in Holy en de Westwijk?", "Ja, we bezorgen in alle wijken van Vlaardingen, inclusief Holy-Noord, Holy-Zuid, de Westwijk en Ambacht. Stuur je postcode mee, dan bevestigen we direct."],
            ["Hoe betaal ik in Vlaardingen?", "Bij aflevering, contant of via Tikkie in overleg. Je hoort het totaalbedrag inclusief bezorging vooraf via WhatsApp, zonder verrassingen achteraf."],
        ],
        "nearby": ["schiedam", "hoek-van-holland", "delfshaven"],
        "lat": 51.912, "lon": 4.342,
    },
    {
        "slug": "capelle-aan-den-ijssel", "name": "Capelle aan den IJssel", "kind": "stad",
        "title": "Lachgas Capelle aan den IJssel | 24/7 via WhatsApp",
        "description": "Lachgas bestellen in Capelle aan den IJssel? Snel en discreet bezorgd via WhatsApp in Schollevaar, Middelwatering, Oostgaarde en Fascinatio. 24/7, 18+.",
        "h1": "Lachgas Capelle aan den IJssel",
        "lead": "Snel en discreet bezorgd in Capelle aan den IJssel, besteld via WhatsApp. 24/7 bereikbaar.",
        "intro": [
            """Capelle aan den IJssel ligt direct tegen Rotterdam Prins Alexander en Kralingen aan en is voor ons gewoon een stukje verder rijden. We bezorgen lachgastanks in Schollevaar, Middelwatering, Oostgaarde, 's-Gravenland, Schenkel, Capelle-West en het nieuwere Fascinatio bij het Rivium. Ook rond winkelcentrum De Koperwiek en langs de Hollandsche IJssel komen we dagelijks. Geen afhaalpunt: je appt je adres, de gewenste maat en het tijdstip, en wij komen naar je deur.""",
            """Vanaf Rotterdam-centrum rijden we via de Abram van Rijckevorselweg of via de A16 en de Capelseweg de gemeente in; vanaf Zuid gaat het via de Van Brienenoordbrug. Metrolijn C stopt bij Capelsebrug, Slotlaan, Schenkel, De Terp en Capelle Centrum, en treinstation Capelle Schollevaar ligt aan de noordkant. Door de korte afstand verschilt de bezorgtijd weinig van die in Rotterdam-Oost; in het weekend kan het iets drukker zijn en krijg je vooraf een eerlijke indicatie.""",
            """Een verjaardag in een rijtjeshuis in Schollevaar, een avondje met vrienden in een appartement in Fascinatio of een groter feest in Oostgaarde: bekijk de <a href="/lachgas-tanks/">lachgastanks</a> in 2KG, 4KG en 10KG en kies wat bij je groep past. Je betaalt bij levering, contant of via Tikkie, en we leveren uitsluitend aan 18+. Bekijk vooraf ook de tips voor <a href="/veilig-gebruik/">veilig gebruik</a>.""",
        ],
        "wijken": "Schollevaar, Middelwatering, Oostgaarde, 's-Gravenland, Schenkel, Capelle-West, Fascinatio, Rivium, De Koperwiek, Capelsebrug",
        "levertijd": "meestal binnen 20 tot 35 minuten",
        "faq": [
            ["Hoe snel bezorgen jullie in Capelle aan den IJssel?", "Meestal binnen 20 tot 35 minuten. Capelle grenst direct aan Prins Alexander en Kralingen, dus de rijtijd vanuit Rotterdam is kort. Bij drukte in het weekend krijg je vooraf een eerlijke indicatie."],
            ["Bezorgen jullie ook in Schollevaar en Fascinatio?", "Ja, in alle wijken van Capelle, van Schollevaar in het noorden tot Fascinatio en het Rivium in het westen. Stuur je postcode via WhatsApp en we bevestigen direct."],
            ["Kan ik bestellen voor een groter feest in Capelle?", """Zeker. Voor een groter feest of evenement is de 4KG of 10KG tank geschikt. Voor de 10KG stemmen we de levering vooraf af via WhatsApp. Lees meer op <a href="/lachgas-feest-evenement/">feest en evenement</a>."""],
        ],
        "nearby": ["prins-alexander", "kralingen-crooswijk", "ijsselmonde"],
        "lat": 51.929, "lon": 4.577,
    },
    {
        "slug": "spijkenisse", "name": "Spijkenisse", "kind": "stad",
        "title": "Lachgas Spijkenisse | Snel bezorgd via WhatsApp",
        "description": "Lachgas bestellen in Spijkenisse? Discreet bezorgd via WhatsApp in Centrum, De Akkers, Waterland, Maaswijk en Sterrenkwartier. 24/7 bereikbaar, alleen 18+.",
        "h1": "Lachgas Spijkenisse",
        "lead": "Snel en discreet bezorgd in Spijkenisse, besteld via WhatsApp. 24/7 bereikbaar.",
        "intro": [
            """Spijkenisse, de grootste kern van de gemeente Nissewaard, ligt op Voorne-Putten aan de overkant van de Oude Maas en hoort bij ons bezorggebied. We bezorgen lachgastanks in het centrum rond het Uitplein en theater De Stoep, in De Akkers, De Hoek, Groenewoud, Maaswijk, Schiekamp, Sterrenkwartier, Vogelenzang, Waterland en Vriesland. Ook het dorp Hekelingen nemen we mee.""",
            """Vanuit Rotterdam rijden we via de A15 en de Hartelbrug of via Hoogvliet en de Spijkenisserbrug het eiland op. Metrolijnen C en D rijden tot Spijkenisse Centrum, Heemraadlaan en eindpunt De Akkers, dus ook die kant van de stad kennen we goed. Spijkenisse ligt wat verder van Rotterdam-centrum dan onze stadswijken; reken op iets meer reistijd, wij geven altijd vooraf een eerlijke indicatie via WhatsApp.""",
            """Of je nu een verjaardag viert in een eengezinswoning in Waterland, een avond met vrienden in Maaswijk of een groter feest in het centrum: kies een <a href="/lachgas-tanks/">lachgastank</a> van 2KG, 4KG of 10KG. Geen afhaalpunt en geen gedoe met vervoer over de brug: wij komen naar je deur. Verzegeld geleverd, betalen bij levering contant of via Tikkie, uitsluitend voor 18+. Lees ook onze tips voor <a href="/veilig-gebruik/">veilig gebruik</a>.""",
        ],
        "wijken": "Spijkenisse Centrum, Uitplein, De Akkers, De Hoek, Groenewoud, Maaswijk, Schiekamp, Sterrenkwartier, Waterland, Hekelingen",
        "levertijd": "meestal binnen 30 tot 45 minuten",
        "faq": [
            ["Hoe lang duurt bezorgen in Spijkenisse?", "Meestal binnen 30 tot 45 minuten. Spijkenisse ligt aan de overkant van de Oude Maas, dus iets verder dan de wijken in Rotterdam. Je hoort vooraf via WhatsApp hoe laat we er zijn."],
            ["Bezorgen jullie ook in De Akkers en Hekelingen?", "Ja, we bezorgen in alle wijken van Spijkenisse, inclusief De Akkers, Waterland en het dorp Hekelingen. Stuur je postcode mee, dan bevestigen we direct of en hoe laat we kunnen komen."],
            ["Kan ik ook 's avonds laat bestellen in Spijkenisse?", """Ja, we zijn 24/7 bereikbaar via WhatsApp, ook 's nachts en in het weekend. Houd 's nachts rekening met de reistijd vanuit Rotterdam. Lees meer op <a href="/lachgas-nachtbezorging/">lachgas 's nachts</a>."""],
        ],
        "nearby": ["hoogvliet", "charlois", "barendrecht"],
        "lat": 51.845, "lon": 4.329,
    },
    {
        "slug": "barendrecht", "name": "Barendrecht", "kind": "stad",
        "title": "Lachgas Barendrecht | 24/7 bezorgd via WhatsApp",
        "description": "Lachgas bestellen in Barendrecht? Snel en discreet bezorgd via WhatsApp in Centrum, Carnisselande, Smitshoek en Vrijenburg. 24/7 bereikbaar, alleen 18+.",
        "h1": "Lachgas Barendrecht",
        "lead": "Snel en discreet bezorgd in Barendrecht, besteld via WhatsApp. 24/7 bereikbaar.",
        "intro": [
            """Barendrecht ligt direct onder Rotterdam-Zuid, ingeklemd tussen IJsselmonde, Charlois en de Oude Maas. We bezorgen lachgastanks in het oude centrum rond de Middenbaan en het Doormanplein, in Molenvliet, Nieuweland, Binnenland en Buitenoord, en in de grote nieuwbouwwijken Carnisselande en Vrijenburg aan de westkant. Ook Smitshoek en Ter Leede horen erbij. Geen afhaalpunt: je appt je adres, de gewenste maat en het tijdstip, en wij komen langs.""",
            """Vanuit Rotterdam-Zuid rijden we via de Vaanweg en het Vaanplein (A15/A29) zo Barendrecht binnen, of via de Kilweg en de Zuidersingel richting Carnisselande. Tramlijn 25 rijdt vanaf Rotterdam-Zuid tot in Carnisselande en treinstation Barendrecht ligt midden in de gemeente. De afstand tot Rotterdam-centrum is beperkt, dus de bezorgtijd ligt dicht bij die van onze stadswijken.""",
            """Barendrechters bestellen bij ons voor een verjaardag in een gezinswoning in Carnisselande, een avond met vrienden in het centrum of een feest in de tuin bij het Kooiwalbos. Bekijk de <a href="/lachgas-tanks/">lachgastanks</a> in 2KG, 4KG en 10KG en kies het formaat dat bij je groep past. Betalen doe je bij levering, contant of via Tikkie, en we leveren uitsluitend aan 18+. Lees ook onze pagina over <a href="/veilig-gebruik/">veilig gebruik</a>.""",
        ],
        "wijken": "Barendrecht Centrum, Middenbaan, Carnisselande, Vrijenburg, Molenvliet, Nieuweland, Binnenland, Buitenoord, Smitshoek, Ter Leede",
        "levertijd": "meestal binnen 25 tot 35 minuten",
        "faq": [
            ["Hoe snel bezorgen jullie in Barendrecht?", "Meestal binnen 25 tot 35 minuten. Barendrecht grenst direct aan IJsselmonde en Charlois, dus vanaf Zuid zijn we er snel. Je krijgt vooraf een eerlijke indicatie via WhatsApp."],
            ["Bezorgen jullie ook in Carnisselande?", "Ja, Carnisselande, Vrijenburg en Smitshoek horen volledig bij ons bezorggebied, net als het centrum en de oudere wijken. Stuur je postcode mee en we bevestigen direct."],
            ["Wat heb ik nodig om in Barendrecht te bestellen?", """Je volledige adres met postcode en huisnummer, de gewenste maat en het tijdstip. Zorg dat je via WhatsApp bereikbaar bent als de bezorger in de buurt is. Bekijk onze <a href="/werkwijze/">werkwijze</a> voor alle stappen."""],
        ],
        "nearby": ["ijsselmonde", "charlois", "ridderkerk"],
        "lat": 51.857, "lon": 4.535,
    },
    {
        "slug": "ridderkerk", "name": "Ridderkerk", "kind": "stad",
        "title": "Lachgas Ridderkerk | Snel bezorgd via WhatsApp",
        "description": "Lachgas bestellen in Ridderkerk? Discreet bezorgd via WhatsApp in Centrum, Bolnes, Slikkerveer, Drievliet en Rijsoord. 24/7 bereikbaar, alleen voor 18+.",
        "h1": "Lachgas Ridderkerk",
        "lead": "Snel en discreet bezorgd in Ridderkerk, besteld via WhatsApp. 24/7 bereikbaar.",
        "intro": [
            """Ridderkerk ligt ten zuidoosten van Rotterdam aan de Nieuwe Maas, direct achter IJsselmonde en de Van Brienenoordbrug. We bezorgen lachgastanks in het centrum rond het Koningsplein en winkelcentrum Ridderhof, in Bolnes en Slikkerveer langs de rivier, in Drievliet en Het Zand, in Ridderkerk-West en Ridderkerk-Oost en in de dorpen Rijsoord en Oostendam. Geen afhaalpunt: je stuurt een WhatsApp-bericht met je adres en de gewenste maat, wij bevestigen en komen langs.""",
            """Vanuit Rotterdam rijden we via de A16 en knooppunt Ridderkerk de gemeente in, of vanaf IJsselmonde via de Rotterdamseweg direct naar Bolnes en Slikkerveer. Omdat Ridderkerk aan de Rotterdamse stadsrand ligt, zijn we er vanaf Zuid meestal snel. Op drukke avonden kan het iets langer duren; je krijgt vooraf een eerlijke indicatie via WhatsApp.""",
            """Een verjaardag in Drievliet, een avond met vrienden in Slikkerveer of een tuinfeest aan de rand van het Waalbos: bekijk de <a href="/lachgas-tanks/">lachgastanks</a> in 2KG, 4KG en 10KG en kies het formaat dat bij je avond past. Verzegeld geleverd, betalen bij levering contant of via Tikkie, en uitsluitend voor personen van 18 jaar en ouder. Lees vooraf onze tips voor <a href="/veilig-gebruik/">veilig gebruik</a>.""",
        ],
        "wijken": "Ridderkerk Centrum, Koningsplein, Bolnes, Slikkerveer, Drievliet, Het Zand, Ridderkerk-West, Ridderkerk-Oost, Rijsoord, Oostendam",
        "levertijd": "meestal binnen 25 tot 40 minuten",
        "faq": [
            ["Hoe lang duurt bezorgen in Ridderkerk?", "Meestal binnen 25 tot 40 minuten. Bolnes en Slikkerveer liggen direct achter IJsselmonde en gaan het snelst; Rijsoord en Oostendam liggen iets verder. Je hoort vooraf via WhatsApp hoe laat we er zijn."],
            ["Bezorgen jullie ook in Rijsoord en Oostendam?", "Ja, ook de dorpen Rijsoord en Oostendam horen bij ons bezorggebied Ridderkerk. Stuur je postcode mee in je bericht, dan bevestigen we direct het levermoment."],
            ["Is er een leeftijdsgrens in Ridderkerk?", "Ja, overal waar we bezorgen leveren we uitsluitend aan personen van 18 jaar en ouder. Bij twijfel kan de bezorger om een identiteitsbewijs vragen."],
        ],
        "nearby": ["ijsselmonde", "barendrecht", "feijenoord"],
        "lat": 51.872, "lon": 4.602,
    },
    {
        "slug": "berkel-en-rodenrijs", "name": "Berkel en Rodenrijs", "kind": "dorp",
        "title": "Lachgas Berkel en Rodenrijs | 24/7 via WhatsApp",
        "description": "Lachgas bestellen in Berkel en Rodenrijs? Snel en discreet bezorgd via WhatsApp in Centrum, Westpolder, Meerpolder en Rodenrijs. 24/7, alleen 18+.",
        "h1": "Lachgas Berkel en Rodenrijs",
        "lead": "Snel en discreet bezorgd in Berkel en Rodenrijs, besteld via WhatsApp. 24/7 bereikbaar.",
        "intro": [
            """Berkel en Rodenrijs is de grootste kern van de gemeente Lansingerland en ligt direct ten noorden van Rotterdam Hillegersberg-Schiebroek. We bezorgen lachgastanks in het centrum rond de Herenstraat, in de nieuwbouwwijken Westpolder en Meerpolder, in Rodenrijs en de Noordpolder en in Berkel-Oost richting Bergschenhoek. Ook de lintbebouwing langs de Rodenrijseweg en de Noordeindseweg nemen we mee. Je appt je adres, de gewenste maat en het tijdstip, wij bevestigen het levermoment en komen langs.""",
            """Vanuit Rotterdam rijden we via de G.K. van Hogendorpweg en de N471 of via de A13 en de N470 bij Rotterdam The Hague Airport de gemeente in. Metrolijn E (RandstadRail) stopt bij Rodenrijs en Berkel Westpolder, dus de adressen rond die stations kennen onze bezorgers goed. Berkel ligt net buiten de stadsgrens; reken op iets meer reistijd dan in Hillegersberg zelf.""",
            """Een verjaardag in een gezinswoning in de Westpolder, een avond met vrienden in Meerpolder of een tuinfeest in Rodenrijs: bekijk de <a href="/lachgas-tanks/">lachgastanks</a> in 2KG, 4KG en 10KG en kies het formaat dat bij je groep past. Je betaalt bij levering, contant of via Tikkie, en we leveren uitsluitend aan 18+. Lees vooraf ook onze pagina over <a href="/veilig-gebruik/">veilig gebruik</a>.""",
        ],
        "wijken": "Berkel Centrum, Herenstraat, Westpolder, Meerpolder, Rodenrijs, Noordpolder, Berkel-Oost, Rodenrijseweg, Noordeindseweg",
        "levertijd": "meestal binnen 25 tot 40 minuten",
        "faq": [
            ["Hoe snel bezorgen jullie in Berkel en Rodenrijs?", "Meestal binnen 25 tot 40 minuten. Berkel ligt direct boven Hillegersberg-Schiebroek, dus vanuit Rotterdam-Noord zijn we er snel. Bij drukte krijg je vooraf een eerlijke indicatie via WhatsApp."],
            ["Bezorgen jullie ook in Bergschenhoek en Bleiswijk?", "Berkel en Rodenrijs is ons vaste gebied in Lansingerland. Woon je in Bergschenhoek of Bleiswijk? Stuur je postcode via WhatsApp, dan laten we direct weten of bezorging mogelijk is."],
            ["Bezorgen jullie in Westpolder en Meerpolder?", "Ja, alle wijken van Berkel en Rodenrijs horen erbij, inclusief de nieuwbouw in Westpolder en Meerpolder en de lintbebouwing in Rodenrijs. Geef je adres door en we bevestigen direct."],
        ],
        "nearby": ["hillegersberg-schiebroek", "overschie", "prins-alexander"],
        "lat": 51.993, "lon": 4.478,
    },
]

HUB = {
    "title": "Lachgas informatie: feiten, veiligheid en regels",
    "description": "Betrouwbare informatie over lachgas: wat het is, de gevolgen voor vitamine B12, veilig bewaren en vervoeren, de regels in Nederland en het verkeer.",
    "h1": "Lachgas informatie",
    "lead": "Feiten over lachgas, zonder marketingpraat. Lees wat N2O is, wat het met je lichaam doet, hoe je een tank veilig bewaart en welke regels in Nederland gelden.",
    "intro": [
        """Lachgas Rotterdam bezorgt lachgastanks aan volwassenen in Rotterdam en omgeving. Maar wie lachgas bestelt, moet ook weten wat het is, wat het met je lichaam doet en welke regels gelden. Op deze pagina bundelen we onze informatieartikelen: feitelijk, zonder marketingpraat en met verwijzingen naar onafhankelijke bronnen als <a href="https://www.drugsinfo.nl">drugsinfo.nl</a> en <a href="https://www.rijksoverheid.nl">rijksoverheid.nl</a>.""",
        """Je leest hier wat distikstofmonoxide (N2O) precies is en waar het vandaan komt, waarom lachgas vitamine B12 onwerkzaam maakt en welke klachten dat kan geven, hoe je een tank veilig bewaart en vervoert, wat er sinds 1 januari 2023 in de Opiumwet staat en waarom lachgas en verkeer nooit samengaan. De praktische basisregels vind je op <a href="/veilig-gebruik/">veilig gebruik</a>; de antwoorden op vragen over bestellen en bezorgen staan in de <a href="/faq/">FAQ</a>.""",
    ],
}

ARTICLES = [
    {
        "slug": "wat-is-lachgas", "label": "Basis",
        "title": "Wat is lachgas (N2O)? Feiten en gebruik",
        "description": "Wat is lachgas precies? Lees over distikstofmonoxide (N2O), de ontdekking in 1772, het gebruik in zorg, voeding en techniek, de werking en de risico's.",
        "h1": "Wat is lachgas?",
        "lead": "Lachgas is de volksnaam voor distikstofmonoxide, een kleurloos gas met een lange geschiedenis in de geneeskunde, de keuken en de techniek. Dit is wat je erover moet weten.",
        "sections": [
            {
                "h2": "Distikstofmonoxide: de chemie in het kort",
                "paragraphs": [
                    """Lachgas is de alledaagse naam voor distikstofmonoxide, chemische formule N2O. Elk molecuul bestaat uit twee stikstofatomen en één zuurstofatoom. Het is een kleurloos gas met een licht zoete geur en smaak. Het is zelf niet brandbaar, maar kan een verbranding wel versterken, omdat het bij hoge temperaturen zuurstof afstaat.""",
                    """In een lachgastank zit het gas onder druk, deels in vloeibare vorm. Zodra de kraan opengaat, zet het gas uit en koelt het sterk af. Daarom is een tank altijd zwaar, koud bij gebruik en nooit bedoeld om rechtstreeks uit te ademen. Meer over het veilig omgaan met tanks lees je op <a href="/veilig-gebruik/">veilig gebruik</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Ontdekt in 1772, beroemd geworden in 1844",
                "paragraphs": [
                    """De Engelse natuurwetenschapper Joseph Priestley maakte distikstofmonoxide voor het eerst in 1772, in dezelfde periode waarin hij ook zuurstof beschreef. Hij noemde het 'nitrous air' en had nog geen idee van de effecten op mensen.""",
                    """Dat veranderde rond 1799, toen de jonge chemicus Humphry Davy het gas op zichzelf en op vrienden uitprobeerde. Hij beschreef de lachbuien en het lichte gevoel dat het opriep en gaf het gas zijn bijnaam: laughing gas, lachgas. Davy vermoedde al dat het pijn kon verlichten, maar het duurde nog decennia voordat de geneeskunde dat oppikte.""",
                    """Op 11 december 1844 liet de Amerikaanse tandarts Horace Wells een kies bij zichzelf trekken terwijl hij lachgas inademde, en voelde daarbij nauwelijks pijn. Dat moment geldt als het begin van lachgas als verdovingsmiddel. Tot op de dag van vandaag gebruiken tandartsen en ziekenhuizen het, in gecontroleerde mengsels met zuurstof.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Waarvoor wordt lachgas gebruikt?",
                "paragraphs": [
                    """Lachgas heeft drie grote, legale toepassingsgebieden. Die drie zijn ook precies de uitzonderingen die de Nederlandse wetgever heeft gemaakt sinds lachgas onder de Opiumwet valt; lees daarover meer in <a href="/lachgas-informatie/is-lachgas-legaal-in-nederland/">is lachgas legaal in Nederland</a>.""",
                ],
                "bullets": [
                    """<strong>Medisch.</strong> Als licht verdovings- en pijnstillend middel bij tandartsen, op verloskamers en op de spoedeisende hulp, altijd gemengd met zuurstof en onder toezicht.""",
                    """<strong>Voeding.</strong> Als drijfgas in slagroomspuiten en spuitbussen met slagroom. Op etiketten herken je het aan het nummer E942. Het lost goed op in vet en geeft slagroom zijn luchtige structuur.""",
                    """<strong>Techniek.</strong> Als oxidator in de autosport om motoren extra vermogen te geven, als drijfgas in de industrie en als procesgas in laboratoria en halfgeleiderfabrieken.""",
                ],
            },
            {
                "h2": "Hoe werkt lachgas op het lichaam?",
                "paragraphs": [
                    """Wie lachgas inademt, merkt binnen enkele seconden effect: een licht, zwevend gevoel, gedempte of vervormde geluiden, giechelen en soms tintelingen. Het effect is kort en verdwijnt meestal binnen één tot enkele minuten, omdat het gas snel via de longen het lichaam weer verlaat.""",
                    """Het gas werkt op meerdere plekken in het zenuwstelsel tegelijk. Het remt bepaalde receptoren die signalen doorgeven, waardoor pijnprikkels minder sterk aankomen, en het maakt stoffen vrij die een kortdurend gevoel van welbehagen geven. Ondertussen krijgt het lichaam even minder zuurstof binnen, wat de duizeligheid verklaart. Dat is ook de reden dat zitten en frisse lucht de basisregels zijn.""",
                    """Minder bekend is dat lachgas een blijvend effect heeft op vitamine B12 in het lichaam, ook als de roes al lang voorbij is. Bij regelmatig gebruik kan dat tot zenuwklachten leiden. Hoe dat werkt lees je in het artikel <a href="/lachgas-informatie/lachgas-en-vitamine-b12/">lachgas en vitamine B12</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Lachgas en het klimaat",
                "paragraphs": [
                    """Distikstofmonoxide is naast koolstofdioxide en methaan een van de belangrijkste broeikasgassen. Per molecuul houdt het over een periode van honderd jaar ongeveer 270 keer zoveel warmte vast als CO2, en het blijft meer dan een eeuw in de atmosfeer. Daarnaast tast het de ozonlaag aan.""",
                    """Het grootste deel van de uitstoot komt overigens niet uit tanks of patronen, maar uit de landbouw: bemesting van akkers en veehouderij zorgen voor het overgrote deel van de wereldwijde N2O-emissies. Toch telt elke onnodig leeggelopen tank mee. Draai de kraan dus altijd goed dicht en lever lege tanks in, zoals beschreven in <a href="/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/">lachgas tank bewaren en vervoeren</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Wat lachgas niet is",
                "paragraphs": [
                    """Rond lachgas bestaan hardnekkige misverstanden. Het is geen onschuldig feestgas zonder risico's, maar ook geen middel dat in één keer verslavend maakt. Het is een stof met een echte farmacologische werking, die in de zorg nuttig is en bij ongecontroleerd gebruik risico's meebrengt.""",
                ],
                "bullets": [
                    """<strong>Het is geen zuurstof.</strong> Lachgas verdringt juist zuurstof. Inademen in een afgesloten ruimte of met een zak over het hoofd is levensgevaarlijk.""",
                    """<strong>Het is geen vervanging voor alcohol.</strong> De combinatie van lachgas met alcohol of andere middelen vergroot de kans op flauwvallen, vallen en ongelukken.""",
                    """<strong>Het is niet geschikt voor minderjarigen.</strong> Wij leveren uitsluitend aan personen van 18 jaar en ouder.""",
                ],
            },
        ],
        "note": """Deze informatie is bedoeld als algemene achtergrond en vervangt geen medisch advies. Heb je gezondheidsklachten na gebruik van lachgas, neem dan contact op met je huisarts; bel bij een noodgeval 112. Onafhankelijke informatie vind je bij <a href="https://www.drugsinfo.nl">drugsinfo.nl</a>.""",
        "related": ["lachgas-en-vitamine-b12", "is-lachgas-legaal-in-nederland", "lachgas-tank-bewaren-en-vervoeren"],
    },
    {
        "slug": "lachgas-en-vitamine-b12", "label": "Gezondheid",
        "title": "Lachgas en vitamine B12: risico's en klachten",
        "description": "Lachgas maakt vitamine B12 onwerkzaam. Lees welke klachten dat geeft, wie extra risico loopt, waarom B12 slikken niet helpt en wanneer je hulp zoekt.",
        "h1": "Lachgas en vitamine B12",
        "lead": "Het bekendste gezondheidsrisico van lachgas heeft niets met de roes zelf te maken, maar met wat er daarna in je lichaam gebeurt: lachgas zet vitamine B12 buiten werking.",
        "sections": [
            {
                "h2": "Wat doet lachgas met vitamine B12?",
                "paragraphs": [
                    """Vitamine B12 bevat een kobaltatoom dat in een bepaalde chemische toestand moet zijn om zijn werk te kunnen doen. Distikstofmonoxide oxideert dat kobalt, waardoor de vitamine onwerkzaam wordt. Je lichaam heeft dan misschien nog wel B12 in het bloed, maar kan het niet meer gebruiken.""",
                    """B12 is onmisbaar voor twee dingen: de aanmaak van myeline, het isolatielaagje rond zenuwbanen, en de aanmaak van rode bloedcellen. Als de werkzame B12 wegvalt, raakt die isolatie beschadigd. Dat gebeurt eerst in het ruggenmerg en in de lange zenuwen naar handen en voeten. Artsen noemen dit een functioneel B12-tekort: de bloedwaarde kan normaal lijken, terwijl het lichaam toch een tekort ervaart.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Welke klachten kun je krijgen?",
                "paragraphs": [
                    """De klachten ontstaan geleidelijk en worden in het begin vaak afgedaan als vermoeidheid of een verkeerde houding. Juist daarom is het belangrijk ze te herkennen.""",
                    """Bij tijdig stoppen en behandelen herstellen veel mensen grotendeels, maar niet altijd volledig. Ziekenhuizen in Nederland zien de laatste jaren jonge mensen met blijvende zenuwschade door intensief lachgasgebruik. Hoe langer de klachten bestaan voordat ze behandeld worden, hoe groter de kans op blijvende schade.""",
                ],
                "bullets": [
                    """<strong>Tintelingen.</strong> Een prikkelend, 'slapend' gevoel in vingers, handen, tenen of voeten, vaak aan beide kanten tegelijk.""",
                    """<strong>Gevoelloosheid.</strong> Een doof gevoel in handen en voeten, waardoor je bijvoorbeeld de grond minder goed voelt bij het lopen.""",
                    """<strong>Spierzwakte.</strong> Minder kracht in armen of benen, dingen laten vallen, moeite met trappen.""",
                    """<strong>Loopproblemen.</strong> Onzeker of wankel lopen, vooral in het donker, omdat de zenuwen die je positie doorgeven niet goed meer werken.""",
                    """<strong>Overige klachten.</strong> Vermoeidheid, concentratieproblemen, geheugenklachten, stemmingswisselingen en in ernstige gevallen problemen met plassen of ontlasting.""",
                ],
            },
            {
                "h2": "Wie loopt extra risico?",
                "paragraphs": [
                    """Het risico hangt vooral af van hoe vaak en hoeveel je gebruikt. Een enkele ballon op een feest is iets anders dan een tank per avond, meerdere keren per week. Maar ook bij minder intensief gebruik lopen sommige groepen meer gevaar.""",
                ],
                "bullets": [
                    """<strong>Frequente gebruikers.</strong> Wie wekelijks of dagelijks gebruikt, of grote hoeveelheden in korte tijd, geeft het lichaam geen kans om de B12-voorraad te herstellen.""",
                    """<strong>Vegetariërs en veganisten.</strong> B12 komt vooral uit dierlijke producten. Wie weinig of geen vlees, vis, eieren of zuivel eet, heeft vaak al een krappe voorraad.""",
                    """<strong>Zwangere vrouwen.</strong> Tijdens de zwangerschap is de behoefte aan B12 groter en kan een tekort ook het ongeboren kind treffen.""",
                    """<strong>Mensen met bepaalde medicijnen of aandoeningen.</strong> Maagzuurremmers, metformine en darmaandoeningen zoals de ziekte van Crohn verminderen de opname van B12 uit voeding.""",
                    """<strong>Ouderen.</strong> Met het ouder worden neemt de opname van B12 uit voeding af.""",
                ],
            },
            {
                "h2": "Helpt het om extra B12 te slikken?",
                "paragraphs": [
                    """Een veelgehoorde gedachte is dat je het risico kunt wegnemen door B12-tabletten te slikken of veel te eten wat rijk is aan B12. Zo werkt het niet. Lachgas maakt ook de B12 die je net hebt ingenomen onwerkzaam. Zolang je blijft gebruiken, blijf je de vitamine uitschakelen, hoeveel je er ook van binnenkrijgt.""",
                    """Extra B12 kan onderdeel zijn van een behandeling nadat je gestopt bent, meestal in de vorm van injecties die een arts voorschrijft. Het is geen vrijbrief om door te gaan en al zeker geen manier om veilig meer te gebruiken.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Wanneer ga je naar de huisarts?",
                "paragraphs": [
                    """Merk je tintelingen, een doof gevoel, minder kracht of een onzekere manier van lopen, en gebruik je lachgas? Maak dan een afspraak met je huisarts en vertel eerlijk hoe vaak en hoeveel je gebruikt. De huisarts kan bloedonderzoek doen naar B12 en aanverwante waarden en zo nodig doorverwijzen naar een neuroloog. Vroeg ingrijpen maakt het verschil tussen herstel en blijvende schade.""",
                    """Bel direct 112 bij acute klachten zoals bewusteloosheid, ernstige verwardheid, hevige benauwdheid, verlammingsverschijnselen of een val met letsel. Twijfel je, maar is het geen noodgeval? Dan kun je ook de huisartsenpost bellen.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Wat kun je zelf doen?",
                "paragraphs": [
                    """De enige manier om het B12-risico echt klein te houden, is weinig en niet vaak gebruiken. Houd je aan de basisregels op onze pagina <a href="/veilig-gebruik/">veilig gebruik</a>: gebruik een ballon, ga zitten, zorg voor frisse lucht en combineer niet met alcohol of andere middelen. Hoor je bij een risicogroep, dan is het verstandig om lachgas helemaal te laten staan.""",
                ],
                "bullets": [
                    """<strong>Houd het incidenteel.</strong> Geef je lichaam weken, niet dagen, om te herstellen.""",
                    """<strong>Let op vroege signalen.</strong> Tintelingen die aanhouden zijn een reden om te stoppen, niet om door te gaan.""",
                    """<strong>Praat erover.</strong> Met vrienden die meegebruiken, en met je huisarts als je twijfelt.""",
                ],
            },
        ],
        "note": """Dit artikel geeft algemene informatie en is geen vervanging voor medisch advies. Heb je klachten, neem dan contact op met je huisarts; bel bij een noodgeval 112. Onafhankelijke informatie over lachgas en gezondheid vind je bij <a href="https://www.drugsinfo.nl">drugsinfo.nl</a> van het Trimbos-instituut.""",
        "related": ["wat-is-lachgas", "lachgas-in-het-verkeer"],
    },
    {
        "slug": "lachgas-tank-bewaren-en-vervoeren", "label": "Praktisch",
        "title": "Lachgas tank bewaren en vervoeren: zo doe je het veilig",
        "description": "Lachgastank veilig bewaren en vervoeren: rechtop, koel en droog, uit de zon, niet in een warme auto, weg van kinderen. En wat doe je met een lege tank?",
        "h1": "Lachgas tank bewaren en vervoeren",
        "lead": "Een lachgastank is een drukhouder. Met een paar simpele gewoontes bewaar en vervoer je hem veilig: thuis, in de auto en als hij leeg is.",
        "sections": [
            {
                "h2": "Waarom een tank aandacht verdient",
                "paragraphs": [
                    """In een lachgastank zit distikstofmonoxide onder hoge druk, deels als vloeistof. Zolang de tank intact is en de kraan dicht zit, gebeurt er niets. Maar druk en temperatuur hangen samen: hoe warmer de tank, hoe hoger de druk binnenin. Daarom draaien bijna alle regels voor bewaren en vervoeren om twee dingen: houd de tank koel en zorg dat hij niet kan vallen of beschadigen.""",
                    """Onze tanks worden verzegeld geleverd. Controleer bij ontvangst of de verzegeling intact is en bewaar de tank daarna op de manier die we hieronder beschrijven. Meer over de formaten lees je op <a href="/lachgas-tanks/">lachgas tanks</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Zo bewaar je een lachgastank thuis",
                "paragraphs": [
                    """Een goed geventileerde ruimte is belangrijk voor het geval er toch iets lekt: lachgas verdringt zuurstof en is zwaarder dan lucht, waardoor het zich onderin een kleine, gesloten ruimte kan ophopen.""",
                ],
                "bullets": [
                    """<strong>Rechtop.</strong> Zet de tank altijd rechtop, zodat de kraan boven zit en de vloeistof onderin blijft. Een liggende tank kan bij openen vloeistof in plaats van gas afgeven, en die is extreem koud.""",
                    """<strong>Vastgezet.</strong> Zorg dat de tank niet kan omvallen: in een hoek, tegen een muur of met een band vastgezet. Een vallende tank kan de kraan beschadigen.""",
                    """<strong>Koel en droog.</strong> Kamertemperatuur of koeler is prima. Niet naast de verwarming, het fornuis, de oven of een andere warmtebron, en niet in een vochtige ruimte waar de tank kan roesten.""",
                    """<strong>Uit de zon.</strong> Ook niet achter een raam. Direct zonlicht kan de tank in de zomer snel opwarmen.""",
                    """<strong>Buiten bereik van kinderen en huisdieren.</strong> Bewaar de tank op een plek waar kinderen er niet bij kunnen en de kraan niet per ongeluk opengedraaid wordt.""",
                    """<strong>Kraan dicht.</strong> Draai na gebruik de kraan altijd goed dicht, ook bij een tank die bijna leeg is. Zo voorkom je dat gas weglekt in een afgesloten ruimte.""",
                ],
            },
            {
                "h2": "Niet in een warme auto",
                "paragraphs": [
                    """De meest gemaakte fout is een tank achterlaten in een geparkeerde auto. Op een zonnige dag loopt de temperatuur in een afgesloten auto snel op tot ver boven de 50 graden, en daarmee stijgt ook de druk in de tank. Dat is onnodig riskant voor de tank, de kraan en de auto zelf. Ook in de winter is een auto geen opslagplaats: trillingen en rondrollen beschadigen de kraan.""",
                    """Haal een tank dus altijd direct uit de auto zodra je thuis bent en laat hem nooit in de kofferbak liggen tot het volgende feest.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Een tank vervoeren",
                "paragraphs": [
                    """Laat je de tank bezorgen, dan hoef je hierover niet na te denken: wij komen naar je deur, in heel Rotterdam en de omliggende gemeenten. Moet je toch zelf een tank verplaatsen, bijvoorbeeld van je huis naar een feestlocatie, houd dan rekening met het volgende.""",
                ],
                "bullets": [
                    """<strong>Nuchter.</strong> Rijd alleen als je niets hebt gebruikt: geen lachgas, geen alcohol, geen andere middelen. Lees waarom in <a href="/lachgas-informatie/lachgas-in-het-verkeer/">lachgas in het verkeer</a>.""",
                    """<strong>Rechtop en vastgezet.</strong> Zet de tank rechtop in de kofferbak of op de vloer en zet hem vast met een spanband of tussen stevige spullen, zodat hij niet kan omvallen of rollen.""",
                    """<strong>Kraan dicht, ventilatie open.</strong> Controleer voor vertrek of de kraan goed dicht zit en zet een raampje op een kier.""",
                    """<strong>Kort en direct.</strong> Vervoer de tank niet langer dan nodig en maak geen tussenstops waarbij de tank in een warme auto achterblijft.""",
                    """<strong>Niet op de fiets of scooter.</strong> Een tank van 2 of 4 kilo plus de stalen houder is zwaar en onhandig; vallen beschadigt de kraan en jezelf.""",
                ],
            },
            {
                "h2": "Wat doe je met een lege tank?",
                "paragraphs": [
                    """Een lege lachgastank is een stalen drukhouder en hoort niet bij het huisvuil, in de glasbak of bij het oud ijzer aan de straat. Ook een tank die leeg voelt, bevat vaak nog restdruk. Lever de tank in bij het milieupark van je gemeente; in Rotterdam zijn dat de milieuparken van de gemeente, in omliggende gemeenten de eigen milieustraat. Vraag daar naar de regels voor gasflessen en drukhouders.""",
                    """Draai voor het inleveren de kraan dicht en vervoer de tank op dezelfde manier als een volle: rechtop, vastgezet en nuchter achter het stuur. Heb je vragen over de tank die je bij ons hebt besteld, stuur ons dan een bericht via WhatsApp.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Samengevat",
                "paragraphs": [
                    """Rechtop, vastgezet, koel, droog, uit de zon, kraan dicht en buiten bereik van kinderen. Niet in een warme auto laten liggen, nuchter en vastgezet vervoeren, en een lege tank naar het milieupark brengen. Wie deze gewoontes aanhoudt, haalt het grootste deel van de risico's uit het bewaren en vervoeren weg. De basisregels voor het gebruik zelf vind je op <a href="/veilig-gebruik/">veilig gebruik</a>.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder, verzegeld en met de verwachting dat je de producten gebruikt volgens de geldende regels. Twijfel je of een tank beschadigd is? Gebruik hem dan niet en neem contact met ons op via WhatsApp.""",
        "related": ["lachgas-in-het-verkeer", "wat-is-lachgas", "is-lachgas-legaal-in-nederland"],
    },
    {
        "slug": "is-lachgas-legaal-in-nederland", "label": "Regels",
        "title": "Is lachgas legaal in Nederland? De regels sinds 2023",
        "description": "Sinds 1 januari 2023 staat lachgas op lijst II van de Opiumwet. Lees wat dat betekent, welke uitzonderingen gelden en wat Rotterdam extra regelt in de APV.",
        "h1": "Is lachgas legaal in Nederland?",
        "lead": "De regels rond lachgas zijn de laatste jaren flink veranderd. Dit artikel zet op een rij wat er sinds 1 januari 2023 geldt en wat dat betekent voor jou als volwassene in Rotterdam.",
        "sections": [
            {
                "h2": "Lachgas op lijst II van de Opiumwet",
                "paragraphs": [
                    """Sinds 1 januari 2023 staat distikstofmonoxide op lijst II van de Opiumwet. Op die lijst staan middelen die de wetgever als softdrugs aanmerkt, zoals ook cannabis. Het gevolg is dat het bezitten, verkopen, vervoeren, produceren en invoeren van lachgas voor recreatief gebruik in principe verboden is.""",
                    """Daarmee kwam een einde aan de periode waarin lachgas via de Warenwet vrij verkrijgbaar was en in veel steden op straat en in winkels werd verkocht. De regering koos voor het landelijke verbod vanwege de gezondheidsrisico's, met name zenuwschade door een tekort aan vitamine B12, en vanwege het aantal verkeersongevallen waarbij lachgas een rol speelde.""",
                ],
                "bullets": [],
            },
            {
                "h2": "De uitzonderingen: medisch, technisch en voeding",
                "paragraphs": [
                    """Lachgas is niet volledig verboden. De wet maakt een uitzondering voor de toepassingen waarvoor het gas al tientallen jaren wordt gebruikt. Het gaat om drie categorieën.""",
                    """Voor deze toepassingen geldt een vrijstelling. De wet legt daarbij de verantwoordelijkheid bij degene die lachgas bezit of verhandelt: die moet aannemelijk kunnen maken dat het om een van deze doeleinden gaat.""",
                ],
                "bullets": [
                    """<strong>Medische toepassingen.</strong> Lachgas als verdovings- en pijnstillend middel bij tandartsen, in ziekenhuizen en bij ambulancediensten, altijd in gecontroleerde mengsels met zuurstof.""",
                    """<strong>Technische toepassingen.</strong> Gebruik in de industrie, in laboratoria en bijvoorbeeld in de autosport, waar lachgas als oxidator dient.""",
                    """<strong>Voedingstoepassingen.</strong> Lachgas als drijfgas voor slagroom en andere voedingsmiddelen, herkenbaar aan het E-nummer E942, zoals het in de horeca en in professionele keukens wordt gebruikt.""",
                ],
            },
            {
                "h2": "Wat regelt de gemeente Rotterdam extra?",
                "paragraphs": [
                    """Naast de landelijke wet hebben veel gemeenten eigen regels in hun Algemene Plaatselijke Verordening (APV). Rotterdam was een van de eerste steden die het gebruik van lachgas in de openbare ruimte aanpakte. In de APV van Rotterdam is het verboden om op of aan de openbare weg lachgas te gebruiken, voorbereidingen daartoe te treffen of lachgas bij je te hebben met het kennelijke doel het daar te gebruiken. Handhavers en politie kunnen hierop boetes uitschrijven.""",
                    """Concreet betekent dit dat je in Rotterdam niet op straat, in parken, op pleinen of in een geparkeerde auto lachgas hoort te gebruiken. Ook omliggende gemeenten zoals Schiedam, Vlaardingen en Capelle aan den IJssel hebben vergelijkbare bepalingen. Controleer de actuele regels van je eigen gemeente.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Lachgas en het verkeer",
                "paragraphs": [
                    """Los van de Opiumwet en de APV geldt de Wegenverkeerswet. Artikel 8 verbiedt het besturen van een voertuig onder invloed van een stof waarvan je weet of redelijkerwijs moet weten dat die je rijvaardigheid vermindert. Lachgas valt daar nadrukkelijk onder, en dat geldt ook voor fietsers en scooterrijders. Lees meer in ons artikel over <a href="/lachgas-informatie/lachgas-in-het-verkeer/">lachgas in het verkeer</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Leeftijd: uitsluitend 18+",
                "paragraphs": [
                    """Al vóór het landelijke verbod gold voor lachgas een leeftijdsgrens van 18 jaar, en die staat niet ter discussie. Lachgas Rotterdam verkoopt en bezorgt uitsluitend aan personen van 18 jaar en ouder. Bij twijfel vraagt onze bezorger om een geldig identiteitsbewijs. Zonder legitimatie wordt er niet geleverd.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Hoe gaat Lachgas Rotterdam hiermee om?",
                "paragraphs": [
                    """Wij leveren in lijn met de geldende regels en alleen aan volwassenen. Onze tanks worden verzegeld geleverd en we verwachten van onze klanten dat zij de producten gebruiken in overeenstemming met de wet- en regelgeving en de doeleinden waarvoor ze bestemd zijn. Je bent zelf verantwoordelijk voor wat je bestelt en hoe je het gebruikt.""",
                    """Dit artikel is bedoeld als algemene informatie, niet als juridisch advies. Wetten en gemeentelijke verordeningen veranderen, en de precieze toepassing in jouw situatie kan afhangen van omstandigheden die wij niet kennen. Raadpleeg voor de actuele landelijke regels <a href="https://www.rijksoverheid.nl">rijksoverheid.nl</a> en voor lokale regels de website van je gemeente. Heb je een concrete juridische vraag, leg die dan voor aan een jurist.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Dit artikel is geen juridisch advies en kan verouderd raken. De actuele wettekst en toelichting vind je op <a href="https://www.rijksoverheid.nl">rijksoverheid.nl</a>. Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder en in lijn met de geldende regels.""",
        "related": ["lachgas-in-het-verkeer", "wat-is-lachgas", "lachgas-tank-bewaren-en-vervoeren"],
    },
    {
        "slug": "lachgas-in-het-verkeer", "label": "Verkeer",
        "title": "Lachgas in het verkeer: regels, risico's en boetes",
        "description": "Lachgas en autorijden, fietsen of scooterrijden gaan niet samen. Lees wat de Wegenverkeerswet zegt, welke risico's je loopt en waarom bezorgen slimmer is.",
        "h1": "Lachgas in het verkeer",
        "lead": "Lachgas achter het stuur is een van de belangrijkste redenen waarom de regels zijn aangescherpt. Dit is wat de wet zegt en waarom je nooit rijdt na gebruik, ook niet op de fiets.",
        "sections": [
            {
                "h2": "Wat zegt de Wegenverkeerswet?",
                "paragraphs": [
                    """Artikel 8 van de Wegenverkeerswet 1994 verbiedt het besturen van een voertuig terwijl je onder zodanige invloed van een stof bent dat je niet meer tot behoorlijk besturen in staat bent. Het artikel noemt alcohol en een lijst van drugs met concrete grenswaarden, maar bevat ook een algemene bepaling voor elke andere stof waarvan je weet of redelijkerwijs moet weten dat die je rijvaardigheid kan verminderen. Lachgas valt onder die algemene bepaling.""",
                    """Dat betekent dat de politie je kan vervolgen voor rijden onder invloed van lachgas, ook zonder dat er een vaste grenswaarde bestaat. Omdat lachgas snel uit het lichaam verdwijnt, baseert de politie zich vaak op waarnemingen: hoe je rijgedrag was, hoe je reageerde bij de controle, ballonnen en tanks in de auto, en eventueel bloedonderzoek. Veroordelingen voor rijden onder invloed van lachgas komen in Nederland regelmatig voor.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Ook op de fiets en de scooter",
                "paragraphs": [
                    """Veel mensen denken dat de regels alleen voor auto's gelden. Dat is onjuist. Artikel 8 geldt voor alle voertuigen, dus ook voor fietsen, e-bikes, scooters, brommers en snorfietsen. Een fietser die onder invloed van lachgas rijdt, is net zo strafbaar als een automobilist, en loopt daarnaast een groot risico op een val of botsing zonder enige bescherming.""",
                    """Op een scooter of brommer komt daar nog bij dat je rijbewijs op het spel staat. Ook een fietser kan een rijontzegging krijgen als de rechter dat passend vindt.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Waarom lachgas en rijden niet samengaan",
                "paragraphs": [
                    """Het effect van lachgas is kort, en juist dat maakt het verraderlijk. Mensen schatten in dat ze na een minuut weer normaal zijn, terwijl het lichaam nog bezig is te herstellen. De risico's zijn concreet.""",
                    """Daarnaast is lachgas gebruiken in een geparkeerde of rijdende auto in Rotterdam en veel omliggende gemeenten ook verboden op grond van de APV, los van de Wegenverkeerswet.""",
                ],
                "bullets": [
                    """<strong>Verminderd reactievermogen.</strong> Je reageert later op remlichten, overstekende voetgangers en onverwachte situaties.""",
                    """<strong>Duizeligheid en flauwvallen.</strong> Een korte black-out achter het stuur is genoeg voor een ernstig ongeluk.""",
                    """<strong>Verstoorde waarneming.</strong> Geluiden klinken vervormd en afstanden zijn moeilijker in te schatten.""",
                    """<strong>Tintelingen en krachtverlies.</strong> Bij frequent gebruik kan zenuwschade door een B12-tekort het gevoel in handen en voeten aantasten, en daarmee het bedienen van pedalen en stuur. Lees meer in <a href="/lachgas-informatie/lachgas-en-vitamine-b12/">lachgas en vitamine B12</a>.""",
                    """<strong>Afleiding.</strong> Een ballon vullen achter het stuur betekent twee handen van het stuur en je ogen van de weg.""",
                ],
            },
            {
                "h2": "Wat zijn de gevolgen als je wordt gepakt?",
                "paragraphs": [
                    """Rijden onder invloed is een misdrijf. Afhankelijk van de situatie kan de officier van justitie een geldboete eisen, een rijontzegging, een taakstraf en bij ongevallen met letsel een gevangenisstraf. Daarnaast kan het CBR een onderzoek naar je rijgeschiktheid starten, met een educatieve maatregel of het ongeldig verklaren van je rijbewijs als mogelijk gevolg. Veroorzaak je een ongeluk, dan kan je verzekeraar de schade op jou verhalen.""",
                    """Tel daarbij op dat lachgas sinds 2023 op lijst II van de Opiumwet staat: tanks of ballonnen in de auto voor recreatief gebruik zijn op zichzelf al een overtreding. Meer daarover lees je in <a href="/lachgas-informatie/is-lachgas-legaal-in-nederland/">is lachgas legaal in Nederland</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Laat het bezorgen, rijd zelf niet",
                "paragraphs": [
                    """De simpelste manier om al deze risico's te vermijden, is zelf niet de weg op te gaan. Lachgas Rotterdam bezorgt aan de deur in heel Rotterdam en in omliggende plaatsen als Schiedam, Vlaardingen, Capelle aan den IJssel, Spijkenisse, Barendrecht, Ridderkerk en Berkel en Rodenrijs. Je stuurt een bericht via WhatsApp, wij bevestigen het levermoment en komen langs, in de stad meestal binnen 20 tot 30 minuten. Bekijk alle <a href="/bezorggebieden/">bezorggebieden</a>.""",
                    """Zo hoef je geen tank in de auto te leggen, geen parkeerplek te zoeken bij een afhaalpunt en vooral: niet te rijden na gebruik. Spreek met je gezelschap van tevoren af wie nuchter blijft als er toch iemand naar huis moet rijden, of regel een taxi of het openbaar vervoer.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Praktische afspraken voor een avond",
                "paragraphs": [
                    """Een paar afspraken vooraf voorkomen dat iemand aan het eind van de avond toch in de auto of op de fiets stapt.""",
                ],
                "bullets": [
                    """<strong>Gebruik alleen op de plek waar je blijft.</strong> Thuis of op de feestlocatie, nooit onderweg en nooit in een auto.""",
                    """<strong>Maak een BOB-afspraak.</strong> Wie rijdt, gebruikt niets: geen lachgas, geen alcohol.""",
                    """<strong>Ga pas rijden als je volledig hersteld bent.</strong> Twijfel je? Dan rijd je niet. Wacht, of regel ander vervoer.""",
                    """<strong>Laat de tank thuis.</strong> Vervoer je toch een tank, doe dat nuchter, rechtop en vastgezet. Lees <a href="/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/">lachgas tank bewaren en vervoeren</a>.""",
                ],
            },
        ],
        "note": """Dit artikel is algemene informatie, geen juridisch advies. De actuele wetgeving vind je op <a href="https://www.rijksoverheid.nl">rijksoverheid.nl</a>. Bij een ongeval of acute klachten bel je 112. Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder.""",
        "related": ["is-lachgas-legaal-in-nederland", "lachgas-en-vitamine-b12", "lachgas-tank-bewaren-en-vervoeren"],
    },
]
