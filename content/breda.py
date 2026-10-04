# -*- coding: utf-8 -*-
"""Content voor nieuwe subpagina's van lachgasbreda.nl.

Toegestane HTML in tekstvelden: <strong>, <em> en <a href="...">.
Bestellen gaat uitsluitend via WhatsApp. Geen prijzen, geen belnummer.
"""

SITE = {"domain": "lachgasbreda.nl", "brand": "Lachgas Breda", "city": "Breda", "aanspreek": "je"}

# ---------------------------------------------------------------------------
# Bezorggebieden
# ---------------------------------------------------------------------------

AREAS = [
    {
        "slug": "teteringen",
        "name": "Teteringen",
        "kind": "dorp",
        "title": "Lachgas Teteringen | Snel bezorgd via WhatsApp",
        "description": "Lachgas bestellen in Teteringen? Via WhatsApp snel en discreet bezorgd rond de Hoolstraat, het Willem-Alexanderplein en de Bouverijen. Alleen 18+.",
        "h1": "Lachgas Teteringen",
        "lead": "Snel en discreet bezorgd in Teteringen, besteld via WhatsApp.",
        "intro": [
            "Teteringen ligt tegen de noordoostkant van Breda, net voorbij Brabantpark en Heusdenhout. Vanuit het centrum rijden onze bezorgers via de Teteringsedijk of de Oosterhoutseweg in een paar minuten het dorp in. We komen overal: van de Hoolstraat en het Willem-Alexanderplein in het hart van het dorp tot de nieuwbouw in de Bouverijen en Meulenspie, en de rustige straten richting de Zwarte Dijk en de Teteringse Heide.",
            "Het dorp heeft een eigen karakter: veel gezinnen, een actief verenigingsleven en een centrum dat vanuit elke straat op loopafstand ligt. Juist daarom is een bezorgservice hier handig. Je hoeft niet naar de stad voor een lachgastank of een doosje slagroompatronen; je stuurt een WhatsApp-bericht met wat je nodig hebt en je adres, en wij komen langs. Of het nu gaat om een verjaardag in een tuin aan de Kerkstraat, een borrel na een wandeling door de Lage Vuchtpolder of een avond met vrienden in een van de nieuwbouwwoningen.",
            "Alle tanks worden verzegeld geleverd en we verkopen uitsluitend aan volwassenen van 18 jaar en ouder. Betalen doe je bij aflevering, contant of via Tikkie. Omdat Teteringen zo dicht bij Breda ligt, hoort het bij onze snelste bezorggebieden. Twijfel je over het formaat voor jouw groep? Bekijk <a href=\"/lachgas-informatie/welke-lachgastank-heb-ik-nodig/\">onze keuzehulp</a> of vraag het ons via WhatsApp.",
        ],
        "wijken": "Hoolstraat, Willem-Alexanderplein, Kerkstraat, Bouverijen, Meulenspie, Zwarte Dijk, Teteringse Heide, Lage Vuchtpolder, Oosterhoutseweg",
        "levertijd": "meestal binnen 20 tot 30 minuten",
        "faq": [
            [
                "Bezorgen jullie ook in de nieuwbouwwijken Bouverijen en Meulenspie?",
                "Ja. De Bouverijen en Meulenspie horen gewoon bij Teteringen en liggen op onze route vanaf Breda. Zet in je bericht wel duidelijk je straat en huisnummer, want in nieuwbouwwijken staan niet alle adressen al goed in de navigatie.",
            ],
            [
                "Hoe lang duurt bezorgen in Teteringen vanaf Breda?",
                "Teteringen ligt op een paar minuten van Brabantpark, dus we zijn er meestal binnen 20 tot 30 minuten. Op een drukke vrijdag- of zaterdagavond kan het iets langer duren; je krijgt bij je bestelling altijd een indicatie via WhatsApp.",
            ],
            [
                "Kan ik in Teteringen ook alleen een cracker of slagroompatronen bestellen?",
                "Zeker. Je hoeft geen tank te bestellen. <a href=\"/product/lachgas-cracker/\">Lachgas crackers</a> en <a href=\"/product/slagroompatronen/\">slagroompatronen</a> per doosje bezorgen we net zo goed in Teteringen. Geef in je bericht aan wat je wilt en wij bevestigen.",
            ],
        ],
        "nearby": ["brabantpark", "oosterhout", "bavel"],
        "lat": 51.6078,
        "lon": 4.8257,
    },
    {
        "slug": "bavel",
        "name": "Bavel",
        "kind": "dorp",
        "title": "Lachgas Bavel | Discreet bezorgd via WhatsApp",
        "description": "Lachgas bestellen in Bavel? Snel en discreet bezorgd via WhatsApp, van de Brigidastraat tot Nieuw Wolfslaar en Lijndonk-Tervoort. Alleen 18+.",
        "h1": "Lachgas Bavel",
        "lead": "Snel en discreet bezorgd in Bavel, besteld via WhatsApp.",
        "intro": [
            "Bavel is het kerkdorp aan de zuidoostkant van Breda, ingeklemd tussen de A27, de A58 en het buitengebied richting Gilze. Vanaf het centrum van Breda zijn onze bezorgers er via de Bavelselaan of de Bavelseweg binnen een kwartier. We bezorgen in het hele dorp: rond de Brigidastraat en de Sint-Brigidakerk, in de Kerkstraat, langs de Gilzeweg en de Dorstseweg, en in de nieuwbouw van Nieuw Wolfslaar, Lijndonk en Tervoort.",
            "Bavel is een echt gezinsdorp, maar met Breepark en de Bavelse Berg om de hoek is er ook regelmatig wat te vieren. Een tuinfeest aan de Roosbergseweg, een verjaardag in een nieuwbouwwoning of een avond napraten met vrienden na een evenement in de buurt: je stuurt ons een WhatsApp-bericht met je bestelling en je adres, en wij komen langs. Geen afhaalpunt, geen omweg naar de stad.",
            "Je kiest uit een Lachgastank 2KG, 4KG of op aanvraag 10KG, aangevuld met lachgas crackers en slagroompatronen. Alles wordt verzegeld geleverd, uitsluitend aan personen van 18 jaar en ouder, en je betaalt bij aflevering contant of via Tikkie. Twijfel je over het formaat? Lees onze <a href=\"/lachgas-informatie/welke-lachgastank-heb-ik-nodig/\">keuzehulp</a> of vraag het ons direct via WhatsApp.",
        ],
        "wijken": "Brigidastraat, Kerkstraat, Gilzeweg, Dorstseweg, Roosbergseweg, Nieuw Wolfslaar, Lijndonk, Tervoort, Bavelse Berg",
        "levertijd": "meestal binnen 20 tot 30 minuten",
        "faq": [
            [
                "Ik ben bij een evenement bij Breepark, kunnen jullie daar bezorgen?",
                "Wij bezorgen op een woonadres of een vooraf afgesproken adres in Bavel en omgeving, niet op het terrein van een evenement. Daar gelden de regels van de organisatie en de gemeente. Ga je na afloop bij iemand thuis verder, stuur dan dat adres door.",
            ],
            [
                "Hoe snel zijn jullie in Bavel?",
                "Vanaf het centrum van Breda is Bavel een korte rit over de Bavelselaan, dus meestal zijn we er binnen 20 tot 30 minuten. In het weekend kan het iets drukker zijn; je ontvangt bij je bestelling een indicatie via WhatsApp.",
            ],
            [
                "Bezorgen jullie ook in Nieuw Wolfslaar en Lijndonk-Tervoort?",
                "Ja, ook in de nieuwere delen van Bavel. Vermeld in je bericht je straat, huisnummer en eventueel een herkenningspunt, dan vindt onze bezorger je adres zonder zoeken.",
            ],
        ],
        "nearby": ["teteringen", "ulvenhout", "ginneken"],
        "lat": 51.5681,
        "lon": 4.8347,
    },
    {
        "slug": "ulvenhout",
        "name": "Ulvenhout",
        "kind": "dorp",
        "title": "Lachgas Ulvenhout | Snel bezorgd via WhatsApp",
        "description": "Lachgas bestellen in Ulvenhout? Discreet bezorgd via WhatsApp in de Dorpstraat, aan de Pennendijk en rond het Mastbos en het Markdal. Uitsluitend 18+.",
        "h1": "Lachgas Ulvenhout",
        "lead": "Snel en discreet bezorgd in Ulvenhout, besteld via WhatsApp.",
        "intro": [
            "Ulvenhout ligt direct ten zuiden van het Ginneken, tussen het Mastbos, het Ulvenhoutse Bos en het Markdal. Onze bezorgers rijden vanuit Breda via de Ginnekenweg en de Ulvenhoutselaan in zo'n tien minuten het dorp binnen. We komen in de hele kern: de Dorpstraat met de Sint-Laurentiuskerk, de Pennendijk, de Molenstraat, de Slotlaan en de lanen rond Landgoed Anneville, tot aan de Chaamseweg en de Strijbeekseweg richting het buitengebied.",
            "Ulvenhout is groen, rustig en geliefd bij gezinnen en bij mensen die net buiten de stad willen wonen. Een bezorgservice past daar goed bij: je hoeft niet richting Breda te rijden voor een tank, een cracker of een doosje slagroompatronen. Stuur ons een WhatsApp-bericht met wat je wilt bestellen en je adres, en wij komen langs. Handig voor een verjaardag in de tuin, een avond met vrienden na een wandeling door het Mastbos of een gezellig samenzijn in de Dorpstraat.",
            "We leveren verzegelde tanks in 2KG en 4KG, en in overleg de 10KG voor grotere gelegenheden. Verkoop is uitsluitend aan 18+, en je betaalt bij aflevering contant of via Tikkie. Gebruik lachgas verstandig: lees vooraf onze pagina over <a href=\"/lachgas-informatie/veilig-gebruik/\">veilig gebruik</a>, zeker als er later op de avond nog iemand naar huis moet.",
        ],
        "wijken": "Dorpstraat, Pennendijk, Molenstraat, Slotlaan, Annevillelaan, Chaamseweg, Strijbeekseweg, Ulvenhoutse Bos, Markdal",
        "levertijd": "meestal binnen 20 tot 30 minuten",
        "faq": [
            [
                "Bezorgen jullie ook in het buitengebied richting Strijbeek en Chaam?",
                "In Ulvenhout zelf en de straten direct daaromheen bezorgen we standaard. Woon je verder weg langs de Chaamseweg of de Strijbeekseweg, stuur dan even je adres via WhatsApp. Dan laten we meteen weten of en hoe snel we kunnen komen.",
            ],
            [
                "Hoe snel zijn jullie in Ulvenhout?",
                "Ulvenhout ligt pal achter het Ginneken, dus meestal zijn we er binnen 20 tot 30 minuten. Bij je bestelling krijg je direct een realistische indicatie, afhankelijk van het moment en de drukte.",
            ],
            [
                "Kan ik ook later op de avond nog bestellen in Ulvenhout?",
                "Ja, we zijn 24/7 bereikbaar via WhatsApp en bezorgen ook 's avonds en 's nachts in Ulvenhout. Lees meer op onze pagina over <a href=\"/lachgas-nachtbezorging/\">bestellen 's avonds en 's nachts</a>.",
            ],
        ],
        "nearby": ["ginneken", "bavel", "breda-centrum"],
        "lat": 51.5570,
        "lon": 4.7950,
    },
    {
        "slug": "rijen",
        "name": "Rijen",
        "kind": "dorp",
        "title": "Lachgas Rijen | Snel bezorgd via WhatsApp",
        "description": "Lachgas bestellen in Rijen? Bezorgd via WhatsApp rond het station, de Hoofdstraat, Vijf Eiken en Vliegende Vennen. Tanks, crackers en patronen. 18+.",
        "h1": "Lachgas Rijen",
        "lead": "Snel en discreet bezorgd in Rijen, besteld via WhatsApp.",
        "intro": [
            "Rijen ligt zo'n twaalf kilometer ten oosten van Breda, precies tussen Breda en Tilburg aan de spoorlijn en de Rijksweg (N282). Onze bezorgers rijden via Dorst of over de A27 en de A58 in ongeveer een kwartier naar het dorp. We bezorgen in heel Rijen: rond het station en de Stationsstraat, in het centrum met de Hoofdstraat, het Wilhelminaplein en het Raadhuisplein, en in de woonwijken Vijf Eiken, Vliegende Vennen en Rijen-Zuid.",
            "Rijen is een dorp van ruim twintigduizend inwoners met een eigen centrum en veel forenzen die in Breda of Tilburg werken of studeren. Een avond met vrienden, een verjaardag in de tuin of een feestje in een huis vlak bij het station: je stuurt een WhatsApp-bericht met je bestelling en je adres, en wij komen langs. Zo hoef je niet naar de stad voor een lachgastank, een cracker of een doosje slagroompatronen.",
            "Omdat Rijen iets verder van Breda ligt, rekenen we hier op 30 tot 40 minuten. Bij je bestelling krijg je een indicatie via WhatsApp. Alle tanks worden verzegeld geleverd, uitsluitend aan 18+, en je betaalt bij aflevering contant of via Tikkie. Lees voordat je begint onze tips over <a href=\"/lachgas-informatie/veilig-gebruik/\">veilig gebruik</a>.",
        ],
        "wijken": "Stationsstraat, Hoofdstraat, Wilhelminaplein, Raadhuisplein, Vijf Eiken, Vliegende Vennen, Rijen-Zuid, Rijksweg, Boswachterij Dorst",
        "levertijd": "meestal binnen 30 tot 40 minuten",
        "faq": [
            [
                "Bezorgen jullie ook in Gilze, Molenschot en Hulten?",
                "Rijen is ons vaste bezorgpunt in de gemeente Gilze en Rijen. Voor Gilze, Molenschot en Hulten kijken we per bestelling of het past; stuur je adres via WhatsApp en je hoort direct of we kunnen komen en hoe lang het duurt.",
            ],
            [
                "Hoe lang duurt bezorgen in Rijen?",
                "Reken op 30 tot 40 minuten vanaf het moment dat we je bestelling bevestigen. Rijen ligt een stuk verder dan de Bredase wijken, en op drukke avonden kan het iets uitlopen. Je krijgt altijd een indicatie vooraf.",
            ],
            [
                "Ik heb maar een paar ballonnen nodig, moet ik dan een hele tank bestellen?",
                "Nee. Voor een klein gezelschap is een <a href=\"/product/lachgas-cracker/\">lachgas cracker</a> met losse patronen een logischer keuze dan een tank. Heb je al een slagroomspuit in huis, dan kun je ook alleen <a href=\"/product/slagroompatronen/\">slagroompatronen</a> bestellen.",
            ],
        ],
        "nearby": ["bavel", "tilburg", "dongen"],
        "lat": 51.5900,
        "lon": 4.9200,
    },
    {
        "slug": "dongen",
        "name": "Dongen",
        "kind": "dorp",
        "title": "Lachgas Dongen | Discreet bezorgd via WhatsApp",
        "description": "Lachgas bestellen in Dongen? Via WhatsApp bezorgd rond de Hoge Ham, het Looiersplein, de Beljaart en Dongen-Vaart. Verzegelde tanks, uitsluitend voor 18+.",
        "h1": "Lachgas Dongen",
        "lead": "Snel en discreet bezorgd in Dongen, besteld via WhatsApp.",
        "intro": [
            "Dongen ligt ongeveer twintig kilometer ten noordoosten van Breda, voorbij Oosterhout, aan het Wilhelminakanaal. Onze bezorgers rijden via de A27 en de Westerlaan of via de Heistraat (N629) in zo'n 25 minuten naar het dorp. We bezorgen in heel Dongen: in het centrum rond de Hoge Ham en het Looiersplein, in Oud-Dongen bij de Laurentiuskerk, in de wijken West 1 en West 2 en de Biezen, in de nieuwbouw op de Beljaart en in de kernen Dongen-Vaart en Klein-Dongen.",
            "Dongen heeft een levendig centrum, een stevige carnavalstraditie en veel gezinnen in de buitenwijken. Voor een verjaardag, een feestje thuis of een avond met vrienden stuur je ons een WhatsApp-bericht met je bestelling en je adres. Wij bevestigen en komen langs, zodat je niet naar Breda, Oosterhout of Tilburg hoeft te rijden voor een lachgastank, een cracker of slagroompatronen.",
            "Omdat Dongen wat verder ligt, houden we hier rekening met 35 tot 45 minuten. Je krijgt direct een indicatie via WhatsApp. Tanks leveren we verzegeld in 2KG en 4KG; de 10KG regelen we in overleg. Verkoop uitsluitend aan 18+, betalen bij aflevering contant of via Tikkie. Gebruik met verstand en lees onze pagina over <a href=\"/lachgas-informatie/veilig-gebruik/\">veilig gebruik</a>.",
        ],
        "wijken": "Hoge Ham, Looiersplein, Oud-Dongen, West 1, West 2, Biezen, Beljaart, Dongen-Vaart, Klein-Dongen, Wilhelminakanaal",
        "levertijd": "meestal binnen 35 tot 45 minuten",
        "faq": [
            [
                "Bezorgen jullie ook in 's Gravenmoer?",
                "Ja. 's Gravenmoer hoort bij de gemeente Dongen en ligt een paar minuten ten noorden van het centrum. Houd rekening met iets meer reistijd dan in Dongen zelf; je krijgt bij je bestelling een indicatie.",
            ],
            [
                "Hoe lang duurt bezorgen in Dongen?",
                "Reken op 35 tot 45 minuten. Dongen ligt achter Oosterhout, dus het is een van onze verder gelegen bezorggebieden. Bestel je voor een feest, doe dat dan liefst een uur van tevoren zodat je zeker op tijd geholpen bent.",
            ],
            [
                "Kunnen jullie tijdens carnaval in Dongen bezorgen?",
                "Ja, ook tijdens de carnavalsdagen bezorgen we in Dongen, maar het is dan drukker en sommige straten in het centrum zijn afgesloten. Geef een adres buiten de afsluitingen door en bestel op tijd. En gebruik verantwoord: niet combineren met alcohol en daarna niet rijden.",
            ],
        ],
        "nearby": ["oosterhout", "rijen", "tilburg"],
        "lat": 51.6260,
        "lon": 4.9390,
    },
    {
        "slug": "zundert",
        "name": "Zundert",
        "kind": "dorp",
        "title": "Lachgas Zundert | Snel bezorgd via WhatsApp",
        "description": "Lachgas bestellen in Zundert, Rijsbergen of Wernhout? Discreet bezorgd via WhatsApp rond de Markt, de Molenstraat en de Randweg. Alleen 18+.",
        "h1": "Lachgas Zundert",
        "lead": "Snel en discreet bezorgd in Zundert, besteld via WhatsApp.",
        "intro": [
            "Zundert ligt ruim vijftien kilometer ten zuidwesten van Breda, vlak bij de Belgische grens. Onze bezorgers rijden via de A16 en de Bredaseweg, of binnendoor via Rijsbergen over de N263, in ongeveer twintig minuten naar het dorp. We bezorgen in heel Zundert: rond de Markt met het Vincent van GoghHuis en de Sint-Trudokerk, in de Molenstraat en de Prinsenstraat, langs de Wernhoutseweg en in de buurten aan de Randweg. Ook Klein-Zundert, Wernhout en Rijsbergen horen bij ons bezorggebied.",
            "Zundert is bekend van het bloemencorso op de eerste zondag van september en van de boomteelt in het buitengebied. Het is een dorp met hechte buurtschappen en veel feesten in eigen kring: een verjaardag in de tuin, een buurtfeest of een avond met vrienden. Stuur ons een WhatsApp-bericht met je bestelling en je adres, en wij komen naar je toe. Geen rit naar Breda, geen afhaalpunt.",
            "Door de afstand rekenen we in Zundert op 35 tot 45 minuten; bij je bestelling krijg je een indicatie. Tanks leveren we verzegeld in 2KG en 4KG, de 10KG in overleg. Uitsluitend 18+, betalen bij aflevering contant of via Tikkie. Lees vooraf onze tips over <a href=\"/lachgas-informatie/veilig-gebruik/\">veilig gebruik</a> en ga na gebruik niet de weg op.",
        ],
        "wijken": "Markt, Molenstraat, Prinsenstraat, Wernhoutseweg, Bredaseweg, Randweg, Klein-Zundert, Wernhout, Rijsbergen",
        "levertijd": "meestal binnen 35 tot 45 minuten",
        "faq": [
            [
                "Bezorgen jullie ook in Rijsbergen en Wernhout?",
                "Ja. Rijsbergen ligt op onze route vanaf Breda en is vaak zelfs iets sneller dan Zundert zelf. Wernhout en Klein-Zundert nemen we ook mee. Voor Achtmaal en het verre buitengebied overleggen we even via WhatsApp.",
            ],
            [
                "Bezorgen jullie tijdens het bloemencorso?",
                "Ja, maar houd er rekening mee dat het centrum van Zundert tijdens corsoweekend grotendeels is afgesloten en het verkeer traag is. We bezorgen dan alleen op een woonadres buiten de afsluitingen, niet langs de route. Bestel ruim op tijd.",
            ],
            [
                "Ik woon net over de grens in België, kunnen jullie ook daar bezorgen?",
                "Nee, wij bezorgen uitsluitend in Nederland. Zundert, Wernhout en Rijsbergen zijn de zuidelijkste plaatsen in ons bezorggebied.",
            ],
        ],
        "nearby": ["etten-leur", "princenhage", "roosendaal"],
        "lat": 51.4710,
        "lon": 4.6560,
    },
]

# ---------------------------------------------------------------------------
# Informatie-artikelen (/lachgas-informatie/<slug>/)
# ---------------------------------------------------------------------------

ARTICLES = [
    {
        "slug": "lachgas-en-vitamine-b12",
        "label": "Gezondheid",
        "title": "Lachgas en vitamine B12: risico's en klachten",
        "description": "Lachgas maakt vitamine B12 in je lichaam onwerkzaam. Lees welke klachten dat geeft, wie extra risico loopt en wanneer je naar de huisarts moet.",
        "h1": "Lachgas en vitamine B12",
        "lead": "Het bekendste gezondheidsrisico van lachgas is het effect op vitamine B12. Hier lees je wat er precies gebeurt, welke klachten erbij horen en wanneer je hulp moet zoeken.",
        "sections": [
            {
                "h2": "Wat doet lachgas met vitamine B12?",
                "paragraphs": [
                    "Vitamine B12 heeft je lichaam nodig om zenuwen gezond te houden, rode bloedcellen aan te maken en DNA te vormen. In de kern van het B12-molecuul zit een kobaltatoom, en precies daar grijpt lachgas (distikstofmonoxide, N2O) in. Het gas oxideert dat kobalt, waardoor de vitamine zijn werk niet meer kan doen. De B12 is dan nog wel in je bloed aanwezig, maar is onwerkzaam geworden.",
                    "Na een enkele keer met een kleine hoeveelheid herstelt het lichaam dit meestal binnen enkele dagen. Het probleem ontstaat wanneer je vaak gebruikt, veel ballonnen kort na elkaar neemt of een hele tank op een avond leegmaakt. Het herstel kan het dan niet meer bijhouden. Het gevolg is een functioneel B12-tekort: de bloedwaarde kan er normaal uitzien, terwijl de vitamine in de praktijk niets meer doet.",
                ],
                "bullets": [],
            },
            {
                "h2": "Welke klachten kun je krijgen?",
                "paragraphs": [
                    "Een B12-tekort door lachgas raakt vooral het zenuwstelsel. De beschermlaag rond de zenuwen (myeline) raakt beschadigd, en dat merk je het eerst in de langste zenuwbanen: die naar je voeten en handen. Klachten beginnen daarom vaak aan beide kanten tegelijk, in de tenen of vingertoppen, en kruipen langzaam omhoog.",
                    "De klachten kunnen al tijdens een periode van veel gebruik ontstaan, maar ook pas dagen of weken daarna.",
                ],
                "bullets": [
                    "<strong>Tintelingen.</strong> Een prikkelend of elektrisch gevoel in voeten, onderbenen, handen of vingers.",
                    "<strong>Gevoelloosheid.</strong> Een doof of 'watten'-gevoel in de huid, soms ook verminderd gevoel voor warmte en kou.",
                    "<strong>Spierzwakte.</strong> Minder kracht in benen of handen, moeite met trappen lopen of iets vasthouden.",
                    "<strong>Loopproblemen.</strong> Onzeker of wankel lopen, struikelen, moeite met evenwicht in het donker.",
                    "<strong>Overige klachten.</strong> Vermoeidheid, concentratieproblemen, geheugenklachten en een sombere of prikkelbare stemming.",
                ],
            },
            {
                "h2": "Wie loopt extra risico?",
                "paragraphs": [
                    "Iedereen die lachgas gebruikt kan een B12-tekort ontwikkelen, maar bij sommige mensen gaat het sneller of is de schade groter. Dat heeft te maken met de hoeveelheid B12 die je lichaam in voorraad heeft en met de snelheid waarmee je die aanvult.",
                ],
                "bullets": [
                    "<strong>Frequente gebruikers.</strong> Wie wekelijks of vaker gebruikt, veel ballonnen per keer neemt of regelmatig uit een tank gebruikt, loopt veruit het grootste risico.",
                    "<strong>Vegetariërs en veganisten.</strong> B12 zit vrijwel alleen in dierlijke producten. Wie weinig of geen vlees, vis, zuivel en eieren eet, heeft vaak een kleinere voorraad en merkt het effect van lachgas eerder.",
                    "<strong>Zwangeren.</strong> Lachgas kan de B12-huishouding van moeder en ongeboren kind verstoren. Tijdens de zwangerschap en bij een zwangerschapswens kun je lachgas beter helemaal laten.",
                    "<strong>Bepaalde medicijnen.</strong> Metformine (bij diabetes) en maagzuurremmers kunnen de opname van B12 verlagen. In combinatie met lachgas stapelt het effect.",
                    "<strong>Maag- en darmaandoeningen.</strong> Bij coeliakie, de ziekte van Crohn of na een maagverkleining neemt het lichaam al minder B12 op.",
                ],
            },
            {
                "h2": "Helpt het om extra vitamine B12 te slikken?",
                "paragraphs": [
                    "Nee, niet op de manier waarop veel gebruikers hopen. Een supplement vult je voorraad aan, maar lachgas maakt ook die aangevulde B12 onwerkzaam. Je neemt het risico dus niet weg door tabletten te slikken of een injectie te halen voordat je gaat gebruiken. Het geeft hooguit een vals gevoel van veiligheid.",
                    "De enige manier om het risico echt te verkleinen is minder en minder vaak gebruiken, of helemaal stoppen. Heeft een arts bij jou een tekort vastgesteld, dan kan een behandeling met B12-injecties nodig zijn om de schade te beperken. Dat is een medische behandeling na een probleem, geen vrijbrief om door te gaan.",
                ],
                "bullets": [],
            },
            {
                "h2": "Wat doe je bij klachten?",
                "paragraphs": [
                    "Merk je tintelingen, gevoelloosheid, krachtverlies of problemen met lopen, stop dan direct met lachgas en maak een afspraak bij je huisarts. Wacht hier niet mee: hoe langer de zenuwen zonder werkende B12 zitten, hoe groter de kans dat een deel van de schade blijvend is.",
                    "Vertel je huisarts eerlijk dat je lachgas gebruikt en hoeveel. Dat is belangrijk, omdat een gewone B12-bloedwaarde bij lachgasgebruik normaal kan lijken. De arts weet dan dat er andere waarden gemeten moeten worden, zoals methylmalonzuur of homocysteïne, en kan sneller de juiste behandeling starten.",
                    "Kun je plotseling niet meer goed staan of lopen, raak je verward of verlies je het bewustzijn, bel dan 112. Dat geldt ook als iemand in je omgeving na lachgasgebruik niet meer goed reageert.",
                ],
                "bullets": [],
            },
            {
                "h2": "Zo beperk je het risico",
                "paragraphs": [
                    "Wie toch kiest voor lachgas, kan het risico op een B12-tekort flink verkleinen door bewust om te gaan met hoeveelheid en frequentie. De vuistregel: zelden, weinig en met pauzes.",
                ],
                "bullets": [
                    "<strong>Gebruik zelden.</strong> Houd het bij af en toe, niet elke week en zeker niet elke dag.",
                    "<strong>Houd het klein.</strong> Een paar ballonnen op een avond is iets anders dan een tank in je eentje leegmaken. Een grotere voorraad is geen reden om meer te nemen.",
                    "<strong>Neem pauzes.</strong> Wacht tussen ballonnen tot je weer helemaal helder bent. Snel achter elkaar gebruiken vergroot zowel het acute risico als het B12-risico.",
                    "<strong>Combineer niet.</strong> Geen alcohol of andere middelen erbij; die maskeren de signalen van je lichaam.",
                    "<strong>Let op elkaar.</strong> Neem klachten bij vrienden serieus. Meer tips lees je op onze pagina over <a href=\"/lachgas-informatie/veilig-gebruik/\">veilig gebruik</a>; onafhankelijke informatie vind je bij <a href=\"https://www.drugsinfo.nl\">drugsinfo.nl</a>.",
                ],
            },
        ],
        "note": "Deze informatie is bedoeld om risico's te beperken, niet om gebruik aan te moedigen en is geen vervanging van medisch advies. Heb je tintelingen, gevoelloosheid, krachtverlies of problemen met lopen na lachgasgebruik? Stop direct en maak een afspraak bij je huisarts. Bij acute ernstige klachten bel je 112.",
        "related": ["veilig-gebruik", "wat-is-lachgas", "lachgas-in-het-verkeer"],
    },
    {
        "slug": "lachgas-tank-bewaren-en-vervoeren",
        "label": "Praktisch",
        "title": "Lachgastank bewaren en vervoeren: zo doe je dat",
        "description": "Hoe bewaar en vervoer je een lachgastank veilig? Rechtop, koel en uit de zon, kraan dicht en vastgezet in de auto. Praktische tips van Lachgas Breda.",
        "h1": "Lachgastank bewaren en vervoeren",
        "lead": "Een lachgastank is een drukhouder en verdient dezelfde zorg als een gasfles. Zo bewaar je hem thuis en zo neem je hem veilig mee.",
        "sections": [
            {
                "h2": "Waarom goed bewaren belangrijk is",
                "paragraphs": [
                    "In een lachgastank zit distikstofmonoxide (N2O) onder hoge druk, deels als vloeistof. Zolang de tank rechtop staat, de kraan dicht is en de temperatuur normaal blijft, is dat volkomen stabiel. Problemen ontstaan als een tank heet wordt, omvalt of beschadigd raakt. Warmte verhoogt de druk in de cilinder, een val kan de kraan of het ventiel beschadigen, en een lekkende tank kan een kleine ruimte snel vullen met gas.",
                    "Wij leveren elke tank verzegeld af; daarna is een veilige plek aan jou. Met een paar simpele gewoontes voorkom je bijna alle risico's.",
                ],
                "bullets": [],
            },
            {
                "h2": "Zo bewaar je een lachgastank thuis",
                "paragraphs": [
                    "De juiste plek is simpel samen te vatten: rechtop, koel, droog en uit de zon. Denk aan een bijkeuken, een berging of een kast op de begane grond, en niet aan een vensterbank, een cv-kast of de kofferbak van je auto.",
                ],
                "bullets": [
                    "<strong>Altijd rechtop.</strong> Zet de tank op een vlakke, stevige ondergrond waar hij niet kan omvallen of omgestoten worden.",
                    "<strong>Koel.</strong> Kamertemperatuur of koeler. Houd afstand tot verwarming, kachel, oven, vaatwasser en andere warmtebronnen.",
                    "<strong>Droog.</strong> Vocht veroorzaakt roest op de cilinder en de kraan. Een vochtige kelder of een natte schuur is geen goede plek.",
                    "<strong>Uit de zon.</strong> Niet achter glas, niet op het balkon en niet in een serre. Direct zonlicht verhit metaal sneller dan je denkt.",
                    "<strong>Kraan dicht.</strong> Draai de kraan volledig dicht zodra je klaar bent, ook als je de tank later die avond weer gebruikt.",
                    "<strong>Buiten bereik van kinderen en huisdieren.</strong> Bewaar de tank hoog of achter een afgesloten deur.",
                    "<strong>Niet in een kleine afgesloten ruimte waar je slaapt.</strong> Mocht een tank lekken, dan moet het gas kunnen ontsnappen; een slaapkamer is daarom ongeschikt.",
                ],
            },
            {
                "h2": "Nooit in een warme auto of in de volle zon",
                "paragraphs": [
                    "Dit is het belangrijkste punt van deze pagina. In een geparkeerde auto loopt de temperatuur op een zomerse dag binnen een uur op tot ver boven de vijftig graden. De druk in de tank stijgt dan flink. Hetzelfde geldt voor een tank die een middag in de zon in de tuin staat, naast een barbecue of een vuurkorf.",
                    "Haal een tank daarom altijd direct uit de auto na het vervoer en zet hem binnen op een koele plek. Laat hem nooit achter in een auto die in de zon staat, ook niet 'even'.",
                ],
                "bullets": [],
            },
            {
                "h2": "Vervoeren: nuchter, rechtop en vastgezet",
                "paragraphs": [
                    "Meestal hoef je zelf niets te vervoeren: wij bezorgen aan de deur in Breda en omgeving. Neem je toch een tank mee naar een ander adres, bijvoorbeeld van je huis naar een feestlocatie, houd dan rekening met een paar dingen. Allereerst: vervoer alleen als je zelf volledig nuchter bent. Niet na alcohol en niet na lachgas. Over de risico's daarvan lees je op onze pagina over <a href=\"/lachgas-informatie/lachgas-in-het-verkeer/\">lachgas in het verkeer</a>.",
                    "Houd er ook rekening mee dat voor lachgas in Nederland strenge regels gelden. Sinds 1 januari 2023 staat het op lijst II van de Opiumwet, met uitzonderingen voor medische, technische en voedingstoepassingen. Wat dat betekent lees je op onze pagina <a href=\"/lachgas-informatie/is-lachgas-legaal-in-nederland/\">is lachgas legaal in Nederland</a>; voor actuele informatie verwijzen we naar <a href=\"https://www.rijksoverheid.nl\">rijksoverheid.nl</a>.",
                ],
                "bullets": [
                    "<strong>Kraan dicht en beschermd.</strong> Controleer voor vertrek of de kraan volledig dicht is en of er niets aan de tank hangt.",
                    "<strong>Rechtop in de kofferbak.</strong> Zet de tank rechtop en zet hem vast met een spanband, in een krat of tussen stevige spullen, zodat hij bij remmen niet kan omvallen of schuiven.",
                    "<strong>Niet los in de passagiersruimte.</strong> Een losse tank wordt bij een noodstop een projectiel.",
                    "<strong>Ventilatie.</strong> Zet een raam op een kier tijdens het vervoer en gebruik de tank nooit in de auto.",
                    "<strong>Direct uitladen.</strong> Haal de tank na aankomst meteen uit de auto en zet hem binnen op een koele plek.",
                ],
            },
            {
                "h2": "Lege tank? Niet bij het huisvuil",
                "paragraphs": [
                    "Een lege lachgastank hoort nooit bij het restafval, in de glasbak of in de metaalcontainer op straat. Er zit vrijwel altijd nog restdruk in, en in een vuilniswagen of verbrandingsoven kan zo'n cilinder ontploffen. Dat is gevaarlijk voor de mensen die het afval verwerken.",
                    "Wat doe je dan wel? Vraag ons via WhatsApp of we de lege tank kunnen meenemen bij een volgende levering; voor de 10KG maken we daar standaard afspraken over. Wil je de tank zelf wegbrengen, informeer dan bij de milieustraat van je gemeente hoe zij gasflessen innemen. Zet een lege tank in de tussentijd gewoon weg zoals een volle: rechtop, koel, kraan dicht.",
                ],
                "bullets": [],
            },
            {
                "h2": "Korte checklist",
                "paragraphs": [
                    "Houd je je hieraan, dan is een lachgastank thuis net zo veilig als elke andere gasfles.",
                ],
                "bullets": [
                    "<strong>Bewaren:</strong> rechtop, koel, droog, uit de zon, kraan dicht, weg van kinderen.",
                    "<strong>Nooit:</strong> in een warme auto, achter glas, naast een warmtebron of in de slaapkamer.",
                    "<strong>Vervoeren:</strong> alleen nuchter, rechtop en vastgezet in de kofferbak, raam op een kier.",
                    "<strong>Leeg:</strong> niet bij het huisvuil; terug via ons of naar de milieustraat.",
                    "<strong>Beschadigd of lekkend?</strong> Niet gebruiken, rechtop buiten op een geventileerde plek zetten en contact met ons opnemen.",
                ],
            },
        ],
        "note": "Een lachgastank is een drukhouder. Behandel hem met zorg, houd hem weg van warmte en kinderen en vervoer hem alleen nuchter en vastgezet. Twijfel je over een beschadigde of lekkende tank? Zet hem rechtop op een geventileerde plek buiten, blijf er niet bij staan en neem contact met ons op via WhatsApp. Bij een acuut gevaarlijke situatie bel je 112.",
        "related": ["veilig-gebruik", "lachgas-in-het-verkeer", "welke-lachgastank-heb-ik-nodig"],
    },
    {
        "slug": "welke-lachgastank-heb-ik-nodig",
        "label": "Assortiment",
        "title": "Welke lachgastank heb ik nodig? 2KG, 4KG of 10KG",
        "description": "Twijfel je tussen een lachgastank van 2KG, 4KG of 10KG? Onze keuzehulp helpt je kiezen op groepsgrootte en gelegenheid. Bestellen via WhatsApp in Breda.",
        "h1": "Welke lachgastank heb ik nodig?",
        "lead": "Twee, vier of tien kilo? Met deze keuzehulp kies je het formaat dat past bij je gezelschap en je gelegenheid, zonder met een overschot te blijven zitten.",
        "sections": [
            {
                "h2": "Eerst de basis: hoeveel ballonnen uit een tank?",
                "paragraphs": [
                    "Onze tanks zijn gevuld met zuiver N2O en worden verzegeld geleverd. Het gewicht op de tank zegt hoeveel gas erin zit, en daarmee ongeveer hoeveel ballonnen je ermee vult. Als vuistregel: een <a href=\"/product/lachgas-tank-2kg/\">Lachgastank 2KG</a> is goed voor ±250 ballonnen, een <a href=\"/product/lachgas-tank-4kg/\">Lachgastank 4KG</a> voor ±500 en een <a href=\"/product/lachgas-tank-10kg/\">Lachgastank 10KG</a> voor ±1250.",
                    "Het zijn indicaties. Hoe groot je de ballonnen vult en hoe zorgvuldig je de kraan bedient, maakt verschil. Bij het kiezen van een formaat gaat het ook niet alleen om het aantal ballonnen, maar om hoeveel mensen er zijn, hoe lang de avond duurt en hoe je zelf met lachgas om wilt gaan. Meer in huis betekent namelijk niet dat je meer moet gebruiken.",
                ],
                "bullets": [],
            },
            {
                "h2": "Lachgastank 2KG: voor een avond met vrienden",
                "paragraphs": [
                    "De 2KG is ons meest bestelde formaat, en voor de meeste situaties in Breda is dit de logische keuze. Hij is handzaam, past in elke kast en is bedoeld voor een kleinere tot middelgrote groep van ongeveer tien tot vijftien personen: een verjaardag thuis, een avond met je huisgenoten of een gezellige vrijdagavond met vrienden.",
                    "Kies de 2KG als je een normale avond plant met een groep van die omvang, of als je voor het eerst een tank bestelt en nog niet weet hoeveel er daadwerkelijk gebruikt wordt. In de praktijk blijft er bij een rustige avond vaak gas over, en dat is prima: een goed bewaarde tank kun je een volgende keer weer gebruiken. Bekijk de <a href=\"/product/lachgas-tank-2kg/\">Lachgastank 2KG</a>.",
                ],
                "bullets": [],
            },
            {
                "h2": "Lachgastank 4KG: voor een groter feest",
                "paragraphs": [
                    "De 4KG bevat bijna het dubbele van de 2KG en is bedoeld voor een groter feestje van ongeveer twintig tot dertig personen. Denk aan een huisfeest, een groot verjaardagsfeest in de tuin of een feest met een studentenvereniging of sportteam. Het voordeel is vooral praktisch: je hoeft halverwege de avond niet bij te bestellen en te wachten op een tweede levering.",
                    "Twijfel je tussen de 2KG en de 4KG? Kijk naar het aantal gasten dat daadwerkelijk zal gebruiken, niet naar het aantal mensen op de gastenlijst. Bij veel feesten gebruikt maar een deel van de aanwezigen, en dan is een 2KG ruim voldoende. Verwacht je echt een grote groep, bekijk dan de <a href=\"/product/lachgas-tank-4kg/\">Lachgastank 4KG</a>.",
                ],
                "bullets": [],
            },
            {
                "h2": "Lachgastank 10KG: voor evenementen en horeca",
                "paragraphs": [
                    "De 10KG is ons grootste formaat en is niet bedoeld voor een gewoon feestje thuis. Deze tank is zwaar, groot en bestemd voor evenementen en horecagelegenheden die een flinke hoeveelheid nodig hebben zonder steeds bij te bestellen. Juist daarom leveren we de 10KG uitsluitend in overleg: we stemmen via WhatsApp het tijdstip, de locatie, de ophaling van de lege tank en eventuele statiegeldafspraken af.",
                    "Organiseer je iets groots in Breda of omgeving, stuur ons dan ruim op tijd een bericht met de datum, het verwachte aantal mensen en de locatie. We denken graag mee of een 10KG past of dat meerdere kleinere tanks handiger zijn. Bekijk de <a href=\"/product/lachgas-tank-10kg/\">Lachgastank 10KG</a> of lees onze pagina over <a href=\"/lachgas-feest-evenement/\">lachgas voor feesten en evenementen</a>.",
                ],
                "bullets": [],
            },
            {
                "h2": "Liever klein: crackers en slagroompatronen",
                "paragraphs": [
                    "Niet elke gelegenheid vraagt om een tank. Ben je met twee of drie mensen, of gebruik je maar heel af en toe, dan is een <a href=\"/product/lachgas-cracker/\">lachgas cracker</a> met losse patronen van 8 gram een stuk logischer. Je koopt het herbruikbare apparaat één keer en daarna alleen nog patronen. Hoe dat werkt lees je in <a href=\"/lachgas-informatie/hoe-werkt-een-lachgas-cracker/\">hoe werkt een lachgas cracker</a>.",
                    "Heb je al een slagroomspuit in huis, dan kun je ook alleen <a href=\"/product/slagroompatronen/\">slagroompatronen</a> bestellen. Die leveren we in doosjes van 10, 24 of 50 stuks, en voor horeca in grotere aantallen op aanvraag.",
                ],
                "bullets": [],
            },
            {
                "h2": "Zo maak je de keuze",
                "paragraphs": [
                    "Samengevat kies je op basis van groepsgrootte en gelegenheid. Houd daarbij in gedachten dat de kleinere optie bijna altijd de verstandige is: een tank die je niet leegmaakt bewaar je gewoon, een tank die te snel leeg is leidt tot bijbestellen en tot meer gebruik dan je van plan was.",
                ],
                "bullets": [
                    "<strong>2 tot 5 personen, incidenteel:</strong> een cracker met patronen.",
                    "<strong>10 tot 15 personen, een avond:</strong> Lachgastank 2KG.",
                    "<strong>20 tot 30 personen, een groot feest:</strong> Lachgastank 4KG.",
                    "<strong>Evenement of horeca:</strong> Lachgastank 10KG, altijd in overleg.",
                    "<strong>Slagroomspuit in huis:</strong> slagroompatronen per doosje.",
                    "<strong>Twijfel?</strong> Kies het kleinere formaat. Bijbestellen kan altijd, en minder is bij lachgas altijd beter.",
                ],
            },
            {
                "h2": "Bestellen in Breda en omgeving",
                "paragraphs": [
                    "Heb je je keuze gemaakt, dan stuur je ons een WhatsApp-bericht met het formaat, het aantal en je adres. We bevestigen en komen langs, in Breda meestal binnen 20 tot 30 minuten en in plaatsen als Oosterhout, Etten-Leur, Rijen of Zundert iets later. Je betaalt bij aflevering, contant of via Tikkie, en we leveren uitsluitend aan personen van 18 jaar en ouder.",
                    "Welk formaat je ook kiest: lees vooraf onze pagina over <a href=\"/lachgas-informatie/veilig-gebruik/\">veilig gebruik</a> en bewaar de tank zoals beschreven in <a href=\"/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/\">lachgastank bewaren en vervoeren</a>.",
                ],
                "bullets": [],
            },
        ],
        "note": "Een grotere tank is geen reden om meer te gebruiken. Houd je aan de tips voor veilig gebruik, neem pauzes tussen ballonnen, combineer niet met alcohol en let op elkaar. Wij leveren uitsluitend aan personen van 18 jaar en ouder.",
        "related": ["veilig-gebruik", "hoe-werkt-een-lachgas-cracker", "lachgas-tank-bewaren-en-vervoeren"],
    },
]

# ---------------------------------------------------------------------------
# Servicepagina's in de root (/<slug>/)
# ---------------------------------------------------------------------------

SERVICE_PAGES = [
    {
        "slug": "lachgas-nachtbezorging",
        "label": "'s Avonds en 's nachts",
        "title": "Lachgas 's avonds en 's nachts bestellen in Breda",
        "description": "Laat op de avond of 's nachts lachgas nodig in Breda? Wij zijn 24/7 bereikbaar via WhatsApp en bezorgen discreet aan de deur. Alleen 18+.",
        "h1": "Lachgas 's avonds en 's nachts bestellen in Breda",
        "lead": "Een avond die langer doorgaat dan gepland? Wij zijn 24/7 bereikbaar via WhatsApp en bezorgen ook 's avonds laat en 's nachts in Breda en omgeving, discreet aan de deur.",
        "sections": [
            {
                "h2": "Zo werkt bestellen 's avonds en 's nachts",
                "paragraphs": [
                    "Bestellen gaat 's nachts precies hetzelfde als overdag. Je stuurt ons een WhatsApp-bericht met wat je wilt bestellen en het adres waar we moeten zijn. Wij bevestigen je bestelling en geven een indicatie van de bezorgtijd. Daarna komt onze bezorger langs, onopvallend en zonder gedoe aan de deur. Je betaalt bij aflevering, contant of via Tikkie.",
                    "In Breda rekenen we meestal op 20 tot 30 minuten, ook laat op de avond. Op piekmomenten, zoals na middernacht in het weekend, kan het iets langer duren. Daarom krijg je altijd eerst een indicatie, zodat je weet waar je aan toe bent. Woon je buiten Breda, bijvoorbeeld in Oosterhout, Etten-Leur of Rijen, dan geldt de bezorgtijd van dat gebied.",
                ],
                "bullets": [],
            },
            {
                "h2": "Thuis na een avond in het centrum van Breda",
                "paragraphs": [
                    "Veel bestellingen 's nachts komen van mensen die na een avond rond de Grote Markt, de Havermarkt of de Haven thuis nog even verder willen met vrienden. Dat kan, maar wel op een woonadres. We bezorgen niet op straat in het uitgaansgebied, niet voor de deur van een café of club en niet in een park. In de openbare ruimte gelden regels van de gemeente Breda, en het is voor jou en voor ons geen plek om een tank over te dragen.",
                    "Praktisch betekent dit: ga eerst naar huis of naar het huis waar je verder gaat, en stuur dan pas je bestelling met het volledige adres. Of je nu in het centrum woont, in Belcrum, de Heuvel of Brabantpark, of in een studentenhuis aan de rand van de stad; wij komen naar de voordeur.",
                ],
                "bullets": [],
            },
            {
                "h2": "Vrijdag- en zaterdagnacht",
                "paragraphs": [
                    "Het weekend is onze drukste periode, vooral tussen elf uur 's avonds en drie uur 's nachts. Wil je zeker weten dat je niet hoeft te wachten, bestel dan eerder op de avond. Je kunt via WhatsApp ook een tijdstip afspreken, zodat we er zijn wanneer jullie thuis zijn. Bestel je toch in de piek, dan houden we je via WhatsApp op de hoogte als het langer duurt dan verwacht.",
                ],
                "bullets": [],
            },
            {
                "h2": "Wat je doorgeeft in je bericht",
                "paragraphs": [
                    "'s Nachts is een compleet bericht nog belangrijker dan overdag: straten zijn donker, huisnummers slecht te zien en bellen is niet altijd gewenst. Met deze gegevens kan onze bezorger meteen op pad.",
                ],
                "bullets": [
                    "<strong>Wat en hoeveel.</strong> Bijvoorbeeld een Lachgastank 2KG, een cracker met patronen of een doosje slagroompatronen.",
                    "<strong>Het volledige adres.</strong> Straat, huisnummer, toevoeging, verdieping en de naam op de bel.",
                    "<strong>Het gewenste tijdstip.</strong> Nu, of een tijd later in de nacht.",
                    "<strong>Een naam.</strong> Zodat de bezorger weet wie hij aan de deur treft.",
                    "<strong>Je legitimatie bij de hand.</strong> We verkopen uitsluitend aan 18+ en kunnen bij twijfel om een identiteitsbewijs vragen, ook 's nachts.",
                ],
            },
            {
                "h2": "Verantwoord na een avond uit",
                "paragraphs": [
                    "Een avond uit in Breda gaat vaak samen met alcohol, en juist die combinatie met lachgas raden we af. Alcohol versterkt de duizeligheid en misselijkheid, maskeert de signalen van je lichaam en vergroot de kans op vallen. Heb je flink gedronken, dan is lachgas die nacht geen goed idee. Wees eerlijk tegen jezelf en tegen je vrienden.",
                    "Gebruik je toch, doe het dan zittend of liggend op een plek met frisse lucht, neem pauzes tussen ballonnen en let op elkaar. Laat niemand alleen die zich niet goed voelt, en bel 112 bij ernstige klachten. En ga daarna niet meer de weg op: niet met de auto, niet op de scooter en ook niet op de fiets. Meer lees je op onze pagina's over <a href=\"/lachgas-informatie/veilig-gebruik/\">veilig gebruik</a> en <a href=\"/lachgas-informatie/lachgas-in-het-verkeer/\">lachgas in het verkeer</a>.",
                ],
                "bullets": [],
            },
        ],
        "note": "Wij bezorgen alleen aan personen van 18 jaar en ouder en alleen op een woonadres of vooraf afgesproken adres. Combineer lachgas niet met alcohol en neem na gebruik nooit deel aan het verkeer. Voelt iemand zich niet goed, blijf erbij en bel bij ernstige klachten 112.",
        "faq": [
            [
                "Tot hoe laat kan ik 's nachts bestellen in Breda?",
                "Er is geen sluitingstijd: we zijn zeven dagen per week, 24 uur per dag bereikbaar via WhatsApp. Stuur je bericht en je krijgt een bevestiging met een indicatie van de bezorgtijd, ook midden in de nacht.",
            ],
            [
                "Duurt bezorgen 's nachts langer dan overdag?",
                "Meestal niet. In Breda zijn we ook 's nachts doorgaans binnen 20 tot 30 minuten bij je. Alleen in de drukste uren van vrijdag- en zaterdagnacht kan het iets uitlopen; dat laten we je dan vooraf weten.",
            ],
            [
                "Kunnen jullie bezorgen op de Grote Markt of bij een café?",
                "Nee. We bezorgen uitsluitend op een woonadres of een vooraf afgesproken adres, niet op straat in het uitgaansgebied, bij een horecazaak of in een park. Ga eerst naar huis en stuur dan je adres door.",
            ],
        ],
        "related": ["veilig-gebruik", "lachgas-in-het-verkeer"],
    },
    {
        "slug": "lachgas-feest-evenement",
        "label": "Feest & evenement",
        "title": "Lachgas voor feesten en evenementen in Breda",
        "description": "Lachgas voor een verjaardag, huisfeest of evenement in Breda? Kies het juiste formaat, bestel tijdig via WhatsApp en houd het veilig. Alleen 18+.",
        "h1": "Lachgas voor feesten en evenementen in Breda",
        "lead": "Van een verjaardag in de huiskamer tot een groot evenement: wij bezorgen de juiste hoeveelheid op het juiste moment in Breda en omgeving, en helpen je het verantwoord te houden.",
        "sections": [
            {
                "h2": "Verjaardag of huisfeest",
                "paragraphs": [
                    "Voor een verjaardag of een huisfeest met tien tot vijftien gasten is de <a href=\"/product/lachgas-tank-2kg/\">Lachgastank 2KG</a> in bijna alle gevallen voldoende. Wordt het groter, met twintig tot dertig mensen, dan voorkomt de <a href=\"/product/lachgas-tank-4kg/\">Lachgastank 4KG</a> dat je halverwege de avond moet bijbestellen. Twijfel je, kies dan het kleinere formaat: wat overblijft bewaar je gewoon voor een volgende keer.",
                    "Je bestelt via WhatsApp, wij bezorgen aan de deur van het feestadres in Breda of een van de omliggende plaatsen, en je betaalt bij aflevering contant of via Tikkie. Zet in je bericht het adres van het feest, niet je eigen adres, als dat verschilt.",
                ],
                "bullets": [],
            },
            {
                "h2": "Studentenfeest",
                "paragraphs": [
                    "Breda is een studentenstad, en veel bestellingen komen uit studentenhuizen in het centrum, Belcrum, de Heuvel en rond de campussen. Voor een huisfeest met een paar huizen samen is de 4KG meestal het juiste formaat; voor een gewone avond met je huisgenoten volstaat de 2KG of zelfs een <a href=\"/product/lachgas-cracker/\">cracker met patronen</a>.",
                    "Houd als gastheer of gastvrouw rekening met de leeftijd van je gasten: wij leveren uitsluitend aan 18+, en op een feest met jongere bezoekers is lachgas geen goed idee. Spreek vooraf af wie nuchter blijft en een oogje in het zeil houdt.",
                ],
                "bullets": [],
            },
            {
                "h2": "Bedrijfsfeest of teamuitje",
                "paragraphs": [
                    "Ook voor een bedrijfsfeest, een teamuitje of een afsluiting van het jaar krijgen we aanvragen. Hier geldt extra: zorg dat de organisatie en de locatie akkoord zijn, dat er alleen volwassenen aanwezig zijn en dat niemand na afloop nog hoeft te rijden. Wij bezorgen op een privé- of bedrijfsadres in Breda en omgeving en stemmen het tijdstip vooraf met je af via WhatsApp.",
                ],
                "bullets": [],
            },
            {
                "h2": "Carnaval in Breda",
                "paragraphs": [
                    "Tijdens carnaval verandert Breda in het Kielegat en is het in het centrum, rond de Grote Markt en de Havermarkt, dagenlang druk. Wij bezorgen die dagen gewoon, maar alleen op een woonadres en niet op straat of in de feesttenten. In de openbare ruimte gelden de regels van de gemeente Breda. Houd er rekening mee dat delen van het centrum zijn afgesloten en dat bezorgen dan wat langer kan duren.",
                    "Carnaval en alcohol gaan vaak samen, en die combinatie met lachgas raden we af. Plan lachgas liever voor een rustig moment thuis met vrienden dan voor na een lange dag in de kroeg.",
                ],
                "bullets": [],
            },
            {
                "h2": "Grotere aantallen en de 10KG tank",
                "paragraphs": [
                    "Voor evenementen, grotere privéfeesten en horeca hebben we de <a href=\"/product/lachgas-tank-10kg/\">Lachgastank 10KG</a>, goed voor ±1250 ballonnen. Dit formaat leveren we uitsluitend in overleg: de tank is groot en zwaar, en we stemmen tijdstip, locatie, ophaling van de lege tank en eventuele statiegeldafspraken vooraf met je af. Soms zijn twee of drie 4KG-tanks praktischer dan één 10KG, bijvoorbeeld als het feest zich over meerdere ruimtes verspreidt.",
                    "Stuur ons voor een groter evenement de datum, de locatie en het verwachte aantal gasten dat gaat gebruiken. We denken mee over de hoeveelheid en of grotere aantallen <a href=\"/product/slagroompatronen/\">slagroompatronen</a> voor je horecazaak handiger zijn. Onze <a href=\"/lachgas-informatie/welke-lachgastank-heb-ik-nodig/\">keuzehulp</a> helpt je alvast op weg.",
                ],
                "bullets": [],
            },
            {
                "h2": "Tijdig bestellen",
                "paragraphs": [
                    "Voor een gewone avond kun je op het moment zelf bestellen; in Breda zijn we meestal binnen 20 tot 30 minuten bij je. Voor een feest met veel gasten, een evenement of een 10KG raden we aan om vooraf via WhatsApp een dag en tijdstip af te spreken, liefst een paar dagen van tevoren. Zo weet je zeker dat alles er is voordat de eerste gasten binnenkomen, en zit je niet in de piek van vrijdag- of zaterdagnacht te wachten.",
                ],
                "bullets": [],
            },
            {
                "h2": "Veilig op een feest",
                "paragraphs": [
                    "Als gastheer of gastvrouw bepaal jij de sfeer. Een paar afspraken vooraf maken een feest met lachgas een stuk veiliger, voor je gasten en voor jezelf.",
                ],
                "bullets": [
                    "<strong>Alleen 18+.</strong> Lachgas is niets voor minderjarigen, ook niet 'een keertje' op een feest.",
                    "<strong>Zitplek en frisse lucht.</strong> Richt een plek in waar mensen zittend kunnen gebruiken, met een open raam of deur. Niet op de trap, niet op een balkon zonder hek.",
                    "<strong>Altijd een ballon.</strong> Nooit direct uit de tank, de cracker of het patroon inhaleren.",
                    "<strong>Geen druk.</strong> Niemand hoeft mee te doen, en niemand hoeft 'nog één'. Pauzes tussen ballonnen zijn normaal.",
                    "<strong>Niet mixen.</strong> Alcohol en andere middelen erbij vergroten de risico's aanzienlijk.",
                    "<strong>Iemand nuchter.</strong> Spreek af wie nuchter blijft, let op gasten die zich niet goed voelen en bel bij ernstige klachten 112.",
                    "<strong>Niemand de weg op.</strong> Regel vooraf hoe gasten thuiskomen: slapen, lopen of een nuchtere chauffeur. Lees onze pagina over <a href=\"/lachgas-informatie/lachgas-in-het-verkeer/\">lachgas in het verkeer</a>.",
                    "<strong>Tank veilig wegzetten.</strong> Rechtop, kraan dicht, weg van kinderen en warmte, zoals beschreven in <a href=\"/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/\">lachgastank bewaren en vervoeren</a>.",
                ],
            },
        ],
        "note": "Lachgas op een feest vraagt om een gastheer die oplet. Houd het bij volwassenen, combineer niet met alcohol, laat niemand na gebruik rijden en blijf bij gasten die zich niet goed voelen. Bel bij ernstige klachten 112. Meer tips vind je op onze pagina over veilig gebruik.",
        "faq": [
            [
                "Hoeveel lachgas heb ik nodig voor een feest met vijftig gasten?",
                "Dat hangt af van hoeveel gasten daadwerkelijk gebruiken; dat is bijna nooit iedereen. Voor een feest van die omvang is een 4KG vaak voldoende, eventueel met een tweede 4KG als reserve. Twijfel je, stuur ons dan de details via WhatsApp en we denken mee, of lees onze <a href=\"/lachgas-informatie/welke-lachgastank-heb-ik-nodig/\">keuzehulp</a>.",
            ],
            [
                "Kan ik voor een feest later in de week alvast een levering afspreken?",
                "Ja. Stuur ons via WhatsApp de datum, het tijdstip en het adres van het feest, dan plannen we de levering in. Voor een 10KG of grotere aantallen is dat zelfs de standaardwerkwijze.",
            ],
            [
                "Nemen jullie de lege tank na het feest weer mee?",
                "Voor de 10KG maken we daar altijd vooraf afspraken over. Voor een 2KG of 4KG kun je via WhatsApp vragen of we de lege tank bij een volgende levering meenemen. Zet een lege tank nooit bij het huisvuil.",
            ],
        ],
        "related": ["welke-lachgastank-heb-ik-nodig", "veilig-gebruik"],
    },
]

# ---------------------------------------------------------------------------
# Veelgestelde vragen (/veelgestelde-vragen/)
# ---------------------------------------------------------------------------

FAQ = {
    "title": "Veelgestelde vragen over lachgas in Breda",
    "description": "Antwoord op veelgestelde vragen over lachgas bestellen in Breda: bezorgen via WhatsApp, formaten, betalen bij levering, 18+ en veilig gebruik.",
    "h1": "Veelgestelde vragen",
    "lead": "Alles wat je wilt weten over bestellen, bezorgen, betalen en veilig gebruik van lachgas in Breda en omgeving. Staat je vraag er niet bij? Stuur ons een bericht via WhatsApp.",
    "groups": [
        {
            "h2": "Bestellen en bezorgen",
            "items": [
                [
                    "Wat zet ik in mijn WhatsApp-bericht?",
                    "Het product en het aantal (bijvoorbeeld een Lachgastank 2KG of een doosje slagroompatronen), het volledige adres met huisnummer en eventueel verdieping of naam op de bel, en het gewenste tijdstip. Wij bevestigen je bestelling en geven een indicatie van de bezorgtijd.",
                ],
                [
                    "Bezorgen jullie in heel Breda, ook in Teteringen, Bavel en Ulvenhout?",
                    "Ja. We bezorgen in alle Bredase wijken, van het centrum en Belcrum tot de Haagse Beemden en Princenhage, en ook in de dorpen die bij Breda horen zoals Prinsenbeek, Teteringen, Bavel en Ulvenhout. Daarbuiten komen we onder meer in Oosterhout, Etten-Leur, Rijen, Dongen, Zundert, Tilburg en Roosendaal. Bekijk het volledige <a href=\"/bezorggebied/\">bezorggebied</a>.",
                ],
                [
                    "Kan ik een bezorgmoment afspreken voor later op de dag of een andere dag?",
                    "Ja. Geef in je WhatsApp-bericht aan op welke dag en rond welke tijd je de levering wilt, dan plannen we dat in. Voor feesten en voor de 10KG tank raden we dat zelfs aan, zodat je niet in de drukte van het weekend hoeft te wachten.",
                ],
                [
                    "Hoe discreet is de levering?",
                    "Onze bezorger komt onopvallend aan de deur, zonder bedrukte kleding of opvallend voertuig, en overhandigt de bestelling persoonlijk. We bezorgen alleen op een woonadres of vooraf afgesproken adres, niet op straat of bij horeca. Buren zien dus niets anders dan iemand die iets afgeeft.",
                ],
            ],
        },
        {
            "h2": "Producten en hoeveelheden",
            "items": [
                [
                    "Wat is het verschil tussen de 2KG, 4KG en 10KG tank?",
                    "Het gewicht geeft aan hoeveel N2O erin zit. De 2KG is goed voor ±250 ballonnen en past bij een groep van tien tot vijftien personen, de 4KG voor ±500 ballonnen en twintig tot dertig personen. De 10KG (±1250 ballonnen) is bedoeld voor evenementen en horeca en leveren we alleen in overleg. Lees onze <a href=\"/lachgas-informatie/welke-lachgastank-heb-ik-nodig/\">keuzehulp</a>.",
                ],
                [
                    "Wat is het verschil tussen een cracker en slagroompatronen?",
                    "Slagroompatronen zijn losse capsules van 8 gram N2O, bedoeld voor een slagroomspuit, en leveren we per doosje van 10, 24 of 50 stuks. Een <a href=\"/product/lachgas-cracker/\">lachgas cracker</a> is een herbruikbaar apparaatje waarin je zo'n patroon plaatst om het gas in een ballon over te brengen. Voor incidenteel gebruik met een klein gezelschap is een cracker voordeliger dan een tank.",
                ],
                [
                    "Zijn de tanks nieuw en verzegeld?",
                    "Elke tank wordt verzegeld geleverd en is gevuld met zuiver N2O. Je ziet bij aflevering zelf dat de verzegeling intact is. Is dat onverhoopt niet zo, neem de tank dan niet aan en laat het ons direct weten via WhatsApp.",
                ],
                [
                    "Wat doe ik met een lege tank?",
                    "Zet een lege tank nooit bij het huisvuil, in de glasbak of in de metaalcontainer; er zit restdruk in en dat is gevaarlijk voor afvalverwerkers. Vraag ons via WhatsApp of we de tank bij een volgende levering meenemen, of informeer bij de milieustraat van je gemeente. Voor de 10KG maken we vooraf afspraken over ophaling.",
                ],
            ],
        },
        {
            "h2": "Betalen en voorwaarden",
            "items": [
                [
                    "Moet ik vooruitbetalen of een account aanmaken?",
                    "Nee. Je hoeft geen account aan te maken en betaalt pas bij aflevering. Je stuurt een WhatsApp-bericht, wij bevestigen, en je rekent af op het moment dat de bezorger voor de deur staat.",
                ],
                [
                    "Kan ik bij de bezorger pinnen?",
                    "Betalen gaat bij levering contant of via Tikkie. Geef in je bericht aan welke van de twee je voorkeur heeft, dan houdt de bezorger daar rekening mee. Zorg bij contante betaling dat je het bedrag zo gepast mogelijk bij de hand hebt.",
                ],
                [
                    "Wat als ik mijn identiteitsbewijs niet kan laten zien?",
                    "Wij leveren uitsluitend aan personen van 18 jaar en ouder en kunnen bij twijfel om een identiteitsbewijs vragen. Kun je op dat moment niet aantonen dat je 18 of ouder bent, dan kunnen we de bestelling niet afgeven. Houd je legitimatie dus bij de hand als je bestelt.",
                ],
                [
                    "Kan ik mijn bestelling nog wijzigen of annuleren?",
                    "Laat het ons zo snel mogelijk weten via WhatsApp. Zolang de bezorger nog niet onderweg is, passen we je bestelling zonder problemen aan. Is hij al vertrokken, dan kijken we samen wat er nog mogelijk is.",
                ],
            ],
        },
        {
            "h2": "Veiligheid en regels",
            "items": [
                [
                    "Mag ik lachgas gebruiken op straat of in een park in Breda?",
                    "Nee, daar raden we het sterk af en de gemeente Breda kan via de Algemene Plaatselijke Verordening regels stellen voor lachgas in de openbare ruimte. Daarnaast staat lachgas sinds 1 januari 2023 op lijst II van de Opiumwet, met uitzonderingen voor medische, technische en voedingstoepassingen. Gebruik thuis, zittend en met frisse lucht. Lees meer op <a href=\"/lachgas-informatie/is-lachgas-legaal-in-nederland/\">is lachgas legaal in Nederland</a>.",
                ],
                [
                    "Wat doe ik als iemand zich niet goed voelt na lachgas?",
                    "Stop direct, zorg voor frisse lucht en laat de persoon zitten of liggen. Blijf erbij en houd in de gaten of hij of zij helder reageert. Blijft iemand duizelig, verward of misselijk, of reageert hij niet meer goed, bel dan 112. Onafhankelijke informatie vind je bij <a href=\"https://www.drugsinfo.nl\">drugsinfo.nl</a>.",
                ],
                [
                    "Mag ik na lachgas nog fietsen of met de auto naar huis?",
                    "Nee. Lachgas verstoort je reactievermogen, evenwicht en waarneming, en ook na het korte roeseffect ben je niet meteen helder. Deelnemen aan het verkeer onder invloed is bovendien strafbaar. Ga lopend, blijf slapen of regel een nuchtere chauffeur. Lees onze pagina over <a href=\"/lachgas-informatie/lachgas-in-het-verkeer/\">lachgas in het verkeer</a>.",
                ],
                [
                    "Hoe vaak is te vaak?",
                    "Hoe vaker en hoe meer je gebruikt, hoe groter het risico op een tekort aan werkzame vitamine B12, met tintelingen, gevoelloosheid en loopproblemen als gevolg. Wekelijks of vaker gebruiken, of grote hoeveelheden per keer, is wat ons betreft te vaak. Lees ons artikel over <a href=\"/lachgas-informatie/lachgas-en-vitamine-b12/\">lachgas en vitamine B12</a> en neem bij klachten contact op met je huisarts.",
                ],
            ],
        },
    ],
}
