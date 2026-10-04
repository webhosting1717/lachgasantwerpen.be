# -*- coding: utf-8 -*-
"""Informatieartikelen 1-7 voor lachgasbrabant.nl (basis, regels, gezondheid, veiligheid).

Toegestane HTML in tekstvelden: <strong> en <a href="..."> (interne paden uit de site-brief of
rijksoverheid.nl / drugsinfo.nl / trimbos.nl / novadic-kentron.nl).
"""

ARTICLES = [
    {
        "slug": "wat-is-lachgas", "label": "Basis",
        "title": "Wat is lachgas? Werking, toepassingen en risico’s",
        "description": "Lachgas (N2O) is een kleurloos gas met een lange geschiedenis in de zorg, techniek en voeding. Lees wat het is, hoe het werkt en waar de risico’s zitten.",
        "h1": "Wat is lachgas eigenlijk?",
        "lead": "Lachgas is de alledaagse naam voor distikstofmonoxide (N2O). Dit artikel legt uit waar het gas vandaan komt, waarvoor het officieel wordt gebruikt en wat het in het lichaam doet.",
        "sections": [
            {
                "h2": "Een klein molecuul met een grote reputatie",
                "paragraphs": [
                    """Lachgas is de volksnaam voor distikstofmonoxide, in scheikundige notatie N2O: twee stikstofatomen en één zuurstofatoom. Bij kamertemperatuur is het een kleurloos gas met een licht zoete geur en smaak. Het is zwaarder dan lucht en brandt zelf niet, maar het kan een vlam wel aanwakkeren omdat het bij verhitting zuurstof afgeeft. In een tank zit lachgas onder druk, grotendeels in vloeibare vorm; zodra de kraan opengaat, verdampt de vloeistof en komt het gas vrij. Dat verdampen kost warmte, waardoor de kraan en de uitstroom ijskoud worden. Die eigenschap verklaart een deel van de ongelukken die met lachgas gebeuren.""",
                    """De naam lachgas dankt het gas aan het giechelige, lichte gevoel dat inademing kan geven. Dat effect is echter maar één kant van het verhaal. In de industrie heet dezelfde stof simpelweg N2O of distikstofoxide, en daar draait het om heel andere eigenschappen: de druk die het levert, de zuurstof die het afgeeft en de stabiliteit waarmee het zich laat opslaan. Wie lachgas begrijpt, ziet dus twee gezichten: een technisch gas met nuttige toepassingen en een roesmiddel met gezondheidsrisico’s. In Nederland is alleen het eerste gezicht nog toegestaan.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Van laboratorium naar tandartsstoel",
                "paragraphs": [
                    """De Engelse scheikundige Joseph Priestley maakte lachgas in 1772 voor het eerst in zijn laboratorium. Ruim twintig jaar later experimenteerde Humphry Davy met het gas en beschreef hij het vrolijke, pijnstillende effect; hij maakte ook de naam laughing gas populair. In 1844 liet de Amerikaanse tandarts Horace Wells zich een kies trekken onder lachgas, waarmee de weg vrijkwam voor gebruik als verdovingsmiddel. In de twintigste eeuw werd het een vast onderdeel van de anesthesie in ziekenhuizen, altijd gemengd met zuurstof. Meer over die ontwikkeling en de mensen erachter lees je in <a href="/informatie/geschiedenis-van-lachgas/">de geschiedenis van lachgas</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Officiële toepassingen in zorg, techniek en voeding",
                "paragraphs": [
                    """Lachgas heeft drie erkende toepassingsgebieden, en precies die drie vormen vandaag de uitzonderingen op het landelijke verbod. In de zorg wordt het gemengd met zuurstof toegediend door professionals, bijvoorbeeld bij pijnlijke ingrepen bij de tandarts, op de verloskamer of in de ambulance. In de techniek dient het als oxidator in motoren en raketaandrijving, als hulpgas in de halfgeleiderindustrie en als ijkgas in laboratoria. In de voedingsindustrie is het toegelaten als drijfgas voor slagroom, herkenbaar aan het E-nummer E942. In alle gevallen gaat het om gecontroleerd gebruik met een duidelijk omschreven doel.""",
                ],
                "bullets": [
                    """<strong>Zorg.</strong> Kortdurende pijnstilling en verdoving, altijd gemengd met zuurstof en onder toezicht van een arts of verpleegkundige.""",
                    """<strong>Techniek.</strong> Oxidator, drijfgas en procesgas in industrie, motorsport en wetenschappelijk onderzoek.""",
                    """<strong>Voeding.</strong> Drijfgas voor slagroom en andere opgeklopte producten; valt onder de levensmiddelenwetgeving.""",
                ],
            },
            {
                "h2": "Wat lachgas in het lichaam doet",
                "paragraphs": [
                    """Na inademing komt lachgas via de longen snel in het bloed en bereikt het binnen seconden de hersenen. Daar remt het onder meer de NMDA-receptoren, die een rol spelen bij pijn en bewustzijn, en zet het de afgifte van lichaamseigen opioïden in gang. Het gevolg is een korte roes: een licht gevoel, lachkriebels, tintelingen, een vervormd gehoor en soms een gevoel van loskomen van de omgeving. Omdat het lichaam het gas niet afbreekt maar vrijwel onveranderd weer uitademt, is het effect na een paar minuten grotendeels verdwenen. Dat korte karakter maakt het middel verleidelijk, maar zegt niets over de veiligheid ervan.""",
                    """Twee risico’s verdienen aandacht. Ten eerste verdringt lachgas zuurstof: wie puur gas inademt, krijgt tijdelijk te weinig zuurstof binnen, met duizeligheid, flauwvallen en in het ergste geval verstikking als gevolg. Ten tweede schakelt lachgas vitamine B12 uit, een vitamine die onmisbaar is voor het zenuwstelsel. Bij regelmatig gebruik kan dat leiden tot tintelingen, krachtverlies en blijvende zenuwschade. Hoe dat werkt, lees je in <a href="/informatie/lachgas-en-vitamine-b12/">lachgas en vitamine B12</a>; de acute gevaren en wat je dan doet, staan in <a href="/informatie/lachgas-bijwerkingen-en-eerste-hulp/">bijwerkingen en eerste hulp</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Hoe Nederland er nu mee omgaat",
                "paragraphs": [
                    """Tot eind 2022 viel lachgas in Nederland onder de Warenwet en was het als consumentenproduct vrij verkrijgbaar. Sinds 1 januari 2023 staat het op lijst II van de Opiumwet. Productie, handel, bezit en vervoer zijn daarmee verboden, met uitzonderingen voor medische, technische en voedingsdoeleinden. De overheid legt dit uit op <a href="https://www.rijksoverheid.nl">rijksoverheid.nl</a>; onafhankelijke gezondheidsinformatie vind je bij <a href="https://www.drugsinfo.nl">drugsinfo.nl</a>. Wat het verbod precies betekent voor bezit, verkoop en vervoer, en welke rol gemeenten daarbij spelen, behandelen we in een apart artikel over de wetgeving.""",
                ],
                "bullets": [],
            },
        ],
        "note": "Dit artikel is bedoeld als achtergrondinformatie en geen aanmoediging tot gebruik. Lachgas is in Nederland uitsluitend toegestaan voor medische, technische en voedingsdoeleinden.",
        "related": ["geschiedenis-van-lachgas", "is-lachgas-legaal-in-nederland", "lachgas-bijwerkingen-en-eerste-hulp", "lachgas-en-vitamine-b12"],
    },
    {
        "slug": "is-lachgas-legaal-in-nederland", "label": "Regels",
        "title": "Is lachgas legaal in Nederland? De regels sinds 2023",
        "description": "Sinds 1 januari 2023 staat lachgas op lijst II van de Opiumwet. Lees wat dat betekent voor bezit, verkoop en vervoer en welke uitzonderingen gelden.",
        "h1": "Is lachgas legaal in Nederland?",
        "lead": "Sinds 1 januari 2023 valt lachgas onder de Opiumwet. Wat mag nog wel, wat is verboden en waar vind je de officiële uitleg? Een nuchter overzicht zonder juridisch jargon.",
        "sections": [
            {
                "h2": "Van vrij verkrijgbaar naar Opiumwet",
                "paragraphs": [
                    """Jarenlang was lachgas in Nederland een gewoon consumentenproduct. Het viel onder de Warenwet, lag in de schappen van winkels en werd online verkocht zonder leeftijdsgrens. Toen het recreatieve gebruik vanaf ongeveer 2016 sterk toenam en ziekenhuizen en gemeenten steeds meer problemen meldden, besloot de regering in te grijpen. Na een lang wetgevingstraject is lachgas op 1 januari 2023 toegevoegd aan lijst II van de Opiumwet, de lijst waarop ook hasj en wiet staan. Vanaf dat moment geldt een landelijk verbod dat de eerdere lokale lappendeken van regels grotendeels heeft vervangen.""",
                    """Lijst II is de lijst voor middelen die de wetgever als minder risicovol beschouwt dan die op lijst I, zoals cocaïne en heroïne. Minder risicovol betekent niet toegestaan: voor alle middelen op lijst II geldt dat produceren, verhandelen, bezitten, vervoeren en in- of uitvoeren verboden is, tenzij een wettelijke uitzondering van toepassing is. Het verschil met lijst I zit vooral in de hoogte van de straffen en in de prioriteit die politie en Openbaar Ministerie aan de handhaving geven. De officiële toelichting van het ministerie staat op <a href="https://www.rijksoverheid.nl">rijksoverheid.nl</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "De uitzonderingen: medisch, technisch en voeding",
                "paragraphs": [
                    """Het verbod is niet absoluut. In het Opiumwetbesluit is geregeld dat lachgas buiten de Opiumwet valt wanneer het bestemd is voor medische toepassingen, technische doeleinden of de bereiding van levensmiddelen. Ziekenhuizen, tandartsen en verloskundigen mogen het daarom blijven gebruiken, de industrie kan het als procesgas inzetten en slagroompatronen voor de keuken blijven in de supermarkt liggen. Bepalend is het doel waarvoor het gas wordt geleverd en gebruikt, niet alleen de verpakking. Wat die drie toepassingen inhouden, lees je in <a href="/informatie/wat-is-lachgas/">wat is lachgas</a>. Zodra het gas bedoeld is om te inhaleren voor een roes, geldt geen enkele uitzondering.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Wat betekent dit voor bezit, verkoop en vervoer?",
                "paragraphs": [
                    """Voor particulieren is de kern simpel: het bezit van lachgas voor recreatief gebruik is sinds 2023 strafbaar, ook in kleine hoeveelheden en ook thuis. Hoe streng daartegen wordt opgetreden, is aan politie en Openbaar Ministerie, die hun capaciteit vooral richten op handel en overlast. Het verkopen of aanbieden van lachgas voor recreatief gebruik is een misdrijf waarop forsere straffen staan, oplopend met de hoeveelheid en de rol van de verdachte. Vervoer telt juridisch als bezit: een tank in de kofferbak die niet voor een vrijgestelde toepassing bestemd is, kan in beslag worden genomen.""",
                ],
                "bullets": [
                    """<strong>Bezit.</strong> Verboden voor recreatief gebruik; de hoeveelheid en de omstandigheden bepalen hoe politie en justitie ermee omgaan.""",
                    """<strong>Verkoop.</strong> Verboden zonder vrijgesteld doel; wie levert, moet kunnen onderbouwen waarvoor het gas bestemd is.""",
                    """<strong>Vervoer.</strong> Juridisch gelijkgesteld aan bezit; onderweg gebruiken valt bovendien onder de verkeerswetgeving.""",
                    """<strong>In- en uitvoer.</strong> Het zwaarst bestraft, net als bij de andere middelen op lijst II.""",
                ],
            },
            {
                "h2": "Gemeenten en de APV",
                "paragraphs": [
                    """Vóór het landelijke verbod probeerden veel gemeenten lachgasoverlast te beteugelen via hun Algemene Plaatselijke Verordening, bijvoorbeeld met een verbod op gebruik in het centrum of bij evenementen. Die lokale regels zijn niet verdwenen. Gemeenten mogen nog altijd bepalingen opnemen tegen overlast in de openbare ruimte en voorwaarden stellen aan evenementenvergunningen. In de praktijk kun je dus met twee niveaus te maken krijgen: de Opiumwet voor bezit en handel, en de APV voor wat er op straat gebeurt. Hoe dat in Noord-Brabant werkt, lees je in <a href="/informatie/lachgas-regels-per-gemeente-brabant/">lachgasregels per gemeente</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Waar vind je betrouwbare informatie?",
                "paragraphs": [
                    """Over de Opiumwet circuleren veel halve waarheden, vooral op sociale media. Houd je daarom aan officiële bronnen. Op rijksoverheid.nl staat de uitleg van het ministerie, de volledige wettekst en het Opiumwetbesluit zijn door de overheid gepubliceerd, en voor gezondheidsinformatie is <a href="https://www.drugsinfo.nl">drugsinfo.nl</a> van het Trimbos-instituut de meest neutrale plek. Twijfel je over een concrete situatie, bijvoorbeeld rond vervoer of een evenement, dan is een jurist of het Juridisch Loket de juiste gesprekspartner. Informatie op websites van aanbieders, ook deze, is geen vervanging van juridisch advies.""",
                    """Voor onze eigen werkwijze betekent de wet dat we uitsluitend leveren aan volwassenen, altijd om een geldig identiteitsbewijs vragen en verzegelde tanks afgeven. Hoe die controle aan de deur verloopt, staat in <a href="/service/leeftijdscontrole-18-plus/">leeftijdscontrole 18+</a>. Ook over rijden met lachgas is de wet duidelijk; dat onderwerp behandelen we in <a href="/informatie/lachgas-in-het-verkeer/">lachgas in het verkeer</a>. Vragen over onze voorwaarden beantwoorden we via WhatsApp.""",
                ],
                "bullets": [],
            },
        ],
        "note": "Wetgeving kan veranderen en dit artikel is geen juridisch advies. Raadpleeg bij twijfel de actuele tekst op rijksoverheid.nl of vraag een jurist.",
        "related": ["lachgas-regels-per-gemeente-brabant", "lachgas-in-het-verkeer", "wat-is-lachgas", "leeftijdscontrole-18-plus"],
    },
    {
        "slug": "lachgas-regels-per-gemeente-brabant", "label": "Regels",
        "title": "Lachgasregels per gemeente in Brabant: zo werkt de APV",
        "description": "Naast de Opiumwet hebben Brabantse gemeenten eigen regels in de APV. Lees hoe zo’n verordening werkt en hoe je de regels van je eigen gemeente vindt.",
        "h1": "Lachgasregels per gemeente in Brabant",
        "lead": "Elke Brabantse gemeente heeft een eigen Algemene Plaatselijke Verordening. Hier lees je hoe die werkt, wat erin kan staan over lachgas en waar je de regels van jouw gemeente vindt.",
        "sections": [
            {
                "h2": "Twee lagen regels: landelijk en lokaal",
                "paragraphs": [
                    """Wie wil weten wat er in zijn woonplaats mag rond lachgas, moet naar twee niveaus kijken. Het eerste is de Opiumwet, die sinds 2023 in heel Nederland bezit, handel en vervoer verbiedt buiten de medische, technische en voedingsuitzonderingen. Het tweede niveau is de gemeente. Elke gemeente in Noord-Brabant, van Bergen op Zoom tot Boxmeer, heeft een eigen Algemene Plaatselijke Verordening met regels voor de openbare ruimte. Die regels gaan niet over de strafbaarheid van het middel zelf, maar over waar gedrag overlast geeft en hoe de gemeente daarop kan ingrijpen. De landelijke basis lees je in <a href="/informatie/is-lachgas-legaal-in-nederland/">is lachgas legaal in Nederland</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Wat is een APV precies?",
                "paragraphs": [
                    """APV staat voor Algemene Plaatselijke Verordening. Het is een verzameling gemeentelijke regels die de gemeenteraad vaststelt en die gaat over orde, veiligheid en leefbaarheid op straat. Denk aan het verbod op alcohol drinken in bepaalde gebieden, regels voor evenementen, het aanlijnen van honden en het parkeren van campers. De APV wordt gehandhaafd door de politie en door gemeentelijke handhavers, de boa’s. Overtreding levert doorgaans een boete op. Gemeenten passen hun verordening regelmatig aan, vaak jaarlijks, en publiceren de actuele tekst op hun eigen website en in de landelijke databank voor lokale regelgeving.""",
                    """Een APV kan geen landelijke wet opzijzetten, maar wel aanvullen. Dat is precies wat bij lachgas gebeurt: de Opiumwet regelt het bezit, de APV regelt het gedrag in de publieke ruimte. Zo kan een gemeente bijvoorbeeld bepalen dat een handhaver mag optreden tegen gebruik op een plein, ook als er verder niets strafbaars te bewijzen valt. Omdat elke raad zijn eigen keuzes maakt, verschillen de teksten van gemeente tot gemeente. Wat in de ene stad een expliciet gebiedsverbod is, valt in een buurgemeente onder een algemene overlastbepaling of ontbreekt helemaal.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Welke soorten lachgasbepalingen komen voor?",
                "paragraphs": [
                    """Zonder uitspraken te doen over afzonderlijke gemeenten, zijn er een paar typen bepalingen die in Nederlandse verordeningen regelmatig terugkomen. Ze richten zich steeds op zichtbaar gebruik en de overlast daaromheen, niet op wat iemand binnen de eigen muren doet. Of een bepaling in jouw gemeente geldt, en voor welk gebied precies, kun je alleen met zekerheid vaststellen door de actuele tekst te lezen. Dit zijn de vormen die je het vaakst tegenkomt:""",
                ],
                "bullets": [
                    """<strong>Gebiedsverbod.</strong> Een verbod op het gebruiken van lachgas in aangewezen gebieden, zoals een uitgaanscentrum, een winkelgebied, een park of de omgeving van een station.""",
                    """<strong>Overlastbepaling.</strong> Een algemener artikel dat gebruik verbiedt wanneer dat hinderlijk is voor anderen, bijvoorbeeld door achtergelaten ballonresten of groepsvorming.""",
                    """<strong>Evenementenvoorwaarden.</strong> Voorschriften in een evenementenvergunning waarmee de organisator verplicht wordt lachgas op het terrein te weren.""",
                    """<strong>Verbod op bezit met kennelijk gebruiksdoel.</strong> Een bepaling uit de periode vóór 2023 die in sommige teksten nog voorkomt, naast de Opiumwet.""",
                ],
            },
            {
                "h2": "Steden, dorpen en evenementen in Brabant",
                "paragraphs": [
                    """Noord-Brabant telt ruim vijftig gemeenten met grote verschillen in schaal. Steden als Eindhoven, Tilburg, Breda en ’s-Hertogenbosch hebben uitgebreide uitgaansgebieden en een drukke evenementenkalender, en hebben daardoor vaker aanleiding gehad om specifieke lachgasbepalingen te overwegen. Kleinere gemeenten in de Kempen, de Peel of het Land van Cuijk volstaan soms met een algemene overlastregel. Rond carnaval, kermissen en festivals gelden daarnaast de huisregels van de organisator, die strenger kunnen zijn dan de APV. Wat wij daarover zelf afspreken met klanten, staat bij <a href="/service/feestdagen-en-evenementen/">feestdagen en evenementen</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Zo vind je de regels van jouw gemeente",
                "paragraphs": [
                    """De enige betrouwbare bron is de actuele verordening zelf. Zoek op de website van je gemeente op de term APV in combinatie met lachgas, of raadpleeg de landelijke databank met lokale regelgeving, waar alle verordeningen in doorzoekbare vorm staan. Kom je er niet uit, dan kun je het team vergunningen of handhaving van de gemeente een vraag stellen. Let in de openbare ruimte ook op bebording: gebieden met een verbod zijn vaak aangegeven. Voor de gezondheidskant verwijzen we naar het Trimbos-instituut op <a href="https://www.trimbos.nl">trimbos.nl</a>, dat ook gemeenten adviseert over lachgasbeleid.""",
                    """Omdat verordeningen veranderen en wij niet alle gemeenten dagelijks kunnen volgen, nemen we in dit artikel bewust geen regels van afzonderlijke plaatsen op. Een lijst die vandaag klopt, kan na de volgende raadsvergadering verouderd zijn. Controleer dus altijd zelf, zeker als je een evenement organiseert of in een uitgaansgebied woont. Vragen over onze eigen voorwaarden en werkwijze beantwoorden we graag via WhatsApp.""",
                ],
                "bullets": [],
            },
        ],
        "note": "Wij noemen bewust geen regels van afzonderlijke gemeenten: verordeningen veranderen regelmatig en alleen de actuele APV van je eigen gemeente is leidend.",
        "related": ["is-lachgas-legaal-in-nederland", "lachgas-in-het-verkeer", "feestdagen-en-evenementen"],
    },
    {
        "slug": "lachgas-en-vitamine-b12", "label": "Gezondheid",
        "title": "Lachgas en vitamine B12: wat er in je lichaam gebeurt",
        "description": "Lachgas schakelt vitamine B12 uit. Lees hoe dat werkt, welke klachten zoals tintelingen en krachtverlies erbij horen en wanneer je naar de huisarts gaat.",
        "h1": "Lachgas en vitamine B12",
        "lead": "Het bekendste gezondheidsrisico van lachgas heeft te maken met vitamine B12. Dit artikel legt het mechanisme uit, beschrijft de klachten en vertelt wanneer je een arts moet zien.",
        "sections": [
            {
                "h2": "Waarom vitamine B12 zo belangrijk is",
                "paragraphs": [
                    """Vitamine B12, ook cobalamine genoemd, is een vitamine die het lichaam niet zelf kan maken. Je krijgt haar binnen via dierlijke producten zoals vlees, vis, eieren en zuivel, en de lever houdt een voorraad aan die normaal jaren meegaat. B12 is nodig voor de aanmaak van rode bloedcellen en DNA, maar vooral voor het onderhoud van de myelineschede, het isolerende laagje rond zenuwbanen. Zonder goed werkende B12 raakt die isolatie beschadigd en gaan zenuwsignalen haperen. Klassieke risicogroepen voor een tekort zijn veganisten, ouderen en mensen met maag- of darmproblemen. Lachgasgebruikers vormen een nieuwe, snel gegroeide groep.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Hoe lachgas B12 uitschakelt",
                "paragraphs": [
                    """Het mechanisme is goed beschreven in de medische literatuur. In het centrum van het B12-molecuul zit een kobaltatoom. Lachgas oxideert dat atoom, waardoor de vitamine van haar actieve in een inactieve vorm verandert. Het enzym methioninesynthase, dat B12 nodig heeft, komt daarmee stil te liggen. Het bijzondere is dat de hoeveelheid B12 in het bloed daarbij normaal kan blijven: de vitamine is er wel, maar werkt niet. Artsen spreken daarom van een functioneel tekort en kijken bij verdenking ook naar stoffen als methylmalonzuur en homocysteïne, die zich ophopen wanneer het enzym niet werkt.""",
                    """Een eenmalige blootstelling, zoals bij een verdoving bij de tandarts, geeft bij gezonde mensen gewoonlijk geen problemen; het lichaam herstelt de voorraad vanzelf. Het risico zit in herhaling. Wie vaak en veel gebruikt, schakelt steeds opnieuw B12 uit voordat het lichaam heeft kunnen herstellen. Hoe korter de tussenpozen en hoe groter de hoeveelheden, hoe sneller de schade zich opbouwt. Mensen die al een lage B12-status hebben, bijvoorbeeld door hun voeding, zijn extra kwetsbaar en kunnen al na relatief weinig gebruik klachten krijgen.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Klachten die op een tekort kunnen wijzen",
                "paragraphs": [
                    """De eerste signalen zijn vaak subtiel en worden gemakkelijk afgedaan als vermoeidheid of een verkeerde houding. Omdat de lange zenuwen naar de benen het kwetsbaarst zijn, beginnen de klachten meestal in de voeten en kruipen ze langzaam omhoog. Ook het ruggenmerg kan aangetast raken, een aandoening die artsen myelopathie noemen. Neem onderstaande klachten serieus, zeker in combinatie met lachgasgebruik, en wacht niet tot ze vanzelf verdwijnen:""",
                ],
                "bullets": [
                    """<strong>Tintelingen of een doof gevoel</strong> in voeten, benen, handen of vingers, vaak aan beide kanten tegelijk.""",
                    """<strong>Onzeker lopen</strong> en balansproblemen, in het bijzonder in het donker of met de ogen dicht.""",
                    """<strong>Krachtverlies</strong> in de benen, moeite met trappen, struikelen of het gevoel op watten te lopen.""",
                    """<strong>Vermoeidheid, concentratie- en geheugenproblemen</strong> en soms stemmingsklachten of prikkelbaarheid.""",
                    """<strong>In ernstige gevallen</strong> verlammingsverschijnselen en problemen met plassen of ontlasting.""",
                ],
            },
            {
                "h2": "Wanneer naar de huisarts?",
                "paragraphs": [
                    """Het eerlijke antwoord: bij de eerste tintelingen die langer dan een paar uur aanhouden, en zeker als ze terugkomen of erger worden. Veel mensen wachten te lang omdat ze zich schamen voor het gebruik of hopen dat het vanzelf wegtrekt. Dat is zonde, want zenuwschade herstelt traag en soms maar gedeeltelijk; hoe eerder de behandeling start, hoe groter de kans op volledig herstel. Vertel de huisarts open dat je lachgas hebt gebruikt. Artsen hebben beroepsgeheim, kennen het beeld inmiddels goed en kunnen gericht bloedonderzoek doen in plaats van te zoeken naar andere oorzaken.""",
                    """De behandeling bestaat uit volledig stoppen met lachgas en het aanvullen van B12, meestal met injecties omdat die het snelst werken. Bij ernstige uitval volgt verwijzing naar een neuroloog. Herstel kan weken tot maanden duren en vraagt geduld. Lukt stoppen niet op eigen kracht, dan is daar hulp voor: in Brabant via <a href="https://www.novadic-kentron.nl">Novadic-Kentron</a>, en algemene informatie via <a href="/informatie/problematisch-lachgasgebruik-hulp/">hulp bij problematisch gebruik</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Wat je zelf kunt doen en wat niet werkt",
                "paragraphs": [
                    """Het belangrijkste wat je kunt doen, is stoppen zodra je klachten herkent en een arts raadplegen. Wat niet werkt, is doorgaan met gebruik en ondertussen B12-tabletten slikken. Zolang er lachgas bijkomt, wordt ook de aangevulde vitamine telkens opnieuw uitgeschakeld; supplementen bieden dus geen bescherming tegen voortgezet gebruik. Een gevarieerd eetpatroon met voldoende dierlijke producten of een goed gekozen vervanging houdt je basisvoorraad op peil, maar is geen vrijbrief. Ken je iemand die de klachten herkent maar niets doet, maak het dan bespreekbaar. De algemene risico’s staan in <a href="/informatie/lachgas-bijwerkingen-en-eerste-hulp/">bijwerkingen en eerste hulp</a>.""",
                ],
                "bullets": [],
            },
        ],
        "note": "Bij tintelingen, een doof gevoel of krachtverlies na lachgasgebruik: wacht niet af en maak een afspraak bij de huisarts. Bij acute uitval of een val bel je 112.",
        "related": ["lachgas-bijwerkingen-en-eerste-hulp", "problematisch-lachgasgebruik-hulp", "wat-is-lachgas"],
    },
    {
        "slug": "lachgas-bijwerkingen-en-eerste-hulp", "label": "Veiligheid",
        "title": "Bijwerkingen van lachgas en eerste hulp bij problemen",
        "description": "Bijwerkingen van lachgas op korte en lange termijn, bevriezingsletsel herkennen en wat je doet als iemand onwel wordt, inclusief wanneer je 112 belt.",
        "h1": "Bijwerkingen van lachgas en eerste hulp",
        "lead": "Lachgas kan flauwvallen, misselijkheid en bevriezingsletsel veroorzaken en op langere termijn zenuwschade. Dit is wat je moet weten om goed te reageren als het misgaat.",
        "sections": [
            {
                "h2": "Korte termijn: wat er direct kan gebeuren",
                "paragraphs": [
                    """De roes van lachgas is kort, maar juist in die paar minuten gebeuren de meeste ongelukken. Veelvoorkomende directe bijwerkingen zijn duizeligheid, hoofdpijn, misselijkheid, een vervormd gehoor en verlies van coördinatie. Omdat het gas zuurstof verdringt, daalt het zuurstofgehalte in het bloed tijdelijk; wie staat, kan daardoor plotseling flauwvallen. Vallen is dan ook de belangrijkste oorzaak van ernstig letsel: een hoofd dat tegen een stoeprand of tafelrand komt, is gevaarlijker dan het gas zelf. Daarnaast komen verwardheid, hartkloppingen en paniek voor, vooral bij mensen die het effect niet verwachten.""",
                    """Ernstige zuurstoftekorten ontstaan vooral wanneer iemand het gas inademt zonder dat er lucht bij komt, bijvoorbeeld met een zak of masker, of in een kleine afgesloten ruimte zoals een auto. Daarbij kan het bewustzijn wegvallen terwijl het gas wordt doorgeademd, met verstikking als mogelijk gevolg. Ook de combinatie met alcohol of andere middelen vergroot de kans dat het misgaat; daarover gaat <a href="/informatie/lachgas-en-alcohol/">lachgas en alcohol</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Lange termijn: zenuwen, bloed en gedrag",
                "paragraphs": [
                    """Bij regelmatig gebruik komen andere problemen in beeld. De bekendste is schade aan het zenuwstelsel door uitgeschakelde vitamine B12, met tintelingen, krachtverlies en loopproblemen; in <a href="/informatie/lachgas-en-vitamine-b12/">lachgas en vitamine B12</a> leggen we dat uit. Datzelfde mechanisme kan bloedarmoede veroorzaken. In medische publicaties wordt bij zwaar gebruik ook een verband gelegd met een verhoogde kans op trombose. Verder melden gebruikers hoofdpijn, concentratieproblemen en een sterke drang om door te gaan, ook al is lachgas lichamelijk niet verslavend op de manier waarop nicotine dat is. Wie merkt dat gebruik niet meer vrijblijvend voelt, vindt informatie op <a href="https://www.drugsinfo.nl">drugsinfo.nl</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Bevriezingsletsel: koud gas en koud metaal",
                "paragraphs": [
                    """Lachgas zit in een tank als vloeistof onder druk. Zodra het de kraan verlaat, verdampt het en onttrekt het daarbij veel warmte aan de omgeving. De kraan, de uitstroom en alles wat ermee in contact komt, kunnen daardoor tot ver onder nul afkoelen. Direct contact met de huid of het inademen van het ijskoude gas rechtstreeks uit een tank of patroon veroorzaakt bevriezingsletsel aan lippen, mond, keel, handen en bovenbenen. Hoe de kou in een tank ontstaat en waarom dat in de winter nog sterker speelt, lees je in <a href="/informatie/lachgas-bij-kou-en-warmte/">lachgas bij kou en warmte</a>.""",
                    """Bevroren huid ziet eerst wit of wasachtig en voelt doof aan; pas later komen pijn, roodheid en blaren. Verwarm het getroffen deel langzaam met lauw water of lichaamswarmte, nooit met heet water, een kachel of door te wrijven, want dat beschadigt het weefsel verder. Bedek het losjes en laat blaren dicht. Bij blaren, aanhoudende gevoelloosheid of letsel in de mond en keel is een bezoek aan huisarts of huisartsenpost nodig. Zwelling in de keel met slikproblemen of benauwdheid is een spoedgeval.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Als iemand onwel wordt",
                "paragraphs": [
                    """Het belangrijkste is dat je in actie komt en bij de persoon blijft. Iemand die wegzakt na lachgas mag nooit alleen worden gelaten om het te laten uitslapen: de ademhaling kan verslechteren zonder dat iemand het merkt. Je hebt geen EHBO-diploma nodig om het verschil te maken; de meldkamer van 112 begeleidt je stap voor stap. Twijfel je, kies dan altijd voor de veiligste optie en bel. Dit zijn de stappen in volgorde:""",
                ],
                "bullets": [
                    """<strong>Spreek aan en schud zachtjes.</strong> Reageert de persoon niet of nauwelijks, bel dan direct 112.""",
                    """<strong>Zorg voor frisse lucht.</strong> Zet ramen open, haal gas en tank weg en breng de persoon zo mogelijk naar buiten.""",
                    """<strong>Ademt de persoon maar is hij bewusteloos:</strong> leg hem in de stabiele zijligging, zodat braaksel niet in de luchtwegen komt.""",
                    """<strong>Ademt de persoon niet normaal:</strong> bel 112, start reanimatie en volg de aanwijzingen van de meldkamer.""",
                    """<strong>Blijf erbij en vertel de hulpdiensten eerlijk</strong> wat er is gebruikt, ook alcohol of andere middelen.""",
                ],
            },
            {
                "h2": "Wanneer bel je 112?",
                "paragraphs": [
                    """Een ambulance bellen voor een drugsgerelateerde situatie voelt voor veel mensen als een drempel, uit angst voor gedoe met politie of ouders. Die angst is in de praktijk onterecht: hulpverleners zijn er om iemand te helpen, niet om te straffen. Bel 112 als iemand niet goed wakker te krijgen is, als de ademhaling stopt of onregelmatig wordt, bij een stuip, bij hoofdletsel gevolgd door braken of verwardheid, bij pijn op de borst, of bij bevriezing in mond of keel met benauwdheid. Twijfel is op zichzelf al reden genoeg om te bellen.""",
                    """Herstelt iemand binnen enkele minuten volledig en heeft hij geen val gemaakt, dan is 112 meestal niet nodig, maar houd de persoon wel een tijd in de gaten. Blijven klachten als hoofdpijn, duizeligheid of tintelingen de volgende dag aanwezig, maak dan een afspraak bij de huisarts. Vragen over hoe wij met veiligheid omgaan bij de levering, beantwoorden we in de <a href="/veelgestelde-vragen/veiligheid/">veelgestelde vragen over veiligheid</a>.""",
                ],
                "bullets": [],
            },
        ],
        "note": "Twijfel je of een situatie ernstig is? Bel dan 112. Een onnodige melding is beter dan een te late.",
        "related": ["lachgas-en-vitamine-b12", "lachgas-en-alcohol", "lachgas-bij-kou-en-warmte", "problematisch-lachgasgebruik-hulp"],
    },
    {
        "slug": "lachgas-en-alcohol", "label": "Gezondheid",
        "title": "Lachgas en alcohol: waarom de combinatie riskant is",
        "description": "Alcohol en lachgas versterken elkaar: meer kans op flauwvallen, overgeven en vallen. Lees welke signalen op gevaar wijzen en wanneer je hulp inschakelt.",
        "h1": "Lachgas en alcohol",
        "lead": "Veel incidenten met lachgas gebeuren op avonden waarop ook gedronken wordt. Dit artikel legt uit waarom die combinatie onvoorspelbaar is, hoe je gevaar herkent en wat je dan doet.",
        "sections": [
            {
                "h2": "Wat alcohol en lachgas afzonderlijk doen",
                "paragraphs": [
                    """Alcohol is een dempend middel dat via het bloed de hersenen bereikt en daar de verwerking van signalen vertraagt. Het gevolg ken je: een langzamere reactie, een losser gevoel, minder scherpe oordelen en een slechtere balans. Daarnaast verwijdt alcohol de bloedvaten, verlaagt het de bloeddruk, prikkelt het de maag en droogt het je uit. Bij grotere hoeveelheden wordt de ademhaling trager en kan het bewustzijn wegvallen. Alcohol blijft uren in het lichaam; de lever breekt het in een vast tempo af, en dat tempo laat zich door koffie, eten of frisse lucht niet versnellen.""",
                    """Lachgas werkt anders en veel korter. Het gas komt via de longen in het bloed, bereikt binnen seconden de hersenen en geeft een roes van een paar minuten waarin de omgeving vervaagt, het gehoor vervormt en de coördinatie wegvalt. Tegelijk verdringt het zuurstof uit de longen, waardoor het zuurstofgehalte in het bloed tijdelijk zakt. Omdat het effect zo snel verdwijnt, lijkt lachgas op zichzelf beheersbaar. Die indruk verandert zodra er alcohol in het spel is. Wat lachgas precies is en doet, lees je in <a href="/informatie/wat-is-lachgas/">wat is lachgas</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Waarom de combinatie erger is dan de som",
                "paragraphs": [
                    """Twee dempende middelen tegelijk versterken elkaar. Alcohol heeft de bloeddruk al verlaagd en de ademhaling vertraagd; komt daar het zuurstoftekort van lachgas bij, dan is de reserve van het lichaam klein. Flauwvallen gebeurt sneller en de val is harder, omdat de reflexen al zijn afgestompt. Alcohol maakt bovendien misselijk en lachgas versterkt dat; overgeven bij een verlaagd bewustzijn kan ertoe leiden dat braaksel in de longen komt. Voor hulpdiensten is dit een bekend en gevreesd scenario, juist omdat het zo snel kan omslaan.""",
                    """Minstens zo belangrijk is het effect op het oordeel. Wie heeft gedronken, schat slecht in hoeveel hij al heeft gehad, negeert signalen van het lichaam en neemt beslissingen die hij nuchter nooit zou nemen, zoals toch nog in de auto stappen. De korte roes van lachgas verleidt dan tot herhalen, terwijl het lichaam juist tijd nodig heeft om te herstellen. Langdurig zware drinkers hebben daarnaast vaker een lage vitamine B12-status, wat de zenuwschade door lachgas kan versnellen. Het Trimbos-instituut waarschuwt daarom uitdrukkelijk tegen het combineren van lachgas met alcohol en andere middelen; zie <a href="https://www.trimbos.nl">trimbos.nl</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Signalen dat het misgaat",
                "paragraphs": [
                    """Op een feest of in een kroeg is het lastig te zien wie gewoon dronken is en wie in gevaar is. Let daarom op de combinatie van signalen hieronder, en vertrouw je onderbuikgevoel als iemand anders dan anders reageert. Vooral het niet goed wakker te krijgen zijn is een alarmsignaal dat je nooit mag negeren, hoe gezellig de avond tot dan toe ook was. Liever één keer voor niets ingegrepen dan één keer te laat.""",
                ],
                "bullets": [
                    """<strong>Wegzakken</strong> en moeilijk of niet wakker te krijgen, ook niet met luid aanspreken.""",
                    """<strong>Trage, onregelmatige of snurkende ademhaling</strong> bij iemand die niet gewoon in slaap is gevallen.""",
                    """<strong>Blauwe of grauwe lippen</strong>, een koude klamme huid of een opvallend bleke kleur.""",
                    """<strong>Braken</strong> terwijl de persoon niet goed bij bewustzijn is.""",
                    """<strong>Een val met hoofdletsel</strong>, gevolgd door verwardheid, sufheid of opnieuw braken.""",
                ],
            },
            {
                "h2": "Wat je doet als het misgaat",
                "paragraphs": [
                    """Laat iemand die wegzakt nooit alleen om het uit te slapen. Leg een bewusteloze maar ademende persoon in de stabiele zijligging, zorg voor frisse lucht en haal gas en drank weg. Reageert hij niet of ademt hij niet normaal, bel dan 112 en volg de aanwijzingen van de meldkamer. Geef geen koffie, water of eten aan iemand die niet goed bij bewustzijn is, en probeer hem niet te laten lopen of douchen. Vertel de hulpverleners eerlijk wat er is gebruikt; dat bepaalt hun aanpak. Een uitgebreid stappenplan staat in <a href="/informatie/lachgas-bijwerkingen-en-eerste-hulp/">bijwerkingen en eerste hulp</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Als het vaker voorkomt",
                "paragraphs": [
                    """Gebeurt het regelmatig dat drank en lachgas samen voorbijkomen, dan is dat op zichzelf een signaal. Niet omdat elke avond uit de hand loopt, maar omdat de combinatie steeds opnieuw de rem wegneemt die je normaal hebt. Praat erover met iemand die je vertrouwt of met je huisarts. In Noord-Brabant kun je terecht bij <a href="https://www.novadic-kentron.nl">Novadic-Kentron</a>, de regionale instelling voor verslavingszorg, ook voor een vrijblijvend gesprek. Landelijke informatie en een anonieme chat vind je via <a href="https://www.drugsinfo.nl">drugsinfo.nl</a>. Hoe je iemand aanspreekt zonder te oordelen, beschrijven we in ons artikel over hulp bij problematisch gebruik.""",
                ],
                "bullets": [],
            },
        ],
        "note": "Combineer je lachgas met alcohol of andere middelen, dan vervalt elke voorspelbaarheid. Zie je iemand wegzakken of braken bij een verlaagd bewustzijn: bel 112.",
        "related": ["lachgas-bijwerkingen-en-eerste-hulp", "problematisch-lachgasgebruik-hulp", "lachgas-in-het-verkeer"],
    },
    {
        "slug": "lachgas-in-het-verkeer", "label": "Regels",
        "title": "Lachgas in het verkeer: verbod, controle en gevolgen",
        "description": "Rijden onder invloed van lachgas is strafbaar en gevaarlijk. Lees hoe de politie controleert, welke gevolgen mogelijk zijn en hoe je veilig thuiskomt.",
        "h1": "Lachgas in het verkeer",
        "lead": "Een roes van lachgas duurt kort, maar lang genoeg om de controle over een auto of scooter te verliezen. Dit zijn de regels, de manier van controleren en de gevolgen.",
        "sections": [
            {
                "h2": "Wat de wet zegt",
                "paragraphs": [
                    """De Wegenverkeerswet verbiedt het besturen van een voertuig onder invloed van een stof waarvan je weet of redelijkerwijs moet weten dat die je rijvaardigheid vermindert. Lachgas valt daar zonder discussie onder. Het verbod geldt voor alle bestuurders, dus ook voor fietsers, scooterrijders en bestuurders van een e-bike of brommobiel. Anders dan bij alcohol en een aantal drugs geldt voor lachgas geen vaste grenswaarde: elk gebruik dat de rijvaardigheid aantast, is strafbaar. Daarnaast is bezit van lachgas sinds 2023 verboden op grond van de Opiumwet, tenzij het voor een vrijgesteld doel bestemd is; een tank in de auto kan dus om twee redenen problemen geven.""",
                    """Hoe de wetgeving precies in elkaar zit en welke uitzonderingen er zijn, lees je in <a href="/informatie/is-lachgas-legaal-in-nederland/">is lachgas legaal in Nederland</a>. De overheid informeert over rijden onder invloed op <a href="https://www.rijksoverheid.nl">rijksoverheid.nl</a>. Wetgeving rond drugs in het verkeer wordt regelmatig aangescherpt, dus controleer bij twijfel altijd de actuele stand van zaken. Dit artikel beschrijft de hoofdlijnen voor Nederland en is uitdrukkelijk geen juridisch advies.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Waarom het zo gevaarlijk is",
                "paragraphs": [
                    """Een roes van lachgas duurt kort, maar in het verkeer is kort genoeg. Bij vijftig kilometer per uur legt een auto ongeveer veertien meter per seconde af; wie een halve minuut niet scherp is, rijdt honderden meters zonder werkelijke controle. Het gas veroorzaakt bovendien precies de uitval die achter het stuur fataal is: duizeligheid, tunnelzicht, vertraagde reacties, verlies van coördinatie en in het ergste geval flauwvallen. Ook passagiers die gebruiken vormen een risico, door afleiding en door het gas dat in een gesloten auto blijft hangen. Volgens de politie speelt lachgas de laatste jaren vaker een rol bij ernstige ongevallen.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Hoe de politie controleert",
                "paragraphs": [
                    """Bij alcohol blaast een bestuurder en bij veel drugs doet de politie een speekseltest. Voor lachgas bestaat zo’n snelle test niet, omdat het gas het lichaam vrijwel direct weer verlaat. De politie werkt daarom met waarnemingen: slingerend of schokkerig rijgedrag, de toestand van de bestuurder bij het staandehouden, vergrote pupillen, een trage reactie en wat er in de auto ligt, zoals een tank of ballonresten. Agenten kunnen een bestuurder psychomotorische testen laten doen en bij verdenking een bloedonderzoek vorderen. Verklaringen van passagiers en getuigen tellen mee als bewijs.""",
                    """Een veelgehoord misverstand is dat je zonder positieve test niets kan gebeuren. Dat klopt niet: de rechter beoordeelt het geheel aan bewijs, en een rijtest in combinatie met een tank op de achterbank en een bekennende verklaring kan ruim voldoende zijn voor een veroordeling. Daarnaast kan de tank zelf op basis van de Opiumwet in beslag worden genomen, ongeacht of de bestuurder heeft gebruikt. Wie denkt slim te zijn door het gas pas na de controle te gebruiken, vergeet dat de volgende controle verderop kan staan.""",
                ],
                "bullets": [],
            },
            {
                "h2": "De gevolgen: strafrecht, rijbewijs en verzekering",
                "paragraphs": [
                    """De gevolgen van rijden onder invloed van lachgas reiken verder dan een boete. Ze spelen op meerdere terreinen tegelijk en kunnen jaren doorwerken, zeker voor jonge bestuurders die nog maar kort hun rijbewijs hebben en voor wie strengere regels gelden. Hieronder staan de belangrijkste; de precieze uitkomst hangt af van de omstandigheden, je rijhistorie en of er schade of letsel is ontstaan.""",
                ],
                "bullets": [
                    """<strong>Strafrechtelijk.</strong> Een geldboete, taakstraf of in ernstige gevallen gevangenisstraf, plus een ontzegging van de rijbevoegdheid. Veroorzaak je een ongeval met letsel, dan gelden zwaardere strafbare feiten.""",
                    """<strong>Rijbewijs.</strong> De politie kan het rijbewijs direct invorderen. Het CBR kan een onderzoek naar de rijgeschiktheid of een cursus opleggen, waarvan de kosten voor eigen rekening komen.""",
                    """<strong>Verzekering.</strong> Verzekeraars kunnen schade aan de eigen auto weigeren te vergoeden en uitgekeerde schade aan anderen op de bestuurder terugvorderen.""",
                    """<strong>Werk en toekomst.</strong> Een veroordeling kan gevolgen hebben voor een verklaring omtrent het gedrag, een rijbewijs voor het werk of een leaseauto.""",
                ],
            },
            {
                "h2": "Veilig thuiskomen",
                "paragraphs": [
                    """De enige veilige keuze is simpel: wie lachgas heeft gebruikt, rijdt niet, ook niet een paar minuten later en ook niet op de fiets. Spreek vooraf af wie nuchter blijft en wie rijdt, net als bij alcohol. Lukt dat niet, bestel dan een taxi, gebruik het openbaar vervoer zolang dat rijdt, of blijf slapen. Buiten de grote Brabantse steden rijdt ’s nachts weinig tot geen openbaar vervoer, dus reken niet op de laatste bus. In een groep is het de verantwoordelijkheid van iedereen om iemand die wil rijden tegen te houden; dat is geen bemoeienis, dat is iemands leven redden.""",
                    """Vervoer je een gesloten tank, dan hoort die stevig vast en buiten bereik te staan, en wordt die onderweg niet geopend. Dat wij aan huis bezorgen, heeft hier ook mee te maken: een tank hoort niet open te gaan in een rijdende auto. Praktische tips over vervoeren staan in <a href="/informatie/lachgastank-bewaren-en-vervoeren/">lachgastank bewaren en vervoeren</a>. Over de combinatie met drank, die in het verkeer extra vaak voorkomt, lees je in <a href="/informatie/lachgas-en-alcohol/">lachgas en alcohol</a>.""",
                ],
                "bullets": [],
            },
        ],
        "note": "Rijden na lachgas is nooit een optie, ook niet na één keer en ook niet op een fiets of scooter. Twijfel je of iemand nog kan rijden? Dan kan die persoon dat niet.",
        "related": ["is-lachgas-legaal-in-nederland", "lachgas-en-alcohol", "lachgastank-bewaren-en-vervoeren", "lachgas-bijwerkingen-en-eerste-hulp"],
    },
]
