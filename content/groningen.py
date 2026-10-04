# -*- coding: utf-8 -*-
"""Content voor nieuwe subpagina's van lachgasgroningen.nl.

Toegestane HTML in tekstvelden: <strong>, <em> en <a href="/pad/"> (intern)
of <a href="https://..."> voor drugsinfo.nl / rijksoverheid.nl.
"""

SITE = {"domain": "lachgasgroningen.nl", "brand": "Lachgas Groningen", "city": "Groningen", "aanspreek": "je"}

# ---------------------------------------------------------------------------
# Bezorggebieden
# ---------------------------------------------------------------------------

AREAS = [
    {
        "slug": "zuidhorn",
        "name": "Zuidhorn",
        "kind": "dorp",
        "title": """Lachgas Zuidhorn | Snel bezorgd via WhatsApp""",
        "description": """Lachgas bestellen in Zuidhorn? Snel en discreet bezorgd via WhatsApp rond De Gast, station Zuidhorn en Oostergast. Tanks in 2KG, 4KG en 10KG. Alleen 18+.""",
        "h1": """Lachgas Zuidhorn""",
        "lead": """Snel en discreet bezorgd in Zuidhorn, besteld via WhatsApp.""",
        "intro": [
            """Zuidhorn ligt zo'n vijftien kilometer ten westen van Groningen, aan de spoorlijn naar Leeuwarden en vlak bij het Van Starkenborghkanaal. Wij bezorgen in het hele dorp: van De Gast en de Dorpsvenne in het oude centrum tot de nieuwbouw in Oostergast, de straten rond station Zuidhorn en de Hanckemalaan. Ook in Noordhorn, aan de overkant van het kanaal, en in Briltil komen we gewoon langs.""",
            """Onze bezorgers rijden vanuit de stad via de Friesestraatweg (N355) het Westerkwartier in. Dat is een rechte route zonder veel oponthoud, waardoor we in Zuidhorn meestal binnen 30 tot 40 minuten aan de deur staan. Op vrijdag- en zaterdagavond kan het iets drukker zijn; je krijgt via WhatsApp altijd een eerlijke indicatie zodra je bestelt.""",
            """Zuidhorn is een forensendorp met veel jonge gezinnen en studenten die in Groningen werken of studeren, maar liever hier wonen. Voor een avond met vrienden in de tuin, een verjaardag of een feestje na een dag in de stad is de <a href="/product/lachgas-tank-2kg/">Lachgastank 2KG</a> meestal ruim voldoende. Groter gezelschap? Dan is de <a href="/product/lachgas-tank-4kg/">4KG</a> een logische keuze. Je stuurt een bericht met je adres in Zuidhorn, wij bevestigen en komen langs. Alleen voor 18+.""",
        ],
        "wijken": """De Gast, Dorpsvenne, Oostergast, Westergast, Hanckemalaan, Klinckemalaan, Station Zuidhorn, Noordhorn, Briltil""",
        "levertijd": """meestal binnen 30 tot 40 minuten""",
        "faq": [
            ["""Bezorgen jullie ook in Noordhorn en Briltil?""", """Ja. Noordhorn ligt direct aan de andere kant van het Van Starkenborghkanaal en Briltil grenst aan Zuidhorn, dus beide horen bij ons bezorggebied. Zet gewoon je volledige adres in je WhatsApp-bericht, dan plannen wij de route."""],
            ["""Hoe lang duurt bezorging in Zuidhorn ten opzichte van de stad?""", """Zuidhorn ligt een kwartier rijden van het centrum van Groningen, dus reken op meestal 30 tot 40 minuten in plaats van de 20 tot 30 minuten in de stad. Bij drukte op vrijdag- of zaterdagavond laten we het je direct weten als het langer wordt."""],
            ["""Kan ik laat op de avond nog bestellen in Zuidhorn?""", """Wij zijn zeven dagen per week bereikbaar via WhatsApp, ook 's avonds en 's nachts. Stuur je bericht, dan hoor je meteen of en hoe snel we in Zuidhorn kunnen zijn. Lees ook onze pagina over <a href="/lachgas-nachtbezorging/">bezorging 's avonds en 's nachts</a>."""],
        ],
        "nearby": ["leek", "vinkhuizen", "roden"],
        "lat": 53.247,
        "lon": 6.405,
    },
    {
        "slug": "eelde-paterswolde",
        "name": "Eelde-Paterswolde",
        "kind": "dorp",
        "title": """Lachgas Eelde-Paterswolde | Bezorgd via WhatsApp""",
        "description": """Lachgas bestellen in Eelde-Paterswolde? Snel en discreet bezorgd via WhatsApp rond de Hoofdweg, het Paterswoldsemeer en Spierveen. Tanks 2KG tot 10KG. 18+.""",
        "h1": """Lachgas Eelde-Paterswolde""",
        "lead": """Snel en discreet bezorgd in Eelde en Paterswolde, besteld via WhatsApp.""",
        "intro": [
            """Eelde-Paterswolde ligt direct onder Groningen, aan de zuidkant van de stad en net over de provinciegrens in Drenthe. Wij bezorgen in beide dorpskernen: langs de Hoofdweg die Eelde en Paterswolde met elkaar verbindt, rond de Burgemeester J.G. Legroweg, in de woonwijk Spierveen en in de straten tussen het Paterswoldsemeer en landgoed De Braak. Ook rond Groningen Airport Eelde en bij Vosbergen komen we langs.""",
            """Vanuit het centrum van Groningen is het een kwartier rijden: via de Paterswoldseweg en de Groningerweg, of over de A28 met de afslag richting Eelde. Daardoor halen we hier bijna dezelfde levertijd als in de stad zelf, meestal binnen 25 tot 35 minuten. Op zomerse avonden rond het meer of in het weekend kan het iets langer duren; dat hoor je direct via WhatsApp.""",
            """Veel inwoners van Eelde-Paterswolde werken of studeren in Groningen en ontvangen vrienden graag thuis, met wat meer ruimte dan in een stadsappartement. Voor een tuinfeest, een verjaardag of een avond na een dag aan het Paterswoldsemeer is de <a href="/product/lachgas-tank-2kg/">Lachgastank 2KG</a> het meest gekozen formaat. Voor een grotere groep adviseren we de <a href="/product/lachgas-tank-4kg/">4KG</a>. Stuur je adres en bestelling via WhatsApp, dan bevestigen we direct. Uitsluitend voor 18+.""",
        ],
        "wijken": """Hoofdweg, Burgemeester J.G. Legroweg, Spierveen, Paterswoldsemeer, De Braak, Vosbergen, Groningerweg, Hooiweg, Groningen Airport Eelde""",
        "levertijd": """meestal binnen 25 tot 35 minuten""",
        "faq": [
            ["""Bezorgen jullie zowel in Eelde als in Paterswolde?""", """Ja, de twee kernen zijn aan elkaar gegroeid en wij bezorgen in beide. Of je nu aan de Hoofdweg in Eelde woont of bij het meer in Paterswolde: stuur je adres via WhatsApp en wij komen langs."""],
            ["""Eelde-Paterswolde ligt in Drenthe. Maakt dat verschil voor de bezorging?""", """Nee. Het dorp grenst direct aan de stad en ligt op een kwartier rijden van het centrum van Groningen. We hanteren dezelfde werkwijze als in de stad: bestellen via WhatsApp, betalen bij aflevering en verkoop uitsluitend aan 18+."""],
            ["""Kunnen jullie bezorgen bij een adres aan het Paterswoldsemeer?""", """Zeker, zolang het een normaal bereikbaar adres is. Geef in je bericht duidelijk aan waar we moeten zijn, bijvoorbeeld een huisnummer of een herkenbaar punt, dan vindt onze bezorger je snel."""],
        ],
        "nearby": ["haren", "helpman", "assen"],
        "lat": 53.133,
        "lon": 6.562,
    },
    {
        "slug": "roden",
        "name": "Roden",
        "kind": "dorp",
        "title": """Lachgas Roden | Snel bezorgd via WhatsApp""",
        "description": """Lachgas bestellen in Roden? Snel en discreet bezorgd via WhatsApp rond de Brink, de Heerestraat en Roderveld. Lachgastanks 2KG, 4KG en 10KG. Alleen 18+.""",
        "h1": """Lachgas Roden""",
        "lead": """Snel en discreet bezorgd in Roden, besteld via WhatsApp.""",
        "intro": [
            """Roden is het grootste dorp van de gemeente Noordenveld en ligt zo'n achttien kilometer ten zuidwesten van Groningen, op de grens van Drenthe en het Groningse Westerkwartier. Wij bezorgen in heel Roden: rond de Brink en de Heerestraat in het centrum, in de woonwijken Roderveld en Middenveld, langs de Kanaalstraat en bij Havezate Mensinge. Ook Nieuw-Roden, Nietap en Leutingewolde vallen binnen ons gebied.""",
            """Onze bezorgers rijden vanuit de stad via Hoogkerk en Peize, of via de A7 en Leek, richting Roden. Reken op een levertijd van meestal 30 tot 40 minuten, afhankelijk van het moment en de drukte. Tijdens de Rodermarkt eind september en op zaterdagavonden kan het iets langer duren; we laten het je via WhatsApp weten zodra je bestelt.""",
            """Roden heeft een actief verenigingsleven en veel jonge huishoudens die voor werk of studie op Groningen zijn gericht. Voor een feestje thuis, een verjaardag of een avond met de vriendengroep is de <a href="/product/lachgas-tank-2kg/">Lachgastank 2KG</a> meestal genoeg; voor een groter gezelschap of een lange avond kies je de <a href="/product/lachgas-tank-4kg/">4KG</a>. Je appt ons je adres in Roden, wij bevestigen en komen langs. Verkoop uitsluitend aan 18+.""",
        ],
        "wijken": """Brink, Heerestraat, Kanaalstraat, Roderveld, Middenveld, Mensinge, Nieuw-Roden, Nietap, Leutingewolde""",
        "levertijd": """meestal binnen 30 tot 40 minuten""",
        "faq": [
            ["""Bezorgen jullie ook in Nieuw-Roden en Nietap?""", """Ja. Nieuw-Roden en Nietap liggen direct tegen Roden aan en horen bij ons bezorggebied, net als Leutingewolde. Vermeld in je WhatsApp-bericht altijd je volledige adres, dan plannen wij de snelste route."""],
            ["""Kan ik tijdens de Rodermarkt bestellen?""", """Dat kan, maar houd rekening met afgesloten straten en extra drukte in het centrum. Geef een adres op dat goed bereikbaar is en reken op een iets langere levertijd dan normaal. Wij geven je via WhatsApp een realistische inschatting."""],
            ["""Wat is de levertijd in Roden vergeleken met Leek?""", """Leek ligt iets dichter bij de A7, maar het verschil is klein: in Roden staan we meestal binnen 30 tot 40 minuten aan de deur. Bestel je vroeg op de avond, dan ben je doorgaans sneller aan de beurt dan rond middernacht in het weekend."""],
        ],
        "nearby": ["leek", "eelde-paterswolde", "zuidhorn"],
        "lat": 53.137,
        "lon": 6.422,
    },
    {
        "slug": "bedum",
        "name": "Bedum",
        "kind": "dorp",
        "title": """Lachgas Bedum | Snel bezorgd via WhatsApp""",
        "description": """Lachgas bestellen in Bedum? Snel en discreet bezorgd via WhatsApp rond de Grotestraat, het Boterdiep en Ter Laan. Tanks in 2KG, 4KG en 10KG. Alleen 18+.""",
        "h1": """Lachgas Bedum""",
        "lead": """Snel en discreet bezorgd in Bedum, besteld via WhatsApp.""",
        "intro": [
            """Bedum ligt een kleine twaalf kilometer ten noorden van Groningen en hoort sinds 2019 bij de gemeente Het Hogeland. Het dorp is bekend van de Walfriduskerk met zijn scheve toren, die verder uit het lood staat dan de toren van Pisa. Wij bezorgen in heel Bedum: rond de Grotestraat en het Boterdiep in het centrum, in de wijk Ter Laan, bij station Bedum en langs de Molenweg. Ook in Zuidwolde, Noordwolde en Onderdendam komen we langs.""",
            """Vanuit de stad rijden onze bezorgers via Zuidwolde langs het Boterdiep naar Bedum, een route van ongeveer een kwartier. Daardoor staan we hier meestal binnen 25 tot 35 minuten aan de deur. In het weekend en op drukke avonden in de stad kan het iets langer duren; je ontvangt via WhatsApp altijd een indicatie zodra je bestelt.""",
            """Bedum is een rustig forensendorp met veel gezinnen en jongeren die in de stad werken of studeren. Een verjaardag in de tuin, een avond met vrienden na het werk of een feestje in het weekend: met de <a href="/product/lachgas-tank-2kg/">Lachgastank 2KG</a> zit je meestal goed, voor een groter gezelschap is de <a href="/product/lachgas-tank-4kg/">4KG</a> een betere keuze. Stuur je bestelling en adres in Bedum via WhatsApp, dan bevestigen we direct. Alleen voor 18+.""",
        ],
        "wijken": """Grotestraat, Boterdiep, Ter Laan, Station Bedum, Molenweg, Walfriduskerk, Zuidwolde, Noordwolde, Onderdendam""",
        "levertijd": """meestal binnen 25 tot 35 minuten""",
        "faq": [
            ["""Bezorgen jullie ook in Zuidwolde en Onderdendam?""", """Ja. Zuidwolde ligt op de route tussen Groningen en Bedum en Onderdendam ligt er net boven; beide horen bij ons bezorggebied. Zet je volledige adres in je bericht, dan weten we precies waar we moeten zijn."""],
            ["""Hoe snel zijn jullie in Bedum?""", """Meestal binnen 25 tot 35 minuten. De route via Zuidwolde langs het Boterdiep is kort en overzichtelijk, dus Bedum is een van de snellere dorpen buiten de stad. Bij drukte hoor je dat direct via WhatsApp."""],
            ["""Kan ik in Bedum ook crackers en slagroompatronen bestellen?""", """Zeker. Naast de lachgastanks bezorgen we ook <a href="/product/lachgas-cracker/">lachgas crackers</a> en <a href="/product/slagroompatronen/">slagroompatronen</a> in Bedum en omgeving. Zet erbij wat je nodig hebt, dan nemen we het in dezelfde rit mee."""],
        ],
        "nearby": ["beijum", "ten-boer", "paddepoel"],
        "lat": 53.301,
        "lon": 6.603,
    },
    {
        "slug": "ten-boer",
        "name": "Ten Boer",
        "kind": "dorp",
        "title": """Lachgas Ten Boer | Snel bezorgd via WhatsApp""",
        "description": """Lachgas bestellen in Ten Boer? Snel en discreet bezorgd via WhatsApp rond het Koopmansplein, de Stadsweg en het Damsterdiep. Tanks 2KG tot 10KG. 18+.""",
        "h1": """Lachgas Ten Boer""",
        "lead": """Snel en discreet bezorgd in Ten Boer, besteld via WhatsApp.""",
        "intro": [
            """Ten Boer ligt ongeveer tien kilometer ten noordoosten van de stad, langs het Damsterdiep, en maakt sinds 2019 deel uit van de gemeente Groningen. Wij bezorgen in het hele dorp: rond het Koopmansplein en de Hendrik Westerstraat in het centrum, bij de Kloosterkerk aan de Kerkstraat, langs de Stadsweg en in de nieuwere woonstraten aan de rand van het dorp. Ook de omliggende dorpen Ten Post, Garmerwolde, Thesinge, Sint Annen en Woltersum vallen binnen ons bezorggebied.""",
            """Onze bezorgers rijden vanuit Groningen via het Damsterdiep (N360) rechtstreeks naar Ten Boer. Dat is een korte, overzichtelijke route, waardoor we hier meestal binnen 25 tot 35 minuten aan de deur staan. In het weekend en bij evenementen in de stad kan het iets langer duren; je ontvangt via WhatsApp altijd een indicatie zodra je bestelt.""",
            """Ten Boer is een dorp met een sterke gemeenschap en veel jonge gezinnen die de stad dichtbij willen hebben zonder er middenin te wonen. Voor een feestje in de schuur, een verjaardag of een avond met vrienden is de <a href="/product/lachgas-tank-2kg/">Lachgastank 2KG</a> het meest gekozen formaat. Komt er een grotere groep? Dan is de <a href="/product/lachgas-tank-4kg/">4KG</a> de logische stap. Stuur je adres in Ten Boer via WhatsApp en wij regelen de rest. Uitsluitend voor volwassenen van 18 jaar en ouder.""",
        ],
        "wijken": """Koopmansplein, Hendrik Westerstraat, Kerkstraat, Stadsweg, Damsterdiep, Ten Post, Garmerwolde, Thesinge, Woltersum""",
        "levertijd": """meestal binnen 25 tot 35 minuten""",
        "faq": [
            ["""Bezorgen jullie ook in Ten Post, Garmerwolde en Thesinge?""", """Ja. De dorpen rond Ten Boer, waaronder Ten Post, Garmerwolde, Thesinge, Sint Annen en Woltersum, horen bij ons bezorggebied. Vermeld je volledige adres in je WhatsApp-bericht, dan plannen wij de route."""],
            ["""Hoort Ten Boer bij jullie stadsbezorging of bij de dorpen?""", """Ten Boer is sinds 2019 onderdeel van de gemeente Groningen, maar ligt wel een stuk buiten de stad. Reken daarom op meestal 25 tot 35 minuten in plaats van de 20 tot 30 minuten in de stadswijken. Verder is de werkwijze precies hetzelfde."""],
            ["""Kan ik bestellen voor een feest in een schuur of op een erf buiten het dorp?""", """Ja, zolang het adres met de auto bereikbaar is. Geef in je bericht een duidelijke omschrijving van de locatie en een telefoonnummer dat bereikbaar is, dan vindt onze bezorger je. Voor grotere feesten lees je ook onze pagina over <a href="/lachgas-feest-evenement/">lachgas voor feesten en evenementen</a>."""],
        ],
        "nearby": ["beijum", "bedum", "korrewegwijk"],
        "lat": 53.278,
        "lon": 6.692,
    },
    {
        "slug": "selwerd",
        "name": "Selwerd",
        "kind": "wijk",
        "title": """Lachgas Selwerd & Zernike | Bezorgd via WhatsApp""",
        "description": """Lachgas bestellen in Selwerd of op Zernike? Snel en discreet bezorgd via WhatsApp rond de Eikenlaan, Park Selwerd en de Zernike Campus. Alleen voor 18+.""",
        "h1": """Lachgas Selwerd""",
        "lead": """Snel en discreet bezorgd in Selwerd en op Zernike, besteld via WhatsApp.""",
        "intro": [
            """Selwerd ligt in het noordwesten van Groningen, ingeklemd tussen Paddepoel, de Korrewegwijk en de Zernike Campus. De wijk is herkenbaar aan de straten met boomnamen: Eikenlaan, Iepenlaan, Berkenlaan, Elzenlaan en Esdoornlaan, met daartussen Park Selwerd. Wij bezorgen in heel Selwerd, van de flats langs de Eikenlaan tot de studentenhuisvesting op Zernike aan de Zernikelaan en de rand van het Reitdiep.""",
            """Vanuit het centrum is het nog geen tien minuten rijden via de Bedumerweg of de Eikenlaan, en Zernike is via de Zonnelaan snel bereikbaar. Daardoor hoort Selwerd bij onze snelste gebieden: meestal staan we binnen 20 tot 30 minuten voor je deur, ook op drukke donderdag- en vrijdagavonden, wanneer veel studenten na het uitgaan thuis verder feesten.""",
            """Selwerd is een echte studentenwijk, met veel kamers, studio's en de grote wooncomplexen op de campus. Voor een huisfeest, een borrel met huisgenoten of een verjaardag in de gezamenlijke keuken is de <a href="/product/lachgas-tank-2kg/">Lachgastank 2KG</a> het meest gekozen formaat; met een vol huis of een grotere groep is de <a href="/product/lachgas-tank-4kg/">4KG</a> handiger. Stuur je adres in Selwerd of op Zernike via WhatsApp en wij bevestigen direct. Verkoop uitsluitend aan 18+.""",
        ],
        "wijken": """Eikenlaan, Iepenlaan, Berkenlaan, Elzenlaan, Esdoornlaan, Park Selwerd, Zernike Campus, Zernikelaan, Selwerderhof""",
        "levertijd": """meestal binnen 20 tot 30 minuten""",
        "faq": [
            ["""Bezorgen jullie ook op de Zernike Campus?""", """Ja. De studentenhuisvesting op Zernike hoort bij ons bezorggebied. Geef in je WhatsApp-bericht het gebouw, het huisnummer en eventueel de ingang door, dan staat onze bezorger op de juiste plek. Bij een gedeelde ingang kun je het beste zelf naar beneden komen."""],
            ["""Ik woon in een flat aan de Eikenlaan. Hoe werkt de aflevering?""", """Onze bezorger belt of appt zodra hij voor de flat staat. Je komt naar beneden of laat hem binnen, de aflevering is discreet en onopvallend. Betalen doe je bij aflevering, contant of via Tikkie in overleg."""],
            ["""Hoe snel zijn jullie in Selwerd?""", """Selwerd ligt dicht bij het centrum en is goed bereikbaar, dus meestal staan we binnen 20 tot 30 minuten voor je deur. Op donderdag- en vrijdagavond kan het druk zijn; je krijgt via WhatsApp altijd een realistische indicatie zodra je bestelt."""],
        ],
        "nearby": ["paddepoel", "vinkhuizen", "korrewegwijk"],
        "lat": 53.2335,
        "lon": 6.545,
    },
]

# ---------------------------------------------------------------------------
# Informatie-artikelen
# ---------------------------------------------------------------------------

ARTICLES = [
    {
        "slug": "lachgas-en-vitamine-b12",
        "label": "Gezondheid",
        "title": """Lachgas en vitamine B12: risico's en klachten""",
        "description": """Lachgas maakt vitamine B12 in je lichaam onwerkzaam. Lees welke klachten dat geeft, wie extra risico loopt en wanneer je naar de huisarts moet.""",
        "h1": """Lachgas en vitamine B12""",
        "lead": """Lachgas en vitamine B12 zijn direct met elkaar verbonden: het gas schakelt de vitamine in je lichaam uit. Wat dat betekent, welke klachten erbij horen en wanneer je hulp moet zoeken, lees je hier.""",
        "sections": [
            {
                "h2": """Wat vitamine B12 doet in je lichaam""",
                "paragraphs": [
                    """Vitamine B12 is onmisbaar voor je zenuwstelsel en voor de aanmaak van rode bloedcellen. De vitamine helpt bij het onderhouden van de beschermlaag rond je zenuwen, de zogeheten myelineschede, en speelt een rol bij de omzetting van stoffen die je lichaam nodig heeft om cellen te laten delen. Zonder goed werkend B12 raken je zenuwen langzaam beschadigd en kun je bloedarmoede ontwikkelen.""",
                    """Je lichaam maakt B12 niet zelf aan. Je krijgt de vitamine binnen via dierlijke producten zoals vlees, vis, eieren en melk, of via supplementen en verrijkte voeding. Je lever houdt een voorraad aan die normaal lang volstaat, en juist dat maakt lachgas verraderlijk: er is op papier genoeg B12, maar het werkt niet meer.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Hoe lachgas vitamine B12 onwerkzaam maakt""",
                "paragraphs": [
                    """Lachgas, oftewel distikstofmonoxide (N2O), reageert met het kobaltatoom in het midden van het B12-molecuul. Door die reactie verandert de vitamine van een actieve in een inactieve vorm. Het B12 is dan nog wel in je bloed aanwezig, maar je lichaam kan er niets meer mee. Daarom spreken artsen van een <strong>functioneel B12-tekort</strong>: niet de hoeveelheid is het probleem, maar de werking.""",
                    """Dit is geen theorie: neurologen in Nederland zien de afgelopen jaren steeds meer jonge mensen met zenuwschade na veelvuldig gebruik. Bij een enkele ballon herstelt de B12-werking zich meestal snel. Bij regelmatig gebruik, en zeker bij grote hoeveelheden achter elkaar, krijgt je lichaam die kans niet en loopt de schade op.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Welke klachten kunnen ontstaan""",
                "paragraphs": [
                    """Klachten van een B12-tekort door lachgas ontstaan sluipend. Veel gebruikers merken eerst iets in handen en voeten en denken dat het wegtrekt. Juist dan moet je stoppen en hulp zoeken: hoe langer je wacht, hoe groter de kans op blijvende schade. Let op de volgende signalen:""",
                ],
                "bullets": [
                    """<strong>Tintelingen.</strong> Een prikkelend of elektrisch gevoel in vingers, handen, tenen of voeten, vaak aan beide kanten tegelijk.""",
                    """<strong>Gevoelloosheid.</strong> Een doof gevoel in de huid, alsof je door een dikke laag watten voelt. Soms begint het aan de voeten en kruipt het omhoog.""",
                    """<strong>Spierzwakte.</strong> Minder kracht in armen of benen, moeite met trappen lopen of met kleine handelingen zoals knopen dichtdoen.""",
                    """<strong>Loopproblemen.</strong> Onzeker lopen, evenwichtsproblemen of struikelen, vooral in het donker wanneer je ogen de zenuwen niet kunnen corrigeren.""",
                    """<strong>Overige klachten.</strong> Vermoeidheid, concentratieproblemen, een sombere stemming, geheugenproblemen en in ernstige gevallen problemen met plassen.""",
                ],
            },
            {
                "h2": """Wie loopt extra risico""",
                "paragraphs": [
                    """Iedereen die lachgas gebruikt, kan een functioneel B12-tekort krijgen. Hoe kleiner je reserve en hoe vaker je gebruikt, hoe sneller het misgaat. De volgende groepen moeten extra voorzichtig zijn, of lachgas beter helemaal laten staan:""",
                ],
                "bullets": [
                    """<strong>Frequente gebruikers.</strong> Wie wekelijks of vaker gebruikt, of in een sessie tientallen ballonnen neemt, geeft het lichaam geen tijd om te herstellen. Dit is veruit de belangrijkste risicofactor.""",
                    """<strong>Vegetariërs en veganisten.</strong> Zonder dierlijke producten is de B12-inname vaak laag en de voorraad kleiner, waardoor de klachten eerder optreden.""",
                    """<strong>Zwangere vrouwen.</strong> Lachgas kan de B12-huishouding van zowel moeder als kind verstoren. Tijdens zwangerschap en bij een kinderwens is lachgas af te raden.""",
                    """<strong>Mensen met bepaalde medicijnen of aandoeningen.</strong> Maagzuurremmers, metformine en darmaandoeningen zoals de ziekte van Crohn verlagen de opname van B12. Twijfel je of dit voor jou geldt, overleg dan met je huisarts of apotheker.""",
                ],
            },
            {
                "h2": """Helpt extra vitamine B12 slikken?""",
                "paragraphs": [
                    """Een veelgehoord idee is dat B12-tabletten of een injectie het risico wegnemen. Dat klopt niet. Lachgas maakt ook het nieuw ingenomen B12 onwerkzaam, dus zolang je blijft gebruiken, blijft het probleem bestaan. Supplementen kunnen hoogstens de voorraad aanvullen voor het moment dat je stopt; ze beschermen je niet tijdens het gebruik.""",
                    """Bovendien geeft het een vals gevoel van veiligheid: je bloedwaarden lijken normaal, terwijl de schade aan je zenuwen doorgaat. De enige manier om het risico echt te beperken is minder of niet gebruiken. Bij klachten is behandeling met B12 onder begeleiding van een arts wel zinvol, maar alleen in combinatie met volledig stoppen.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Wanneer naar de huisarts en wanneer 112""",
                "paragraphs": [
                    """Neem klachten na lachgasgebruik altijd serieus. Zenuwschade door een B12-tekort is in een vroeg stadium vaak goed te behandelen, maar kan blijvend worden als je te lang wacht. Vertel je huisarts eerlijk hoeveel en hoe vaak je gebruikt, zodat de juiste onderzoeken worden gedaan.""",
                ],
                "bullets": [
                    """<strong>Maak een afspraak met je huisarts</strong> bij tintelingen, gevoelloosheid, krachtverlies of onzeker lopen, ook als de klachten mild zijn of af en toe wegtrekken.""",
                    """<strong>Bel 112</strong> als iemand na gebruik niet meer kan staan of lopen, plotseling uitval heeft in armen of benen, bewusteloos raakt of ernstige ademhalingsproblemen heeft.""",
                    """<strong>Wees open.</strong> Zorgverleners zijn er om te helpen, niet om te oordelen; informatie over je gebruik maakt de behandeling sneller en beter.""",
                ],
            },
            {
                "h2": """Het risico beperken""",
                "paragraphs": [
                    """Wij verkopen lachgas uitsluitend aan volwassenen en willen dat je weet waar je aan begint. Gebruik met mate, houd lange pauzes tussen momenten van gebruik en stop direct bij de eerste signalen die hierboven staan. Meer praktische tips vind je op onze pagina over <a href="/lachgas-informatie/veilig-gebruik/">veilig gebruik van lachgas</a>, en onafhankelijke informatie bij <a href="https://www.drugsinfo.nl">Drugsinfo van het Trimbos-instituut</a>.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Deze informatie is bedoeld om risico's te beperken, niet om gebruik aan te moedigen, en vervangt geen medisch advies. Heb je tintelingen, gevoelloosheid of loopproblemen na lachgasgebruik, neem dan contact op met je huisarts. Bel bij acute uitval of bewusteloosheid altijd 112.""",
        "related": ["veilig-gebruik", "wat-is-lachgas", "lachgas-in-het-verkeer"],
    },
    {
        "slug": "lachgas-tank-bewaren-en-vervoeren",
        "label": "Praktisch",
        "title": """Lachgastank bewaren en vervoeren: zo doe je dat veilig""",
        "description": """Hoe bewaar en vervoer je een lachgastank veilig? Rechtop, koel, uit de zon, kraan dicht en vastgezet in de auto. Praktische tips van Lachgas Groningen.""",
        "h1": """Lachgastank bewaren en vervoeren""",
        "lead": """Een lachgastank staat onder hoge druk en vraagt daarom om een beetje zorg, thuis en onderweg. Met deze praktische regels bewaar en vervoer je je tank veilig.""",
        "sections": [
            {
                "h2": """Waarom zorgvuldig bewaren belangrijk is""",
                "paragraphs": [
                    """In een lachgastank zit distikstofmonoxide onder hoge druk, deels in vloeibare vorm. Die druk stijgt mee met de temperatuur: hoe warmer de tank, hoe hoger de druk binnenin. Een tank is daarop berekend, maar extreme hitte, vallen of een beschadigde kraan vergroten de kans op lekkage. Vrijkomend lachgas is extreem koud en kan bevriezingsletsel veroorzaken.""",
                    """Daarnaast is het gas zwaarder dan lucht en verdringt het zuurstof. In een kleine afgesloten ruimte kan een lekkende tank daarom gevaarlijk zijn, ook zonder dat je het merkt: lachgas ruik je nauwelijks.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Thuis bewaren: rechtop, koel en droog""",
                "paragraphs": [
                    """Zet de tank altijd <strong>rechtop</strong> op een vlakke, stabiele ondergrond waar hij niet kan omvallen. Ligt een tank op zijn kant, dan kan er vloeibaar gas bij de kraan komen. Bewaar hem <strong>koel</strong>, bij kamertemperatuur of lager, en zeker niet boven de 50 graden. Kies een <strong>droge</strong> plek, zodat de kraan en de aansluiting niet gaan roesten.""",
                    """Geschikte plekken zijn een bijkeuken, een kast in de gang of een berging zonder verwarming. Ongeschikt zijn de buurt van een kachel, cv-ketel of oven en een vensterbank in de zon. Zorg voor wat ventilatie. Houd de tank ook uit de buurt van open vuur, kaarsen en sigaretten: lachgas is zelf niet brandbaar, maar het onderhoudt verbranding wel.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Niet in de zon en niet in een warme auto""",
                "paragraphs": [
                    """De grootste fout die we zien is een tank die na een feestje in de auto blijft staan. Op een zonnige dag loopt de temperatuur in een geparkeerde auto snel op tot boven de 50 graden, met een flinke drukstijging als gevolg. Datzelfde geldt voor een tank in de volle zon op een balkon of in de tuin. Haal de tank dus altijd direct uit de auto en zet hem binnen op een koele plek.""",
                    """Komt een koude tank uit de kofferbak een warme kamer in, laat hem dan rustig op kamertemperatuur komen voordat je hem gebruikt; snelle temperatuurwisselingen belasten de kraan en de afdichting onnodig.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Kinderen, huisgenoten en de kraan""",
                "paragraphs": [
                    """Bewaar de tank <strong>buiten het bereik van kinderen</strong>, het liefst in een afgesloten kast of ruimte. Een tank ziet er voor een kind uit als iets om mee te spelen, en een geopende kraan kan ernstig letsel geven. Vertel ook huisgenoten wat er in de kast staat, zodat niemand er per ongeluk tegenaan loopt.""",
                    """Draai de <strong>kraan altijd volledig dicht</strong> na gebruik, ook als je denkt dat de tank leeg is. Controleer of er geen sissend geluid hoorbaar is. Forceer nooit iets met gereedschap. Onze tanks worden verzegeld geleverd; vertrouw je de kraan of de verzegeling niet, gebruik de tank dan niet en neem contact met ons op via WhatsApp.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Een lachgastank vervoeren in de auto""",
                "paragraphs": [
                    """Moet je een tank meenemen naar een ander adres, bijvoorbeeld van je huis naar een feestlocatie, dan geldt allereerst: <strong>vervoer alleen nuchter</strong>. Wie lachgas, alcohol of andere middelen heeft gebruikt, hoort niet achter het stuur. Lees daarover onze pagina <a href="/lachgas-informatie/lachgas-in-het-verkeer/">lachgas in het verkeer</a>. Gebruik de tank nooit in de auto, ook niet als passagier: de ruimte is klein en slecht geventileerd.""",
                ],
                "bullets": [
                    """<strong>Zet de tank vast.</strong> Rechtop in de kofferbak, geklemd tussen bagage of met een spanband, zodat hij bij remmen niet kan rollen of omvallen.""",
                    """<strong>Kraan dicht en beschermd.</strong> Controleer voor vertrek of de kraan goed dicht is en of er niets tegen de kraan aan kan stoten.""",
                    """<strong>Ventileer.</strong> Zet een raam op een kier en laat de tank niet onnodig lang in een geparkeerde auto staan, zeker niet bij warm weer.""",
                    """<strong>Houd het kort.</strong> Rij rechtstreeks van A naar B. Een tank is geen bagage om een dag mee rond te rijden.""",
                    """<strong>Laat ons bezorgen.</strong> De eenvoudigste oplossing is om de tank direct op het feestadres te laten bezorgen. Dan hoef je zelf niets te vervoeren.""",
                ],
            },
            {
                "h2": """Wat doe je met een lege tank?""",
                "paragraphs": [
                    """Een lege lachgastank hoort <strong>niet bij het huisvuil</strong> en zeker niet in de glasbak of de ondergrondse container. Het is een stalen drukhouder die apart verwerkt moet worden. Neem contact met ons op via WhatsApp: in overleg halen wij tanks op, zoals we dat ook doen bij de <a href="/product/lachgas-tank-10kg/">Lachgastank 10KG</a>. Je kunt een lege tank ook inleveren bij het afvalbrengstation van je gemeente, bij het metaal of de gasflessen.""",
                    """Tot het moment van ophalen of inleveren bewaar je de lege tank precies zoals een volle: rechtop, koel, kraan dicht en buiten het bereik van kinderen. Een tank die leeg lijkt, kan nog restdruk bevatten.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Checklist in één oogopslag""",
                "paragraphs": [
                    """Loop deze punten na voordat je de tank wegzet of meeneemt. Meer tips over verantwoord gebruik vind je op onze pagina <a href="/lachgas-informatie/veilig-gebruik/">veilig gebruik van lachgas</a>.""",
                ],
                "bullets": [
                    """<strong>Rechtop</strong> op een stabiele ondergrond, niet liggend.""",
                    """<strong>Koel en droog</strong>, uit de zon, niet bij een kachel of ketel.""",
                    """<strong>Nooit achterlaten</strong> in een geparkeerde auto.""",
                    """<strong>Kraan dicht</strong> na elk gebruik, verzegeling en aansluiting intact.""",
                    """<strong>Buiten bereik</strong> van kinderen en onwetende huisgenoten.""",
                    """<strong>Vervoer nuchter</strong>, vastgezet en rechtop, zonder gebruik in de auto.""",
                    """<strong>Lege tank</strong> niet bij het huisvuil: laat ophalen of lever in bij het afvalbrengstation.""",
                ],
            },
        ],
        "note": """Deze tips beperken risico's en vervangen geen officiële veiligheidsinstructies. Komt er onverhoopt gas vrij in een afgesloten ruimte, ventileer dan direct en ga naar buiten. Bel bij bevriezingsletsel, benauwdheid of bewusteloosheid altijd 112.""",
        "related": ["veilig-gebruik", "welke-lachgastank-heb-ik-nodig", "lachgas-in-het-verkeer"],
    },
    {
        "slug": "welke-lachgastank-heb-ik-nodig",
        "label": "Assortiment",
        "title": """Welke lachgastank heb ik nodig? 2KG, 4KG of 10KG""",
        "description": """Twijfel je tussen een lachgastank van 2KG, 4KG of 10KG? Deze keuzehulp helpt je kiezen op basis van groepsgrootte en gelegenheid. Bezorgd in Groningen.""",
        "h1": """Welke lachgastank heb ik nodig?""",
        "lead": """Een 2KG, 4KG of toch een 10KG lachgastank? Met deze keuzehulp weet je binnen een minuut welk formaat past bij je groep en je gelegenheid.""",
        "sections": [
            {
                "h2": """Waar hangt de keuze van af?""",
                "paragraphs": [
                    """De juiste tank kies je op basis van drie dingen: hoeveel mensen er zijn, hoe lang de avond duurt en wat voor gelegenheid het is. Een rustige avond met vier vrienden vraagt iets anders dan een huisfeest met veertig gasten of een evenement met horeca. Te klein kiezen betekent bijbestellen en wachten; te groot kiezen betekent dat je met een halfvolle tank blijft zitten.""",
                    """Houd ook rekening met verantwoord gebruik. Een grotere tank is geen uitnodiging om meer te gebruiken. Wij adviseren altijd om met mate te gebruiken, pauzes te nemen en de tips op onze pagina <a href="/lachgas-informatie/veilig-gebruik/">veilig gebruik</a> te volgen. De richtlijnen hieronder gaan uit van een gezelschap dat verspreid over een avond gebruikt, niet van intensief gebruik door enkele personen.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Lachgastank 2KG: het standaardformaat""",
                "paragraphs": [
                    """De <a href="/product/lachgas-tank-2kg/">Lachgastank 2KG</a> is ons meest bestelde product en voor de meeste situaties de beste keuze. De tank bevat 2KG zuiver N2O, goed voor ongeveer 250 ballonnen, en past prima bij een groep van ongeveer 10 tot 15 personen voor een avond. De tank is compact, makkelijk neer te zetten in een woonkamer of studentenhuis en snel bezorgd in Groningen en omgeving.""",
                    """Kies de 2KG voor een avond met vrienden, een verjaardag thuis, een borrel met huisgenoten of een kleine afterparty. Twijfel je tussen de 2KG en de 4KG bij een groep rond de 15 personen? Dan is de 2KG meestal genoeg, zeker als niet iedereen gebruikt.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Lachgastank 4KG: voor een groter feestje""",
                "paragraphs": [
                    """De <a href="/product/lachgas-tank-4kg/">Lachgastank 4KG</a> bevat het dubbele van de 2KG en is bedoeld voor een groter gezelschap of een langere avond. Denk aan een huisfeest met 20 tot 30 gasten, een verjaardag waar veel mensen op afkomen, of een avond die van de vroege borrel tot diep in de nacht doorloopt. Met de 4KG hoef je tussendoor niet bij te bestellen en te wachten op een tweede bezorging.""",
                    """De 4KG is ook een praktische keuze als je een feest op een dorpsadres buiten de stad organiseert, bijvoorbeeld in Zuidhorn, Roden of Ten Boer, waar bijbestellen door de langere rijtijd minder handig is. Eén bezorging, één tank, klaar.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Lachgastank 10KG: evenementen en horeca""",
                "paragraphs": [
                    """De <a href="/product/lachgas-tank-10kg/">Lachgastank 10KG</a> is bedoeld voor grote evenementen, studentenverenigingen en horeca. Dit formaat leveren we op aanvraag en in overleg: we stemmen vooraf de levering af en halen de tank na afloop weer op. Een 10KG tank is groot en zwaar, dus zorg voor een vaste, stabiele plek waar hij rechtop kan staan en niemand eroverheen struikelt.""",
                    """Voor een gewoon huisfeest is de 10KG overbodig. Kies dit formaat alleen als je echt een grote groep verwacht, bijvoorbeeld bij een verenigingsfeest, een afstudeerborrel met de hele jaargroep of een besloten evenement. Neem ruim van tevoren contact op via WhatsApp, dan bespreken we de mogelijkheden. Lees ook onze pagina over <a href="/lachgas-feest-evenement/">lachgas voor feesten en evenementen</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Crackers en slagroompatronen""",
                "paragraphs": [
                    """Niet iedereen heeft een tank nodig. Voor een heel klein gezelschap of voor wie flexibel wil blijven, zijn <a href="/product/slagroompatronen/">slagroompatronen</a> in combinatie met een <a href="/product/lachgas-cracker/">lachgas cracker</a> een alternatief. Een cracker is herbruikbaar en opent de patronen één voor één, zodat je precies zoveel gebruikt als je wilt. Patronen bestel je per doosje of in grotere aantallen voor horeca en slagroomspuiten.""",
                    """Het nadeel: per ballon ben je meer tijd kwijt en bij een groep van meer dan een handvol mensen loopt het aantal patronen snel op. Vanaf ongeveer acht tot tien personen is een 2KG tank praktischer. Hoe een cracker precies werkt, lees je op <a href="/lachgas-informatie/hoe-werkt-een-lachgas-cracker/">hoe werkt een lachgas cracker</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Keuzehulp in één oogopslag""",
                "paragraphs": [
                    """Hieronder de vuistregels op een rij. Twijfel je nog, stuur dan via WhatsApp een bericht met het aantal personen en de gelegenheid; wij denken graag mee.""",
                ],
                "bullets": [
                    """<strong>Tot ongeveer 8 personen, af en toe een ballon.</strong> Slagroompatronen met een cracker, of een 2KG tank als je het gemak van een tank wilt.""",
                    """<strong>10 tot 15 personen, één avond.</strong> Lachgastank 2KG, ons standaardformaat met ongeveer 250 ballonnen.""",
                    """<strong>20 tot 30 personen of een lange nacht.</strong> Lachgastank 4KG, zodat je niet hoeft bij te bestellen.""",
                    """<strong>Groot evenement, vereniging of horeca.</strong> Lachgastank 10KG, op aanvraag en in overleg over levering en ophaling.""",
                    """<strong>Feest buiten de stad.</strong> Kies eerder een maat groter; bijbestellen duurt op een dorpsadres langer.""",
                ],
            },
            {
                "h2": """Bestellen via WhatsApp""",
                "paragraphs": [
                    """Heb je je keuze gemaakt? Stuur ons een WhatsApp-bericht met het formaat, het aantal tanks, je adres en het gewenste tijdstip. Wij bevestigen direct en bezorgen in Groningen meestal binnen 20 tot 30 minuten; in de omliggende dorpen duurt het iets langer. Je betaalt bij aflevering, contant of via Tikkie in overleg. Alle tanks worden verzegeld geleverd en we verkopen uitsluitend aan personen van 18 jaar en ouder.""",
                ],
                "bullets": [],
            },
        ],
        "note": """De aantallen in deze keuzehulp zijn richtlijnen voor een gezelschap dat verspreid over een avond gebruikt, niet een advies om meer te gebruiken. Gebruik met mate, combineer lachgas nooit met alcohol of andere middelen en raadpleeg bij klachten je huisarts. Bel in geval van nood 112.""",
        "related": ["veilig-gebruik", "hoe-werkt-een-lachgas-cracker", "lachgas-tank-bewaren-en-vervoeren"],
    },
]

# ---------------------------------------------------------------------------
# Servicepagina's (root van de site)
# ---------------------------------------------------------------------------

SERVICE_PAGES = [
    {
        "slug": "lachgas-nachtbezorging",
        "label": """'s Avonds en 's nachts""",
        "title": """Lachgas 's nachts bestellen in Groningen | WhatsApp""",
        "description": """Lachgas 's avonds of 's nachts bestellen in Groningen? Wij zijn 24/7 bereikbaar via WhatsApp en bezorgen discreet aan de deur, ook na middernacht. 18+.""",
        "h1": """Lachgas 's avonds en 's nachts bestellen in Groningen""",
        "lead": """Het feest loopt uit, de voorraad is op of het plan ontstaat pas na middernacht. Wij zijn 24/7 bereikbaar via WhatsApp en bezorgen ook 's avonds en 's nachts in Groningen en omgeving.""",
        "sections": [
            {
                "h2": """Zo werkt bestellen in de avond en nacht""",
                "paragraphs": [
                    """Bestellen gaat 's nachts precies zoals overdag: je stuurt een WhatsApp-bericht met wat je wilt bestellen en je adres, wij bevestigen en geven een realistische indicatie van de levertijd. In de stad staan we meestal binnen 20 tot 30 minuten voor de deur. Na middernacht in het weekend, als veel bestellingen tegelijk binnenkomen, kan het iets langer duren. Je hoort dat vooraf, zodat je niet voor niets zit te wachten.""",
                    """Betalen doe je bij aflevering, contant of via Tikkie in overleg. Zorg dat je telefoon aanstaat en dat iemand de deur kan openen: onze bezorger belt of appt zodra hij er is. De aflevering is discreet en onopvallend, ook midden in de nacht in een straat vol buren.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Rond de Grote Markt, Poelestraat en Vismarkt""",
                "paragraphs": [
                    """Het uitgaansleven van Groningen speelt zich af in een compact gebied: de Grote Markt, de Poelestraat, de Peperstraat, de Vismarkt en de straten daaromheen. Wij bezorgen niet in de kroeg of op straat, maar wel op het woonadres waar de avond verdergaat. Dat kan een appartement boven een winkel in de <a href="/bezorggebied/binnenstad/">Binnenstad</a> zijn, een studentenhuis in de <a href="/bezorggebied/korrewegwijk/">Korrewegwijk</a> of een huis in de <a href="/bezorggebied/oosterpoort/">Oosterpoort</a>.""",
                    """Bestel je vanuit de binnenstad, geef dan duidelijk je straat, huisnummer en eventueel de bel of ingang door. In de smalle straten rond de Poelestraat kan onze bezorger niet altijd voor de deur parkeren; kom even naar beneden als hij belt, dan is het binnen een minuut geregeld.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Studentenstad: van huisfeest tot afterparty""",
                "paragraphs": [
                    """Groningen is een studentenstad en dat merken we aan onze avonden. Donderdag is traditioneel de drukste uitgaansavond, en na sluitingstijd verplaatst het feest zich naar studentenhuizen in <a href="/bezorggebied/selwerd/">Selwerd</a>, <a href="/bezorggebied/paddepoel/">Paddepoel</a>, de Korrewegwijk en op Zernike. Wij bezorgen daar 's nachts net zo goed als overdag.""",
                    """Een praktische tip: bestel voordat de voorraad op is, niet erna. Een bericht om elf uur wordt doorgaans sneller afgehandeld dan een bericht om half drie, en je voorkomt dat het feest stilvalt. Wil je zeker weten dat je genoeg hebt, lees dan onze keuzehulp <a href="/lachgas-informatie/welke-lachgastank-heb-ik-nodig/">welke lachgastank heb ik nodig</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Vrijdag, zaterdag en de rest van de week""",
                "paragraphs": [
                    """In het weekend zijn we het drukst tussen ongeveer tien uur 's avonds en drie uur 's nachts. Dan rijden er meerdere bezorgers, maar kan de levertijd oplopen tot boven de 30 minuten, vooral voor adressen buiten de stad zoals <a href="/bezorggebied/haren/">Haren</a>, <a href="/bezorggebied/hoogezand/">Hoogezand</a> of <a href="/bezorggebied/zuidhorn/">Zuidhorn</a>. Door de week is het rustiger en zijn we meestal sneller ter plaatse.""",
                    """Wij zijn zeven dagen per week bereikbaar via WhatsApp. Krijg je even geen antwoord, dan zijn we onderweg; je bericht wordt altijd beantwoord in de volgorde van binnenkomst.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Wat je doorgeeft in je bericht""",
                "paragraphs": [
                    """Een compleet bericht bespaart heen-en-weer appen en maakt de bezorging sneller. Zet dit erin:""",
                ],
                "bullets": [
                    """<strong>Je bestelling.</strong> Welk formaat tank (2KG, 4KG of 10KG), het aantal, en eventueel crackers of slagroompatronen.""",
                    """<strong>Je volledige adres.</strong> Straat, huisnummer, toevoeging en bij flats of studentencomplexen de ingang of verdieping.""",
                    """<strong>Een bereikbaar nummer.</strong> Het nummer waarmee je appt is prima, zolang je telefoon aanstaat en niet op stil.""",
                    """<strong>Bijzonderheden.</strong> Afgesloten straat, geen bel, achteringang: alles wat onze bezorger helpt om je snel te vinden.""",
                    """<strong>Je leeftijd.</strong> We leveren uitsluitend aan 18+ en kunnen bij aflevering om een identiteitsbewijs vragen.""",
                ],
            },
            {
                "h2": """Verantwoord gebruik na een avond uit""",
                "paragraphs": [
                    """Na een avond in de stad is de kans groot dat er alcohol is gedronken. Lachgas en alcohol zijn geen goede combinatie: de kans op duizeligheid, misselijkheid, vallen en bewustzijnsverlies neemt sterk toe. Heb je flink gedronken, dan is het verstandig om lachgas te laten staan. Gebruik anders met mate, zittend, in een geventileerde ruimte en met voldoende pauzes. Alle tips staan op onze pagina <a href="/lachgas-informatie/veilig-gebruik/">veilig gebruik van lachgas</a>.""",
                    """Ga na gebruik nooit zelf de weg op, ook niet op de fiets. Rijden onder invloed van lachgas is verboden en gevaarlijk. Lees waarom op <a href="/lachgas-informatie/lachgas-in-het-verkeer/">lachgas in het verkeer</a>. Laat de tank na het feest rechtop en met de kraan dicht staan, buiten het bereik van kinderen en niet in de auto.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Wij bezorgen 's avonds en 's nachts aan volwassenen die bewust kiezen en verantwoord gebruiken. Voel je je na gebruik onwel, raak je in paniek of heeft iemand in je gezelschap uitval of ademhalingsproblemen, bel dan direct 112. Onafhankelijke informatie vind je bij <a href="https://www.drugsinfo.nl">Drugsinfo</a>.""",
        "faq": [
            ["""Tot hoe laat kan ik 's nachts bestellen?""", """Wij zijn 24/7 bereikbaar via WhatsApp, dus je kunt op elk moment een bericht sturen. Na middernacht in het weekend kan de levertijd iets oplopen; we laten je altijd vooraf weten hoe snel we er kunnen zijn."""],
            ["""Bezorgen jullie in het uitgaansgebied zelf?""", """Nee, wij bezorgen alleen op woonadressen en privélocaties, niet op straat, voor de kroeg of op de Grote Markt. Geef het adres door waar het feest verdergaat, dan komen we daar langs."""],
            ["""Is bezorging 's nachts duurder dan overdag?""", """Onze prijzen krijg je op aanvraag via WhatsApp; vraag gerust naar het tarief voor jouw bestelling en tijdstip. Je betaalt altijd pas bij aflevering, contant of via Tikkie in overleg."""],
        ],
        "related": ["veilig-gebruik", "lachgas-in-het-verkeer"],
    },
    {
        "slug": "lachgas-feest-evenement",
        "label": "Feest & evenement",
        "title": """Lachgas voor feesten en evenementen in Groningen""",
        "description": """Lachgas voor een huisfeest, verjaardag, verenigingsfeest of evenement in Groningen? Tanks van 2KG tot 10KG, besteld via WhatsApp en discreet bezorgd. 18+.""",
        "h1": """Lachgas voor feesten en evenementen in Groningen""",
        "lead": """Van een verjaardag in de woonkamer tot een verenigingsfeest met honderden gasten: wij leveren het juiste formaat lachgastank op het juiste moment, overal in Groningen en omgeving.""",
        "sections": [
            {
                "h2": """Huisfeest in de stad""",
                "paragraphs": [
                    """Het klassieke Groningse huisfeest: een woonkamer in de Oosterpoort of Korrewegwijk, een speaker, een volle koelkast en twintig tot dertig mensen die in en uit lopen. Voor deze gelegenheid is de <a href="/product/lachgas-tank-4kg/">Lachgastank 4KG</a> meestal de beste keuze; bij een kleiner gezelschap volstaat de <a href="/product/lachgas-tank-2kg/">2KG</a>. Zet de tank op een vaste plek waar hij rechtop kan staan, uit de loop en weg van de dansvloer.""",
                    """Bestel bij voorkeur voordat de eerste gasten binnenkomen. Dan heb je de tank rustig staan, kun je de kraan controleren en hoef je tijdens het feest niet op een bezorger te wachten. Loopt het later toch uit? Wij bezorgen ook <a href="/lachgas-nachtbezorging/">'s avonds en 's nachts</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Studentenvereniging, introweek en jaarclub""",
                "paragraphs": [
                    """Groningen telt tientallen studentenverenigingen, huizen en jaarclubs, en de KEI-week in augustus zet de hele stad op zijn kop. Voor een verenigingsavond, een huisweekend of een jaarclubfeest met veel gasten adviseren we de 4KG of, bij echt grote aantallen, de <a href="/product/lachgas-tank-10kg/">Lachgastank 10KG</a>. Die laatste leveren we op aanvraag en in overleg, inclusief ophaling na afloop.""",
                    """Spreek binnen je commissie af wie de bestelling regelt en wie bij aflevering aanwezig is. Wij leveren uitsluitend aan personen van 18 jaar en ouder en kunnen bij aflevering om een identiteitsbewijs vragen. Zorg dat de persoon die de tank aanneemt daar rekening mee houdt, zeker tijdens de introweek waarin veel eerstejaars nog geen achttien zijn.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Verjaardag, housewarming of tuinfeest""",
                "paragraphs": [
                    """Voor een verjaardag of housewarming met vrienden en familie is de 2KG het meest gekozen formaat: compact, discreet en goed voor ongeveer 250 ballonnen. Vier je in de tuin, bijvoorbeeld in <a href="/bezorggebied/haren/">Haren</a>, <a href="/bezorggebied/eelde-paterswolde/">Eelde-Paterswolde</a> of <a href="/bezorggebied/bedum/">Bedum</a>, zet de tank dan in de schaduw en haal hem naar binnen zodra het feest is afgelopen. Een tank hoort nooit in de volle zon of in een warme auto te staan.""",
                    """Houd rekening met je gasten. Niet iedereen wil of mag lachgas gebruiken, en op een gemengd feest met ouders, kinderen of zwangere vrouwen is het netjes om de tank uit het zicht te houden en alleen onder volwassenen te gebruiken.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Bedrijfsborrel en besloten evenement""",
                "paragraphs": [
                    """Ook voor een bedrijfsborrel, een personeelsfeest of een besloten evenement op een gehuurde locatie leveren we lachgastanks. Bespreek vooraf met de locatie of lachgas is toegestaan; veel horecagelegenheden en zalen hanteren eigen huisregels. Is het akkoord, dan stemmen we via WhatsApp de levering af op het tijdstip waarop de locatie open is en iemand de tank kan aannemen.""",
                    """Voor evenementen met horeca of een grote groep bezoekers is de 10KG het meest geschikt. We bespreken dan ook direct de ophaling, zodat je na afloop niet met een lege tank blijft zitten. Over het bewaren en vervoeren van tanks op een locatie lees je meer in <a href="/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/">lachgastank bewaren en vervoeren</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Grotere aantallen en de 10KG tank""",
                "paragraphs": [
                    """Verwacht je meer dan vijftig gasten, of organiseer je meerdere avonden achter elkaar? Dan is het slim om vooraf even te overleggen. Soms is één 10KG tank het handigst, soms juist meerdere 4KG tanks verspreid over verschillende ruimtes of momenten. Wij denken graag mee en zorgen dat er voldoende voorraad is zonder dat je te veel bestelt.""",
                ],
                "bullets": [
                    """<strong>Eén centrale plek.</strong> Een 10KG tank is zwaar en hoort op één vaste, stabiele plek te staan, rechtop en uit de loop.""",
                    """<strong>Verantwoordelijke aanwezig.</strong> Zorg dat iemand van 18 jaar of ouder de tank aanneemt, toezicht houdt en de kraan na afloop dichtdraait.""",
                    """<strong>Ophaling afspreken.</strong> Bij de 10KG spreken we vooraf af wanneer we de tank weer ophalen. Een lege tank hoort niet bij het huisvuil.""",
                    """<strong>Meerdere formaten.</strong> Twijfel je, lees dan onze keuzehulp <a href="/lachgas-informatie/welke-lachgastank-heb-ik-nodig/">welke lachgastank heb ik nodig</a>.""",
                ],
            },
            {
                "h2": """Tijdig bestellen""",
                "paragraphs": [
                    """Voor een gewone bestelling in de stad hoef je niet te reserveren: een WhatsApp-bericht is genoeg en we zijn meestal binnen 20 tot 30 minuten ter plaatse. Voor een 10KG tank, voor grotere aantallen of voor een vast tijdstip op een locatie vragen we je om ruim van tevoren contact op te nemen, het liefst een dag of meer vooraf. Zo kunnen we de levering en ophaling inplannen en weet jij zeker dat alles op tijd staat.""",
                    """Op drukke avonden zoals de KEI-week, Koningsnacht, Bevrijdingsdag en de laatste tentamenweek lopen de levertijden op. Bestel dan vroeg op de dag, dan ben je zeker van je voorraad voordat het druk wordt.""",
                ],
                "bullets": [],
            },
            {
                "h2": """Veilig op een feest""",
                "paragraphs": [
                    """Hoe gezelliger het feest, hoe makkelijker het is om de basisregels te vergeten. Spreek daarom vooraf af hoe jullie met de tank omgaan. Gebruik zittend, in een geventileerde ruimte en met pauzes; nooit rechtstreeks uit de tank en nooit in combinatie met alcohol of andere middelen. Houd de tank weg van minderjarigen en zorg dat niemand na gebruik achter het stuur of op de fiets stapt. Alle aandachtspunten staan op onze pagina <a href="/lachgas-informatie/veilig-gebruik/">veilig gebruik van lachgas</a>.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Wij leveren uitsluitend aan volwassenen en verwachten dat lachgas op een feest alleen door volwassenen en met mate wordt gebruikt. Wordt iemand onwel, valt iemand of heeft iemand ademhalingsproblemen, bel dan direct 112. Twijfel je over je gezondheid na gebruik, neem contact op met je huisarts.""",
        "faq": [
            ["""Hoeveel lachgas heb ik nodig voor een feest met 30 gasten?""", """Voor 20 tot 30 gasten verspreid over een avond is de Lachgastank 4KG meestal de juiste keuze. Gebruikt maar een deel van de gasten, dan kan een 2KG volstaan. Twijfel je, stuur dan het aantal personen en de gelegenheid via WhatsApp en wij adviseren je."""],
            ["""Kunnen jullie op een gehuurde locatie of in een zaal bezorgen?""", """Ja, zolang de locatie het toestaat en er iemand van 18 jaar of ouder aanwezig is om de tank aan te nemen. Controleer vooraf de huisregels van de locatie en geef ons het adres, het tijdstip en een bereikbaar nummer door."""],
            ["""Halen jullie de tank na het feest weer op?""", """Bij de Lachgastank 10KG spreken we de ophaling altijd vooraf af. Voor 2KG en 4KG tanks kun je via WhatsApp vragen naar de mogelijkheden; een lege tank hoort in ieder geval niet bij het huisvuil."""],
        ],
        "related": ["welke-lachgastank-heb-ik-nodig", "veilig-gebruik"],
    },
]

# ---------------------------------------------------------------------------
# Veelgestelde vragen (/veelgestelde-vragen/)
# ---------------------------------------------------------------------------

FAQ = {
    "title": """Veelgestelde vragen over lachgas in Groningen""",
    "description": """Antwoord op veelgestelde vragen over lachgas bestellen in Groningen: bezorging, formaten, betalen bij aflevering, leeftijdscontrole en veilig gebruik.""",
    "h1": """Veelgestelde vragen""",
    "lead": """Alles wat je wilt weten over lachgas bestellen bij Lachgas Groningen, overzichtelijk op een rij. Staat je vraag er niet bij? Stuur ons een bericht via WhatsApp.""",
    "groups": [
        {
            "h2": """Bestellen en bezorgen""",
            "items": [
                ["""Wat zet ik in mijn WhatsApp-bericht?""", """Zet in je bericht welk product je wilt (bijvoorbeeld een Lachgastank 2KG), het aantal, je volledige adres met huisnummer en eventuele toevoeging, en een bereikbaar telefoonnummer. Woon je in een flat of studentencomplex, vermeld dan ook de ingang of verdieping. Zo kunnen we direct bevestigen en hoeven we niet heen en weer te appen."""],
                ["""Bezorgen jullie ook buiten de stad Groningen?""", """Ja. Naast alle stadswijken bezorgen we in Assen, Hoogezand, Leek en Winschoten en in dorpen rond de stad zoals Haren, Zuidhorn, Eelde-Paterswolde, Roden, Bedum en Ten Boer. Buiten de stad is de levertijd meestal 25 tot 40 minuten. Bekijk het volledige <a href="/bezorggebied/">bezorggebied</a> of vraag het via WhatsApp als je adres er niet bij staat."""],
                ["""Kan ik een bezorging voor een bepaald tijdstip plannen?""", """Dat kan. Geef in je bericht aan wanneer je de tank wilt ontvangen, bijvoorbeeld rond acht uur 's avonds, dan houden we daar rekening mee. Voor een 10KG tank of grotere aantallen vragen we je om minimaal een dag vooraf contact op te nemen."""],
                ["""Hoe discreet is de aflevering?""", """Onze bezorger komt in onopvallende kleding en zonder reclame, belt of appt bij aankomst en overhandigt je bestelling aan de deur. Buren of voorbijgangers zien een gewone bezorging. Je hoeft niets te bevestigen via een app of account; het hele contact loopt via WhatsApp."""],
            ],
        },
        {
            "h2": """Producten en hoeveelheden""",
            "items": [
                ["""Wat is het verschil tussen de 2KG, 4KG en 10KG tank?""", """De <a href="/product/lachgas-tank-2kg/">Lachgastank 2KG</a> bevat ongeveer 250 ballonnen en past bij een groep van 10 tot 15 personen. De <a href="/product/lachgas-tank-4kg/">4KG</a> bevat het dubbele en is bedoeld voor grotere feesten of een lange avond. De <a href="/product/lachgas-tank-10kg/">10KG</a> is voor evenementen en horeca en leveren we op aanvraag, in overleg over levering en ophaling. Onze <a href="/lachgas-informatie/welke-lachgastank-heb-ik-nodig/">keuzehulp</a> helpt je kiezen."""],
                ["""Zijn jullie tanks verzegeld?""", """Ja, alle tanks worden verzegeld geleverd en zijn gevuld met zuiver N2O. Controleer bij aflevering of de verzegeling intact is. Twijfel je ergens over, laat het de bezorger direct weten of stuur ons een bericht via WhatsApp."""],
                ["""Leveren jullie ook ballonnen, crackers en slagroompatronen?""", """Wij bezorgen naast tanks ook <a href="/product/lachgas-cracker/">lachgas crackers</a> en <a href="/product/slagroompatronen/">slagroompatronen</a>, per doosje of in grotere aantallen voor horeca. Vraag via WhatsApp naar de mogelijkheden en wat we in dezelfde rit kunnen meenemen."""],
                ["""Wat doe ik met een lege tank?""", """Een lege tank hoort niet bij het huisvuil. Bij de 10KG spreken we de ophaling vooraf af; voor andere formaten kun je via WhatsApp naar de mogelijkheden vragen of de tank inleveren bij het afvalbrengstation van je gemeente. Bewaar een lege tank tot die tijd rechtop en met de kraan dicht. Meer tips vind je in <a href="/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/">lachgastank bewaren en vervoeren</a>."""],
            ],
        },
        {
            "h2": """Betalen en voorwaarden""",
            "items": [
                ["""Moet ik vooruitbetalen?""", """Nee. Je betaalt pas bij aflevering, contant of via Tikkie in overleg. We vragen geen aanbetaling, geen account en geen gegevens vooraf; alleen je bestelling en je adres via WhatsApp."""],
                ["""Waar vind ik de prijzen?""", """Onze prijzen krijg je op aanvraag via WhatsApp. Stuur een bericht met het formaat en het aantal dat je wilt bestellen, dan ontvang je direct het tarief voor jouw bestelling, inclusief bezorging op jouw adres."""],
                ["""Wat gebeurt er als ik niet thuis ben bij aflevering?""", """Onze bezorger belt of appt bij aankomst. Krijgt hij geen gehoor, dan wacht hij kort en neemt hij de bestelling weer mee. Zorg dus dat je telefoon aanstaat en dat iemand van 18 jaar of ouder de deur kan openen. Een gemiste bezorging kun je via WhatsApp opnieuw inplannen."""],
                ["""Kan ik een bestelling annuleren of wijzigen?""", """Zolang de bezorger nog niet onderweg is, kun je je bestelling via WhatsApp aanpassen of annuleren. Is hij al vertrokken, laat het dan zo snel mogelijk weten; we zoeken dan samen naar een oplossing. Wees eerlijk en op tijd, dat voorkomt onnodige ritten."""],
            ],
        },
        {
            "h2": """Veiligheid en regels""",
            "items": [
                ["""Controleren jullie mijn leeftijd?""", """Ja. Wij leveren uitsluitend aan personen van 18 jaar en ouder en kunnen bij aflevering om een geldig identiteitsbewijs vragen. Kun je dat niet laten zien of blijk je jonger dan 18, dan gaat de bezorging niet door. Houd je ID dus bij de hand als je bestelt."""],
                ["""Hoe zit het met de wetgeving rond lachgas?""", """Sinds 1 januari 2023 staat lachgas op lijst II van de Opiumwet, met uitzonderingen voor medische, technische en voedingstoepassingen. Wij leveren in lijn met de geldende regels en alleen aan volwassenen. Lees meer op onze pagina <a href="/lachgas-informatie/is-lachgas-legaal-in-nederland/">is lachgas legaal in Nederland</a> en bij <a href="https://www.rijksoverheid.nl">de Rijksoverheid</a>."""],
                ["""Mag ik na gebruik nog fietsen of autorijden?""", """Nee. Rijden onder invloed van lachgas is verboden en gevaarlijk, ook op de fiets en ook als je je weer helder voelt. Lachgas vermindert je reactievermogen en kan plotselinge duizeligheid of bewustzijnsverlies geven. Lees meer op <a href="/lachgas-informatie/lachgas-in-het-verkeer/">lachgas in het verkeer</a>."""],
                ["""Wat zijn de belangrijkste gezondheidsrisico's?""", """Op korte termijn: duizeligheid, misselijkheid, vallen en bevriezingsletsel bij gebruik rechtstreeks uit een tank of cracker. Bij regelmatig gebruik maakt lachgas vitamine B12 onwerkzaam, wat kan leiden tot tintelingen, gevoelloosheid en loopproblemen. Lees onze pagina's over <a href="/lachgas-informatie/veilig-gebruik/">veilig gebruik</a> en <a href="/lachgas-informatie/lachgas-en-vitamine-b12/">lachgas en vitamine B12</a>, en neem bij klachten contact op met je huisarts."""],
            ],
        },
    ],
}
