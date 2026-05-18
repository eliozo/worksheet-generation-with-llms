# Pamatošanas kļūdas algebriskos spriedumos 5.–9. klasē

Kļūdu un nepilnību saraksts, kas raksturīgs iesācēju risinātāju
algebriskiem pamatojumiem. Tās ir gan tehniskas 
(nepareizs pārveidojums), gan loģiskas 
(secinājums izdarīts nepareizā virzienā, izlaista pārbaude). 
Atsevišķas kļūdas ir saistītas ar konkrētu pamatošanas 
metožu nepareizu izmantošanu, citas ir vispārīgākas.

Lielākā daļa šo kļūdu nav tehniskas (aprēķinu) — tās ir 
loģikas vai uzmanības trūkums uzdevuma strukturēšanā. 
Tipiskākās uzraudzības vietas pārbaudītājam:
- **Aritmētiskajās operācijās:** #1, #2, #3, #10 
(kas, kāpēc, kāpēc nemainās zīme/sakne).
- **Loģikas struktūrā:** #4, #5, #6, #11 
(vai visi gadījumi, vai virziens pareizs, 
vai netika pārkāpta loģikas ķēde).
- **Konteksta saderībā:** kļūdas #7, #8, #9 
(vai atbilde der praktiski, vai uzdevuma teksts pareizi pārveidots).

5.–6.klases skolēniem visbiežāk parādās kļūdas #4, #6, #8 — vienkārši pieredzes trūkums sistemātiskā darbā ar gadījumiem un teksta pārtulkošanā.
7.–9.klašu skolēniem pievienojas #1, #2, #3, #7, #10, #11 — tieši saistīti ar formālo algebras tehniku un nevienādību pierādījumiem.

Kļūdas, kuras bieži pārklājas ar konkrētām pamatošanas metodēm:

* #1 un #5 saistītas ar metodi `EquivalentTransformationsOfEquationsAndInequalities` 
* #2 un #3 ar `FactorAndUseZeroProductRule` vai `SubstitutionForSimplification`, 
* #4 ar `CaseAnalysisBySignOrInterval`, 
* #11 ar `ProvingByEquivalenceChain`.



---

## 1. SignFlipForgottenInInequality

**(1)** No 7.klases.  
**(2) Aizmirsta zīmes maiņa, reizinot vai dalot nevienādību ar negatīvu skaitli**
**(3) Forgotten sign flip when multiplying or dividing an inequality by a negative quantity**

**(4) Apraksts.** Risinot nevienādību vai pārveidojot to ekvivalentā formā, abas puses reizina vai dala ar izteiksmi, kurai var būt negatīva vērtība, taču nevienādības zīme tiek atstāta tāda pati. Tipiski tas notiek, ja reizinātājs satur mainīgo (piem., reizina ar $x − 3$ neapsverot, vai $x − 3 > 0$ vai $< 0$), vai ja skolēns ir aizmirsis, ka, reizinot ar $(−1)$, no $a > b$ seko $−a < −b$, nevis $−a > −b$.

**(5) Piemēri.**
- Risinot $−3x < 12$, skolēns abas puses dala ar $−3$ un raksta $x < −4$ — pareizi būtu $x > −4$. Zīmes maiņa nav veikta.
- Pierādīšanā $(7 − x)/(x − 2) \geq 1$ skolēns reizina abas puses ar $x − 2$, neapsverot zīmi. Pareizi būtu jāizšķir divi gadījumi: ja $x > 2$, tad $7 − x \geq x − 2$; ja $x < 2$, tad $7 − x \leq x − 2$ (zīme pagriežas), un katram gadījumam atsevišķi atrast atrisinājuma daļu.
- Pierādot `LV.NOL.2023.11.1`-stila nevienādību $x^{2} + y^{2} + 1/2 \geq x + y$, skolēns pārveidotā formā $−x − y + x^{2} + y^{2} + 1/2 \geq 0$ reizina ar $−1$ (lai iegūtu “pārskatāmāku” formu) un saglabā $\geq$ zīmi — tādējādi pierāda pretējo nevienādību.

---

## 2. RootLossByDivisionByExpression

**(1)** No 7.klases.  
**(2) Sakņu pazaudēšana, dalot ar izteiksmi, kas var būt nulle**
**(3) Loss of roots when dividing by an expression that may equal zero**

**(4) Apraksts.** Vienādojuma atrisināšanā skolēns dala abas puses ar izteiksmi, kas satur nezināmo (piem., ar $x$, ar $x − 1$), neapsverot, ka šī izteiksme varētu būt nulle. Visas tās $x$ vērtības, kurām dalītājs ir nulle, tādējādi tiek izmestas no atrisinājumu kopas, lai gan dažas no tām patiesībā ir vienādojuma saknes. Šī kļūda īpaši bīstama vienādojumos formā $f(x) · g(x) = 0$ (kur pareizais paņēmiens ir $f(x) = 0$ vai $g(x) = 0$), ja skolēns mēģina abas puses dalīt ar $g(x)$.

**(5) Piemēri.**
- Vienādojuma $x^{2} = 3x$ atrisinājumā skolēns abas puses dala ar $x$ un raksta $x = 3$. Pareizi: $x^{2} − 3x = 0$, no kā $x(x − 3) = 0$, tātad $x = 0$ vai $x = 3$. Sakne $x = 0$ ir pazaudēta.
- Vienādojuma $(x − 1)(x + 2) = 3(x − 1)$ atrisinājumā skolēns abas puses dala ar $(x − 1)$ un raksta $x + 2 = 3$, tātad $x = 1$. Pareizi: $(x − 1)(x + 2) − 3(x − 1) = 0$, $(x − 1)(x + 2 − 3) = 0$, no kā $x = 1$ vai $x = 1$. Sakne $x = 1$ ir tā, kas tika pazaudēta (un faktiski sakrīt ar otru — bet vispārīgi gadījumā šī ir bieža kļūda).
- `LV.NOL.2021.10.1`-stila uzdevumā ar vienādojumu $1.2/x + 3/(x + 2) = 1$ skolēns reizina abas puses ar $5x(x+2)$, neminot pārbaudi, ka $x \neq 0$ un $x \neq −2$. Praktiski tas nesabojā šī uzdevuma atrisinājumu, bet ir pierakstā jānorāda — citādi pārbaudītājs nevar redzēt, vai skolēns to apzinās.

---

## 3. ExtraneousRootsAfterSquaring

**(1)** No 7.klases.  
**(2) Svešsakņu rašanās pēc abu pušu kvadrātēšanas (vai citas neatgriezeniskas operācijas)**
**(3) Extraneous roots appearing after squaring (or other non-equivalent operations)**

**(4) Apraksts.** Atrisinot vienādojumu, kas satur kvadrātsakni vai absolūto vērtību, skolēns abas puses kāpina kvadrātā vai atbrīvojas no moduļa, neatzīmējot, ka šī operācija nav ekvivalents pārveidojums — tā var ieviest jaunas “saknes”, kas sākotnējo vienādojumu neapmierina. Pareizs pieraksts beigās prasa pārbaudīt, vai katra iegūtā kandidāta vērtība der sākotnējam vienādojumam (it īpaši: vai izteiksme zem saknes ir nenegatīva, vai kvadrātsaknes vērtība iznāk nenegatīva).

**(5) Piemēri.**
- Vienādojumā $\sqrt{x + 4} = x − 2$ skolēns kāpina kvadrātā un iegūst $x + 4 = x^{2} − 4x + 4$, no kā $x^{2} − 5x = 0$, $x = 0$ vai $x = 5$. Bet $x = 0$ neder, jo $\sqrt{4} = 2 \neq 0 − 2 = −2$. Trūkst beigu pārbaudes; sakne $x = 5$ ir vienīgā derīgā.
- Vienādojumā $|x − 3| = 2x$ skolēns raksta $(x − 3)^{2} = (2x)^{2}$, atrod abas saknes un nepārbauda, ka labā puse jābūt nenegatīvai, t.i., $x \geq 0$. Viena no kandidātēm ($x = −3$) jāizslēdz.
- `LV.NOL.2022.12.2`-stila uzdevumā par $4x⁴ − 11x^{2} + 9x − 2 = 0$ skolēns aizvieto $t = x^{2}$ un atrisina kvadrātvienādojumu attiecībā pret $t$, iegūst negatīvu $t$ vērtību, un to “arī ieliek” kā $x = \pm \sqrt{t}$. Faktiski negatīva $t$ nedod reālu $x$.

---

## 4. CaseAnalysisIncomplete

**(1)** No 5.klases.  
**(2) Nepilnīga gadījumu šķirošana**
**(3) Incomplete case analysis**

**(4) Apraksts.** Risinājuma autors sadala uzdevumu vairākos gadījumos atkarībā no nezināmā zīmes, lieluma vai cita parametra, bet aizmirst kādu gadījumu (piemēram, $x = 0$ starp pozitīviem un negatīviem skaitļiem; vienlīdzības gadījumu starp $<$ un $>$; vai trūkst paritātes gadījuma). Vēl viens variants — visi gadījumi minēti, bet kādam no tiem nav veikts atsevišķs pamatojums, un autora pierakstā tas izklausās tā, it kā secinājums būtu acīmredzams. Beigu sintēzes solī jāpārbauda, vai gadījumi pārklāj visas iespējas.

**(5) Piemēri.**
- Salīdzinot $2a$ un $4a$, skolēns raksta: “ja $a > 0$, tad $4a > 2a$; ja $a < 0$, tad $4a < 2a$” — bet aizmirst gadījumu $a = 0$, kurā abi ir vienādi (sk. GRAMATAS 4.3.8. nodaļas piemēru, kur tieši šī kļūda nosaukta kā tipiska).
- Risinot uzdevumu par `LV.NOL.2022.8.3`-stila platleņķa vienādsānu trijstūri (∠ABC = 20°), skolēns aplūko tikai gadījumu $AB = AC$ un secina $3AC = 3AB > AB$, neapsverot otru gadījumu, kur $BC = AC$. Risinājums jākonstruē kā divu gadījumu apvienojums.
- Vienādojumā ar absolūto vērtību $|x − 2| + |x + 1| = 5$ skolēns aplūko tikai gadījumu $x \geq 2$ un gadījumu $x \leq −1$, bet aizmirst vidējo gadījumu $−1 \leq x \leq 2$. Atrasti tikai daži atrisinājumi; pārbaudē iztrūkst pilnais skaitlīnijas pārklājums.

---

## 5. WrongDirectionOfInequalityChain

**(1)** No 7.klases.  
**(2) Secinājums nepareizā virzienā (nevienādības “pavājināšana” pierādījumam)**
**(3) Wrong direction of inference in an inequality chain**

**(4) Apraksts.** Pierādot nevienādību $A \geq B$, skolēns pavājina vienu no pusēm un secina nepareizi. Konkrētāk: lai pierādītu $A \geq B$, pietiek atrast tādu $C$, ka $A \geq C \geq B$ (pastiprināšana caur starpniecību). Bet, ja skolēns no $A \geq C$ un $B \geq C$ secina $A \geq B$, tas nekādā ziņā neseko — abas puses ir “lielākas par C”, bet to savstarpējais sakārtojums nav noteikts. Cita variante: lai pierādītu $A \leq B$, skolēns atrod $C$, ka $A \leq C$, un secina $C \leq B$, bet tas pats par sevi nepierāda $A \leq B$. Šī kļūda parasti rodas no neuzmanības vai no “pa daļām” pierādījumu rakstīšanas, kur autors aizmirst, kura virziena nevienādība bija pierādāma.

**(5) Piemēri.**
- Lai pierādītu $a^{2} + b^{2} \geq 2$, skolēns raksta: “Mēs zinām, ka $a^{2} \geq 0$ un $b^{2} \geq 0$, tātad $a^{2} + b^{2} \geq 0$. Bet $2 \geq 0$, tātad $a^{2} + b^{2} \geq 2$.” Šis ir loģikas pārkāpums — no $A \geq 0$ un $2 \geq 0$ neseko $A \geq 2$. (Patiesībā nevienādība $a^{2} + b^{2} \geq 2$ arī nav patiesa visiem $a, b$, piemēram, neder $a = b = 0$.)
- Pierādījumā par `LV.AMO.2024.11.1`-stila nevienādību $(a^{2}+2bc)/(b^{2}+c^{2}) + (b^{2}+2ac)/(a^{2}+c^{2}) + (c^{2}+2ab)/(a^{2}+b^{2}) > 3$ skolēns raksta: “Katrs saskaitāmais ir lielāks par $2bc/(b^{2}+c^{2}) \geq 0$, tāpēc visa summa ir lielāka par $0$.” Pavājināts gan novērtējums ($2bc/(b^{2}+c^{2}) \geq 0$ ir trivials, neredz, ka saskaitāmais > 1), gan beigu secinājums (jāpierāda $> 3$, ne $> 0$).
- Pierādot $3·AC > AB$ `LV.NOL.2022.8.3`-stila uzdevumā, skolēns raksta: “Tā kā $AC > 0$ un $AB > 0$, tad $3·AC > AB$.” Šis pavisam neizmanto uzdevuma nosacījumus un nepierāda neko — vienkārši konstatē, ka abas puses ir pozitīvas.

---

## 6. ConcreteToGeneralLeap

**(1)** No 5.klases.  
**(2) Vispārinājums no atsevišķa gadījuma (induktīvs lēciens bez pamatojuma)**
**(3) Hasty generalization from a particular case**

**(4) Apraksts.** Skolēns aplūko vienu vai divus konkrētus piemērus un secina, ka apgalvojums ir patiess vispār — bez papildu pamatojuma vai pārbaudes ar pretpiemēriem. Šī ir tipiska kļūda olimpiāžu uzdevumos formā “Vai patiesi, ka …?” vai “Pierādīt, ka …”, kur risinājuma autors atrod vienu piemēru un raksta to kā pilno pierādījumu. Pretējā kļūda — atrast vienu pretpiemēru un būt pārliecinātam, ka uzdevums ir “neatrisināms vispār” (tas ir korekti, ja prasīts pamatot apgalvojumu pretrunīgumu, bet bīstami citos kontekstos).

**(5) Piemēri.**
- `LV.TVC.2005/2006`-stila uzdevumā “Salīdzini $x$ un $y$, ja $3x = y$ un $x, y$ ir naturāli skaitļi”. Skolēns paņem $x = 1, y = 3$ un secina $x < y$ — bet neminot, kāpēc tas izpildās visiem naturāliem $x, y$. Pareizi būtu: tā kā $y = 3x$ un $x \geq 1$, tad $y − x = 2x \geq 2 > 0$, tātad $y > x$. (GRAMATAS norāžu pirmais punkts tieši brīdina: pārbaudi, vai hipotēze, kas iegūta no piemēriem, izpildās *visos gadījumos*.)
- Pierādot, ka $n^{2} + n$ ir pāra skaitlis visiem naturāliem $n$, skolēns pārbauda $n = 1, 2, 3, 4$ un secina, ka tas patiess vispār. Trūkst vispārējā arguments (piem., $n^{2} + n = n(n+1)$ ir divu secīgu skaitļu reizinājums, un viens no tiem ir pāra).
- Atbildot uz “Vai eksistē tāds…”, skolēns saka “Nē, nav”, jo trīs mēģinājumos neatrada. Tāds pierādījums nav korekts; jāparāda neeksistence ar struktūras argumentu (piem., paritāte, dalāmība, novērtējums).

---

## 7. MissedSolutionsWhenSquareRootOfSquare

**(1)** No 7.klases.  
**(2)** $\sqrt{x^{2}} = x$ vietā jābūt $|x|$
**(3)** Treating $\sqrt{x^{2}}$ as $x$ instead of $|x|$

**(4) Apraksts.** Skolēns vienkāršo $\sqrt{x^{2}}$ uz $x$ neapsverot, ka $x$ var būt negatīvs. Pareizais pārveidojums ir $\sqrt{x^{2}} = |x|$, kas vienlaikus pārklāj abus gadījumus. Šī kļūda parādās arī izteiksmēs ar diskriminantu ($\sqrt{D}$ vai $\pm\sqrt{D}$), kvadrātvienādojuma sakņu formulā un Pitagora teorēmas lietojumos, kur tiek aizmirsts, ka attālums vai mala jābūt pozitīvai (jāņem nenegatīvā sakne).

**(5) Piemēri.**
- Atrisinot $x^{2} = 49$, skolēns raksta $x = \sqrt{49} = 7$, aizmirstot otru sakni $x = −7$. Pareizi: $x^{2} = 49 \Leftrightarrow |x| = 7 \Leftrightarrow x = 7$ vai $x = −7$.
- `LV.NOL.2022.9.1`-stila uzdevumā par $D = (2m+3)^{2} − 24m = (2m−3)^{2}$ skolēns raksta $\sqrt{D} = 2m − 3$ un atrod tikai vienu saknes formulu. Pareizi: $\sqrt{D} = |2m − 3|$, un, lai izsekotu abām saknēm, jāizšķir gadījumi $m \geq 3/2$ un $m < 3/2$ (vai vienkārši lietot $\pm|2m − 3|$, kas ir tas pats kā $\pm(2m − 3)$).
- Pitagora teorēmas lietojumā: no $c^{2} = 25$ skolēns raksta $c = \pm 5$, aizmirstot, ka $c$ ir trijstūra malas garums (jābūt pozitīvai vērtībai); jāizvēlas tikai $c = 5$.

---

## 8. IncorrectTranslationOfWordProblem

**(1)** No 5.klases.  
**(2) Nepareizi sastādīts vienādojums teksta uzdevumam (kļūdaina situācijas pārtulkošana matemātikā)**
**(3) Incorrect translation of a word problem into an equation**

**(4) Apraksts.** Risinot teksta uzdevumu, skolēns nepareizi pārvērš situācijas aprakstu vienādojumā. Tipiski:
- “par tik vairāk/mazāk nekā” tiek samainīts ar “tik reižu vairāk/mazāk nekā” (sajaucot saskaitīšanu ar reizināšanu),
- “a salīdzinājumā ar b” samainās ar “b salīdzinājumā ar a”,
- procentu uzdevumā “par 20% palielinās” tiek pārveidots par “tagad ir 20% no sākotnējā” (kas ir samazinājums uz piekto daļu),
- lielumus, kuriem dažādās uzdevuma daļās ir dažādas mērvienības (km/h un km/min; minūtes un stundas), saskaita kā vienādus.

**(5) Piemēri.**
- “Aitas ir par 6 vairāk nekā zirgu” skolēns pieraksta kā $a = 6z$. Pareizi: $a = z + 6$. (Tas ir tieši `LV.TVC.2007/2008.4` tips, kur jāatrod, kura no piedāvātajām vienādībām ir aplama.)
- “Maruta ir trīsreiz vecāka par Elīnu” skolēns pieraksta kā $M + 3 = E$ (sajauc “trīsreiz vairāk” ar “par 3 vairāk”) vai pat kā $3M = E$ (samaina, kurš no kā izteikts).
- `LV.AMO.2022A.7.1` stilā: “Vilnis uz 4 jautājumiem atbild 30 sekundēs” — skolēns raksta $V = 30/4$ un domā, ka tas ir “Viļņa ātrums” (sekundes uz jautājumu), bet uzdevuma turpinājumā šo lielumu lieto kā “jautājumi uz minūti”, sajaucot apgriezto attiecību. Risinājuma pieraksts izlasās konsekventi tikai tad, ja vienreiz izvēlēts virziens un tas tiek ievērots līdz galam.

---

## 9. UncheckedConsistencyOfFoundValues

**(1)** No 7.klases.  
**(2) Atrasto vērtību nepārbaudīšana sākotnējā uzdevumā (konteksta saderības trūkums)**
**(3) Failure to verify found values against the original problem's constraints**

**(4) Apraksts.** Skolēns atrisina vienādojumu vai sistēmu, iegūst kandidāta vērtības, bet neveic pārbaudi, vai tās atbilst:
- sākotnējam vienādojumam (uzdevums pieprasa tieši to, nevis tā ekvivalentu pārveidojumu),
- uzdevuma kontekstam (piem., teksta uzdevumā cilvēku skaits jābūt nenegatīvs vesels, ātrums — pozitīvs, vecums — pozitīvs, summa naudā — nenegatīva),
- definīcijas apgabalam (piem., $x \neq 0$ zem dalītāja, $x \geq 0$ zem kvadrātsaknes).

Pierakstā tas izpaužas kā tas, ka skolēns saraksta visas kandidātes un nepiebilst, kura no tām pieņemama. Vai arī raksta atbildi kā kandidātu skaitu, neaizvākājot nederīgos.

**(5) Piemēri.**
- `LV.NOL.2021.10.1` (Marutas un Elīnas darba uzdevums): atrisinot $5x^{2} − 11x − 12 = 0$ iegūst $x = 3$ un $x = −0.8$. Vērtība $x = −0.8$ neder, jo $x$ apzīmē stundu skaitu (jābūt pozitīvam). Pareizā atbildē tieši to ir vērts piezīmēt — “neder”.
- Vienādojumā $\sqrt{x + 4} = x − 2$ skolēns kāpinot kvadrātā un atrisinot atrod $x = 0$ un $x = 5$, raksta abus kā atbildi. 
Bet $x = 0$ neder, jo $\sqrt{4} = 2 \neq −2$ (sakne nevar būt negatīva).
- Teksta uzdevumā par viesu skaitu, ar kvadrātvienādojumu atrasti kandidāti $n = 37$ un $n = −38$. Atbildē tikai $n = 37$ ir saturīgi nozīmīga; negatīvā kandidāta klātbūtne jāpiemin un jāatmet kā “neder”.

---

## 10. UnjustifiedCancellationOrCombination

**(1)** No 7.klases.  
**(2) Nepamatota daļu vai darbību “vienkāršošana” (analoģija ar saskaitīšanu, atklājot iekavas u.tml.)**
**(3) Unjustified cancellation or distribution (false algebra by analogy)**

**(4) Apraksts.** Skolēns veic “vienkāršojumu”, kas vizuāli izskatās kā darbību īpašības lietojums, bet patiesībā nav korekts. Tipiskākie piemēri:
- $(a + b)^{2} = a^{2} + b^{2}$ (aizmirstot vidējo locekli $2ab$);
- $\sqrt{a + b} = \sqrt{a} + \sqrt{b}$ (nepareizi “sadala” sakni summā);
- $1/(a + b) = 1/a + 1/b$ (analoģijas no reizināšanas);
- $(a + b)/c = a + b/c$ (aizmirsts dalīt arī $a$);
- $(a \cdot b)/(c \cdot b) = a/c$ veikts pat tad, ja $b = 0$.

Bieži tas notiek, ja skolēns pārveidojumu “automātiski” pārceļ no analoģiska konteksta, kurā tas der.

**(5) Piemēri.**
- `LV.AMO.2023.10.2`-stila pierādījumā $9x^{2} + 5y^{2} − 8xy − 4x + 2 > 0$ skolēns vēlas pārveidot $9x^{2} − 8xy = (3x − \ldots)^{2}$ un raksta $(3x − 4y)^{2}$, atverot par $9x^{2} − 24xy + 16y^{2}$ — bet patiesībā vajadzēja iegūt $9x^{2} − 8xy + ...$, kas atbilst $(3x − 4y/3)^{2}$, ko grūti panākt. Tipiskais nepareizais solis: aizmirsts pārbaudīt, vai pilnais kvadrāts atver tieši to, ko gribēja.
- Risinot $\sqrt{x^{2} + 9} = x + 3$, skolēns raksta 
$\sqrt{x^{2} + 9} = \sqrt{x^{2}} + \sqrt{9} = x + 3$ 
un secina, ka tas der visiem $x \geq 0$. Patiesībā 
$\sqrt{x^{2} + 9} \neq \sqrt{x^{2}} + \sqrt{9}$ — 
tā nav patiesa identitāte (vienkārši pārbaudāms ar 
$x = 4$: $\sqrt{25} = 5$, bet $4 + 3 = 7$).
- Pārveidojot $(a + b)/(a + c)$, skolēns “saīsina” $a$ un raksta 
$b/c$. Tas ir aplami, jo skaitītāja un saucēja $a$ nav reizinātāji, bet saskaitāmie.

---

## 11. CircularReasoningOrAssumingTheConclusion

**(1)** No 7.klases.  
**(2) Apļa pierādījums (pieņem to, kas jāpierāda) jeb secināšana no pierādāmā**
**(3) Circular reasoning / begging the question**

**(4) Apraksts.** Skolēns pierādīšanas gaitā kā starpsoli izmanto pašu pierādāmo apgalvojumu — vai nu tieši, vai netieši (piem., izmanto kādu sekvenci, kas patiesa tikai tad, ja pierādāmais ir patiess). Tipiskākais variants: skolēns sāk ar pierādāmo nevienādību, veic ekvivalentus pārveidojumus, nonāk pie acīmredzami patiesa apgalvojuma (piem., $0 \leq 1$) un pasludina, ka pierādījums ir gatavs. Patiesībā šis pieraksts ir “otrādi” — no pierādāmā secina patieso, nevis no patiesā secina pierādāmo. Korekti būtu vai nu izpildīt to pretējā secībā (no patiesā uz pierādāmo), vai eksplicīti norādīt, ka visi soļi ir ekvivalenti ($\Leftrightarrow$), un tad ķēde der abos virzienos.

**(5) Piemēri.**
- Pierādīšanā, ka $(a + b)^{2} \geq 4ab$ reāliem $a, b$, skolēns raksta: “$(a + b)^{2} \geq 4ab$ ⟹ $a^{2} + 2ab + b^{2} \geq 4ab$ ⟹ $a^{2} − 2ab + b^{2} \geq 0$ ⟹ $(a − b)^{2} \geq 0$, kas ir patiesi.” Pieraksts pretējā virzienā — no pierādāmā uz patieso. Korekti būtu sākt ar $(a − b)^{2} \geq 0$ un secināt augšup, vai aizvietot $⟹$ ar $⟺$ un pamatot, ka katrs solis ir ekvivalents pārveidojums.
- Pierādīšanā, ka $\sqrt{2}$ ir iracionāls, skolēns raksta: 
“Pieņemsim, ka $\sqrt{2} = p/q$ ($p, q$ veseli, savstarpēji pirmskaitļi). Tad $p^{2} = 2q^{2}$, tātad $p$ ir pāra, tāpēc $p = 2k$. Tad 
$4k^{2} = 2q^{2}$, $q^{2} = 2k^{2}$, tātad $q$ ir pāra. Bet tad gan $p$, gan $q$ dalās ar 2, kas ir pretrunā ar to, ka tie savstarpēji pirmskaitļi.” Šis ir korekts. Bet kļūdains variants: “Pieņemsim, ka $\sqrt{2} = p/q$. Tad $\sqrt{2}$ ir racionāls. Bet tas ir pretrunā ar to, ka $\sqrt{2}$ ir iracionāls.” — šeit izsmelts secinājums pieņem pašu apgalvojumu.
- Aprēķinot izteiksmes $a + 1/a$ (zinot, ka $a + 1/a = 3$) vērtību kvadrātā: skolēns raksta $(a + 1/a)^{2} = a^{2} + 2 + 1/a^{2} = 9$, tātad $a^{2} + 1/a^{2} = 7$. *Tas ir korekti.* Bet kļūdains variants: “Mēs zinām, ka $a^{2} + 1/a^{2} = 7$, tāpēc $(a + 1/a)^{2} = 9$, tāpēc $a + 1/a = 3$.” — šis pieņem to, kas jāpierāda (sākotnējais dotais nosacījums) un to “atvasina”.


