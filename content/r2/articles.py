# -*- coding: utf-8 -*-
"""Nieuwe informatieartikelen en servicepagina's voor lachgasrotterdam.nl (fase 2).

Toegestane HTML in tekstvelden: strong en a (interne paden of drugsinfo.nl / rijksoverheid.nl / trimbos.nl).
"""

ARTICLES = [
    {
        "slug": "lachgas-en-alcohol", "label": "Gezondheid",
        "title": "Lachgas en alcohol combineren: waarom het riskant is",
        "description": "Lachgas en alcohol combineren vergroot de kans op flauwvallen, misselijkheid, vallen en foute inschattingen. Herken de signalen en bel op tijd 112.",
        "h1": "Lachgas en alcohol: waarom combineren extra risico geeft",
        "lead": "Lachgas en alcohol versterken elkaar op een manier die lastig te voorspellen is. Dit is wat er in je lichaam gebeurt, welke signalen op gevaar wijzen en wanneer je hulp inschakelt.",
        "sections": [
            {
                "h2": "Twee dempende middelen tegelijk",
                "paragraphs": [
                    """Lachgas en alcohol werken allebei dempend op het centrale zenuwstelsel. Alcohol vertraagt je reactievermogen, verlaagt je remmingen en maakt je coördinatie slechter. Lachgas verdringt tijdelijk zuurstof in je longen en geeft een kortdurende roes waarin je omgeving vervaagt. Wie de twee combineert, stapelt die effecten: het lichaam krijgt minder zuurstof op een moment dat de hersenen al trager werken. Daardoor is de kans op flauwvallen, overgeven en ongelukken bij een combinatie duidelijk groter dan bij elk middel apart. Dit is geen gebruiksadvies, wel informatie waarmee je in een lastige situatie beter kunt handelen.""",
                    """Het Trimbos-instituut waarschuwt specifiek voor het combineren van lachgas met alcohol en andere middelen. Niet omdat elke combinatie direct levensgevaarlijk is, maar omdat de voorspelbaarheid verdwijnt: wat iemand nuchter zonder problemen ervaart, kan met drank in het lichaam een heel ander effect hebben. Onafhankelijke informatie hierover vind je op <a href="https://www.drugsinfo.nl">drugsinfo.nl</a>. De basisfeiten over het gas zelf staan in <a href="/lachgas-informatie/wat-is-lachgas/">wat is lachgas</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Wat er in je lichaam gebeurt",
                "paragraphs": [
                    """Alcohol verwijdt de bloedvaten en verlaagt de bloeddruk. Lachgas zorgt ervoor dat er korte tijd minder zuurstof in het bloed komt. Samen kan dat leiden tot een plotselinge daling van de bloeddruk en een tekort aan zuurstof in de hersenen, met duizeligheid en flauwvallen als gevolg. Daarnaast prikkelt alcohol de maag en veroorzaakt lachgas bij veel mensen misselijkheid, dus de kans op overgeven neemt toe. Wie overgeeft terwijl het bewustzijn verlaagd is, loopt het risico braaksel in te ademen. Dat is een van de redenen dat hulpdiensten combinaties van middelen als extra gevaarlijk beschouwen.""",
                ],
                "bullets": [
                    """<strong>Bloeddruk.</strong> Beide middelen verlagen de bloeddruk; de combinatie kan een plotselinge dip geven waardoor je omvalt.""",
                    """<strong>Zuurstof.</strong> Lachgas verdringt zuurstof, terwijl alcohol je ademhaling vertraagt. Het lichaam heeft daardoor minder reserve.""",
                    """<strong>Misselijkheid.</strong> Overgeven komt vaker voor en is gevaarlijker bij een verlaagd bewustzijn.""",
                    """<strong>Bewustzijn.</strong> De roes van lachgas en de sufheid van alcohol versterken elkaar; wegraken duurt langer en is dieper.""",
                    """<strong>Lichaamstemperatuur.</strong> Alcohol verstoort je warmteregulatie; buiten in de kou merk je afkoeling minder snel op.""",
                ],
            },
            {
                "h2": "Vallen en verkeerde inschattingen",
                "paragraphs": [
                    """Een groot deel van de ongevallen met lachgas heeft niets te maken met het gas zelf, maar met vallen. Wie staat tijdens een roes kan omvallen, en met alcohol in het lichaam is de kans groter dat je niet op tijd reageert of je hoofd stoot. Hoofdletsel is een van de meest gemelde verwondingen op de spoedeisende hulp na lachgasgebruik. Bij harde ondergronden, trappen, balkons en water, denk aan de Maas, de singels en de havens in Rotterdam, is het risico nog groter dan binnen op een bank.""",
                    """Daar komt bij dat alcohol je oordeel aantast. Je schat afstanden, hoeveelheden en je eigen toestand slechter in. Mensen die gedronken hebben, zijn eerder geneigd door te gaan terwijl hun lichaam al signalen geeft, of om in een auto of op een fiets te stappen. Over dat laatste lees je meer in <a href="/lachgas-informatie/lachgas-in-het-verkeer/">lachgas in het verkeer</a>. Ook de inschatting of een vriend hulp nodig heeft, wordt slechter naarmate iedereen in de groep meer gedronken heeft.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Andere middelen: cannabis, GHB, ketamine en medicatie",
                "paragraphs": [
                    """Niet alleen alcohol is een risicovolle combinatie. Cannabis versterkt duizeligheid en misselijkheid en kan paniekgevoelens oproepen. GHB en ketamine zijn net als alcohol dempende middelen; met lachgas erbij wordt bewusteloosheid waarschijnlijker en moeilijker te onderscheiden van een gewone roes. Stimulerende middelen zoals cocaïne of speed belasten hart en bloedvaten, terwijl lachgas op dat moment de zuurstoftoevoer verlaagt. En wie medicijnen gebruikt, bijvoorbeeld bloeddrukverlagers, slaapmiddelen, antidepressiva of middelen tegen epilepsie, moet weten dat lachgas daar onvoorspelbaar op kan reageren. Drugsinfo.nl geeft per combinatie een overzicht van de bekende risico's.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Signalen dat het misgaat",
                "paragraphs": [
                    """Een roes van lachgas duurt normaal gesproken kort en iemand komt binnen een minuut weer bij. Bij een combinatie met alcohol of andere middelen kan dat anders lopen. Het lastige is dat een groep waarin iedereen gedronken heeft, de signalen later opmerkt en eerder denkt dat iemand 'gewoon even weg is'. Spreek daarom vooraf af dat minstens één persoon nuchter blijft en een oogje in het zeil houdt. Let op de volgende signalen en handel direct als je er een ziet.""",
                ],
                "bullets": [
                    """Iemand komt na een minuut niet bij of reageert niet op aanspreken en zacht schudden.""",
                    """Blauwe lippen, een grauwe huid of een onregelmatige, oppervlakkige ademhaling.""",
                    """Overgeven terwijl iemand suf is of op de rug ligt.""",
                    """Een val met een klap op het hoofd, ook als de persoon zegt dat het wel gaat.""",
                    """Verwardheid, krampen, trillen of stuiptrekkingen.""",
                    """Een hartslag die opvallend snel, traag of onregelmatig is.""",
                ],
            },
            {
                "h2": "Wanneer bel je 112 en wat doe je in de tussentijd",
                "paragraphs": [
                    """Twijfel je, bel dan 112. Je hoeft niet zeker te weten dat het ernstig is; de meldkamer helpt je inschatten en stuurt zo nodig een ambulance. Zeg eerlijk wat er gebruikt is: lachgas, alcohol en eventueel andere middelen. Hulpverleners zijn er om te helpen, niet om te oordelen, en die informatie bepaalt welke behandeling iemand krijgt. Blijf aan de lijn en volg de aanwijzingen van de centralist op.""",
                    """Zorg in de tussentijd voor frisse lucht en leg iemand die buiten bewustzijn is maar wel ademt in de stabiele zijligging, zodat braaksel niet in de luchtpijp komt. Blijf erbij en controleer de ademhaling. Houd de persoon warm met een jas of deken. Ademt iemand niet, start dan reanimatie als je dat kunt; de meldkamer begeleidt je stap voor stap. Meer over eerste hulp lees je in <a href="/lachgas-informatie/lachgas-bijwerkingen-en-eerste-hulp/">lachgas bijwerkingen en eerste hulp</a>.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Dit artikel geeft algemene informatie en is geen medisch advies. Bij twijfel over iemands toestand bel je 112. Onafhankelijke informatie over het combineren van middelen vind je bij <a href="https://www.drugsinfo.nl">drugsinfo.nl</a> van het Trimbos-instituut. Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder.""",
        "related": ["lachgas-bijwerkingen-en-eerste-hulp", "lachgas-in-het-verkeer", "wat-is-lachgas"],
    },
    {
        "slug": "lachgas-bijwerkingen-en-eerste-hulp", "label": "Veiligheid",
        "title": "Lachgas bijwerkingen en eerste hulp: wat je moet weten",
        "description": "Lachgas bijwerkingen op korte en lange termijn: duizeligheid, hoofdpijn, tintelingen, bevriezingsletsel, B12-tekort. Wat doe je als iemand onwel wordt?",
        "h1": "Lachgas bijwerkingen en eerste hulp",
        "lead": "Lachgas is niet onschuldig. Dit zijn de bijwerkingen op korte en lange termijn, en dit doe je als iemand in je buurt onwel wordt.",
        "sections": [
            {
                "h2": "Bijwerkingen op korte termijn",
                "paragraphs": [
                    """De roes van lachgas is kort, maar de bijwerkingen kunnen langer aanhouden dan de roes zelf. De meeste klachten ontstaan doordat de hersenen tijdelijk minder zuurstof krijgen en doordat het gas het evenwichtsorgaan en de maag beïnvloedt. Bij de meeste mensen verdwijnen ze binnen een uur, maar ze maken je in de tussentijd kwetsbaarder voor ongelukken. Hoofdpijn en een licht gevoel in het hoofd zijn de meest genoemde klachten, gevolgd door misselijkheid en tintelingen in handen en voeten.""",
                ],
                "bullets": [
                    """<strong>Duizeligheid.</strong> Een draaierig of zwevend gevoel dat enkele minuten tot een half uur kan aanhouden, met valgevaar als belangrijkste risico.""",
                    """<strong>Hoofdpijn.</strong> Vaak drukkend, soms kloppend, en versterkt door weinig drinken, lawaai en slaapgebrek.""",
                    """<strong>Misselijkheid en overgeven.</strong> Vooral in combinatie met alcohol of een volle maag.""",
                    """<strong>Tintelingen.</strong> Prikkelingen in vingers, tenen of lippen. Houden ze uren aan of komen ze terug, dan is dat een vroeg teken van een vitamine B12-probleem.""",
                    """<strong>Flauwvallen.</strong> Een kort zuurstoftekort in de hersenen kan leiden tot wegraken, zeker bij staan.""",
                    """<strong>Verwardheid en gehoorsensaties.</strong> Vervormd geluid, oorsuizen en moeite met praten of nadenken, meestal kortdurend.""",
                    """<strong>Hartkloppingen.</strong> Een snelle of onregelmatige hartslag, vooral bij mensen met hart- of longklachten.""",
                ],
            },
            {
                "h2": "Bevriezingsletsel door kou uit de tank",
                "paragraphs": [
                    """Een risico dat vaak wordt onderschat, is bevriezingsletsel. Lachgas zit als vloeistof onder druk in de tank. Wanneer het gas ontsnapt en uitzet, koelt het razendsnel af tot ver onder nul; ook de kraan en de bovenkant van de tank worden ijskoud. Direct contact van huid, lippen of mond met dat koude metaal of met de gasstraal veroorzaakt binnen seconden een koudebrandwond. Op de spoedeisende hulp worden regelmatig bevriezingswonden aan lippen, neus, handen en dijen gezien die terug te voeren zijn op lachgas.""",
                    """Een koudebrandwond herken je aan een witte, harde of wasachtige plek die eerst gevoelloos is en daarna pijnlijk, rood en gezwollen wordt; soms ontstaan blaren. Spoel de plek met lauw, niet heet, water, wrijf niet en dek de wond losjes af. Bij blaren, een grote wond of aantasting van lippen of ogen ga je naar de huisartsenpost of de spoedeisende hulp. Een liggende of omgevallen tank vergroot het risico; lees waarom in <a href="/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/">lachgas tank bewaren en vervoeren</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Risico's op lange termijn",
                "paragraphs": [
                    """Wie vaker of langdurig lachgas gebruikt, loopt risico's die niet na een uur verdwijnen. De belangrijkste is een functioneel tekort aan vitamine B12: lachgas maakt de B12 in je lichaam onwerkzaam, ook als je er via voeding genoeg van binnenkrijgt. B12 is nodig voor de aanmaak van rode bloedcellen en voor de beschermlaag rond je zenuwen. Een tekort geeft eerst vermoeidheid en tintelingen, later gevoelloosheid, spierzwakte, moeite met lopen en in ernstige gevallen blijvende zenuwschade in het ruggenmerg. De uitgebreide uitleg staat in <a href="/lachgas-informatie/lachgas-en-vitamine-b12/">lachgas en vitamine B12</a>.""",
                    """Daarnaast kan lachgas psychisch afhankelijk maken. Het effect is kort en de drempel om opnieuw te gebruiken is laag, waardoor sommige mensen in korte tijd veel gaan gebruiken. Het Trimbos-instituut en verslavingszorginstellingen zien sinds enkele jaren meer mensen met problematisch lachgasgebruik, vaak jongvolwassenen. Hoe je dat herkent en waar je hulp vindt, lees je in <a href="/lachgas-informatie/lachgas-afkicken-en-hulp/">problematisch lachgasgebruik: signalen en hulp</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Als iemand onwel wordt",
                "paragraphs": [
                    """Wordt iemand in je buurt onwel na lachgasgebruik, dan tellen de eerste minuten. De belangrijkste doelen zijn zuurstof, een vrije luchtweg en voorkomen dat iemand valt of braaksel inademt. Blijf kalm en blijf bij de persoon. Je hebt geen medische kennis nodig om de stappen hieronder toe te passen, en het is altijd beter om onnodig 112 te bellen dan te laat. Doorloop de stappen op volgorde.""",
                ],
                "bullets": [
                    """<strong>Frisse lucht.</strong> Haal de persoon weg bij de tank en zet een raam open of ga naar buiten.""",
                    """<strong>Aanspreken.</strong> Spreek de persoon aan en schud zacht aan de schouders. Komt er reactie, laat de persoon dan rustig zitten of liggen met de benen iets omhoog.""",
                    """<strong>Stabiele zijligging.</strong> Geen reactie maar wel ademhaling: leg de persoon op de zij, hoofd iets naar achteren en mond naar beneden, zodat braaksel weg kan lopen.""",
                    """<strong>112.</strong> Bel bij geen reactie binnen een minuut, blauwe lippen, onregelmatige ademhaling, krampen of een val op het hoofd. Noem eerlijk wat er is gebruikt.""",
                    """<strong>Reanimatie.</strong> Ademt iemand niet, start dan reanimatie als je dat kunt; de meldkamer begeleidt je.""",
                    """<strong>Blijf erbij.</strong> Houd de persoon warm en laat niemand alleen 'uitslapen' in een andere kamer.""",
                ],
            },
            {
                "h2": "Wanneer ga je naar de huisarts",
                "paragraphs": [
                    """Niet elke klacht is een spoedgeval, maar sommige verdienen wel een afspraak. Ga naar je huisarts bij tintelingen of gevoelloosheid die langer dan een dag aanhouden of terugkomen, bij moeite met lopen of een onvast gevoel, bij hoofdpijn die niet verdwijnt, of als je merkt dat je steeds meer gebruikt. Vertel eerlijk dat je lachgas hebt gebruikt; de huisarts kan dan gericht je B12 laten bepalen en zo nodig doorverwijzen. Hoe eerder zenuwklachten worden behandeld, hoe groter de kans op volledig herstel. Algemene informatie vind je bij <a href="https://www.drugsinfo.nl">drugsinfo.nl</a>.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Dit artikel geeft algemene informatie en is geen vervanging voor medisch advies. Bel bij een noodgeval 112 en neem bij aanhoudende klachten contact op met je huisarts. Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder.""",
        "related": ["lachgas-en-vitamine-b12", "lachgas-en-alcohol", "lachgas-tank-bewaren-en-vervoeren"],
    },
    {
        "slug": "lachgas-bezorgservice-kiezen", "label": "Praktisch",
        "title": "Lachgas bezorgservice kiezen: waar let je op?",
        "description": "Een lachgas bezorgservice kiezen in Rotterdam? Checklist: bereikbaarheid, prijs vooraf, verzegelde tanks, leeftijdscontrole, discretie en eerlijke info.",
        "h1": "Een lachgas bezorgservice kiezen: waar let je op?",
        "lead": "Er zijn veel bezorgservices actief in Rotterdam en de verschillen zijn groot. Met deze checklist zie je snel of een aanbieder serieus en betrouwbaar is.",
        "sections": [
            {
                "h2": "Waarom de keuze ertoe doet",
                "paragraphs": [
                    """Een lachgastank is een drukhouder met een gas dat gezondheidsrisico's heeft. Wie zo'n product aan huis levert, draagt verantwoordelijkheid: voor de staat van de tank, voor wie hem ontvangt en voor de informatie die erbij komt. Toch gaat het bij veel aanbieders alleen over snelheid en hoeveelheid. Als volwassene in Rotterdam heb je de keuze, en het loont om die bewust te maken. Een slordige service levert niet alleen een slechtere ervaring, maar vergroot ook de kans op een beschadigde tank, onduidelijke kosten of gedoe aan de deur.""",
                    """Hieronder staat waar je op let, zonder namen van aanbieders. Gebruik de punten als checklist bij elke service, inclusief de onze, en vergelijk aanbieders steeds op dezelfde manier. Niet elk punt weegt even zwaar, maar een aanbieder die op meerdere punten tekortschiet, kun je beter laten liggen. Hoe wij zelf werken en wat je van ons mag verwachten, lees je op <a href="/werkwijze/">werkwijze</a> en <a href="/voordelen/">voordelen</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "De checklist",
                "paragraphs": [
                    """Loop deze punten door voordat je bestelt. Een goede service hoeft hier niet over na te denken; de antwoorden staan gewoon op de website of komen vanzelf in het eerste WhatsApp-bericht, zonder dat je ernaar hoeft te vragen. Twijfel je over een punt, stel de vraag dan gewoon. Aan de manier waarop een aanbieder reageert op een kritische vraag, merk je vaak al genoeg over hoe serieus hij zijn klanten neemt.""",
                ],
                "bullets": [
                    """<strong>Bereikbaarheid.</strong> Is er één duidelijk kanaal waarop je snel antwoord krijgt, ook 's avonds en in het weekend? Een service die overdag pas na een uur reageert, is 's nachts ook niet bereikbaar.""",
                    """<strong>Prijs vooraf.</strong> Je hoort het totaalbedrag inclusief bezorging voordat de bezorger vertrekt, en dat bedrag verandert niet aan de deur.""",
                    """<strong>Verzegelde tanks.</strong> De tank komt verzegeld aan, met een intacte kraan en zonder deuken of roest. Vraag ernaar als het niet op de website staat.""",
                    """<strong>Leeftijdscontrole.</strong> Een serieuze service vraagt om een legitimatie en levert niet aan minderjarigen. Dat is geen wantrouwen, maar fatsoen.""",
                    """<strong>Discretie.</strong> Neutrale verpakking, een bezorger zonder opvallende reclame en geen gegevens die langer bewaard worden dan nodig.""",
                    """<strong>Eerlijke informatie.</strong> De aanbieder benoemt risico's en de wettelijke situatie en verwijst naar onafhankelijke bronnen, in plaats van te doen alsof lachgas onschuldig is.""",
                    """<strong>Geen druk.</strong> Je krijgt geen opdringerige berichten om meer of groter te bestellen en geen acties die aanzetten tot meer gebruik.""",
                ],
            },
            {
                "h2": "Rode vlaggen",
                "paragraphs": [
                    """Sommige signalen zijn een reden om een aanbieder meteen te laten liggen, hoe snel of aantrekkelijk die zich ook presenteert. Ze wijzen erop dat de service vooral bezig is met omzet en niet met de mensen aan wie hij levert. Kom je een van de onderstaande punten tegen, zoek dan verder; er is in Rotterdam genoeg keuze en een serieuze aanbieder vind je snel.""",
                ],
                "bullets": [
                    """Geen enkele vermelding van een leeftijdsgrens, of een bezorger die zonder vragen levert aan iemand die duidelijk jong is.""",
                    """Een totaalbedrag dat pas aan de deur duidelijk wordt, of dat hoger uitvalt dan afgesproken.""",
                    """Tanks zonder verzegeling, met deuken, een losse kraan of een afwijkende kleur.""",
                    """Teksten die lachgas als onschuldig neerzetten of het vergelijken met een onschuldige traktatie.""",
                    """Aandringen op grotere maten of combinaties omdat dat 'voordeliger' zou zijn.""",
                    """Verzoeken om een foto van je legitimatie te sturen voordat er iets geleverd is, of om vooruit te betalen op een privérekening.""",
                ],
            },
            {
                "h2": "Zo werken wij",
                "paragraphs": [
                    """Wij zijn een van de bezorgservices in Rotterdam en meten ons graag aan dezelfde lat. Je bestelt via WhatsApp met je adres, de gewenste maat (2KG, 4KG of 10KG) en het tijdstip, en je krijgt het totaalbedrag vooraf bevestigd. Betalen doe je bij levering, contant of via Tikkie. We leveren uitsluitend aan personen van 18 jaar en ouder en vragen daarom om een legitimatie aan de deur. De tanks komen verzegeld aan en we bewaren geen gegevens die we niet nodig hebben voor de levering. Op <a href="/voordelen/">voordelen</a> en <a href="/werkwijze/">werkwijze</a> lees je precies wat je van ons kunt verwachten.""",
                    """Even belangrijk: we schrijven eerlijk over de risico's en de regels, ook als dat commercieel niet het handigste verhaal is. Lachgas staat sinds 2023 op lijst II van de Opiumwet, met uitzonderingen voor medisch, technisch en voedingsgebruik; lees daarover <a href="/lachgas-informatie/is-lachgas-legaal-in-nederland/">is lachgas legaal in Nederland</a>. Op <a href="/veilig-gebruik/">veilig gebruik</a> staat wat je moet weten voordat je bestelt. Een service die daarover zwijgt, verdient wat ons betreft je wantrouwen.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Samengevat",
                "paragraphs": [
                    """Een betrouwbare lachgas bezorgservice in Rotterdam is bereikbaar, noemt het totaalbedrag vooraf, levert verzegelde tanks, controleert leeftijd, werkt discreet, informeert eerlijk en zet je niet onder druk. Ontbreken meerdere van die punten, kies dan een andere aanbieder. Heb je vragen over hoe wij werken, stuur ons dan een bericht via WhatsApp; je krijgt een eerlijk antwoord, ook als dat betekent dat je beter niet bestelt.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder. Dit artikel noemt bewust geen andere aanbieders; de checklist geldt voor elke bezorgservice, inclusief de onze. Lees over de wettelijke situatie op <a href="https://www.rijksoverheid.nl">rijksoverheid.nl</a>.""",
        "related": ["lachgastank-2kg-4kg-of-10kg", "lachgas-tank-bewaren-en-vervoeren", "is-lachgas-legaal-in-nederland"],
    },
    {
        "slug": "lachgastank-2kg-4kg-of-10kg", "label": "Producten",
        "title": "Lachgastank 2KG, 4KG of 10KG: welke maat past?",
        "description": "Lachgastank 2KG, 4KG of 10KG: de verschillen in gewicht, afmetingen en gebruikssituatie, van klein gezelschap tot evenement, plus bewaren en verzegeling.",
        "h1": "Lachgastank 2KG, 4KG of 10KG: welke maat past?",
        "lead": "Dezelfde inhoud, drie formaten. Het verschil zit in gewicht, afmetingen en de situatie waarvoor je bestelt.",
        "sections": [
            {
                "h2": "Drie formaten, dezelfde inhoud",
                "paragraphs": [
                    """Alle lachgastanks die wij bezorgen bevatten hetzelfde: distikstofmonoxide (N2O) van voedingskwaliteit, onder druk in een stalen cilinder. Het getal in de naam, 2KG, 4KG of 10KG, staat voor de nettohoeveelheid gas in kilogram. De tank zelf weegt daar nog bovenop, want een drukhouder is van dik staal en heeft een kraan en vaak een beschermkap. Het verschil tussen de maten zit dus niet in de kwaliteit of de werking, maar in hoeveel gas erin zit, hoe zwaar en groot de tank is en hoe lang je ermee doet.""",
                    """Op <a href="/lachgas-tanks/">lachgas tanks</a> staan de drie formaten naast elkaar. In dit artikel gaan we dieper in op de praktische kant: wat weegt zo'n tank eigenlijk, past hij in je auto of in de lift, en welk formaat is logisch voor welke situatie. We noemen bewust geen aantallen per tank, omdat dat sterk afhangt van de omstandigheden en omdat we niemand willen aanzetten tot meer gebruik dan gepland.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Gewicht en afmetingen",
                "paragraphs": [
                    """De getallen hieronder zijn indicaties; cilinders van verschillende fabrikanten verschillen iets in maat en wanddikte, en ook de kraan en de beschermkap tellen mee. Houd er rekening mee dat het totaalgewicht beduidend hoger ligt dan het nettogewicht van het gas. Een 10KG tank til je niet zomaar drie trappen op in een portiekwoning; vraag dan hulp of laat ons bezorgen tot aan de deur van de locatie.""",
                ],
                "bullets": [
                    """<strong>2KG tank.</strong> Ongeveer 2 kilo netto N2O; totaalgewicht met cilinder en kraan rond de 4 tot 5 kilo. Hoogte ruwweg 40 tot 45 centimeter, diameter zo'n 10 tot 12 centimeter. Past rechtop in een stevige tas of krat.""",
                    """<strong>4KG tank.</strong> Ongeveer 4 kilo netto; totaal rond de 7 tot 9 kilo. Hoogte ongeveer 50 tot 55 centimeter. Nog goed te tillen door één persoon, maar niet geschikt voor de fiets of scooter.""",
                    """<strong>10KG tank.</strong> Ongeveer 10 kilo netto; totaal al snel 15 tot 20 kilo. Hoogte rond de 70 tot 80 centimeter, diameter 18 tot 20 centimeter. Vraagt een vaste, rechtopstaande plek en bij voorkeur twee personen om te verplaatsen.""",
                ],
            },
            {
                "h2": "Welke maat voor welke situatie",
                "paragraphs": [
                    """Een klein gezelschap thuis, een verjaardag met een handvol vrienden of een avond op een bovenwoning in Kralingen: dan is een 2KG tank de logische keuze. Hij is licht, neemt weinig ruimte in en is makkelijk rechtop weg te zetten. Voor een groter huisfeest of een avond met een grotere groep kiezen veel klanten een 4KG tank, omdat die nog hanteerbaar is maar langer meegaat zonder dat je hoeft bij te bestellen.""",
                    """De 10KG tank is bedoeld voor evenementen, grotere feesten of locaties waar meerdere kleinere tanks onpraktisch zouden zijn, bijvoorbeeld een loods, een gehuurde zaal of een terrein met een vaste plek voor de tank. Vanwege het gewicht en de afmetingen is het verstandig vooraf te bedenken waar de tank komt te staan en wie hem verplaatst. Organiseer je iets groters, lees dan ook <a href="/lachgas-feest-evenement/">lachgas voor feest en evenement</a>; daar staat wat je vooraf regelt en waarom we bij grote bestellingen graag even overleggen.""",
                    """Twijfel je tussen twee maten? Kies liever de kleinere en bestel bij als dat nodig blijkt. Een grotere tank nodigt uit tot meer gebruik dan je van plan was, en een halfvolle tank staat daarna maandenlang in de weg. In Rotterdam zijn we bij een nabestelling meestal binnen 20 tot 30 minuten terug, dus je hoeft niet op voorhand groot in te kopen.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Bewaren en vervoeren per formaat",
                "paragraphs": [
                    """De regels zijn voor elk formaat hetzelfde: rechtop, vastgezet, koel, droog, uit de zon en met de kraan dicht. Het verschil zit in de praktijk. Een 2KG tank zet je makkelijk in een hoek of kast; een 10KG tank heeft een vaste plek nodig waar hij niet omgeduwd kan worden, bijvoorbeeld tegen een muur met een spanband. In de auto geldt voor elke maat: nooit achterlaten in een warme wagen, altijd rechtop en vastgezet in de kofferbak, en nuchter achter het stuur. Alle details staan in <a href="/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/">lachgas tank bewaren en vervoeren</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Verzegeling en controle bij levering",
                "paragraphs": [
                    """Elke tank komt verzegeld bij je aan, ongeacht het formaat. De verzegeling laat zien dat de tank na het vullen niet geopend is en dat de kraan ongebruikt is. Controleer bij ontvangst drie dingen: is het zegel intact, zit de kraan vast en vertoont de cilinder geen deuken of roest? Is er iets niet in orde, neem de tank dan niet aan en laat het ons direct weten via WhatsApp; we wisselen hem om. We leveren uitsluitend aan personen van 18 jaar en ouder en vragen om een legitimatie aan de deur. Lees ook de basisregels op <a href="/veilig-gebruik/">veilig gebruik</a>.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Gewichten en afmetingen zijn indicaties en kunnen per fabrikant iets afwijken. Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder; het totaalbedrag hoor je vooraf via WhatsApp.""",
        "related": ["lachgas-tank-bewaren-en-vervoeren", "lachgas-bezorgservice-kiezen", "wat-is-lachgas"],
    },
    {
        "slug": "lachgas-en-het-milieu", "label": "Achtergrond",
        "title": "Lachgas en het milieu: wat je moet weten",
        "description": "Lachgas (N2O) is een broeikasgas, 265 tot 300 keer sterker dan CO2. Waar komt de uitstoot vandaan, wat draagt recreatief gebruik bij en wat doe je zelf?",
        "h1": "Lachgas en het milieu: wat je moet weten",
        "lead": "Distikstofmonoxide is niet alleen een roesmiddel, maar ook een krachtig broeikasgas. Dit is wat erover bekend is en wat je zelf kunt doen.",
        "sections": [
            {
                "h2": "N2O als broeikasgas",
                "paragraphs": [
                    """Distikstofmonoxide, de stof in een lachgastank, is naast koolstofdioxide en methaan het derde belangrijke broeikasgas dat door menselijk handelen in de atmosfeer komt. Per kilogram houdt N2O over een periode van honderd jaar ongeveer 265 tot 300 keer zoveel warmte vast als CO2. Het gas blijft bovendien lang in de atmosfeer, ruim honderd jaar, en draagt in de hogere luchtlagen bij aan de afbraak van de ozonlaag. Een kleine hoeveelheid N2O heeft dus een onevenredig groot effect op het klimaat.""",
                    """Het aandeel van N2O in de totale Nederlandse broeikasgasuitstoot ligt volgens cijfers van het RIVM en de Emissieregistratie op enkele procenten, uitgedrukt in CO2-equivalenten. Dat is veel kleiner dan het aandeel van CO2, maar niet verwaarloosbaar. De Nederlandse N2O-uitstoot is sinds 1990 flink gedaald, vooral door maatregelen in de chemische industrie en de landbouw. Op <a href="https://www.rijksoverheid.nl">rijksoverheid.nl</a> vind je het klimaatbeleid waarin de verdere reductie van N2O een eigen plek heeft.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Waar komt de uitstoot vandaan",
                "paragraphs": [
                    """Het grootste deel van de N2O-uitstoot in Nederland komt uit de landbouw. Wanneer stikstof uit kunstmest en dierlijke mest in de bodem terechtkomt, zetten bacteriën een deel ervan om in N2O. Ook mestopslag en begrazing dragen bij. Daarnaast ontstaat N2O bij verbrandingsprocessen in verkeer en industrie, bij de productie van kunstmest en bepaalde chemicaliën, en in rioolwaterzuiveringen. Medisch gebruik als narcosemiddel in ziekenhuizen en tandartspraktijken is een kleine, aparte bron die in sommige landen inmiddels wordt afgebouwd.""",
                ],
                "bullets": [
                    """<strong>Landbouw.</strong> Bemesting en veehouderij; in Nederland verreweg de grootste bron.""",
                    """<strong>Industrie.</strong> Productie van kunstmest, salpeterzuur en caprolactam; sterk teruggebracht sinds de jaren negentig.""",
                    """<strong>Verkeer en verbranding.</strong> Een beperkte bijdrage uit motoren en verbrandingsinstallaties.""",
                    """<strong>Waterzuivering.</strong> Rioolwaterzuiveringen stoten N2O uit bij de afbraak van stikstofverbindingen.""",
                    """<strong>Medisch en recreatief gebruik.</strong> Relatief klein, maar het gas komt direct en volledig in de atmosfeer.""",
                ],
            },
            {
                "h2": "Het aandeel van recreatief gebruik",
                "paragraphs": [
                    """Hoe groot het aandeel van recreatief gebruik precies is, is lastig vast te stellen; er zijn geen volledige cijfers over het aantal tanks en patronen dat jaarlijks in Nederland wordt gebruikt. Schattingen op basis van verkoopcijfers wijzen erop dat het gaat om een klein deel van de totale N2O-uitstoot, waarschijnlijk minder dan één procent. Dat klinkt gering, maar het verschil met de landbouw is dat recreatief gebruikt lachgas voor honderd procent in de atmosfeer terechtkomt: elke kilo die uit een tank komt, is een kilo broeikasgas.""",
                    """Daar komt een tweede milieuprobleem bij: zwerfafval. Lege patronen en tanks in parken, op straat en in het water zijn in veel steden, ook in Rotterdam, een zichtbaar probleem. Stalen tanks horen niet in de natuur en ook niet bij het restafval, omdat ze bij de afvalverwerking restdruk kunnen bevatten en in een verbrandingsoven gevaarlijk zijn. Meer over de regels rond lachgas lees je in <a href="/lachgas-informatie/is-lachgas-legaal-in-nederland/">is lachgas legaal in Nederland</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Wat je zelf kunt doen",
                "paragraphs": [
                    """Je hebt als volwassene die lachgas bestelt geen invloed op de landbouw, maar wel op wat er met jouw tank gebeurt. Een paar gewoontes maken het verschil tussen een tank die netjes wordt hergebruikt of gerecycled en een tank die in de Kralingse Plas of de Nieuwe Maas eindigt. Ze kosten weinig moeite en zijn eigenlijk niet meer dan normaal omgaan met een drukhouder.""",
                ],
                "bullets": [
                    """<strong>Kraan dicht.</strong> Laat een tank nooit leeglopen om hem 'leeg te krijgen'. Alles wat ontsnapt, is direct broeikasgas.""",
                    """<strong>Niet in de natuur of op straat.</strong> Een lege tank hoort niet in het park, langs de singel of naast een afvalbak.""",
                    """<strong>Niet bij het restafval.</strong> Een drukhouder in de vuilniswagen of verbrandingsoven is gevaarlijk voor afvalverwerkers.""",
                    """<strong>Inleveren of retour.</strong> Breng een lege tank naar het milieupark van je gemeente, of vraag ons via WhatsApp naar retour bij een volgende levering.""",
                    """<strong>Bestel niet meer dan nodig.</strong> Een tank die maanden halfvol staat, loopt vaker leeg en wordt vaker verkeerd weggegooid.""",
                ],
            },
            {
                "h2": "Samengevat",
                "paragraphs": [
                    """N2O is een krachtig broeikasgas dat vooral uit de landbouw komt; recreatief gebruik is een klein maar niet verwaarloosbaar deel, en zwerfafval van tanks en patronen is een probleem op zich. Wat je zelf kunt doen is eenvoudig: kraan dicht, tank niet laten leeglopen, en een lege tank inleveren of retour geven in plaats van hem bij het afval of in de natuur te zetten. Hoe je een tank bewaart en vervoert tot het moment van inleveren, lees je in <a href="/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/">lachgas tank bewaren en vervoeren</a>.""",
                ],
                "bullets": [],
            },
        ],
        "note": """De genoemde cijfers zijn afgerond en gebaseerd op openbare bronnen van onder meer het RIVM en de Rijksoverheid; exacte waarden verschillen per rapportage en jaar. Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder.""",
        "related": ["lachgas-tank-bewaren-en-vervoeren", "wat-is-lachgas", "is-lachgas-legaal-in-nederland"],
    },
    {
        "slug": "lachgas-afkicken-en-hulp", "label": "Hulp",
        "title": "Problematisch lachgasgebruik: signalen en hulp",
        "description": "Wanneer wordt lachgasgebruik een probleem? Herken de signalen, begrijp waarom stoppen lastig is en lees waar je in Rotterdam en online hulp vindt.",
        "h1": "Problematisch lachgasgebruik: signalen en hulp",
        "lead": "Voor de meeste mensen blijft het bij af en toe, maar voor sommigen groeit het gebruik uit tot een probleem. Dit zijn de signalen en zo vind je hulp, zonder oordeel.",
        "sections": [
            {
                "h2": "Wanneer wordt gebruik een probleem",
                "paragraphs": [
                    """Er is geen vaste grens waarbij gebruik problematisch wordt. Het gaat niet om een aantal keren per maand, maar om de rol die lachgas in je leven inneemt. Als het gebruik vaker wordt dan je zelf wilt, als je er dingen voor laat die je belangrijk vindt, of als je lichamelijke klachten krijgt en toch doorgaat, dan is er reden om stil te staan. Het Trimbos-instituut ziet dat een kleine groep gebruikers in korte tijd heel veel gaat gebruiken, soms dagelijks en in grote hoeveelheden. Juist bij die groep ontstaan de ernstigste gezondheidsproblemen.""",
                    """Dit artikel is geschreven voor iedereen die zich afvraagt of het eigen gebruik of dat van een naaste uit de hand loopt. We oordelen niet; we beschrijven wat bekend is en waar je terechtkunt. Onafhankelijke informatie vind je bij <a href="https://www.drugsinfo.nl">drugsinfo.nl</a> en <a href="https://www.trimbos.nl">trimbos.nl</a>. Beide bieden ook een informatielijn en chat waar je anoniem je vraag kunt stellen, zonder dat je meteen in een hulptraject terechtkomt.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Signalen van problematisch gebruik",
                "paragraphs": [
                    """De volgende signalen betekenen niet automatisch dat iemand verslaafd is, maar meerdere tegelijk zijn een reden om het gesprek aan te gaan of hulp te zoeken. Let vooral op veranderingen: iemand die vroeger af en toe meedeed op een feest en nu alleen of overdag gebruikt, verdient aandacht. Hetzelfde geldt voor iemand die geïrriteerd of ontwijkend reageert zodra het onderwerp ter sprake komt.""",
                ],
                "bullets": [
                    """Vaker en meer gebruiken dan van plan, of grotere tanks bestellen om niet steeds te hoeven bijbestellen.""",
                    """Alleen gebruiken, of gebruiken op doordeweekse dagen en overdag.""",
                    """Tintelingen, gevoelloosheid, een onvast gevoel bij het lopen of vermoeidheid die niet weggaat: tekenen van een vitamine B12-probleem.""",
                    """Geld, slaap, werk of studie die eronder lijden.""",
                    """Vrienden of familie die zich zorgen maken, en daar geïrriteerd op reageren.""",
                    """Pogingen om te stoppen of te minderen die niet lukken.""",
                    """Lachgas gebruiken om stress, somberheid of verveling weg te drukken in plaats van voor de gelegenheid.""",
                ],
            },
            {
                "h2": "Waarom stoppen lastig kan zijn",
                "paragraphs": [
                    """Lachgas geeft geen zware lichamelijke ontwenningsverschijnselen zoals alcohol of opiaten, en juist daardoor onderschatten mensen hoe moeilijk stoppen kan zijn. De afhankelijkheid is vooral psychisch: het effect is kort, direct en makkelijk te herhalen, en het gevoel van even weg zijn wordt een manier om met spanning of nare gevoelens om te gaan. Omdat een tank thuis staat en bestellen eenvoudig is, ontbreken de natuurlijke remmen die er bij andere middelen wel zijn.""",
                    """Daar komt bij dat de lichamelijke gevolgen, zoals een tekort aan vitamine B12, concentratieproblemen en vermoeidheid kunnen geven, wat het weer moeilijker maakt om een goed voornemen vol te houden. En in een vriendengroep waar iedereen gebruikt, voelt stoppen als buitengesloten worden. Dat zijn geen excuses, maar wel verklaringen waarom wilskracht alleen vaak niet genoeg is. Lees meer over de lichamelijke kant in <a href="/lachgas-informatie/lachgas-en-vitamine-b12/">lachgas en vitamine B12</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Waar je hulp vindt",
                "paragraphs": [
                    """Je hoeft dit niet alleen te doen, en hulp zoeken is geen teken van zwakte. De huisarts is de eerste stap: die kan je B12-waarden laten controleren, zenuwklachten beoordelen en je doorverwijzen naar verslavingszorg. Een gesprek met de huisarts is vertrouwelijk. In Rotterdam en omgeving bieden verslavingszorginstellingen zoals Antes en Youz (voor jongeren en jongvolwassenen) begeleiding bij problematisch middelengebruik, van een enkel adviesgesprek tot een behandeltraject. Online en anoniem kun je terecht bij <a href="https://www.drugsinfo.nl">drugsinfo.nl</a>, dat een informatielijn en chat heeft, en bij het Trimbos-instituut via <a href="https://www.trimbos.nl">trimbos.nl</a>.""",
                ],
                "bullets": [
                    """<strong>Huisarts.</strong> Voor lichamelijke klachten, een B12-controle en een verwijzing. Vertel eerlijk wat en hoeveel je gebruikt.""",
                    """<strong>Drugsinfo.nl.</strong> Onafhankelijke informatie, een informatielijn en een chat waar je anoniem je vraag kunt stellen.""",
                    """<strong>Trimbos-instituut.</strong> Kennis over middelengebruik en hulp bij het vinden van passende zorg.""",
                    """<strong>Verslavingszorg in Rotterdam.</strong> Antes en Youz bieden advies en behandeling; aanmelden kan vaak ook zonder verwijzing.""",
                    """<strong>112.</strong> Bij een acuut noodgeval, bijvoorbeeld bewusteloosheid of plotselinge uitvalsverschijnselen.""",
                ],
            },
            {
                "h2": "Hoe spreek je iemand aan",
                "paragraphs": [
                    """Maak je je zorgen over een vriend, partner of familielid, dan is de verleiding groot om te waarschuwen of te verbieden. Dat werkt zelden. Kies een rustig moment waarop niemand gebruikt heeft, en vertel wat jij ziet en wat dat met jou doet: 'Ik merk dat je de laatste tijd vaker alleen gebruikt en ik maak me zorgen.' Stel vragen en luister, in plaats van te overtuigen. Bied aan om mee te gaan naar de huisarts of om samen te kijken wat drugsinfo.nl erover zegt.""",
                    """Verwacht geen doorbraak na één gesprek; het gaat erom dat de ander weet dat je er bent zonder oordeel. Blijf grenzen stellen aan wat jij acceptabel vindt, bijvoorbeeld niet gebruiken als je samen bent, zonder de relatie op te zeggen. Zorg ook voor jezelf: verslavingszorginstellingen bieden ook gesprekken voor naasten aan. Twijfel je of iemand direct gevaar loopt, bel dan 112; aarzelen is in zo'n situatie nooit beter dan bellen.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Dit artikel is geen vervanging voor professionele hulp. Maak je je zorgen over je eigen gebruik of dat van een ander, neem dan contact op met je huisarts of met <a href="https://www.drugsinfo.nl">drugsinfo.nl</a>. Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder en helpt je graag met informatie, ook als dat betekent dat je beter niet bestelt.""",
        "related": ["lachgas-en-vitamine-b12", "lachgas-bijwerkingen-en-eerste-hulp", "lachgas-en-alcohol"],
    },
]

SERVICE_PAGES = [
    {
        "slug": "lachgas-spoedbezorging", "label": "Spoed",
        "title": "Lachgas spoedbezorging Rotterdam | Snel aan de deur",
        "description": "Lachgas met spoed nodig in Rotterdam? Wij bezorgen meestal binnen 20 tot 30 minuten, ook 's nachts en in het weekend. Bestel via WhatsApp, alleen voor 18+.",
        "h1": "Lachgas spoedbezorging in Rotterdam",
        "lead": "Snel een lachgastank nodig? In Rotterdam staan we meestal binnen 20 tot 30 minuten aan de deur, 24/7 via WhatsApp.",
        "sections": [
            {
                "h2": "Hoe snel bezorgen we",
                "paragraphs": [
                    """Spoedbezorging is bij ons geen aparte dienst, maar de manier waarop we altijd werken: zodra je bestelling via WhatsApp is bevestigd, vertrekt een bezorger. In Rotterdam zelf staan we meestal binnen 20 tot 30 minuten aan de deur, of je nu in het centrum zit, in Kralingen, op Zuid of in Prins Alexander. In buurgemeenten zoals Schiedam, Capelle aan den IJssel en Barendrecht is dat meestal 25 tot 40 minuten, en voor plaatsen verder weg, zoals Dordrecht, Gouda of Zoetermeer, meestal 35 tot 50 minuten. Bij de bevestiging krijg je altijd een eerlijke indicatie voor dat moment.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Zo laat je het snel verlopen",
                "paragraphs": [
                    """De grootste vertraging ontstaat niet op de weg, maar in het heen-en-weer appen vooraf. Met één compleet bericht en een telefoon die je direct beantwoordt, win je vaak tien minuten. Daarom een paar praktische punten die het verschil maken tussen een vlotte levering en onnodig wachten op de stoep.""",
                ],
                "bullets": [
                    """<strong>Alles in één bericht.</strong> Stuur je volledige adres met postcode, de gewenste maat (2KG, 4KG of 10KG) en het tijdstip. Dan kunnen we direct bevestigen.""",
                    """<strong>Blijf bereikbaar.</strong> Houd je telefoon bij de hand; de bezorger appt als hij er bijna is of de ingang niet vindt.""",
                    """<strong>ID klaar.</strong> We leveren alleen aan 18+ en vragen om een legitimatie. Leg die klaar, dan is de overdracht in een minuut gedaan.""",
                    """<strong>Betaling klaar.</strong> Je betaalt bij levering, contant of via Tikkie. Het totaalbedrag heb je vooraf bevestigd gekregen.""",
                    """<strong>Duidelijke ingang.</strong> Bij een portiek, bedrijventerrein of feestlocatie: noem de bel, de etage of een herkenningspunt.""",
                ],
            },
            {
                "h2": "Wat we niet beloven",
                "paragraphs": [
                    """We zeggen bewust 'meestal' en geven geen garantie. Op vrijdag- en zaterdagavond, bij grote evenementen in de stad, bij noodweer of als de Maastunnel of een brug dicht is, kan het langer duren. In dat geval hoor je dat vooraf, zodat je zelf kunt beslissen of je wacht. We rijden nooit onverantwoord hard om een tijd te halen, en we leveren niet aan iemand die geen legitimatie kan tonen, ook niet bij spoed. Liever een eerlijke 45 minuten dan een loze belofte van 20. Hoe een bestelling precies verloopt, lees je op <a href="/werkwijze/">werkwijze</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Ook 's nachts en in de regio",
                "paragraphs": [
                    """Spoed houdt zich niet aan kantooruren. We zijn 24/7 bereikbaar via WhatsApp, ook na middernacht en in het weekend; lees meer op <a href="/lachgas-nachtbezorging/">lachgas nachtbezorging</a>. Buiten Rotterdam bezorgen we in de hele regio, van Hoek van Holland tot Dordrecht en van Delft tot Oud-Beijerland. Op <a href="/bezorggebieden/">bezorggebieden</a> vind je per plaats de gebruikelijke levertijd en de wijken die we aandoen. Ook daar geldt: hoe completer je eerste bericht, hoe sneller we kunnen bevestigen en vertrekken.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Levertijden zijn indicaties op basis van onze ervaring en geen garantie. Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder, verzegeld en met legitimatiecontrole aan de deur. Lees de basisregels op <a href="/veilig-gebruik/">veilig gebruik</a>.""",
        "faq": [
            ["Hoe snel kunnen jullie er zijn in Rotterdam?", "Meestal binnen 20 tot 30 minuten na bevestiging via WhatsApp. In het weekend of bij evenementen kan het langer duren; dat hoor je vooraf, zodat je zelf kunt beslissen."],
            ["Wat moet ik sturen om het snel te laten gaan?", "Je volledige adres met postcode, de gewenste maat (2KG, 4KG of 10KG) en het tijdstip, alles in één bericht. Houd daarna je telefoon bij de hand en leg je legitimatie klaar."],
            ["Bezorgen jullie ook met spoed 's nachts?", """Ja, we zijn 24/7 bereikbaar, ook na middernacht. Lees meer op <a href="/lachgas-nachtbezorging/">lachgas nachtbezorging</a>."""],
        ],
        "related": ["lachgas-bezorgservice-kiezen", "lachgastank-2kg-4kg-of-10kg"],
    },
    {
        "slug": "lachgas-bestellen-zonder-account", "label": "Bestellen",
        "title": "Lachgas bestellen zonder account | Via WhatsApp",
        "description": "Lachgas bestellen zonder account of webshop: één WhatsApp-bericht met adres, maat en tijdstip is genoeg. Totaalbedrag vooraf, geen onnodige gegevens, 18+.",
        "h1": "Lachgas bestellen zonder account of webshop",
        "lead": "Geen account aanmaken, geen winkelwagen, geen wachtwoord. Eén WhatsApp-bericht is genoeg en je weet vooraf precies waar je aan toe bent.",
        "sections": [
            {
                "h2": "Waarom via WhatsApp en niet via een webshop",
                "paragraphs": [
                    """We hebben bewust geen webshop met accounts. Een lachgastank is geen product dat je anoniem in een winkelwagen gooit en morgen met de post ontvangt; het is een drukhouder die we persoonlijk aan een volwassene overhandigen. WhatsApp past daar beter bij. Je spreekt direct met iemand die je vragen kan beantwoorden, je hoort het totaalbedrag inclusief bezorging voordat we vertrekken, en je kunt een tijdstip afspreken dat jou past. Er is geen formulier dat je verplicht om een profiel aan te maken met gegevens die we helemaal niet nodig hebben.""",
                    """Het is ook sneller. Een webshop stuurt een bevestigingsmail en verwerkt je bestelling 'binnen 24 uur'; wij reageren meestal binnen enkele minuten en in Rotterdam staat de bezorger meestal binnen 20 tot 30 minuten aan de deur. Heb je een vraag over welke maat past of over bewaren, dan stel je die in hetzelfde gesprek. Hoe het precies werkt, lees je op <a href="/werkwijze/">werkwijze</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Zo bestel je stap voor stap",
                "paragraphs": [
                    """Het hele proces bestaat uit een paar berichten. Je hoeft niets te installeren behalve WhatsApp, dat je waarschijnlijk al hebt, en je hoeft niets te onthouden voor een volgende keer.""",
                ],
                "bullets": [
                    """<strong>Stap 1.</strong> Stuur een WhatsApp-bericht met je adres en postcode, de gewenste maat (2KG, 4KG of 10KG) en het tijdstip waarop je de tank wilt ontvangen.""",
                    """<strong>Stap 2.</strong> Wij bevestigen het totaalbedrag inclusief bezorging en het verwachte levermoment. Pas als jij akkoord geeft, vertrekt de bezorger.""",
                    """<strong>Stap 3.</strong> De bezorger appt als hij er bijna is. Aan de deur laat je je legitimatie zien; we leveren uitsluitend aan 18+.""",
                    """<strong>Stap 4.</strong> Je controleert of de verzegeling intact is en betaalt bij levering, contant of via Tikkie. Klaar.""",
                ],
            },
            {
                "h2": "Wat we van je vragen",
                "paragraphs": [
                    """We vragen alleen wat nodig is om de tank bij de juiste persoon op het juiste adres te krijgen: je bezorgadres met postcode, de gewenste maat, het tijdstip en aan de deur een legitimatie waaruit blijkt dat je 18 jaar of ouder bent. We maken geen kopie of foto van je legitimatie en vragen die ook niet vooraf via WhatsApp. Een naam voor de bezorger is handig maar hoeft niet je volledige naam te zijn. Meer over de formaten vind je op <a href="/lachgas-tanks/">lachgas tanks</a>.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Privacy en je gegevens",
                "paragraphs": [
                    """Omdat er geen account is, is er ook geen database met bestelgeschiedenis, wachtwoorden of profielen. Het WhatsApp-gesprek bevat alleen wat jij zelf hebt gestuurd en wat nodig was voor de levering. We delen je gegevens niet met anderen en gebruiken ze niet voor reclame of nieuwsbrieven; je krijgt van ons geen ongevraagde berichten om opnieuw te bestellen. Wil je dat we het gesprek verwijderen, laat het weten en we doen het. Hoe we met gegevens omgaan, staat op <a href="/privacy/">privacy</a>; voor andere vragen kun je terecht op <a href="/contact/">contact</a>.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder. Het totaalbedrag wordt vooraf bevestigd via WhatsApp; je betaalt bij levering, contant of via Tikkie. Lees vooraf <a href="/veilig-gebruik/">veilig gebruik</a>.""",
        "faq": [
            ["Moet ik een account aanmaken om te bestellen?", "Nee. Je stuurt één WhatsApp-bericht met je adres, de gewenste maat en het tijdstip. Er is geen webshop, geen profiel en geen wachtwoord."],
            ["Welke gegevens hebben jullie nodig?", "Alleen je bezorgadres met postcode, de maat, het tijdstip en aan de deur een legitimatie voor de leeftijdscontrole. We maken daar geen kopie van."],
            ["Hoe weet ik vooraf wat ik betaal?", "We bevestigen het totaalbedrag inclusief bezorging in het WhatsApp-gesprek voordat de bezorger vertrekt. Aan de deur verandert daar niets aan; je betaalt contant of via Tikkie."],
        ],
        "related": ["lachgas-bezorgservice-kiezen", "lachgastank-2kg-4kg-of-10kg"],
    },
    {
        "slug": "lachgas-bezorgen-weekend", "label": "Weekend",
        "title": "Lachgas bezorgen in het weekend | Rotterdam 24/7",
        "description": "Lachgas bezorgen in het weekend in Rotterdam: vrijdag- en zaterdagavond zijn druk, zo plannen wij en zo bestel je slim. Ook zondag, 24/7 via WhatsApp, 18+.",
        "h1": "Lachgas bezorgen in het weekend in Rotterdam",
        "lead": "Vrijdag- en zaterdagavond zijn onze drukste momenten. Zo plannen we het weekend en zo zorg jij dat je tank op tijd aan de deur staat.",
        "sections": [
            {
                "h2": "Vrijdag en zaterdag: de drukste avonden",
                "paragraphs": [
                    """Het merendeel van onze bestellingen komt binnen tussen vrijdagmiddag en zondagochtend, met een duidelijke piek op vrijdag- en zaterdagavond tussen tien uur en twee uur 's nachts. Dat is logisch: huisfeesten, verjaardagen en avonden met vrienden vallen in het weekend, en veel mensen bestellen pas als de avond al begonnen is. Voor ons betekent dat tientallen adressen tegelijk, verspreid over Rotterdam en de regio, van een bovenwoning in het Oude Noorden tot een feest in Nesselande of Barendrecht. We vertellen je dat eerlijk, zodat je weet waarom een levertijd in het weekend soms aan de bovenkant van onze indicatie zit.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Hoe we het weekend plannen",
                "paragraphs": [
                    """In het weekend rijden er meer bezorgers dan op een doordeweekse avond, verdeeld over de stad: iemand voor het centrum en Noord, iemand voor Zuid en iemand voor Oost en de buurgemeenten. Zo hoeft een bezorger zelden de hele stad te doorkruisen. Bestellingen bevestigen we in volgorde van binnenkomst, en bij elke bevestiging krijg je een indicatie die klopt met de drukte op dat moment, niet het standaardgetal. Rotterdam zelf blijft meestal binnen 20 tot 30 minuten, buurgemeenten meestal 25 tot 40 minuten; bij piekdrukte zeggen we het als het langer wordt.""",
                ],
                "bullets": [],
            },
            {
                "h2": "Tips om vlot geleverd te krijgen",
                "paragraphs": [
                    """Je hebt zelf veel invloed op hoe soepel een weekendlevering verloopt. De belangrijkste tip is simpel: bestel vroeg. Een tank die om acht uur 's avonds wordt bezorgd, staat er ruim voordat de drukte begint, en bewaren is geen probleem als je hem rechtop en koel wegzet.""",
                ],
                "bullets": [
                    """<strong>Bestel vroeg op de avond of overdag.</strong> Weet je dat je zaterdag een feest hebt, app dan in de middag. Je kiest zelf het bezorgmoment.""",
                    """<strong>Eén compleet bericht.</strong> Adres met postcode, maat (2KG, 4KG of 10KG) en tijdstip in één keer, dan staat je bestelling direct in de rij.""",
                    """<strong>Kies het juiste formaat.</strong> Voor een groter feest is een 4KG of 10KG tank praktischer dan twee keer bijbestellen op het drukste moment. Lees <a href="/lachgas-feest-evenement/">lachgas voor feest en evenement</a>.""",
                    """<strong>Blijf bereikbaar.</strong> Op een feest hoor je je telefoon niet; zet hem op trillen of spreek af wie de deur opendoet.""",
                    """<strong>Legitimatie klaar.</strong> We controleren altijd op 18+, ook om twee uur 's nachts en ook als het druk is.""",
                ],
            },
            {
                "h2": "Ook op zondag en in de nacht",
                "paragraphs": [
                    """Het weekend stopt voor ons niet op zaterdagnacht. Ook op zondag bezorgen we de hele dag, van een late brunch tot een rustige avond, en meestal met kortere levertijden dan op zaterdag. Na middernacht blijven we bereikbaar; hoe dat werkt en waar je op moet letten, lees je op <a href="/lachgas-nachtbezorging/">lachgas nachtbezorging</a>. Organiseer je in het weekend iets groters, een verjaardag met veel gasten of een evenement, neem dan vooraf contact op; zie <a href="/lachgas-feest-evenement/">lachgas voor feest en evenement</a> voor wat we dan graag van je weten.""",
                ],
                "bullets": [],
            },
        ],
        "note": """Levertijden in het weekend zijn indicaties en geen garantie. Lachgas Rotterdam levert uitsluitend aan personen van 18 jaar en ouder, verzegeld, met legitimatiecontrole aan de deur. Lees vooraf <a href="/veilig-gebruik/">veilig gebruik</a>.""",
        "faq": [
            ["Hoe laat kan ik in het weekend bestellen?", """Op elk moment: we zijn 24/7 bereikbaar via WhatsApp, ook vrijdag- en zaterdagnacht en op zondag. Lees meer op <a href="/lachgas-nachtbezorging/">lachgas nachtbezorging</a>."""],
            ["Duurt bezorgen in het weekend langer?", "Op vrijdag- en zaterdagavond tussen tien en twee uur kan het aan de bovenkant van onze indicatie zitten. Je hoort bij de bevestiging een eerlijke tijd voor dat moment; bestel je eerder op de avond, dan ben je de drukte voor."],
            ["Kan ik vooraf een bezorgmoment afspreken voor zaterdagavond?", "Ja. App overdag je adres, de maat en het gewenste tijdstip, dan plannen we de levering in en staat de tank er voordat je gasten komen."],
        ],
        "related": ["lachgastank-2kg-4kg-of-10kg", "lachgas-bezorgservice-kiezen"],
    },
]
