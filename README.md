Product ETL Pipeline
Ett Python-program som följer ett ETL-flöde för produktdata.
Struktur
product-etl-pipeline/
├── data/
│   └── products_100.csv     # Produktdata (100 rader)
├── src/
│   ├── extract.py           # Steg 1 – läser in CSV med pandas
│   ├── transform.py         # Steg 2 – städar data och beräknar statistik
│   └── load.py              # Steg 3 – strömmar topp 5 och sparar resultat
├── main.py                  # Kör hela pipelinen i ett kommando
├── pyproject.toml
└── uv.lock
Dataflöde
products_100.csv  →  extract.py  →  transform.py  →  load.py
   (CSV-fil)          (inläsning)    (bearbetning)    (ström + spara)

Extract – läser in products_100.csv med pandas och visar en förhandsgranskning
Transform – städar ogiltiga rader, berikar med lagervärde och beräknar statistik per kategori
Load – strömmar topp 5 dyraste produkterna en i taget och sparar resultatet till data/results.csv

Installation
bashuv init
uv add pandas fastapi uvicorn
Kör projektet
bash# Kör hela ETL-pipelinen
uv run python main.py

# Kör varje steg separat
uv run python src/extract.py
uv run python src/transform.py
uv run python src/load.py
Statistik som beräknas

Totalt antal produkter
Snittpris, högsta och lägsta pris
Totalt lagervärde
Antal produkter och snittpris per kategori
Topp 5 dyraste produkter (visas som ström)


MVP – Minimum Viable Product
MVP för det här projektet definierades som ett fungerande ETL-flöde där:

En CSV-fil med produktdata kan läsas in automatiskt
Datan bearbetas och grundläggande statistik beräknas
Resultatet presenteras tydligt i terminalen

MVP uppnåddes efter Sprint 1 och utgjorde grunden för de efterföljande sprintarna.

Sprintmål
Sprint 1 – MVP: Extract + Transform
Mål: Få ett fungerande flöde från CSV till statistik

Läsa in products_100.csv med pandas
Städa data och ta bort ogiltiga rader
Beräkna snittpris, max, min och kategoriöversikt
Skriva ut resultatet i terminalen

Leverans: extract.py + transform.py
Sprint 2 – Load: Stegvis ström
Mål: Skicka vidare data stegvis som ett Kafka-liknande flöde

Identifiera topp 5 dyraste produkter
Strömma dem en i taget med fördröjning
Spara rensad data till ny CSV-fil

Leverans: load.py
Sprint 3 – Ihopsättning + dokumentation
Mål: Koppla ihop hela pipelinen och dokumentera projektet

Skapa main.py som kör alla tre steg i ordning
Skriva README med instruktioner och reflektion
Sätta upp GitHub Projects med issues och Kanban-tavla

Leverans: main.py + README.md + GitHub Projects

Reflektion – Agilt arbetssätt
Vad jag gjorde
Projektet byggdes steg för steg i en tydlig ordning: extract → transform → load → main.
Varje steg testades i terminalen innan nästa påbörjades och pushades som en egen commit.
Arbetet delades upp i tre sprintar med konkreta leveransmål.
Vad som fungerade bra
Att bygga en sak i taget gjorde det enkelt att testa och felsöka. När extract fungerade
visste jag att transform-steget fick korrekt data, och så vidare. Det gav ett tryggt
och kontrollerbart flöde genom hela projektet.
GitHub Issues med user stories gjorde det tydligt vad varje del skulle åstadkomma
ur ett användarperspektiv, inte bara tekniskt. Det hjälpte till att fokusera på
värdet av varje funktion snarare än bara implementationen.
Vad som hade kunnat göras mer agilt
Branches från start – Varje sprint hade kunnat ha en egen branch från början
(feature/extract, feature/transform, feature/load) istället för att allt
byggdes direkt på main. Det hade gett ett tydligare historik och möjlighet att
jobba parallellt om det hade varit ett team.
Pull requests med beskrivningar – Varje PR hade kunnat kopplas till sitt issue
och innehålla en kort beskrivning av vad som ändrades och varför. Det hade gjort
code review enklare och historiken mer läsbar.
Daily standups – I ett team hade korta dagliga möten (15 min) hjälpt till att
synka arbetet och fånga upp blockeringar tidigt. Även solo hade det varit värdefullt
att skriva en kort daglig notering om vad som gjorts och vad som är nästa steg.
Retroaktiv förbättring – Efter varje sprint hade en kort retrospektiv (vad gick bra,
vad kan förbättras) gjort att arbetssättet kontinuerligt förfinats under projektets gång.
Val och motiveringar
Varför pandas? Pandas är industristandard för databearbetning i Python och ger
kraftfulla verktyg för filtrering, aggregering och statistik med minimal kod.
Varför uv? uv är ett modernt och snabbt verktyg för pakethantering i Python som
ersätter pip och venv i ett enda verktyg. Det förenklar setup och reproducerbarhet.
Varför simulerad ström istället för riktig Kafka? En riktig Kafka-uppsättning
kräver en broker-server och är oproportionerligt komplex för ett projekt av den här
storleken. time.sleep() demonstrerar samma koncept – stegvis leverans av data –
utan onödig infrastruktur.
Sammanfattning
Det agila arbetssättet hade framförallt hjälpt till att:

Leverera ett fungerande MVP tidigt i projektet
Göra prioriteringarna tydligare om tiden hade tagit slut
Hålla arbetet synligt och strukturerat från start till leverans
Skapa en tydlig koppling mellan user stories, kod och leverans