# Kombinatorikas pamatošanas metodes 5.–9. klases olimpiāžu uzdevumos

Loģiskās pamatošanas metodes kombinatorikas uzdevumu risinājumos. 
Pieņemam, ka skolēns jau ir interpretējis uzdevumu (piemēram, 
sapratis, ka tas ir par grafiem); 
metodes apraksta nākamos soļus — kā iegūt secinājumus, 
saskaitīt variantus, izveidot bijekciju utml.

Metodes ir sakārtotas no vienkāršākām uz sarežģītākām. Vienā uzdevumā parasti prasa vairāku metožu kombināciju. 

Optimizācijas uzdevumi (`questionType:FindOptimal`) gandrīz vienmēr izmanto metodi 5 (`BoundPlusMatchingConstructionForOptimum`) kā galveno struktūru, kurā augšējais novērtējums parasti nāk no metodēm 7, 8, 9, 10 vai 13.

Iespējamības uzdevumi (`questionType:ProveDisprove`) parasti sadalās: pozitīvajā gadījumā lieto metodi 4 (konstrukcija), negatīvajā — metodi 6 (pretruna), kuras iekšienē izmanto kādu invariantu (9), krāsošanu (10) vai citu argumentu.

---

## 1. RuleOfSumDisjointCases

**(1)** No 5.klases.  
**(2) Saskaitīšanas likums (disjunkti gadījumi)**
**(3) Rule of sum (disjoint cases)**

**(4) Apraksts.** Ja meklējamo objektu kopa sadalās vairākās savstarpēji nekrustojošās (disjunktās) apakšgrupās, tad kopējais objektu skaits ir vienāds ar katras grupas objektu skaitu summu. Risinājuma autoram ir jāpierāda divi: ka grupas tiešām nepārklājas (neviens objekts neietilpst divās grupās vienlaicīgi) un ka grupas pārklāj visus iespējamos gadījumus (neviens objekts nav izlaists). Šī metode parasti parādās kā pirmais solis, kad uzdevuma struktūra dabīgi sadalās vairākos scenārijos.

**(5) Piemēri.**
- `LV.AMO.2019.9.1` (paralelogrami no taisnēm): tā kā paralelograma malu pāri var sastāvēt no horizontālām, vertikālām vai slīpām taisnēm, ir trīs disjunkti gadījumi — atbildē tos saskaita: 60 + 18 + 30 = 108 paralelogrami.
- `LV.AMO.2022B.8.1` (skaitļa $N597M$ dalāmība ar 12): risinājums sadalās divos gadījumos pēc $M$ vērtības ($M = 2$ vai $M = 6$), katrā atrod $N$ derīgās vērtības un beigās saskaita: 3 + 3 = 6 veidi.
- *Karoga krāsošanas piemērs no GRAMATAS (sk. 5.3.1. nodaļas piemēru ar trijstūru karogu):* gadījumi tiek šķiroti pēc tā, vai 1. un 3. trijstūrim ir vienāda vai dažāda krāsa; rezultāti 36 + 48 = 84.

---

## 2. RuleOfProductIndependentChoices

**(1)** No 5.klases.  
**(2) Reizināšanas likums (neatkarīgas izvēles)**
**(3) Rule of product (independent choices)**

**(4) Apraksts.** Ja kāds objekts (piem., virkne, kortežs, ceļš) tiek konstruēts ar vairākiem secīgiem soļiem, un katrā solī ir kāds skaits izvēļu, kas nav atkarīgs no iepriekšējām izvēlēm (vai vismaz katrā solī izvēļu skaits ir vienāds neatkarīgi no iepriekšējām izvēlēm), tad kopējais konstrukciju skaits ir izvēļu skaitu reizinājums. Faktoriālā skaita formula $n! = n \cdot (n−1) \cdot \ldots \cdot 1$ ir šī likuma tipisks pielietojums permutācijām. Skolēnam svarīgi pareizi konstatēt soļu skaitu un katrā solī palikušo izvēļu skaitu — šeit visbiežāk rodas kļūdas.

**(5) Piemēri.**
- `LV.NOL.2021TEST.7.1` (5 skolēnu izvietojums rindā): pirmajā vietā 5 iespējas, otrajā — 4, trešajā — 3, ceturtajā — 2; piektā tiek noteikta viennozīmīgi. Kopā $5! = 120$.
- `LV.AMO.2019.9.1` (turpinot 1. piemēru): katrā no trim gadījumiem izmanto reizināšanas likumu (piem., $6 \cdot 10 = 60$ paralelogrami no horizontālajām un vertikālajām taisnēm).
- *GRAMATAS karoga piemērs (sk. 1. metodes piemērā):* $4 \cdot 3 = 12$ veidi 1. un 2. trijstūra krāsošanai pirms iziešanas tālākos gadījumos.

---

## 3. ExhaustiveEnumerationOfCases

**(1)** No 5.klases.  
**(2) Pilnā pārlase (visu gadījumu pārbaude)**
**(3) Exhaustive enumeration**

**(4) Apraksts.** Risinātājs sistemātiski uzskaita visus iespējamos uzdevuma stāvokļus, scenārijus vai vērtību kombinācijas un katram no tiem pārbauda, vai izpildās uzdevuma nosacījumi. Šī metode darbojas, kad iespējamo gadījumu kopa ir galīga un pietiekami maza. Pierakstā parasti tiek izveidota tabula vai skaidri numurēts saraksts. Lai pierādījums būtu pilnīgs, jāpamato, ka neviens gadījums nav izlaists.

**(5) Piemēri.**
- `LV.AMO.2023.7.4` (monētas summa $S$ un skaits $M$): risinājumā veidota tabula visiem $S ≤ 7$ un $M ≤ S$; katrā kombinācijā pārbauda, vai izvietojums viennozīmīgs. Atbilde $S = 8$ izriet tieši no tā, ka visi mazākie gadījumi izsmelti.
- `LV.AMO.2022B.8.2` (skolēna 8 punktu/–5 punktu uzdevums): risinājumā izveido tabulu visām nepāra $y$ vērtībām no 1 līdz 11; pārbauda, kura no tām dod naturālu $x$ vērtību. Vienīgā derīgā ir $y = 7, x = 6$.
- *GRAMATAS piemērs (sk. 5.4.5. nodaļu):* uzdevumā par 50 = pirmskaitļu summu visi pirmskaitļi līdz 50 tiek izrakstīti un katrs pārbaudīts pa pāriem.

---

## 4. ConstructiveExampleForExistence

**(1)** No 5.klases.  
**(2) Konstruktīvs piemērs eksistences pierādīšanai**
**(3) Constructive example for existence**

**(4) Apraksts.** Lai pierādītu, ka kaut kas ir iespējams (uzdevumi formā “Vai iespējams …?”, “Kāds var būt …?”, “Atrast piemēru …”), pietiek uzbūvēt vienu konkrētu konfigurāciju, kas izpilda visus uzdevuma nosacījumus, un pārbaudīt, ka tā tiešām izpildās. Pierakstā jābūt: (a) skaidri aprakstītam piemēram (parasti zīmējumam, tabulai vai konkrētai skaitļu virknei), un (b) pārbaudei, ka šis piemērs apmierina visus nosacījumus. Šī metode visbiežāk veido uzdevuma “Jā, var” daļu pretī pretruna-no-pretējā argumentam, kas veido “Nē, nevar” daļu.

**(5) Piemēri.**
- `LV.AMO.2023.9.5` ($S = 100$ no 16 skaitļu starpību summas pa apli): risinājumā doti konkrēti 16 skaitļi un norādīts, ka starpību summa tiešām ir 100.
- `LV.NOL.2024.8.5(A)` (skaitļi rūtiņās ar bultu noteiktiem nosacījumiem): tiek dota viena konkrēta tabula 24.att., kas pierāda, ka šāds izvietojums eksistē.
- `LV.AMO.2022A.12.2`-stila piemērs (bumbiņu trauks): pretējā daļā (kuras šeit nav, bet ja būtu jautāts “vai pēdējā var būt melna”) atbilde būtu “jā”, parādot konkrētu darbību secību.

---

## 5. BoundPlusMatchingConstructionForOptimum

**(1)** No 7.klases.  
**(2) Augšējais/apakšējais novērtējums + atbilstošs piemērs ekstrēmajiem uzdevumiem**
**(3) Bound plus matching construction for optimization**

**(4) Apraksts.** Optimizācijas uzdevumos formā “Kāds ir lielākais (mazākais) …?” risinājumam jābūt divām daļām: (a) parāda piemēru, kurā atbildes vērtība tiek sasniegta (sk. metodi #4), un (b) pierāda, ka neviens piemērs ar lielāku (attiecīgi mazāku) vērtību nav iespējams. Otrā daļa parasti izmanto kādu novērtējuma argumentu — kapacitāšu summēšanu, Dirihlē principu, paritāti, krāsošanu vai citu. Šī ir kanoniska struktūra uzdevumiem ar `questionType:FindOptimal`.

**(5) Piemēri.**
- `LV.AMO.2023.5.5` (Gunas konfektes, lielākais viesu skaits): (a) piemērs ar 21 viesi un konkrētu sadalījumu konfektēs; (b) pierādījums, ka vairāk par 21 nav iespējams, jo katrs viesis prasa vismaz divas konfektes no kopas “Serenādes/Lācīši/Vāverītes”, un to kopā ir tikai 42.
- `LV.AMO.2024.7.4` (figūru izgriešana 10×10 kvadrātā): (a) konstrukcija ar 16 figūrām (10.att.); (b) novērtējums $100 : 6 = 16$, atlikumā 4, tātad vairāk par 16 nav iespējams.
- `LV.NOL.2024.8.3` (punktu nodzēšana, lai uz katras taisnes nebūtu trīs punktu): (a) parāda, kā nodzēst tieši 15 punktus; (b) pamatojums, ka katrā rindā vajag nodzēst vismaz 3, tātad kopā vismaz 15.

---

## 6. ContradictionForImpossibility

**(1)** No 7.klases.  
**(2) Pretruna no pretējā (neiespējamības pierādīšanai)**
**(3) Proof by contradiction**

**(4) Apraksts.** Lai pierādītu, ka kāda konfigurācija nav iespējama (uzdevumi formā “Vai iespējams …?” ar atbildi “nē”, vai “Pierādīt, ka … nav iespējams”), pieņem pretējo — ka tāda konfigurācija eksistē — un no šī pieņēmuma atvasina pretrunu ar zināmu faktu vai uzdevuma nosacījumiem. Pretrunu var iegūt caur paritāti, dalāmību, novērtējumu, Dirihlē principu vai jebkuru citu argumentu. Šī ir izplatītākā metode kombinatorikas uzdevumos ar `questionType:ProveDisprove` un negatīvu atbildi.

**(5) Piemēri.**
- `LV.AMO.2023.9.4` (kartīšu sadalīšana sešās grupās pa sešām): pieņem pretējo, ka sadalījums eksistē; tad katras grupas summai jābūt 18, bet pēc Dirihlē principa kādā grupā ir vismaz divas “devītnieka” kartītes, un atlikumā jābūt summai 0, kas nav iespējams.
- `LV.NOL.2024.8.5(B)` (skaitļi ar bultu virzienu): aplūko četras rūtiņas, ievērojot bultu virzienus, jāizpildās $B1 < B2 < B3 < B4 < B1$, kas nav iespējams.
- `LV.AMO.2023.7.5` (bizbizmārītes): pieņem, ka pirmās trīs bizbizmārītes visas melo; no tā seko, ka visas melo; bet tad pirmā saka patiesību — pretruna.

---

## 7. PigeonholePrincipleBasic

**(1)** No 5.klases.  
**(2) Dirihlē princips (pamata variants)**
**(3) Pigeonhole principle (basic form)**

**(4) Apraksts.** Ja vairāk nekā $n$ objekti tiek izvietoti $n$ grupās, tad noteikti ir grupa, kurā ir vismaz divi objekti. Lietošanai uzdevumā skolēnam jāizdomā, kas būs “objekti” (truši) un kas — “grupas” (būri); būtu skaidri jānorāda, kāpēc katrs objekts ietilpst tieši vienā grupā. Tipiskas grupu izveides shēmas: pēc dzimšanas mēneša, pēc atlikuma dalot ar $n$, pēc krāsas, pēc tabulas rindas vai kolonnas. Pamata variantu nav grūti aizvietot ar tiešu pretrunas argumentu (“ja katrā grupā būtu ne vairāk kā viens, tad kopā būtu ne vairāk kā $n$”), bet skaidri norādīts princips palīdz pārskatāmībai.

**(5) Piemēri.**
- `LV.AMO.2023.9.4` (kartītes sešās grupās, sk. 6. metodes piemērā): pēc Dirihlē principa vismaz vienā grupā ir vairāk par vienu “devītnieka” kartīti.
- `LV.NOL.2024.8.4` (5 gardēži, 16 tortes, 125 € budžets): pieņem pretējo, ka visas 16 nopirktas; pēc Dirihlē principa kāds gardēdis nopircis vismaz 4 ($16 = 5\cdot3+1$); bet 4 lētākās tortes maksā 126 € > 125 € — pretruna.
- *GRAMATAS klasiskais piemērs (sk. 2.15. nodaļu):* no 8 naturāliem skaitļiem var izvēlēties divus, kuru starpība dalās ar 7. Atlikumi dalīšanā ar 7 var būt 7 dažādi ($0, 1, …, 6$); 8 skaitļiem pēc Dirihlē divi dod vienādu atlikumu, tātad to starpība dalās ar 7.

---

## 8. PigeonholePrincipleGeneralized

**(1)** No 7.klases.  
**(2) Dirihlē princips (vispārinātais variants)**
**(3) Pigeonhole principle (generalized form)**

**(4) Apraksts.** Ja vairāk nekā $m \cdot n$ objekti tiek izvietoti $n$ grupās, tad noteikti ir grupa, kurā ir vismaz $m + 1$ objekts. Tas ir pamata varianta nostiprinājums, ko izmanto, kad jāatrod ne tikai pāris, bet trīs, četri vai vairāk objekti vienā grupā. Skolēnam jāizvēlas pareiza grupu skaita un objektu skaita kombinācija, lai iegūtu nepieciešamo skaitu vienā grupā. Bieži jākombinē ar gadījumu šķirošanu, ja tiešais aprēķins nedod pietiekamu skaitu.

**(5) Piemēri.**
- `LV.AMO.2024.9.2` (28 skolēni, atzīmes no 0 līdz 10): grupē 11 atzīmes 9 grupās (atzīmes 0–7 katra atsevišķi, atzīmes 8–10 vienā kopā); $28 > 3 \cdot 9 = 27$, tātad kādā grupā vismaz 4 skolēni. Tālāk šķir gadījumus, vai šī grupa ir “8–10” vai viena no atsevišķajām atzīmēm.
- *Klasisks piemērs:* ja 100 punkti izvietoti $9 × 9$ kvadrātā, tad pēc vispārinātā Dirihlē principa kādā no 9 rindām ir vismaz 12 punkti ($100 > 11 \cdot 9 = 99$).
- *GRAMATAS 16 punktu piemērs (sk. 2.15. nodaļu):* septiņi melnie + deviņi baltie 16 punktos 4 rindās; pēc Dirihlē kādā rindā ir vismaz 3 baltie ($9 > 2 \cdot 4 = 8$).

---

## 9. FixedInvariantNumeric

**(1)** No 5.klases.  
**(2) Skaitlisks invariants (paritāte, dalāmība, summa)**
**(3) Numeric invariant (parity, divisibility, sum)**

**(4) Apraksts.** Lai pierādītu, ka kādu beigu stāvokli nevar sasniegt no dotā sākumstāvokļa ar atļautām darbībām, atrod skaitlisku lielumu (invariantu), kas: (a) sākotnēji ir vienā vērtībā vai vienā paritātes/dalāmības klasē, (b) pēc katras atļautās darbības saglabā šo īpašību, (c) beigu stāvoklim būtu cita vērtība vai paritātes klase. Visbiežāk lieto: paritāte (pāra/nepāra), dalāmība ar 3 vai citu skaitli, kopējā summa, atlikums dalot ar $m$, pirmskaitļu skaits.

**(5) Piemēri.**
- `LV.AMO.2024.9.3` (Agnese, trīs skaitļi 11, 12, 13): paritāte (viens pāra, divi nepāra) saglabājas pēc katra gājiena $c \rightarrow 2(a+b)−c$. Beigu stāvoklim $20, 24, 25$ ir cita paritāte (divi pāra, viens nepāra), tāpēc to sasniegt nevar.
- `LV.AMO.2022A.12.2` (bumbiņu trauks): balto bumbiņu skaits traukā A vai nu samazinās par 2, vai paliek nemainīgs; tas saglabā skaita paritāti. Sākumā tās ir 2022 (pāra) → beigās viena balta bumbiņa nav iespējama.
- `LV.AMO.2023.5.4(B), (C)` (kauliņa diagonāles gājieni 10×10 un 11×11): šaha krāsojuma invariants — kauliņš vienmēr paliek vienas krāsas rūtiņās, un mērķa stūra rūtiņa ir citā krāsā.

---

## 10. ColoringArgumentForCoverageOrUnreachability

**(1)** No 7.klases.  
**(2) Krāsošanas arguments noklāšanai vai nesasniedzamībai**
**(3) Coloring argument for tiling or unreachability**

**(4) Apraksts.** Krāsošana ir invariantu metodes specifisks variants, ko parasti lieto rūtiņu figūru sagriešanas, noklāšanas vai kauliņa pārvietošanas uzdevumos. Idea: rūtiņas tiek nokrāsotas vairākās krāsās (šaha veidā, joslās, diagonālēs vai citādi), un tad parāda, ka katra ielikta figūra (vai katrs kauliņa gājiens) skar krāsas noteiktā konfigurācijā, kas ne sakrīt ar visu rūtiņu krāsojuma sadalījumu. Galvenais lēmums: kādu krāsojumu izvēlēties. Standarta variants — šaha (melnbalts), bet bieži der arī 3 vai 4 krāsu krāsojumi joslās vai diagonālēs.

**(5) Piemēri.**
- `LV.AMO.2022B.9.5(B)` (muzeja maršruts 9×11): šaha krāsojums; maršruts cauri visām 99 rūtiņām (nepāra skaits) beidzas tādas pašas krāsas rūtiņā kā sākums, bet uzdevuma nosacījums prasa beigām būt blakus sākumam — kas ir pretējā krāsā. Pretruna.
- `LV.AMO.2023.5.4(B), (C)` (sk. 9. metodes piemēru): kauliņš pārvietojas pa diagonāli izlaižot rūtiņu; krāsojums saglabā paritāti.
- *GRAMATAS 4×11 noklāšanas piemērs (sk. 2.17. nodaļu):* šaha krāsojums — taisnstūrī 22 melnās rūtiņas (pāra), bet 11 figūras katra noklāj nepāra skaitu melno → pretruna.

---

## 11. MonovariantStrictlyChangingQuantity

**(1)** No 7.klases.  
**(2) Monovariants (stingri augoša vai dilstoša lieluma izsekošana)**
**(3) Monovariant (strictly increasing or decreasing quantity)**

**(4) Apraksts.** Atšķirībā no invarianta (kas nemainās), monovariants ir lielums, kas pēc katras atļautās darbības stingri palielinās (vai stingri samazinās), nepārkāpjot kādu robežu. Skolēns atrod tādu lielumu un secina, ka konkrēta beigu konfigurācija nav sasniedzama, jo prasītu lieluma pretēju virzību. Alternatīvi: monovariantu izmanto, lai pierādītu, ka process noteikti beidzas (lielums nevar mūžīgi mainīties starp galīgām vērtībām).

**(5) Piemēri.**
- `LV.AMO.2023.9.1(B)` (daļa $10/2023$, darbības: pieskaitīt naturālu vai reizināt): nevienādība starp skaitītāju un saucēju (`skaitītājs < saucējs`) ir invariants, bet daļas vērtība monotoni paliek $< 1$. Vērtību $1$ sasniegt nevar.
- *Piemērs no starptautiskās prakses:* sk. uz tāfeles skaitļus, kuru kopējais skaits katrā gājienā samazinās par 1; tā kā skaitlis nevar kļūt negatīvs, process beidzas.
- *Klasisks piemērs:* tabulā ierakstītu skaitļu summa pēc katra gājiena stingri samazinās; tā kā summa ir nenegatīva, gājienu skaits ir galīgs.

---

## 12. ExtremalElementArgument

**(1)** No 7.klases.  
**(2) Ekstrēmā elementa apskate**
**(3) Extremal element argument**

**(4) Apraksts.** Pierādījumā vai apgalvojuma izpētes laikā atlasa kādu konfigurācijas elementu ar ekstrēmu īpašību: lielāko, mazāko, ar visvairāk kaimiņiem grafā, ar vislielāko vērtību tabulā. Bieži šī izvēle atklāj struktūru, kas paliek slēpta, ja apskata patvaļīgu elementu. Bieži kombinē ar pretruna-no-pretējā argumentu: atlasa ekstrēmo elementu, izsecina kādu īpašību par tā kaimiņiem, un iegūst pretrunu.

**(5) Piemēri.**
- `LV.NOL.2024.8.4` (5 gardēži, 16 tortes): 4 lētākās tortes maksā $30 + 31 + 32 + 33 = 126$ EUR, kas pārsniedz $125$ EUR — šeit izvēlas ekstrēmo (lētāko) 4 toršu kopumu, lai parādītu, ka pat to viens gardēdis nevar atļauties.
- `LV.NOL.2023.10.5` (volejbola turnīrs): atlasa komandu $A$ ar vislielāko uzvaru skaitu $y$; tās uzvarētās $y$ komandas savā starpā spēlējušas $y(y−1)/2$ spēles, un izvēloties ekstrēmo iegūst $y \geq y(y−1)/2$, no kā $y ≤ 3$. Tālāk šķir gadījumus.
- *GRAMATAS vecmāmiņu piemērs (sk. 2.7. nodaļu):* aplūko vecmāmiņu $B$, kas nav $A$ paziņa; pierāda, ka $B$ nevar pazīt nevienu no $A$ paziņām, no kā seko, ka jābūt vēl 4 citām vecmāmiņām.

---

## 13. DoubleCountingSameQuantityTwoWays

**(1)** No 7.klases.  
**(2) Dubultsaskaitīšana (vienu lielumu skaita divos veidos)**
**(3) Double counting**

**(4) Apraksts.** Vienu un to pašu lielumu (parasti elementu pāru, šķautņu, atzīmējumu skaitu) saskaita divos atšķirīgos veidos. Iegūto vienādību (kas ir tiešs nekonstrukcionālas saskaitīšanas rezultāts) izmanto kā algebrisku attiecību starp uzdevuma lielumiem. Tipiski lietojumi: rokasspiedienu lemma grafos (šķautņu skaits = pakāpju summas puse), tabulu elementu summas (saskaitīt pa rindām = saskaitīt pa kolonnām), atzīmējumu skaits sarakstos. Bieži saskaitīšana “otrādā” virzienā atklāj uzdevuma slēpto struktūru.

**(5) Piemēri.**
- `LV.AMO.2022B.6.5` (273 ciema iedzīvotāji, 378 “jā” atbildes): kopā saņemtas 378 atbildes; katrs patiesotājs saka “jā” vienreiz, katrs melis sešas reizes — saskaita divos veidos, lai iegūtu lineāru sakarību.
- `LV.AMO.2024.7.5` (Anita, Maija, Ināra, Sandra, dziesmas): katru dziesmu dzied 3 meitenes, tātad katras meitenes dziedāto dziesmu summa ir `3 \cdot (kopējais dziesmu skaits)`. No tā seko, ka $7 + 4 + M + I$ dalās ar 3.
- `LV.NOL.2025.7.4`-stila uzdevums (pirmklasnieki/otrklasnieki aplī, sadošanās rokās): saskaita rokas turējumus divos veidos — pēc bērna grupas un kopējais — un iegūst dalāmības nosacījumu.

---

## 14. HandshakingLemmaSumOfDegreesEven

**(1)** No 9.klases.  
**(2) Rokasspiedienu lemma (pakāpju summa ir pāra)**
**(3) Handshaking lemma (sum of degrees is even)**

**(4) Apraksts.** Grafā jebkurai šķautnei ir tieši divi gali, tāpēc, summējot pakāpes (no katras virsotnes izejošo šķautņu skaitu) visās virsotnēs, katra šķautne tiek saskaitīta divreiz. Tātad pakāpju summa ir pāra skaitlis, kas ir vienāds ar `2 \cdot (šķautņu skaits)`. Sekas: nepāra pakāpju virsotņu skaitam jābūt pāra skaitlim. Šī ir tieša rokasspiedienu lemmas formulējuma sekas un kalpo kā ātrs paritātes arguments grafu uzdevumos.

**(5) Piemēri.**
- `LV.NOL.2023.5.2`-stila uzdevums (sk. arī GRAMATAS 2.7. nodaļu): 8 mājām ir attiecīgi $1, 2, 2, 2, 2, 3, 4, 5$ taciņu; summa $1+2+2+2+2+3+4+5 = 21$ ir nepāra, kas neiespējami, jo taciņu galu skaits jābūt pāra (katra taciņa = 2 gali).
- *GRAMATAS 2023 lampiņu piemērs (sk. 2.7. nodaļu):* 2023 lampiņas, katrai tieši 3 vadi → kopējais galu skaits $2023 \cdot 3 = 6069$ (nepāra) → neiespējami.
- `LV.AMO.2019.8.4` (rūķīši, kuru draugu skaits ir kubs): ja katram rūķītim ir tieši 1 draugs (mazākais kubs \geq 1), tad rūķīšu skaitam jābūt pāra (no rokasspiedienu lemmas). Ja $m$ ir nepāra un $m ≤ 7$, nav iespējams cits kubs 8 draugu, tāpēc nepāra $m ≤ 7$ neder.

---

## 15. SymmetryStrategyInTwoPlayerGames

**(1)** No 7.klases.  
**(2) Simetrijas stratēģija divu spēlētāju spēlēs**
**(3) Symmetry strategy in two-player games**

**(4) Apraksts.** Divu spēlētāju spēlēs (parasti `domain:Comb`, `subdomain:DOM_CombinatorialGames`) viens spēlētājs uzvar, kopējot pretinieka gājienus simetriski — vai nu attiecībā pret centrālo punktu (centrālā simetrija), vai pret asi (osu simetrija). Lai pierādītu uzvarošu stratēģiju, jāpierāda: (a) ka spēlētājs vienmēr var izdarīt simetrisku gājienu (parasti caur konstrukciju — “ja pretinieka gājiens ir derīgs, tad simetriskais arī”), un (b) ka simetriskā situācija ir labvēlīga (parasti caur invariantu vai punktu sadalījumu). Pirmajam spēlētājam parasti darbojas centra okupēšana pirmajā gājienā + simetrija; otrajam spēlētājam — tieša simetrijas kopēšana.

**(5) Piemēri.**
- `LV.AMO.2019.9.2` (9×9 tabulas krāsošana, melnais sāk): pirmais spēlētājs ieņem centra rūtiņu un tad katru pretinieka gājienu kopē centrāli simetriski. Centrālajā rindā un kolonnā melnās rūtiņas dominēs.
- `LV.AMO.2022B.12.5(A), (B)` ($n × n$ tabula ar $±1$): $n = 2021$ gadījumā Ilmārs ieņem centru un spēlē simetriski; $n = 2022$ gadījumā Kims spēlē simetriski pret vertikālo asi.
- *GRAMATAS tulpju vāžu piemērs (sk. 4. nodaļu):* divām vāzēm ar 46 un 43 tulpēm — viens spēlētājs vispirms izlīdzina vāzes un tad simetriski kopē pretinieka gājienus.

---

## 16. CountingViaSymmetryClasses

**(1)** No 9.klases.  
**(2) Skaitīšana caur simetrijas klasēm (pārklājuma izslēgšana)**
**(3) Counting via symmetry classes (overcounting correction)**

**(4) Apraksts.** Ja objekti ir uzskatāmi par vienādiem, ja tos var iegūt vienu no otra ar kādu simetrijas operāciju (pagriešanu, spoguļattēlu), tad var izmantot šādu paņēmienu: vispirms saskaita visus formāli atšķirīgos objektus (ignorējot simetrijas), tad dala ar simetrijas grupas lielumu. Vienkāršajā gadījumā, ja katrai simetrijas klasei pieder vienāds skaits formāli atšķirīgu objektu, dalīšana dod precīzu atbildi. Sarežģītākos gadījumos jāatdala fiksētie objekti, bet 5.–9.kl. līmenī parasti pietiek ar vienkāršo dalīšanas argumentu.

**(5) Piemēri.**
- `LV.AMO.2022A.X.X` (plāksnītes ar 5 skaitļiem, ko var pagriezt un apgriezt): formāli $5! = 120$ izvietojumi; pagriešanas dod 5 ekvivalentus → dala ar 5; spoguļattēli dod vēl 2 ekvivalentus → dala ar 2. Kopā $120 / 5 / 2 = 12$ dažādu plāksnīšu.
- *Klasisks piemērs (5.–6.kl.):* cik dažādās secībās 4 cilvēki var apsēsties pie apaļa galda? Formāli $4! = 24$; pēc apaļā galda rotācijas (4 ekvivalenti) → $24/4 = 6$ veidi.
- *7.–8.kl. piemērs:* kaklarotā uz auklas izvietoti 6 dažādas krāsas pērlītes. Atšķirīgu kaklarotu skaits, ja drīkst gan rotēt, gan apgriezt, ir $6!/(6\cdot2) = 60$.

---

## 17. BijectionBetweenTwoSets

**(1)** No 9.klases.  
**(2) Bijekcija (savstarpēji nepārklājoša atbilstība starp divām kopām)**
**(3) Bijection between two sets**

**(4) Apraksts.** Lai pierādītu, ka divām kopām ir vienāds elementu skaits (vai lai vienas kopas elementu skaitu aprēķinātu, izmantojot otras kopas zināmo elementu skaitu), izveido viennozīmīgu atbilstību starp tām: katram pirmās kopas elementam piekārto tieši vienu otrās kopas elementu un otrādi, un visi otrās kopas elementi tiek aizsniegti. Šī metode bieži parādās caur kodējumu — uzdevuma objektu pārveido par vienkāršāku objektu (skaitļu virkni, kortežu, ceļu rūtiņu tīklā) tā, ka katram oriģinālajam objektam atbilst tieši viens kodējums.

**(5) Piemēri.**
- *Klasiska 7.–8.kl. uzdevums:* saskaitīt, cik dažādos veidos var nokļūt no rūtiņas A uz rūtiņu B $m × n$ rūtiņās, ejot tikai pa labi vai uz augšu. Katram ceļam piekārto burtu virkni no $m$ burtiem L un $n$ burtiem U; bijekcija ar virknēm dod atbildi $C(m+n, m)$.
- `LV.AMO.2022A.X.X` (plāksnītes): risinājums-1 izmanto bijekciju starp “plāksnītēm” un “neuzlikto skaitļu pāriem”, fiksējot skaitļa 1 pozīciju.
- *7.kl. piemērs:* cik dažādos veidos var sadalīt 10 vienādas konfektes 3 bērniem (katram vismaz vienai)? Bijekcija ar 7-elementa virkni, kurā jāizvēlas 2 vietas “starpsienām” — atbilde $C(9.2) = 36$.

---

## 18. EulerVennDiagramRegions

**(1)** No 7.klases.  
**(2) Eilera–Venna diagrammas (apgabalu aizpildīšana)**
**(3) Euler–Venn diagram regions**

**(4) Apraksts.** Ja uzdevumā ir vairākas savstarpēji pārklājošās kopas (piem., skolēni, kas mācās matemātiku/fiziku/ķīmiju; cilvēki ar cepurītēm dažādās krāsās), izveido apļus, kas atbilst kopām, un tos pārklājot iegūstos apgabalus aizpilda ar attiecīgo elementu skaitu. Aizpildīšana parasti notiek no centra (visu kopu kopīgais apgabals) uz āru. Šī metode pārklāj iekļaušanas–izslēgšanas principu vienkāršos gadījumos (2–3 kopas).

**(5) Piemēri.**
- *GRAMATAS trollīšu piemērs (sk. 2.6. nodaļu):* trīs kopas (sarkanu, zaļu, dzeltenu cepurīšu īpašnieki), katrai pa 666; dots arī kopīgo daļu skaits; aizpilda diagrammu no centra uz āru un iegūst $1366$ trollīšus.
- *GRAMATAS Šreka un Ledus laikmeta piemērs (sk. 2.6. nodaļu):* divas kopas; aizpilda divus apļus ar “tikai Šreks”, “tikai Ledus laikmets”, “abus”.
- `LV.NOL.2021.6.1` (1243 skolēni, 3 priekšmeti): Eilera diagramma ar trim apļiem, aizpildīta no kopīgā centra uz āru.

---

## 19. RecursiveSequenceForCounting

**(1)** No 7.klases.  
**(2) Rekurenta virkne skaita aprēķināšanai**
**(3) Recursive sequence for counting**

**(4) Apraksts.** Ja jāatrod kāda objektu skaita atkarība no parametra $n$, parasti var izveidot rekurentu sakarību: parāda, kā $n$-tā tipa objektus var iegūt no $(n−1)$-tā vai dažu iepriekšējo līmeņu objektiem, un izrēķina bāzes gadījumus ($n = 0, 1, 2$). Šī metode īpaši darbojas pakāpieniem, ceļiem rūtiņu tīklā, dalījumiem, izvietojumiem ar ierobežojumiem. Iegūto virkni parasti aprēķina pakāpeniski (5.–7.kl. līmenī), bez slēgtas formulas.

**(5) Piemēri.**
- *GRAMATAS pakāpienu piemērs (sk. 2.11. nodaļu):* uz 12 pakāpienus var kāpt soļiem 1, 2 vai 3 — rekurenta sakarība $a_n = a_{n−1} + a_{n−2} + a_{n−3}$.
- `LV.NOL.2021TEST.6.18` (varde ar šķēršļiem): katrā rūtiņā uzraksta veidu skaitu, kuros varde tajā var nonākt; tas ir summa no rūtiņas zem un pa kreisi (rekurenta sakarība).
- *GRAMATAS ziloņa piemērs (sk. 5.3.1. nodaļu):* zilonis pārvietojas uz augšu, pa labi vai pa diagonāli — $x = c + d + e$, kur $c, d, e$ ir trīs iepriekšējās rūtiņas.

---

## 20. PeriodicSequenceForLongIndex

**(1)** No 7.klases.  
**(2) Periodiska virkne tāla locekļa noteikšanai**
**(3) Periodic sequence for distant index determination**

**(4) Apraksts.** Ja jāatrod virknes (parasti rekurenti definētas vai modulāri augošas) tāls loceklis (piem., 2018. vai 100. loceklis), aprēķina dažus pirmos virknes locekļus un pārliecinās, vai virkne kļūst periodiska. Ja jā, no perioda garuma un sākumposma garuma izrēķina prasīto vērtību. Šī metode darbojas tieši tāpēc, ka virkne, kuras katra nākamā vērtība ir vienznozīmīgi atkarīga no vienas (vai dažām) iepriekšējām, un kuras vērtības pieder galīgai kopai, vienmēr kļūst periodiska.

**(5) Piemēri.**
- `LV.AMO.2022B.10.1` (skaitļa $2022^2022$ pēdējais cipars): virkne $2^n mod 10$ ir periodiska ar periodu 4 ($2, 4, 8, 6, 2, 4, …$); $2022 = 4\cdot505 + 2$ → atbilde ir 2. perioda loceklis, kas ir 4.
- *GRAMATAS skaitļa virknes piemērs (sk. 2.11. nodaļu):* virkne sākas ar 11 un katrs nākamais ir iepriekšējā kvadrāta ciparu summa; pēc dažiem locekļiem ($11, 4, 7, 13, 16, 13, 16, …$) virkne kļūst periodiska ar periodu 2.
- `LV.AMO.2024` skaitļu virkne ar reizinātāju paritāti (61. loceklis): pirmreizinātāju skaita paritāte ir periodiska virkne $n, p, n, p, …$; no 61. pozīcijas un sākotnējā skaita izriet, ka 61. loceklim ir nepāra pirmreizinātāju skaits.

---

## 21. AveragingArgumentForExistenceOfElement

**(1)** No 9.klases.  
**(2)** Vidējās vērtības spriedums (eksistē elements, kas atbilst vidējam novērtējumam)
**(3) Averaging argument**

**(4) Apraksts.** Ja kopas elementu kopējais lielums ir $S$, bet elementu skaits ir $n$, tad vismaz viens elements ir $\geq S/n$ un vismaz viens ir $\leq S/n$. Šī ir Dirihlē principa kvantitatīvā variante. Lieto, ja jāpamato, ka eksistē objekts ar pietiekami lielu vai pietiekami mazu vērtību; rēķina kopējo summu (parasti caur dubultsaskaitīšanu) un dala ar elementu skaitu.

**(5) Piemēri.**
- `LV.NOL.2023.10.5` (volejbola turnīrs): kopējais uzvaru skaits $x$ komandām ir $x(x−1)/2$; vidēji uz komandu — $(x−1)/2$; tātad ir komanda ar vismaz $(x−1)/2$ uzvarām. No tā tālāk seko ekstrēmais arguments.
- *Klasiska 7.–8.kl. uzdevums:* 30 studenti uzrakstīja kontroldarbu, kopējais punktu skaits ir 1530. Pierādīt, ka kāds students ieguvis vismaz 51 punktu. $1530 / 30 = 51$.
- *GRAMATAS stila uzdevums:* 6 cilvēki nodzīvojuši kopā 360 gadus. Pierādīt, ka kādam ir vismaz 60 gadi ($360/6 = 60$).

---

## 22. EncodingForBijectionOrInvariant

**(1)** No 9.klases.  
**(2) Kodēšana (kodējums kā instruments bijekcijai vai invariantam)**
**(3) Encoding for bijection or invariant**

**(4) Apraksts.** Uzdevuma objektus pārveido par vienkāršāku objektu kodējumu — visbiežāk binārajām virknēm, koordinātu pāriem, atlikumu virknēm vai citu pierakstu, kas saglabā nepieciešamo informāciju, bet padara analīzi vienkāršāku. Piemēri: hameleona krāsu izsaka kā $0$ vai $1$; kauliņa pozīciju kā `(rinda, kolonna)`; permutāciju kā tās pieraksta secību. Pēc kodēšanas parasti seko cita metode (bijekcija, invariants, dubultsaskaitīšana), kas darbojas tieši ar kodējumu.

**(5) Piemēri.**
- `LV.AMO.2024.11.5(B)` (hameleoni krāsās): sarkanos hameleonus apzīmē ar $1$, zaļos ar $0$; krāsojumu kombinācija = 7-bitu virkne; kopā $2^7 = 128$ kombinācijas. Tālāk analīzē izmanto kongruences pēc moduļa 2.
- *Klasisks piemērs:* ceļus rūtiņu tīklā no $(0.0)$ uz $(m,n)$ kodē kā burtu virknes ar $m$ burtiem $L$ un $n$ burtiem $U$; bijekcija ar šādām virknēm tieši dod $C(m+n, m)$ ceļu skaitu.
- *Permutāciju kodēšana:* `LV.NOL.2023.11.5` (virkņu $a_i$, $b_i$, $c_i$ permutācijas): risinājumā virknes uzraksta vienu zem otras un strādā ar pozīciju kodējumu, lai izsekotu, kā skaitļi pārvietojas.

---

## 23. InclusionExclusionCounting

**(1)** No 6.–7. klases.
**(2)** Ieslēgšanas un izslēgšanas princips.
**(3)** Inclusion–exclusion principle.
**(4) Apraksts.** Kopu apvienojuma elementu skaitu izsaka caur atsevišķu kopu un to šķēlumu
elementu skaitiem: $|A \cup B| = |A| + |B| - |A \cap B|$; trīs kopām $|A \cup B \cup C| = |A| + |B|
+ |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$. Šī metode ir izšķiroša, kad
tieši saskaitīt apvienojuma elementus ir grūti, bet šķēlumus — viegli. Dalāmības kontekstā
šķēlumi atbilst dalāmībai ar mazāko kopīgo dalāmo: skaitļi, kas dalās gan ar $3$, gan ar $5$,
ir tieši tie, kas dalās ar $15$. Metode ir noderīga arī uzdevumos par “tieši $k$ no $n$ īpašībām”
(skaita ieslēgti tieši divos, tieši trijos krāsotos sarakstos utt.).
**(5) Piemēri.** LV.AMO.2022B.6.1 (Amanda apvelk skaitļus, kas dalās ar $3$, $5$, $7$; jāatrod,
cik dalās ar vismaz divām krāsām — tas ir $|A \cap B| + |A \cap C| + |B \cap C| - 2 |A \cap B \cap C|$,
kur $A$, $B$, $C$ ir attiecīgi $3, 5, 7$ daudzkārtņu kopas, un šķēlumi atbilst dalāmībai ar $15$,
$21$, $35$, $105$); klasisks olimpiāžu uzdevums “cik skaitļu no $1$ līdz $100$ nedalās ne ar $2$,
ne ar $3$, ne ar $5$?” — atbilde $100 - |A \cup B \cup C|$, kur tieši pielieto trīsobjektu formulu;
LV.NOL.2018./19. 7. klase (Eilera funkcijas tipa uzdevums par savstarpēji pirmskaitļiem ar
$n$).

---

## 24. InvariantByColoring

**(1)** No 5.–7. klases.
**(2)** Krāsošanas invariants tabulās un režģos.
**(3)** Coloring-based invariant.
**(4) Apraksts.** Lai pierādītu, ka kāds rezultāts nav sasniedzams, rūtiņas vai elementi tiek
nokrāsoti vairākās krāsās (piem., šaha krāsošana ar $2$ krāsām; krāsošana pa $3$ vai $4$
modulo; vai diagonāļu krāsošana). Pēc tam aplūko invariantu, kas saglabājas pie atļautām
darbībām — visbiežāk tā ir dažādu krāsu rūtiņās ierakstīto skaitļu summu starpība vai
attiecība. Sākotnējais un mērķa stāvoklis atšķiras šī invarianta vērtībā, tādēļ pāreja nav
iespējama. Vienkāršākais variants — klasiskā šaha krāsošana $8 \times 8$ tabulā ar
$32$ baltām un $32$ melnām rūtiņām. Sarežģītāki invarianti rodas, kad tabulā ierakstīti
skaitļi un saskaita atsevišķi melno un balto rūtiņu skaitļu summas.
**(5) Piemēri.** LV.AMO.2007.6.3 (četru reizes četru tabulā ar veseliem pozitīviem skaitļiem,
ar gājienu pieskaitot $1$ divām blakus rūtiņām — šaha krāsojumā divas blakus rūtiņas
vienmēr ir dažādās krāsās, tādēļ summu starpība starp melnajām un baltajām rūtiņām
saglabājas invariantā; ja sākotnējā konfigurācijā starpība nav $0$, vienādu skaitļu izvietojumu
sasniegt nevar); klasisks uzdevums par $8 \times 8$ rūtiņu tabulas pārklāšanu ar $1 \times 3$
domino, izņemot vienu stūra rūtiņu — pārklāšana neiespējama, jo modulo $3$ krāsojumā
katra $1 \times 3$ domino pārklāj pa vienai katras krāsas rūtiņai, bet izņemtā stūra rūtiņa
sabojā krāsu līdzsvaru; LV.NOL.2014./15. 6. klase 4. uzd. (figūru izgriešana no krāsotas
tabulas).


---

## 25. DynamicProgramming

**(1)** No 7.–8. klases.
**(2)** Dinamiskā programmēšana (pakāpeniska skaitīšana ar starprezultātiem).
**(3)** Dynamic programming.
**(4) Apraksts.** Skaita iespējamo variantu skaitu pakāpeniski, sākot no mazākiem
apakšuzdevumiem un veidojot rezultātu lielākiem. Vienkāršākajā variantā tas ir rekurents
sakarību lietojums virknē — piem., $a_n = a_{n-1} + a_{n-2}$, ja katra nākamā pozīcija atkarīga
no pēdējām divām. Vispārīgāks variants — režģī vai labirintā, kur katras rūtiņas “sasniegšanas
veidu skaits” iegūstams kā summa pa visiem ceļiem no kaimiņrūtiņām, no kurām var ienākt.
Šķēršļi (rūtiņas, kuras nevar apmeklēt) tiek apstrādāti, šajās rūtiņās ierakstot vērtību $0$.
Tipiska uzdevuma struktūra: iezīmē sākuma rūtiņu ar $1$ un secīgi aprēķina visu pārējo
rūtiņu vērtības atbilstoši atļautajām pārvietošanās kustībām.
**(5) Piemēri.** LV.NOL/LV.AMO uzdevums par “ziloņa” (figūras ar pārvietošanos uz augšu,
pa labi vai pa diagonāli) ceļu skaitu no rūtiņas $A$ uz rūtiņu $B$ ar šķērsli — katras
rūtiņas vērtība iegūta kā summa no kreisās, apakšējās un kreisi-apakšējās rūtiņas vērtībām;
šķērsļa rūtiņā vērtība $0$; GRAMATA piemērs par 12 pakāpienu kāpšanu pa $1$, $2$ vai $3$
soļiem ($a_n = a_{n-1} + a_{n-2} + a_{n-3}$ ar sākotnējām vērtībām $a_1 = 1$, $a_2 = 2$,
$a_3 = 4$, iegūstot $a_{12} = 927$); klasiska olimpiāžu uzdevums par karaļa vai tornīša
ceļu skaitu uz šaha galda no $A1$ uz $H8$ ar šķēršļiem.
