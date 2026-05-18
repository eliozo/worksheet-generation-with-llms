# Raksturīgākās pamatošanas kļūdas kombinatoriskos spriedumos 5.–9. klasē

Šis ir papildinājums kombinatorikas pamatošanas metožu sarakstam — kļūdu apkopojums, kas tipiski parādās iesācēju risinātāju kombinatoriskos pamatojumos. Kļūdas ietver gan tehniskas (saskaitīšanas, pārklāšanās), gan loģiskas (vispārināšana no atsevišķa gadījuma, neuzbūvēts viens no “Kāds lielākais” pierādījuma diviem soļiem), gan strukturālas (jaucot uzdevumu tipus “Vai iespējams” un “Vai vienmēr”). Numerācija sākas ar 1, lai to nesajauktu ar metožu sarakstu.

---

## 1. DoubleCountingTheSameObject

**(1)** No 5.klases.
**(2)** Viena un tā paša objekta saskaitīšana divreiz.  
**(3)** Counting the same object twice  
**(4) Apraksts.** Skaitot objektus, kas pieder vairākām grupām vai apmierina vairākus nosacījumus, skolēns saskaita kopas tieši, neatņemot pārklājošos objektus. Visbiežāk šī kļūda parādās uzdevumos ar Eilera-Venna diagrammām (2 vai 3 kopas) un saskaitīšanas likuma lietojumos, kur grupas patiesībā nav disjunktas. Tipiska forma: $|A \cup B| = |A| + |B|$, aizmirstot atņemt $|A \cap B|$, vai trīs kopu gadījumā nepareizi summējot, neapsverot triju kopu pārklājumu. Skolēns šeit pieņem disjunkta sadalījuma struktūru tur, kur tās nav.

**(5) Piemēri.**
- Klasē ir $30$ skolēnu, $18$ patīk matemātika, $15$ patīk fizika, $8$ patīk abas. Skolēns saka: "Kopā $18 + 15 = 33$ skolēni patīk vismaz viens priekšmets" — bet rezultāts pārsniedz pat klases lielumu! Pareizi: $|M \cup F| = 18 + 15 - 8 = 25$, tātad $5$ skolēniem nepatīk neviens.
- `LV.NOL.2021.5.1`-stila uzdevumā ar trim mācību priekšmetiem (matemātika, sociālās zinības, latviešu valoda): skolēns saskaita visus skaitļus no apraksta (piem., $400 + 100 + 40 + 90 + 71 = 701$) un atņem no kopuma, neapsverot, ka skaitlis $71$ (visi trīs priekšmeti) jau ir ieskaitīts skaitļos $400$, $100$, $40$, ja tie ir formulēti kā "patīk šie divi un kāds cits", nevis "patīk tieši šie divi". Šeit uzdevums apzināti formulēts ar "...bet nepatīk...", lai izvairītos no šīs kļūdas, taču risinātājs to var nepamanīt.
- *Klasiska kļūda:* "Cik divciparu skaitļu dalās ar $2$ vai $3$?" — skolēns rēķina $45 + 30 = 75$, aizmirstot atņemt skaitļus, kas dalās ar $6$ (kuri ir saskaitīti gan pirmajā, gan otrajā grupā). Pareizi: $45 + 30 - 15 = 60$.

---

## 2. ForgettingToSubtractOvercountingFromSymmetries

**(1)** No 7.klases.
**(2)** Neatņem simetriju radīto pārskaitījumu.  
**(3)** Failing to divide out symmetries  
**(4) Apraksts.** Kad uzdevumā objekti tiek uzskatīti par identiskiem, ja tos var iegūt vienu no otra ar pagriešanu, spoguļattēlu vai cita veida simetriju, skolēns saskaita visus formāli atšķirīgos izvietojumus un nedala ar simetrijas grupas lielumu. Vai arī otrādi: dala, bet ar nepareizu skaitli — neapsver, ka daži objekti var būt paši savu spoguļattēlu (un tāpēc dalīšanas argumenta vienkāršais variants neder). Šī kļūda parādās uzdevumos par cilvēkiem ap apaļu galdu, simboliem uz monētām/plāksnītēm, kaklarotām, krāsojumiem, ko var pagriezt.

**(5) Piemēri.**
- `LV.AMO.2022A` plāksnītes uzdevumā (5 skaitļi piecstūra virsotnēs, plāksnītes var grozīt un apgriezt): skolēns aprēķina $5! = 120$ izvietojumus un raksta to kā atbildi, neapsverot, ka plāksnīti var pagriezt $5$ veidos un apgriezt vēl $2$ veidos. Pareizā atbilde: $120/(5 \cdot 2) = 12$.
- *Klasisks 7.–8.kl. uzdevums:* "Cik dažādās secībās $5$ cilvēki var apsēsties ap apaļu galdu?" Skolēns raksta $5! = 120$ — bet patiesībā jādala ar $5$ (rotāciju skaits), tātad atbilde ir $24$. Vai vēl smalkāk: ja apaļā galda divi izvietojumi, kas ir spoguļattēli viens otram, ir uzskatāmi par vienādiem, jādala vēl ar $2$ — atbilde $12$.
- *6.–7.kl. uzdevums par krellēm:* "Cik dažādas kaklarotas var izveidot no $6$ dažādu krāsu pērlītēm?" Skolēns raksta $6! = 720$. Pareizi: jādala ar $6 \cdot 2 = 12$ (rotācijas + apgriešana), atbilde $60$. Vai pat tikai ar $6$ ($120$ veidi), ja kaklarotu nevar apgriezt otrādi.

---

## 3. ConfusingOrderedVsUnorderedSelections

**(1)** No 7.klases.
**(2)** Sajauc sakārtotas un nesakārtotas izlases.  
**(3)** Confusing ordered and unordered selections  
**(4) Apraksts.** Skolēns izvēļas formulu (reizināšanas likumu, faktoriālu, kombinācijas, permutācijas), neapsverot, vai uzdevumā objektu secībai ir nozīme. Tipiskās sekas: vai nu pārskaita (izmanto sakārtotu izlasi tur, kur secībai nav nozīmes), vai pārāk maz saskaita. Šis ir tieši GRAMATAS norādītais izaicinājums: "Ievēro elementu secību: vai uzdevumā ir svarīgi, kurš ir pirmais, kurš otrais?" — kas iesācējiem bieži paliek nepamanīts. Skolēnam jāprot atšķirt "izvēlēties $3$ no $10$" (bez secības, $C(10,3) = 120$) no "izveidot trīsvietīgu rindu no $10$ kandidātiem" (ar secību, $10 \cdot 9 \cdot 8 = 720$).

**(5) Piemēri.**
- *Tipisks 7.kl. uzdevums:* "Cik veidos no $5$ skolēniem var izvēlēties komandu $3$ skolēnu sastāvā?" Skolēns raksta $5 \cdot 4 \cdot 3 = 60$, neapsverot, ka komandas elementu secībai nav nozīmes. Pareizi: $60 / 3! = 10$.
- *6.–7.kl. uzdevums:* "Cik dažādos veidos $4$ bērni var apsēsties uz $4$ krēsliem rindā?" Skolēns raksta $C(4,4) = 1$ (uzskata, ka nav svarīgi, kurš kur sēž) — bet patiesībā uzdevumā ir runa par rindu, kur kreisais/labais galiņš ir atšķirams. Pareizi: $4! = 24$.
- `LV.AMO.2019.9.1`-stila uzdevumā ar paralelogramiem (sk. risinājumu, kur izvēloties divas no $4$ horizontālajām taisnēm, raksta $4 \cdot 3 : 2 = 6$): skolēns var aizmirst dalīt ar $2$ un saskaitīt $4 \cdot 3 = 12$, neapsverot, ka taišņu pāris $(t_1, t_2)$ un $(t_2, t_1)$ veido vienu un to pašu paralelogrāmu pāru malu izvēli.

---

## 4. MissingConstructionPartInOptimalProblems

**(1)** No 7.klases.
**(2)** "Kāds lielākais" uzdevumos trūkst piemēra (vai pierādījuma, ka lielāks neder).  
**(3)** Missing construction or upper bound in optimum problems  
**(4) Apraksts.** Optimizācijas uzdevumiem ar `questionType:FindOptimal` ir divas daļas: (a) konstruktīvs piemērs, kurā atbildes vērtība tiek sasniegta, un (b) pierādījums, ka neviens piemērs ar lielāku (vai mazāku) vērtību nav iespējams. Skolēns bieži aizmirst vai nu vienu no šīm daļām. Visbiežāk trūkst (b) daļa: skolēns atrod labu piemēru ar, teiksim, $21$ viesi (sk. `LV.AMO.2023.5.5`), bet neapsver, kāpēc tieši $22$ nav iespējami — un pasludina, ka atbilde ir $21$. Vai pretēji: skolēns parāda novērtējumu ($x \leq 21$), bet nepamato, ka šī vērtība arī tiek sasniegta — varbūt tā ir tikai virsējais novērtējums, un patiesā atbilde ir mazāka.

**(5) Piemēri.**
- `LV.AMO.2024.7.4` (10×10 rūtiņas, figūras pa $6$ rūtiņām): skolēns raksta "$100 : 6 = 16$, atlikumā $4$, tātad atbilde ir $16$" — bet neuzkonstruē piemēru ar $16$ figūrām. Patiesībā novērtējums dod tikai $\leq 16$; lai pierādītu, ka tieši $16$ tiek sasniegts, jāuzrāda izvietojums (10.att. risinājumā).
- `LV.AMO.2023.5.5` (Gunas konfektes, lielākais viesu skaits): skolēns raksta tikai konstrukciju ar $21$ viesi un pasludina atbildi $21$, neapsverot, kāpēc $22$ nav iespējami. Vai arī pretēji — pierāda, ka vairāk par $21$ nav iespējami caur kontroldarbu skaita ierobežojumu, bet konkrētu piemēru ar $21$ neuzkonstruē, tā ka nav skaidrs, vai atbilde nav $20$ vai mazāk.
- *Klasisks piemērs:* "Kāds ir mazākais virsotņu skaits grafam, kurā katrai virsotnei ir pakāpe $3$?" Skolēns raksta "vajag vismaz $4$, jo no katras virsotnes iziet $3$ šķautnes" — bet neuzrāda nevienu reālu grafu ar $4$ virsotnēm, kur tas izpildās. Faktiski jāpierāda, ka tieši $4$ ir sasniedzami (piem., pilnais grafs $K_4$).

---

## 5. ConfusingExistenceVsUniversalityQuantifier

**(1)** No 6.klases.
**(2)** Sajauc "Vai eksistē" ar "Vai vienmēr" uzdevumu struktūru.  
**(3)** Confusing existence ("can it be?") with universality ("is it always?")  
**(4) Apraksts.** GRAMATĀ (1.3. nodaļā) tiek skaidri šķirti divi uzdevumu tipi: "Vai iespējams/eksistē...?" (kur "jā" atbilde prasa vienu piemēru, "nē" atbilde prasa vispārīgu pierādījumu) un "Vai noteikti/vienmēr/visiem...?" (kur situācija ir tieši pretēja: "jā" prasa vispārīgu pierādījumu, "nē" prasa pretpiemēru). Skolēns parasti to sajauc — uz "Vai vienmēr...?" jautājumu sniedz vienu piemēru, kur tas izpildās, un secina, ka "jā, vienmēr", neapsverot, ka jautājums prasa to izpildīšanos visos gadījumos.

**(5) Piemēri.**
- *Klasisks 5.–6.kl. uzdevums (GRAMATĀ kā 6. piemērs):* "Vai skaitļa kvadrāts noteikti ir lielāks nekā pats skaitlis?" Skolēns raksta "Jā, jo $3^2 = 9 > 3$" — bet uzdevums prasa, vai tas izpildās *visiem* skaitļiem. Pareizi: "Nē, ne noteikti. Piemēram, $\left(\tfrac{1}{2}\right)^2 = \tfrac{1}{4} < \tfrac{1}{2}$" (vienu pretpiemēru pietiek).
- *GRAMATAS 7. piemērs:* "Vai vienmēr, negatīvam skaitlim pieskaitot tā kvadrātu, iegūst pozitīvu skaitli?" Skolēns raksta "Jā, jo $(-2) + (-2)^2 = 2 > 0$" — bet jāatrod pretpiemērs, piem., $(-1) + (-1)^2 = 0$, kas nav pozitīvs.
- `LV.AMO.2023.9.4` stila uzdevums ("Vai vienmēr var sadalīt sešās grupās...?"): skolēns konstruē vienu piemēru, kur var sadalīt, un raksta "Jā, vienmēr". Patiesībā uzdevums prasa atbildi par *visiem* iespējamiem sākotnējiem datiem; pierādījumam jābūt vispārīgam, vai arī jāatrod pretpiemērs (kā risinājumā ar $4 \times 9$ tabulu).

---

## 6. ConcreteToGeneralLeapInCombinatorialClaim

**(1)** No 5.klases.
**(2)** Vispārinājums no atsevišķa gadījuma ("nepilnā indukcija").  
**(3)** Hasty generalization from particular cases  
**(4) Apraksts.** Skolēns pārbauda apgalvojumu $2$–$3$ konkrētos gadījumos (piem., $n = 1, 2, 3$), redz, ka tas izpildās, un secina, ka tas izpildās *visiem* $n$, bez vispārīga pamatojuma. Šī ir kombinatorikas tipiska kļūda, kas paplašina algebrai raksturīgo "concreteToGeneralLeap" arī uz kombinatoriskām struktūrām: skolēns atrod likumsakarību mazos gadījumos un to izmanto kā pierādījumu. Lai gan induktīvi spriedumi (hipotēzes formulēšana) ir noderīgi, tos jāpārbauda ar vispārīgu argumentu — vai nu matemātisku struktūras analīzi, vai matemātisko indukciju (vidusskolā).

**(5) Piemēri.**
- *Klasisks piemērs (GRAMATĀ pieminēts):* skolēns pārbauda, ka $n^2 - n + 41$ ir pirmskaitlis, ja $n = 1, 2, 3, \ldots, 10$, un secina, ka $n^2 - n + 41$ vienmēr ir pirmskaitlis. Patiesībā pie $n = 41$ tas dod $41^2$, kas nav pirmskaitlis.
- *7.–8.kl. uzdevums:* "Cik daudzstūru var izveidot no $n$ punktiem, no kuriem nekādi trīs nav uz vienas taisnes?" Skolēns pārbauda $n = 3, 4, 5$ un secina formulu, neapsverot, vai tā darbojas pie lielākiem $n$ (jāveic strukturāls arguments par to, kā punktu pievienošana ietekmē skaitu).
- `LV.NOL.2021TEST.7.2`-stila uzdevums (aplī izvietoti skaitļi): skolēns pārbauda mazākus gadījumus ($n = 4, 5, 6$ skaitļiem) un izteic hipotēzi par mazāko maiņu skaitu. Hipotēze jāpārbauda struktūras līmenī, nevis tikai jāuztic, ka tā darbojas arī pie $n = 8$.

---

## 7. ImplicitAssumptionAboutObjectsBeingDistinct

**(1)** No 6.klases.
**(2)** Klusais pieņēmums, ka objekti ir atšķirīgi (vai pretēji — vienādi).  
**(3)** Implicit assumption that objects are distinct (or identical)  
**(4) Apraksts.** Skolēns nepamana, ka uzdevumā objekti var būt vienādi vai atšķirīgi — un izvēlas formulu, kas atbilst nepareizam pieņēmumam. Piemēram, sadalot $10$ konfektes $3$ bērniem: ja konfektes ir vienādas, ir $C(12,2) = 66$ veidi (zvaigznes un spraugas); ja katra konfekte ir atšķirīga, tad katra konfekte tiek piešķirta vienam no $3$ bērniem neatkarīgi — $3^{10}$ veidi. Otrs variants: uzdevumā par dažādu izvietojumu skaitīšanu skolēns aizmirst, ka objekti, kas formāli ir dažādi, varbūt simetrijas dēļ jāuzskata par vienādiem (sk. kļūdu #2). Šī kļūda parasti rodas no uzdevuma teksta nepilnīgas izlasīšanas.

**(5) Piemēri.**
- *Klasisks 7.kl. uzdevums:* "Cik veidos $5$ vienādu konfekšu kaudzīti var sadalīt $2$ bērniem (varbūt vienam nedabū)?" Skolēns raksta $2^5 = 32$ (uzskata, ka katra konfekte tiek piešķirta atsevišķi) — bet konfektes ir vienādas, tāpēc atbilde ir $6$ (kaudzīte, kas atbilst Aigaram, var būt $0, 1, 2, 3, 4$ vai $5$ konfektes lielumā).
- *6.kl. uzdevums:* "Cik veidos var izlikt $3$ vienādas grāmatas un $2$ vienādas glāzes uz plaukta?" Skolēns raksta $5! = 120$, neapsverot, ka grāmatas vienai ar otru savstarpēji ir vienādas, un tāpat glāzes. Pareizi: $\frac{5!}{3! \cdot 2!} = 10$.
- *Inverss piemērs (skolēns pieņem, ka objekti vienādi, lai gan tie ir atšķirīgi):* "Cik veidos $4$ studenti var pasūtīt $3$ veidu kafiju (espresso, late, kapučino)?" Skolēns raksta $C(4+2, 2) = 15$ kā kombinācijas ar atkārtošanu — bet katrs students ir konkrēts cilvēks, kas atšķirams no citiem; tāpēc pareizi ir $3^4 = 81$ veidi (katrs students neatkarīgi izvēlas vienu no $3$ veidiem).

---

## 8. IncompleteCaseAnalysisInCombinatorialBranching

**(1)** No 6.klases.
**(2)** Nepilnīga gadījumu šķirošana zaru uzskaitījumā.  
**(3)** Incomplete case analysis  
**(4) Apraksts.** Risinātājs sadala uzdevumu vairākos gadījumos (piem., pēc kāda parametra vērtības, krāsas, paritātes, lieluma), bet kādu gadījumu izlaiž — vai nu aizmirst vispār, vai uzskata par "neiespējamu" bez pārbaudes. Tas attiecas gan uz pārlasi (kļūda #3 metožu sarakstā), gan uz pretrunas argumentu, gan uz Eilera-Venna diagrammām. Galvenais — risinātājs pieņem, ka viņa minēto gadījumu kopa pārklāj visas iespējas, bez skaidras pamatošanas. Tipiska forma: skolēns aplūko gadījumus $n = $ pāra un $n = $ nepāra, bet kāds no tiem nav pilnībā izpētīts.

**(5) Piemēri.**
- `LV.AMO.2019.8.4` (rūķīši, kuru draugu skaits ir kubs): risinājumā jāizšķir gadījumi pēc $m$ paritātes. Skolēns aplūko tikai $m$ — pāra ($m$ rūķīšus sadala pa pāriem) un raksta "Atbilde — visi pāra skaitļi", aizmirstot pārbaudīt, vai un kuriem nepāra $m$ tas der. Pareizi: nepāra $m \geq 9$ arī der, bet $m \leq 7$ neder.
- `LV.NOL.2024.8.4` (5 gardēži, 16 tortes): skolēns aplūko gadījumu, kad katrs gardēdis pērk tieši $3$ tortes, un secina, ka tādā gadījumā kopā nopērk $15$. Bet skolēns aizmirst aplūkot gadījumus, kur gardēdis pērk $1$ vai $2$ tortes — kas patiesībā arī jāizslēdz, jo katram gardēdim atļauts pirkt ne vairāk kā $3$ tortes.
- *Klasiska 7.–8.kl. spēļu uzdevums:* "Pirmajā gājienā pirmais spēlētājs aizpilda centra rūtiņu". Skolēns parasti apraksta tikai stratēģiju gadījumam, kad otrais spēlētājs aizpilda noteiktu rūtiņu, un nepārbauda visus iespējamos pretinieka gājienus. GRAMATĀ tieši šis ir pieminēts kā "raksturīgākā kļūda — neņemot vērā visus iespējamos spēlētāju gājienus".

---

## 9. ConfusingNecessaryWithSufficientCondition

**(1)** No 8.klases.
**(2)** Sajauc nepieciešamo un pietiekamo nosacījumu.  
**(3)** Confusing necessary with sufficient conditions  
**(4) Apraksts.** Skolēns parāda, ka kāda īpašība $P$ ir nepieciešama (no $A$ seko $P$), un bez papildu pamatojuma secina, ka tā ir arī pietiekama (no $P$ seko $A$). Šī ir tipiska kļūda Dirihlē principa un invarianta argumentos. Piemēram, paritātes argumentā: skolēns parāda, ka kopējais skaits ir pāra invariants, un tāpēc beigu stāvoklis ar pāra skaitu ir teorētiski sasniedzams — neapsverot, ka tas tiešām tiek sasniegts (parasti tas prasa konstruēt piemēru). Vai otrādi: skolēns parāda, ka summas atlikums dalot ar $n$ ir invariants, un tāpēc tikai atbilstoši mērķi ir nesasniedzami — bet kāds no tiem patiesībā arī nav sasniedzams citu iemeslu dēļ. Skolēnam nav apzināta robežas starp "neder, jo neapmierina nosacījumu" un "nederība ir pierādīta tieši".

**(5) Piemēri.**
- `LV.AMO.2024.9.3` (Agnese, trīs skaitļi $11, 12, 13$): skolēns pierāda, ka skaitļu paritātes konfigurācija (viens pāra, divi nepāra) ir invariants. Mērķis $(20, 24, 25)$ ir cita paritātes konfigurācija (divi pāra, viens nepāra), tāpēc neder. Tas ir korekts pretrunas arguments. Bet, ja mērķis būtu $(20, 22, 27)$ (viens pāra, divi nepāra — tāda pati paritāte kā sākotnējā), skolēns varētu secināt: "tāda pati paritāte, tāpēc to var sasniegt". Tas ir kļūdaini — paritātes saglabāšanās ir tikai nepieciešams nosacījums, bet ne pietiekams; var būt citi šķēršļi (piem., kopējās summas invariants).
- `LV.AMO.2023.9.5(A)` (16 starpību summa $S = 100$): skolēns konstatē, ka $S$ vienmēr ir pāra (jo tā ir paritātes invariants), un secina, ka jebkura pāra vērtība starp $1$ un $maksimālo$ ir sasniedzama. Patiesībā jāpārbauda katra atsevišķi — daži pāra skaitļi var arī nebūt sasniedzami.
- *Klasiska kļūda Dirihlē principa lietojumā:* "$8$ punkti $7$ rindās, tāpēc kādā rindā ir vismaz $2$ punkti." Skolēns secina: "tātad visās rindās ir vismaz $2$ punkti" — sajaucot eksistences apgalvojumu ($\exists$ rinda ar $\geq 2$) ar universālo ($\forall$ rinda ar $\geq 2$). Dirihlē princips garantē tikai eksistenci.

---

## 10. MisusingPigeonholeWithWrongCounts

**(1)** No 7.klases.
**(2)** Dirihlē principa nepareiza pielietošana ar kļūdainu būru/trušu skaitu.  
**(3)** Misapplying pigeonhole with wrong pigeon/hole counts  
**(4) Apraksts.** Dirihlē principu skolēns formāli zina, bet to lieto uzdevumā ar nepareizu trušu un būru identificēšanu — vai nu apgriež trušus un būrus (kas dod aplamus secinājumus), vai izvēlas tādus, kuriem nav neapšaubāmas $1$-uz-$1$ attiecības, vai vienkārši kļūdaini saskaita kopas lielumus. Variants ar vispārinātu Dirihlē principu: skolēns aizmirst, ka, lai būtu vismaz $m+1$ objekts vienā grupā, nepieciešams *vairāk nekā* $m \cdot n$ objekti, nevis $\geq m \cdot n$. Vēl viens variants: skolēns Dirihlē principu lieto tur, kur faktiski strādātu vienkāršāks pretrunas arguments, un kļūdās ar grupu izveidi.

**(5) Piemēri.**
- *Klasiska kļūda (GRAMATAS stilā):* "$12$ skolēnu klase. Vai noteikti ir mēnesis, kurā dzimuši vismaz divi skolēni?" Skolēns saka "Jā, pēc Dirihlē principa, jo $12$ skolēni, $12$ mēneši". Patiesībā $12$ skolēni var būt sadalīti pa $1$ vienā mēnesī — Dirihlē princips šeit nedarbojas, jo nav *vairāk* skolēnu nekā mēnešu. Vajag $13$ skolēnus, lai princips strādātu.
- `LV.AMO.2024.9.2` (28 skolēni, atzīmes no $0$ līdz $10$, vajag $4$ ar vienādu): skolēns piemēro Dirihlē principu tieši: "$28$ skolēni, $11$ atzīmes, $28 = 11 \cdot 2 + 6$, tātad kādā grupā ir vismaz $3$" — kas ir patiess, bet nepietiekams (vajadzīgi $4$). Pareizi: jāizmanto pārgrupēšana (piem., atzīmes $8, 9, 10$ vienā grupā), kā risinājumā parādīts.
- *7.–8.kl. tipiska kļūda:* "$20$ studenti uzrakstīja kontroldarbu ar maksimālo punktu skaitu $100$. Vai noteikti $2$ studenti saņēma vienādu punktu skaitu?" Skolēns saka "Jā, pēc Dirihlē, jo $20$ studenti, $100$ iespējamie punktu vērtējumi" — bet $20 < 100$, tāpēc princips šeit *nedarbojas*. Patiesībā nav noteikti — visi $20$ var saņemt dažādus punktus.

---

## 11. ImplicitParityOrModularAssumption

**(1)** No 8.klases.
**(2)** Klusais pieņēmums par paritāti vai dalāmību.  
**(3)** Implicit assumption about parity or divisibility  
**(4) Apraksts.** Skolēns invariantu argumentā pamana paritāti vai modulāru īpašību, ko saglabā atļautās darbības, bet aizmirst pārbaudīt visus iespējamos gājienu veidus — pārbauda dažus tipiskus un secina, ka invariants saglabājas. Vai arī otrādi: lieto invarianta argumentu, neformulējot to nepārprotami. Piemēram, raksta "katrā gājienā summa pieaug par pāra skaitli" — bet patiesībā kāds gājiena variants summu maina arī par nepāra skaitli; skolēns šo gadījumu aizmirst pārbaudīt. Šī kļūda parasti rodas, kad atļauto darbību ir vairākas (piem., pieskaitīt $3$ vai atņemt $7$), bet skolēns pārbauda invariantu tikai vienai no tām.

**(5) Piemēri.**
- `LV.AMO.2022A.12.2` (bumbiņu trauks ar diviem darbību variantiem): skolēns aplūko tikai vienu gadījumu (piem., kad paņemtas divas baltas), parāda, ka balto bumbiņu skaits samazinās par $2$, un secina "tātad paritāte saglabājas". Bet jāpārbauda *visi trīs gadījumi* (b+b, m+m, b+m) un parādīt, ka katrā no tiem paritāte saglabājas. Risinājumā šis tieši ir izdarīts kā tabula — pareizais paņēmiens.
- *7.–8.kl. klasiska kļūda:* "Uz tāfeles uzrakstīts skaitlis $5$. Ar vienu gājienu var pieskaitīt $7$ vai atņemt $3$. Vai var iegūt skaitli $2$?" Skolēns saka: "Katrā gājienā skaitļa atlikums dalot ar $5$ saglabājas, jo $7 \equiv 2 \pmod 5$ un $-3 \equiv 2 \pmod 5$" — pārbauda tikai vienu invariantu un secina, ka $2 \not\equiv 0 \pmod 5$ (bet $5 \equiv 0$), tāpēc neder. Patiesībā $7 \equiv 2 \pmod 5$ un $-3 \equiv 2 \pmod 5$ tiešām dod modulāru ierobežojumu, bet pareizais arguments ir atšķirīgs: $7$ un $3$ ir savstarpēji pirmskaitļi, tāpēc ar to lineāru kombināciju var iegūt jebkuru veselu skaitli — un atbilde patiesībā ir "jā" (piem., $5 + 7 + 7 - 3 - 7 - 7 = -2$, kas nav $2$; pareizais aprēķins: $5 - 3 = 2$). Skolēns te kļūdījies, lietojot modulāro invariantu uz darbībām, kas to nesaglabā.
- `LV.AMO.2024` skaitļu virkne (pirmreizinātāju skaita paritāte): skolēns var aizmirst, ka skaitlis $4$ var tikt iegūts gan reizinot ar $2$ (paritāte mainās), gan ar $3$ (paritāte arī mainās). Bet ja skolēns aizmirst gadījumu, kad reizina ar tādu skaitli, kas pats ir izteikts kā vairāku pirmreizinātāju reizinājums, viņa argumenta paritātes pārbaude nav pilnīga.

---

### Piezīme par kļūdu raksturu un saistību ar pamatošanas metodēm

Lielākā daļa kombinatorikas kļūdu ir strukturālas (loģikas) kļūdas, kas saistītas ar uzdevuma tipa nepareizu izpratni vai pamatojuma daļas izlaišanu:

- **Saskaitīšanas un struktūras kļūdas (#1, #2, #3, #7):** rodas no neuzmanības attiecībā uz objektu identitāti, simetrijām vai izlases secības lomu. Bieži saistītas ar metožu sarakstu (`RuleOfSumDisjointCases`, `RuleOfProductIndependentChoices`, `CountingViaSymmetryClasses`).
- **Pierādījuma struktūras kļūdas (#4, #5):** trūkst kāda pierādījuma daļa, vai arī risinātājs nepareizi izprot, vai uzdevumu tipā jāatrod viens piemērs, vai jāpierāda visiem gadījumiem. Tieši attiecas uz `BoundPlusMatchingConstructionForOptimum`, `ConstructiveExampleForExistence` un `ContradictionForImpossibility`.
- **Loģikas kļūdas (#6, #9):** nepareizs vispārinājums vai nepieciešamo/pietiekamo nosacījumu sajaukšana.
- **Konkrēto metožu lietojuma kļūdas (#8, #10, #11):** rodas, lietojot specifiskas metodes (gadījumu pārlasi, Dirihlē principu, invariantus), bet to formālu lietojumu neveicot pilnībā.

5.–6. klases skolēniem visbiežāk parādās kļūdas #1, #5, #6 — tās saistītas ar pamata loģikas un saskaitīšanas iemaņām.
7.–9. klasēs pievienojas #2, #3, #4, #7, #8, #10 — kompleksākas struktūras un formālāku metožu lietojumam.
8.–9. klašu līmenī parādās arī #9, #11 — saistītas ar abstraktāku argumentu uzbūvi un invariantu/krāsojumu lietojumu.
