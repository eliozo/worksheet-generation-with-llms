# Algebras pamatošanas (loģisko spriedumu) metodes 5.–9. klases olimpiādēs

Avoti:

* Latvijas pamatizglītības matemātikas programma (5.–9. klase), 
* Latvijas olimpiāžu uzdevumu materiāli (LV.NOL, LV.AMO), 
* JBMO, BMO, MEMO, AMC 8/10,
* Krievijas, Polijas, Ungārijas nacionālās olimpiādes, USA MATHCOUNTS,
* Tournament of Towns.

Saraksts sākas ar vienkāršākajām un agrāk apgūstamajām (5.–6.kl.) uz sarežģītākajām (8.–9.kl.). Katrai metodei norādīts: 

1. No kuras klases sākts izmantot.
2. Nosaukums latviski, 
3. Nosaukums angliski, 
4. Īss apraksts
5. Daži piemēri no Latvijas olimpiādēm

Daži novērojumi par algebras metodēm:

* Metodes bieži kombinējas. Piemēram, lielākā daļa nevienādību 
  pierādījumu apvieno **EquivalentTransformations** (#3) + 
  **CompleteTheSquare** (#4) + **UseStandardIdentities** (#5).
* Teksta uzdevumi praktiski vienmēr sākas ar **IntroduceVariables** (#1) 
  un bieži turpinās ar **ExpressOneUnknownThroughAnother** (#2) 
  vai **SystemOfEquations** (#13).
* Optimizācijas uzdevumiem (*atrast lielāko/mazāko*) 
  raksturīga shēma: parāda **piemēru** ar attiecīgo vērtību, 
  tad **NumericalEstimation** (#15) vai **ProofByContradiction** (#20), 
  pamatojot, ka atrasto vērtību nevar uzlabot.

---

## 1. IntroduceVariablesAndFormEquation

**(1)** No 5.klases ar ievietojamiem skaitļiem.
No 7.klases ar burtiem.  
**(2)** Mainīgo ieviešana un vienādojuma sastādīšana.  
**(3)** Introducing variables, equations in a word problem.  
**(4) Apraksts.** Teksta uzdevumā nezināmos 
apzīmē ar burtiem ($x$, $y$, u.c.), 
pārraksta uzdevuma nosacījumus kā vienādības starp 
izteiksmēm. Iegūto vienādojumu vai sistēmu atrisina, 
un atbildi atkal interpretē uzdevuma kontekstā. 
Jāizvēlas, kurus lielumus pieņemt par mainīgo - tieši meklējamo 
mainīgo vai to, kurš ļauj iespējami vienkārši izteikt pārējos.  
**(5) Piemēri.**  
- `LV.NOL.2021.10.1`: Marutas un Elīnas darba uzdevumā ar $x$ apzīmē Marutai vajadzīgās stundas; Elīnai nepieciešams $x+2$; nosacījumu “strādājot kopā, pabeidza darbu” pārraksta kā $1.2/x + 3/(x+2) = 1$, no kurienes nāk kvadrātvienādojums.
- `LV.AMO.2023.5.5` (ekvivalents, no AMO 2023): zaļo bruņinieku skaits $x$, sarkano $10−x$; no izteikumiem seko $x = 10 − x$, tātad $x = 5$.
- `LV.NOL.2025.8.1`: piramīdas šūnas vērtību apzīmē ar $x$ un izsaka pārējos lielumus; iegūst $11 − x = 3x − 20 + 7$, no kā $x = 6$.

---

## 2. ExpressOneUnknownThroughAnother

**(1)** No 5.klases.  
**(2)** Viena nezināmā izteikšana caur citu.  
**(3)** Expressing one unknown in terms of another.  
**(4) Apraksts.** Ja uzdevumā ir vairāki nezināmie, bieži ērti 
vienu izteikt caur otru un samazināt mainīgo skaitu. 
Šo metodi izmanto gan vienādojumu sistēmās, gan 
optimizācijas uzdevumos (atrast lielāko/mazāko vērtību), 
gan teksta uzdevumos, kur ir vairāki lielumi (skaits, 
masa, ātrums, naudas summa). Tipiska shēma: dots 
$a + b = S$; apzīmējam $b = S − a$ un visu pārējo izsakām 
caur $a$.  
**(5) Piemēri.**  
- `LV.AMO.2014/2015.9`: no visiem skaitļu pāriem, kuru starpība ir 2015, atrast tos divus, kuru reizinājums vismazākais — vienu skaitli apzīmē ar $x$, otru ar $x − 2015$ (vai $x + 2015$), un pēta funkciju $f(x) = x(x − 2015)$.
- `LV.NOL.2022.8.4`: piecu pēc kārtas esošu skaitļu summa — apzīmē tos ar $n−2, n−1, n, n+1, n+2$, summa ir $5n$; izsakot caur vidējo, citi izteikumi vienkāršojas.
- `LV.AMO.2022B.6.4`: svari līdzsvarā — piecstūra masa izteikta caur aplīšiem, bultiņa caur aplīšiem; tad sākotnējais jautājums kļūst par parastu lineāru aprēķinu.

---

## 3. EquivalentTransformationsOfEquationsAndInequalities

**(1)** No 5.klases.  
**(2) Ekvivalenti pārveidojumi vienādojumiem un nevienādībām**
**(3) Equivalent transformations of equations and inequalities**

**(4) Apraksts.** Vienādojumu vai nevienādību soli pa solim pārveido par ekvivalentu (ar to pašu atrisinājumu kopu), izmantojot atļautās darbības: pieskaitīt/atņemt vienu un to pašu izteiksmi abām pusēm, reizināt/dalīt ar nenulles skaitli (uzmanīgi ar zīmi nevienādībās!), atvērt iekavas, pārvietot saskaitāmos uz otru pusi. Mērķis — iegūt formu, kurā nezināmais ir atsevišķi vai kuras patiesumu var tieši pārbaudīt. Pierādījuma uzdevumos to dažreiz formulē tā: lai pierādītu $A \geq B$, parāda ekvivalenci ar $A − B \geq 0$ un pēc tam patieso pēdējo nevienādību.

**(5) Piemēri.**
- `LV.NOL.2023.11.1`: pierādīt $x^{2} + y^{2} + 1/2 \geq x + y$ — 
abas puses reizina ar 4, pārvieto locekļus, iegūst 
$(2x−1)^{2} + (2y−1)^{2} \geq 0$, kas ir patiesi.
- `LV.AMO.2023.10.2`: pierādīt 
$9x^{2} + 5y^{2} − 8xy − 4x + 2 > 0$ — ar ekvivalentiem 
pārveidojumiem nonāk pie $(2x−2y)^{2} + y^{2} + (2x−1)^{2} + x^{2} + 1 > 0$.
- `LV.NOL.2024.12.2`: dotā vienādība $(x+y)/(x−y) + (x−y)/(x+y) = 7$ 
ar ekvivalentiem pārveidojumiem (reizinot ar saucēju, savelkot līdzīgos) nonāk pie $y^{2} = (5/9) x^{2}$.

---

## 4. CompleteTheSquareForNonNegativity

**(1)** No 9.klases.  
**(2) Pilnā kvadrāta atdalīšana nenegatīvitātes pierādīšanai**
**(3) Completing the square to prove non-negativity**

**(4) Apraksts.** Algebriskas izteiksmes nenegatīvitāti vai pozitivitāti pierāda, pārveidojot to par viena vai vairāku kvadrātu summu (varbūt plus pozitīva konstante). Pamatojas uz to, ka skaitļa kvadrāts vienmēr ir nenegatīvs ($t^{2} \geq 0$) un divu nenegatīvu skaitļu summa ir nenegatīva. Saistīta tehnika: ja meklē izteiksmes mazāko vērtību, pārveido to par $(…)^{2} + C$, kur $C$ ir konstante, — tad mazākā vērtība ir $C$. Tā pati ideja darbojas pierādījumiem, ka kāds izteiksmes vērtējums vienmēr ir spēkā.

**(5) Piemēri.**
- `LV.NOL.2023.12.1`: atrast mazāko $a$, lai visiem reāliem $x, y, z$ būtu $x^{2} + y^{2} + z^{2} + a \geq x + 2y + 3z$ — pilnā kvadrāta atdalīšana noved pie atbildes $a = 7/2$.
- `LV.AMO.2023.12.2`: atrast $2x^{2} − 8xy + 4x + 9y^{2} − 14y + 9$ mazāko vērtību — pārveido par $2(x − 2y + 1)^{2} + (y − 3)^{2} − 2$, tātad mazākā vērtība ir $−2$.
- `LV.AMO.2023.11.2`: pierādīt $a^{2}c + ac^{2} − 6abc + 3b^{2}c + ab^{2} \geq 0$ ($a, b, c > 0$) — pārveido par $c(a − 2b)^{2} + a(c − b)^{2} \geq 0$.

---

## 5. UseStandardIdentities

**(1)** No 7.klases.  
**(2) Saīsinātās reizināšanas formulu (standartidentitāšu) izmantošana**
**(3) Use of standard algebraic identities**

**(4) Apraksts.** Mērķtiecīgi izmanto pamatformulu kopumu: 
$(a \pm b)^{2} = a^{2} \pm 2ab + b^{2}$, 
$a^{2} − b^{2} = (a−b)(a+b)$, 
$(a \pm b)³ = a^{3} \pm 3a^{2}b + 3ab^{2} \pm b^{3}$, 
$a^{3} \pm b^{3} = (a \pm b)(a^{2} \mp ab + b^{2})$, 
$a^{2} + b^{2} + c^{2} + 2(ab+bc+ca) = (a+b+c)^{2}$. 
Pamato vai nu, atverot iekavas pretējā virzienā 
(no kvadrāta uz polinomu), vai sadalot reizinātājos, 
lai parādītu dalāmību, salīdzinātu izteiksmes vai 
vienkāršotu sarežģītu izteiksmi. Bieži apvienojas ar 
pilnā kvadrāta atdalīšanu (metode #4).

**(5) Piemēri.**
- `LV.NOL.2017/2018.8` (no GRAMATAS): zinot $a + 1/a = 3$, aprēķina $a^{2} + 1/a^{2} + 2$ — pārveido $(a + 1/a)^{2} = a^{2} + 2 + 1/a^{2}$, tālāk $a⁴ + 1/a⁴$ ar pilnā kvadrāta paņēmienu.
- `LV.NOL.2021.9.4`: ja $p + 1 = n^{4}$, tad 
$p = n^{4} − 1 = (n−1)(n+1)(n^{2}+1)$, kas pie 
$n > 1$ ir salikts skaitlis; iegūst, ka $k = 4$ der.
- `LV.AMO.2022B.11.2`: $x^{2} + x + p = 0$ saknēm 
$x_1 + x_2 = −1$, $x₁x₂ = p$; sakņu kvadrātu summu izsaka kā 
$(x_1+x_2)^{2} − 2 x_1x_2 = 1 − 2p$ un atrisina 
vienādojumu attiecībā pret $p$.

---

## 6. VietasFormulas

**(1)** No 9.klases.  
**(2) Vjeta formulas kvadrātvienādojumam**
**(3) Vieta's formulas for a quadratic equation**

**(4) Apraksts.** Kvadrātvienādojumam $ax^{2} + bx + c = 0$ 
ar saknēm $x₁, x₂$ izpildās $x_1 + x_2 = −b/a$ un 
$x_1 \cdot x_2 = c/a$. Šo izmanto, lai aprēķinātu 
simetriskas izteiksmes no saknēm ($x_1^{2} + x_2^{2}$, 
$x_1^{3} + x_2^{3}$, $1/x_1 + 1/x_2$ utt.), 
neatrisinot pašu vienādojumu, kā arī otrādi — uzdevumos par
kvadrātvienādojuma parametriem, kur prasīts kaut kas par saknēm. 
Pamato kā tiešas sekas no $ax^{2} + bx + c = a(x − x_1)(x − x_2)$.

**(5) Piemēri.**
- `LV.AMO.2022B.11.2`: $x^{2} + x + p$, sakņu kvadrātu summa = 16; ar Vjeta $x_1^{2} + x_2_^{2} = 1 − 2p = 16$, tātad $p = −7.5$.
- `LV.AMO.2022B.12.2`: tas pats vienādojums, sakņu kubu summa ir 
$−16$; izsaka 
$x_1^{3} + x_2^{3} = (x_1+x_2)(x_1^{2} − x_1x_2 + x_2^{2}) = 3p − 1 = −16$, no kā $p = −5$.
- `LV.NOL.2021.9` (par parabolu, kuras visi koeficienti pozitīvi): Vjeta dēļ $x_1 + x_2 = −b/a < 0$, tātad nevar būt divas pozitīvas saknes — risinājuma viena versija.

---

## 7. FactorAndUseZeroProductRule

**(1)** No 7.klases.  
**(2) Sadalīšana reizinātājos un nulles reizinājuma īpašības izmantošana**
**(3) Factoring and using the zero-product property**

**(4) Apraksts.** Polinomu vai izteiksmi sadala reizinājumā 
($P(x) = (x − a) \cdot Q(x)$ u.tml.), izmantojot kopīgo reizinātāju iznešanu, grupēšanu, saīsinātās reizināšanas formulas vai polinomu dalīšanu (vecākajās klasēs). Vienādojumam $A \cdot B = 0$ izmanto: vai nu $A = 0$, vai $B = 0$ — tas ir, sadala uzdevumu divos gadījumos. Tā pati metode dod arī dalāmības secinājumus skaitļu teorijā un ļauj redzēt, kāpēc kāda izteiksme nevar būt pirmskaitlis.

**(5) Piemēri.**
- `LV.NOL.2022.12.2`: $4x^4 − 11x^{2} + 9x − 2 = 0$ — 
uzminot sakni $x = 1$, sadala par 
$(x − 1)(4x³ + 4x^{2} − 7x + 2)$, 
tālāk vēl par $(x + 2)(2x − 1)^{2}$.
- `LV.NOL.2022.9.1`: pārveido $2x^{2} + (2m+3)x + 3m$ 
par $(m + x)(2x + 3)$; saknes ir $−m$ un $−3/2$, 
no tā secina, kādam jābūt $m$, lai būtu vesela sakne.
- `LV.NOL.2014/2015.8`: $3999991 = a^{2} − b^{2}$ 
ar atbilstošu izvēli $a, b$, pielieto formulu 
$a^{2} − b^{2} = (a−b)(a+b)$, lai parādītu, 
ka skaitlis nav pirmskaitlis.

---

## 8. SubstitutionForSimplification

**(1)** No 9.klases.  
**(2) Ievietošana / substitūcija izteiksmes vienkāršošanai**
**(3) Substitution to simplify an expression**

**(4) Apraksts.** Sarežģītu izteiksmi vai vienādojumu 
vienkāršo, ieviešot jaunu mainīgo, kas apzīmē atkārtojošos 
bloku. Piemēram, $t = x^{2}$, lai pārvērstu bikvadrātu 
par kvadrātvienādojumu; vai $s = x + y$, $p = xy$, 
lai simetriskā uzdevumā samazinātu mainīgo skaitu. 
Iegūto vienādojumu atrisina parastā veidā un beigās 
atgriežas pie sākotnējiem mainīgajiem (ar pārbaudi, 
vai jaunajam mainīgajam pieļaujamās vērtības 
tiek ievērotas — piem., $t = x^{2} \geq 0$).

**(5) Piemēri.**
- `LV.NOL.2017/2018.8` (no GRAMATAS): aprēķinot $a^{4} + 1/a^{4}$, 
ievieš $u = a^{2} + 1/a^{2}$ un izsaka $a^{4} + 1/a^{4} = u^{2} − 2$.
- `LV.NOL.2017/2018.9`: $t = x^{2}$ pārveido bikvadrātvienādojumu par kvadrātvienādojumu attiecībā pret $t$.
- `LV.NOL.2024.12.2`: ievieš substitūciju $y^{2} = (5/9) x^{2}$, ko atrod no dotās vienādības, un to ievieto pierādāmajā nevienādībā.

---

## 9. ProvingByEquivalenceChain

**(1)** No 9.klases.  
**(2) Pierādīšana ar ekvivalentu nevienādību ķēdi**
**(3) Proving via a chain of equivalent inequalities**

**(4) Apraksts.** Lai pierādītu nevienādību $A \geq B$, izveido virkni ekvivalentu pārveidojumu $A \geq B ⇔ A₁ \geq B₁ ⇔ … ⇔ Aₙ \geq Bₙ$, kur pēdējā nevienādība ir acīmredzami patiesa (piemēram, kvadrāts ir nenegatīvs, vai modulis ir nenegatīvs). Tā kā visi pārejas soļi ir ekvivalenti, no pēdējās patiesības seko sākotnējās. Šo metodi bieži kombinē ar metodi #4 (pilnā kvadrāta atdalīšana). Svarīgi atcerēties, ka, reizinot ar negatīvu skaitli, nevienādības zīme mainās — tas var sabojāt ekvivalenci.

**(5) Piemēri.**
- `LV.NOL.2023.11.1`: ekvivalentu pārveidojumu ķēde $x^{2} + y^{2} + 1/2 \geq x + y ⇔ 4x^{2} − 4x + 4y^{2} − 4y + 2 \geq 0 ⇔ (2x−1)^{2} + (2y−1)^{2} \geq 0$.
- `LV.AMO.2023.10.2`: nevienādību $9x^{2} + 5y^{2} − 8xy − 4x + 2 > 0$ ar ekvivalentu pārveidojumu ķēdi pārveido par četru kvadrātu plus 1 summu.
- `LV.AMO.2022A.7.1`: kvalitatīvi — Vilnis 1 minūtē atbild uz 8, Raimonds 2 minūtēs uz 15; secīgi un ekvivalenti pārveido, kamēr nonāk pie atbildes $64$ minūtes.

---

## 10. CaseAnalysisBySignOrInterval

**(1)** No 5.klases.  
**(2) Gadījumu šķirošana pēc zīmes vai intervāla**
**(3) Case analysis by sign or interval**

**(4) Apraksts.** Ja izteiksmes vērtība vai algebriskās attiecības patiesums ir atkarīgs no nezināmā zīmes vai novietojuma uz skaitļu taisnes (piemēram, $2x$ un $3x$ salīdzināšanā svarīgi, vai $x > 0$, $x = 0$ vai $x < 0$; izteiksmē $|x − a|$ — vai $x \geq a$ vai $x < a$), uzdevumu sadala vairākos gadījumos un katrā risina atsevišķi. Pēc visu gadījumu izskatīšanas atbildes apvieno. Šī metode parādās arī absolūtās vērtības, parametra un teksta uzdevumos, kur ir vairākas iespējamas konfigurācijas.

**(5) Piemēri.**
- `LV.TVC.2005/2006.2.kārta` (no GRAMATAS): salīdzināt $2a$ un $4a$ — jāizšķir trīs gadījumi $a > 0$, $a = 0$, $a < 0$.
- `LV.NOL.2022.8.3`: pierādīt $3 \cdot AC > AB$ platleņķa vienādsānu trijstūrī, kuram $\sphericalangle ABC = 20^{\circ}$ — 
divi gadījumi ($AB = AC$ un $BC = AC$), katrs atsevišķi.
- `LV.NOL.2022.9.1`: $2x^{2} + (2m+3)x + 3m = 0$ — atsevišķi jāizskata gadījums, kad $m$ vesels skaitlis un kad nav.

---

## 11. ParameterizedInvariantValue

**(1)** No 7.klases.  
**(2) Visu parametru grupai kopīga punkta/vērtības atrašana**
**(3) Finding a value (or point) common to a whole parameter family**

**(4) Apraksts.** Funkciju saimei $y = f(x; a, b, \ldots)$, 
kur parametrus saista kāda lineāra sakarība 
(piem., $a + 18b = 2021$), atrod tādas $x$ vērtības, 
kuras likvidē atkarību no parametriem. Praktiski — 
pārkārto formulu tā, lai parādītos sakarības labā 
puse kā kopīgs reizinātājs. Tāpēc pie šādām $x$ vērtībām 
funkciju saimei ir vienāda $y$ vērtība, t.i., visi 
grafiki iet caur šiem punktiem.

**(5) Piemēri.**
- `LV.NOL.2021.10.2`: funkciju saimei 
$y = ax^{2} + 2x + 2b$, kur $a + 18b = 2021$, 
parādās, ka pie $x = ±1/3$ izteiksme satur 
$(1/9)(a + 18b)$, tāpēc $y$ ir noteikts.
- `LV.NOL.2011/2012.9`: funkciju saimei 
$y = ax^{2} − 2x + b$, kur $a + b = 2012$, atrod kopīgos punktus, izmantojot to, ka $x = 1$ dod $a + b$.
- `LV.NOL.2020/2021.8`: lineāras funkcijas $y = bx − 71 + m$, 
kur $b + 2m = 2021$, — atrod $x$, ar kuru izteiksmes 
vērtība atkarīga tikai no $b + 2m$.

---

## 12. CountTheSameQuantityInTwoWays

**(1)** No 5.klases.  
**(2) Tā paša lieluma saskaitīšana divos dažādos veidos un pielīdzināšana**
**(3) Counting (or summing) the same quantity in two different ways and equating**

**(4) Apraksts.** Lielumu (summu, daudzumu, skaitu, laukumu) izsaka divos atšķirīgos veidos un saskaņā ar to, ka rezultāts ir viens un tas pats, izveido vienādību, no kuras secina nezināmo. Algebrā tipiskākie piemēri: izsaka kopējo darbu kā “katra darītāja izdarītā summa” un kā “viss darbs”; izsaka tabulas šūnu summu pa rindām un pa kolonnām; izsaka divu vienādību saskaitīšanu, lai eliminētu mainīgo. (Šo metodi plaši izmanto arī kombinatorikā — “dubultsaskaitīšana”.)

**(5) Piemēri.**
- `LV.NOL.2022.10.5`: izteiksmē $\pm 1 \pm  2 \pm  \ldots \pm 120$ apzīmē $P$ (summa ar $+$) un $M$ (moduļu summa ar $−$); 
$P + M = 1+2+ \ldots +120 = 7260$ un $P − M = 2022$, 
no šīm divām vienādībām atrod $P$ un $M$.
- `LV.NOL.2021.10.1` (Marutas un Elīnas): kopējais darbs ir 
1 (viss darbs) un vienlaikus $(1.2/x) + (3/(x+2))$ 
(katras meitenes daļas summa); pielīdzina.
- `LV.NOL.2025.7.4` (lielā mērā šīs metodes ilustrācija): 
otrklasnieku roku skaitu saskaita divējādi — gan kā "katra bērna otrklasnieku roku summa", gan kā divkāršots otrklasnieku skaits.

---

## 13. SystemOfEquationsAdditionOrSubstitution

**(1)** No 7.klases.  
**(2) Vienādojumu sistēmas risināšana ar saskaitīšanas vai ievietošanas metodi**
**(3) Solving systems by elimination or substitution**

**(4) Apraksts.** Divu (vai vairāku) vienādojumu sistēmu ar diviem (vairākiem) nezināmajiem atrisina, vai nu reizinot vienādojumus ar piemērotiem skaitļiem un saskaitot, lai izslēgtu vienu nezināmo (saskaitīšanas/eliminācijas metode), vai izsakot vienu nezināmo no viena vienādojuma un ievietojot otrā (ievietošanas metode). Saskaitīšanas metode pamatojas uz to, ka, ja $A = B$ un $C = D$, tad $A + C = B + D$. Tā ir vispārējās metodes #12 elementārākā forma.

**(5) Piemēri.**
- `LV.NOL.2022.10.5`: sistēma ${ P − M = 2022; P + M = 7260 }$ — saskaitot iegūst $2P = 9282$, tātad $P = 4641$.
- `LV.AMO.2019.9.4` (no LV.AMO.2019): $A + B = x + 777777$, $A = x + 500290$, $B = x + 5998$ — ievietošanas paņēmiens ļauj atrast $x = 271489$.
- `LV.SOL.2015/2016.9` (no GRAMATAS): kvadrātvienādojuma $3x^{2} + 3ax + (x−1)b = 0$ saknēm ir 1 un 2 — ievietojot abas saknes, iegūst sistēmu pret $a, b$.

---

## 14. UseFunctionGraphForRootsAndComparisons

**(1)** No 9.klases.  
**(2) Funkcijas grafika izmantošana sakņu skaita vai izteiksmju salīdzināšanai**
**(3) Using a function graph to determine number of roots or compare expressions**

**(4) Apraksts.** Vienādojumu $f(x) = g(x)$ interpretē kā divu grafiku krustpunktu meklēšanu, nevienādību $f(x) \geq g(x)$ — kā vienas līnijas atrašanos otras līnijas augšpusē. Lineāras funkcijas, parabolas (kvadrātfunkcijas), apgriezti proporcionālas funkcijas grafiku īpašības (virsotne, krustpunkti ar asīm, augšanas/dilšanas intervāli) ļauj spriest par sakņu skaitu un izteiksmju zīmi, neaprēķinot precīzās vērtības. Vidējās klasēs to pārsvarā lieto kvalitatīvi.

**(5) Piemēri.**
- `LV.NOL.2018/2019.9` (no GRAMATAS): $y = (m^{2} − 3m)x + 4m − 4$ krusto $x$ asi punktā $x = 2$ — ievieto, iegūst vienādojumu, no tā nosaka $m$, un katrā gadījumā atsevišķi izvērtē, vai funkcija augoša vai dilstoša.
- `LV.NOL.2020/2021.9`: ar vienkāršiem ģeometriskiem un grafiska novietojuma argumentiem (parabolas virsotnes abscisa, krustpunktu zīmes, Vjeta formulas) noskaidro, vai dotie grafiki var būt funkciju $y = ax^{2} + bx + c$ un $y = bx^{2} + cx + a$ grafiki.
- `LV.AMO.2014/2015.9` (no GRAMATAS): no skaitļu, kuru starpība 2015, atrod tos, kam reizinājums mazākais — pēta funkciju $f(x) = x(x − 2015)$, parabola, kuras virsotne dod meklēto vērtību.

---

## 15. NumericalEstimation

**(1)** No 7.klases.  
**(2) Skaitliska novērtēšana (izteiksmes novērtēšana augšā/lejā)**
**(3) Numerical estimation / bounding an expression**

**(4) Apraksts.** Lai pierādītu, ka kāds piemērs ir optimāls (mazākais, lielākais), izteiksmi vai daudzumu novērtē no augšas vai no apakšas ar zināmu izteiksmi, kuras vērtību var precīzi aprēķināt. Pierādījumu parasti veido divos posmos: 1) parāda atbilstošu piemēru ar konkrēto vērtību; 2) parāda, ka labākas vērtības būt nevar (novērtējums + pretrunas vai monotonums). Algebriskos uzdevumos novērtēšanu bieži kombinē ar nevienādību saskaitīšanu vai izteiksmju salīdzināšanu.

**(5) Piemēri.**
- `LV.NOL.2022.10.5`: pierāda, ka $+$ zīmju skaits nevar būt vairāk par 95 — pieņem pretējo, novērtē $P$ no apakšas ($P \geq 1+2+…+96 = 4656$), kas ir pretrunā ar $P = 4641$.
- `LV.NOL.2021.9.5`: $120$ skaitļu pāru summu īpašība — pieņem pretējo ($a₂₂ + a₉₉ \leq 1000$), tad katrs no $a₁,…,a₂₂$ varētu būt pārī tikai ar kādu no $a₁₀₀,…,a₁₂₀$, tas ir, 22 skaitļiem tiek piedāvāti tikai 21 pāri — pretruna.
- `LV.AMO.2023.5.5` (jau pieminēts): pretrunas pamatojums caur novērtējumiem, ka nevar būt vairāk vai mazāk par 5 zaļiem bruņiniekiem.

---

## 16. UseTrivialInequalitiesAndAddThem

**(1)** No 9.klases.  
**(2) Tipisku nevienādību ($x^{2} \geq 0$, AM-GM) izmantošana un to saskaitīšana**
**(3) Use of trivial inequalities and adding them together**

**(4) Apraksts.** Pamato sarežģītu nevienādību, atvasinot to no vienkāršām, jau zināmām nevienādībām: $x^{2} \geq 0$ jebkuram reālam $x$; $(a − b)^{2} \geq 0$, tātad $a^{2} + b^{2} \geq 2ab$ (AM-GM divu skaitļu gadījumā); $|a + b| \leq |a| + |b|$ (trijstūra nevienādība). Vairākas patiesas nevienādības var saskaitīt (ja tām ir vienādas pieturzīmes “\geq” vai “\leq”) un iegūt jaunu patiesu nevienādību. Mēģina sākotnējo nevienādību sadalīt vairākās šādās komponentēs.

**(5) Piemēri.**
- `LV.AMO.2023.11.2`: $a^{2}c + ac^{2} − 6abc + 3b^{2}c + ab^{2} \geq 0$ — sadala par $c(a − 2b)^{2} + a(c − b)^{2}$, izmantojot, ka katrs kvadrāts un katrs no skaitļiem $a, c$ ir nenegatīvi/pozitīvi.
- `LV.AMO.2011/2012.8` (no GRAMATAS): pierāda, ka attālumu summa no trijstūra iekšēja punkta līdz virsotnēm ir lielāka par pusi no perimetra — uzrakstot trijstūra nevienādības trim sektoru trijstūriem un saskaitot tās.
- `LV.AMO.2022B.11.4`: $(x−y)^{2} + (y−z)^{2} + (z−x)^{2} \leq 2$, kas savukārt ekvivalents pierādāmajai nevienādībai par $x^{2} + y^{2} + z^{2} − xy − yz − xz \leq 1$, tālāk argumentē par vienīgajiem iespējamiem trijniekiem.

---

## 17. BruteForceCheckOverFiniteSet

**(1)** No 5.klases.  
**(2) Pilnā pārlase pār galīgu mainīgo vērtību kopu**
**(3) Brute-force enumeration over a finite set of values**

**(4) Apraksts.** Ja mainīgais var pieņemt tikai galīgi daudz vērtību (piem., decimāls cipars var būt no 0 līdz 9; nezināmajam ir maza pieļaujamā vērtību kopa; dalāmības nosacījums savieto vienu mainīgo ar lieliem soļiem), tad vienkārši pārlasa visas iespējas, pārbaudot katru. Algebrā šī metode parādās uzdevumos par “atrast visus dotā tipa vienādojumu naturālos atrisinājumus” vai “rēbusu risināšana”. Bieži pirms pārlases vēl tiek noteikts, ka noteiktas vērtības ir izslēgtas (ar dalāmības vai zīmes argumentiem), tādējādi samazinot pārlasāmo gadījumu skaitu.

**(5) Piemēri.**
- `LV.NOL.2025.10.1`: $100a + 10b + c = 5abc$ — vispirms izsecina, ka $c = 5$, tad pārlasa $2b + 1 \in \{5, 10, 15, \ldots \}$ 
un katrai iespējamai $b$ vērtībai pārbauda, vai $a$ 
ir derīgs cipars; vienīgā atbilde — 175.
- `LV.PCK.2011/2012.4.nod`: $a^{2}b + 12 = 2012$ jeb $a^{2}b = 2000$; pārlasa kvadrātus, ar kuriem dalās 2000.
- `LV.AMO.2019.5.4`: vienādojums $xzy < yaz < yax < zxa$ par 4 trīsciparu skaitļiem — pārlasa, kuri cipari iederas, ar argumentu, ka pirmais cipars nosaka skaitļa kārtu.

---

## 18. MonovariantOrSymmetryArgumentForExtremalCases

**(1)** No 9.klases.  
**(2) Simetrijas vai vienveidības (monovarianta) izmantošana, lai noteiktu ekstremālo gadījumu**
**(3) Symmetry or monovariant argument for extremal cases**

**(4) Apraksts.** Lai noteiktu izteiksmes lielāko vai mazāko vērtību (vai parādītu, kāds nosacījumu komplekts ir izpildāms), izmanto simetrijas vai vienveidības argumentu: ja izteiksme ir simetriska attiecībā pret $x$ un $y$, tad ekstrēma vērtība bieži tiek sasniegta pie $x = y$ (jāpārbauda atsevišķi); ja zināms, ka pie pārmaiņām kāda lieluma vērtība monotoni mainās, tad ekstrēms ir robežpunktā. Šī ir mīkstāka pieeja, kas papildina #14 un #15.

**(5) Piemēri.**
- `LV.AMO.2014/2015.9` (no GRAMATAS): no visiem pāriem ar starpību 2015 reizinājums minimizējas, kad pāra elementi novietoti simetriski attiecībā pret nulli ($x = −1007.5$, $x + 2015 = 1007.5$); to pamato, pētot parabolas virsotni.
- `LV.AMO.2023.12.3`: $S_{CEF} = (a^{2}+b^{2}−ab)/2 = ((a−b)^{2} + ab)/2 \geq ab/2 = S_{ABD}$. Simetrijas dēļ vienlīdzība iestājas, kad $a = b$ (kvadrāts).
- `LV.AMO.2022B.11.4`: $(x−y)^{2} + (y−z)^{2} + (z−x)^{2} \leq 2$ — simetrisks ierobežojums; iespējamie trijnieki simetriski sadalās trīs šablonu klasēs $(k,k,k)$, $(k,k,k+1)$, $(k,k+1,k+1)$.

---

## 19. ParityOrModularArgumentForEquations

**(1)** No 7.klases.  
**(2) Paritātes un atlikumu argumenti algebriskā vienādojumā**
**(3) Parity / modular arguments applied to an equation**

**(4) Apraksts.** Tieši algebriskos kontekstos (atšķirībā no skaitļu teorijas) paritātes un atlikumu argumenti parādās, kad apgalvojums ir par vienādību patiesumu/aplamību: aprēķina abu pušu paritāti (vai atlikumu pēc maza moduļa) un parāda neatbilstību, tāpēc vienādības būt nevar (vai noteikti atrisinājuma nav). Pamatā ir tas, ka pārveidojumi nemaina paritāti vai atlikumu, ja darbības ir veiktas pareizi. Šī ir robežmetode starp algebru un skaitļu teoriju — algebriskajā lietojumā galvenais ir vienādības struktūra, ne pats skaitļa pieraksts.

**(5) Piemēri.**
- `LV.NOL.2022.10.5`(a): $P − M = 2023$ nav iespējams, jo $P + M = 7260$ ir pāra skaitlis, tātad $P, M$ vienādas paritātes, tātad $P − M$ arī pāra; bet 2023 ir nepāra.
- `LV.NOL.2022.8.4`: pierāda, ka pieci secīgi veseli skaitļi summā dod $5n$; lai summa būtu 2022, vajadzētu $5n = 2022$, kas nav iespējams, jo 2022 nedalās ar 5.
- `LV.NOL.2024.11.5(A)`: ja $n = 2024$ kastes, tad ābolu kopskaits ir $1012(2a + 2023)$ (pāra) un kopējais auglu skaits arī, bet tas vienlaikus prasa būt $2k + 2023$ (nepāra struktūra) — pretruna.

---

## 20. ProofByContradictionInAlgebra

**(1)** No 9.klases. 
**(2) Pierādīšana no pretējā algebriskā uzdevumā**
**(3) Proof by contradiction in algebraic context**

**(4) Apraksts.** Lai pierādītu apgalvojumu $P$, pieņem pretējo ($P$ ir aplams) un nonāk pie pretrunas ar dotajiem nosacījumiem, ar algebrisku patiesību vai ar kādu pareizi atvasinātu agrāku rezultātu. Algebrā tas tipiski parādās uzdevumos par nevienādību pierādīšanu (pieņem, ka nevienādība ir pretēja, un meklē pretrunu), par vienādojumu naturālo/veselo atrisinājumu trūkumu un par optimuma pamatojumu (ka labākas vērtības nav). Pretrunu sasniedz, izmantojot tieši to ekvivalentu pārveidojumu (#3), pilnā kvadrāta (#4) vai novērtēšanas (#15) tehniku.

**(5) Piemēri.**
- `LV.NOL.2021.9.5`: pierādījums $a_{22}_ + a_{99} > 1000$ no pretējā: pieņem $a_{22} + a_{99} \leq 1000$ un parāda, ka 22 mazāko skaitļu pāra partneriem nepietiek ar pieejamo skaitļu skaitu.
- `LV.NOL.2022.10.5`(a): pieņemot pretējo (ka iespējams iegūt 2023), nonāk pie paritātes pretrunas.
- `LV.NOL.2025.11.2`: pieņem, ka $A$ dalās ar 216 = $2^{3} \cdot 3^{3}$; tad dažādu dalītāju skaita formula prasa 
$(k+1)(m+1)\cdot \ldots = 111 = 3 \cdot 37$, kur abi 
$k+1, m+1 \geq 4$ — bet $111$ šādā veidā sadalīt nevar; pretruna.


---

## 21. TelescopingSum

**(1)** No 9.klases.  
**(2) Teleskopiska summa**  
**(3) Telescoping sum**  
**(4) Apraksts.** Sarežģītu saskaitāmu summu vai reizinājumu pārveido formā, kurā katru locekli izsaka kā divu izteiksmju starpību (vai dalījumu) tā, ka secīgi locekļi atceļas — paliek tikai pirmais un pēdējais. Galvenās identitātes: $1/(k(k+1)) = 1/k − 1/(k+1)$; $k = (k+1)k/2 − k(k−1)/2$; vispārīgāk, ja $a_{k} = b_{k+1} − b_l$, tad $\sum a_k = b_{n+1} − b_1$. Reizinājumiem analoģiski: $(k+1)/k$-tipa faktorizācijās blakus locekļi savstarpēji saīsinās. Latvijas materiālos šī metode parādās tikai ļoti šauri (piem., reizinājums $(1+1/2)(1+1/3)…(1+1/70)$ no SOL 2019/2020), bet starptautiski tā ir kanoniska 7.–9.klases tehnika.

**(5) Piemēri (no starptautiskās olimpiāžu prakses).**
- *Klasisks JBMO/AMC stila uzdevums:* aprēķināt 
$1/(1 \cdot 2) + 1/(2 \cdot 3) + … + 1/(99 \cdot 100)$. 
Katru locekli pārraksta kā $1/k − 1/(k+1)$; 
pēc atcelšanas paliek $1 − 1/100 = 99/100$.
- *AMC 10 stilā:* Aprēķināt 
$(1 − 1/4)(1 − 1/9)(1 − 1/16)\cdots(1 − 1/n^{2})$. 
Katru reizinātāju pārraksta kā $((k−1)(k+1))/k^{2}$; 
reizinājumi ar teleskopisko summu saīsinās par $(n+1)/(2n)$.
- *MEMO/Krievija 8.–9.kl. stila:* dota virkne 
$a_k = k \cdot k!$; pierādīt, ka 
$a_1 + a_2 + \ldots + a_n = (n+1)! − 1$. 
Pamatojas uz $k \cdot k! = (k+1)! − k!$.

*Iespējams iekļaut Latvijas kanonā uzdevumam:* SOL 8.kl., 2019./2020. (reizinājuma $(1+1/2)(1+1/3)…(1+1/70)$ aprēķins) ir tieši šis paņēmiens, tikai pierakstīts citā formā.

---

## 22. WeightedAMGMOrTwoVariableAMGM

**(1)** No 9.klases.  
**(2)** Aritmētiski-ǵeometriskā vidējā nevienādība  
($(a+b)/2 \geq \sqrt{ab}$) un tās lietojumi  
**(3)** AM-GM inequality (two-variable version) and its applications  
**(4) Apraksts.** Diviem nenegatīviem reāliem skaitļiem $a, b$ 
izpildās $(a+b)/2 \geq \sqrt{ab}$, kas ekvivalents 
$a + b \geq 2\sqrt{ab}$, kā arī $a^{2} + b^{2} \geq 2ab$. 
Vienādība ir tad un tikai tad, ja $a = b$. Ekvivalences 
pamatošanai izmanto $(\sqrt{a} − \sqrt{b})^{2} \geq 0$, 
vai pat tikai $(a − b)^{2} \geq 0$. Šī nevienādība junioru 
olimpiādēs parādās kā instruments citu nevienādību pierādīšanā, ekstrēmu uzdevumos un optimizācijā ar fiksētu reizinājumu vai summu (piem., pierādīt, ka starp visiem taisnstūriem ar fiksētu perimetru lielākais laukums ir kvadrātam). Latvijas pamatskolas olimpiādēs to parasti 
nesauc vārdā; risinājumā parādās $(a−b)^{2} \geq 0$, nepiešķirot 
tam īpašu nosaukumu.  
**(5) Piemēri.**
- *JBMO 2018 stila uzdevums (8.–9.kl. līmenis):* pierādīt, ka pozitīviem $a, b, c$ izpildās $(a+b)(b+c)(c+a) \geq 8abc$. Pa pāriem $a + b \geq 2√(ab)$, $b + c \geq 2√(bc)$, $c + a \geq 2√(ca)$; sareizinot iegūst $8√(a^{2}b^{2}c^{2}) = 8abc$.
- *MATHCOUNTS / AMC 8 stila uzdevums:* atrast lielāko taisnstūra laukumu ar perimetru 40. Apzīmē malas $a, b$; $a + b = 20$. Pēc AM-GM $ab \leq ((a+b)/2)^{2} = 100$, vienlīdzība pie $a = b = 10$. Latvijas olimpiādēs šādu uzdevumu risina tikai caur kvadrātfunkcijas virsotni (sk. metodi #14).
- *BMO/Polijas 9.kl. stila:* pozitīviem $x, y, z$ ar $x + y + z = 3$ pierādīt $xy + yz + zx \leq 3$. Caur $(x+y+z)^{2} = x^{2}+y^{2}+z^{2} + 2(xy+yz+zx)$ un $x^{2} + y^{2} + z^{2} \geq xy + yz + zx$ (kas seko no trim AM-GM piemērošanas reizēm).

*Piezīme:* Latvijā šo metodi 5.–9.klasē apzināti neievada — to atstāj 10.–12.klases programmai. Starptautiski (it īpaši JBMO un Balkānu valstīs) šī ir absolūti standarta 8.–9.kl. tehnika, un Latvijas skolēniem, dodoties uz BalticWay vai JBMO, tā jāzina.

---

## 23. SOSAndSchurSquaresOnTheLine

**(1)** No 9.klases.  
**(2)** Pierādījumi ar $(a−b)^{2} + (b−c)^{2} + (c−a)^{2}$ tipa kvadrātu summu.
**(3)** SOS (sum of squares) method.

**(4) Apraksts.** Simetriskas nevienādības pierādīšanai ar 
trim mainīgajiem ($a, b, c$) izteiksmi pārveido formā 
$\lambda_1(a−b)^{2} + \lambda_2(b−c)^{2} + \lambda_3(c−a)^{2}$, 
kur $\lambda_i \geq 0$. Tādā gadījumā visa summa ir nenegatīva, 
jo katrs kvadrāts ir nenegatīvs. Šī ir metodes #4 
(pilnais kvadrāts) un metodes #16 (trivial inequalities) 
paplašinājums trim mainīgajiem, bet ar īpašu, 
atpazīstamu struktūru. Pamatā identitāte: 
$a^{2} + b^{2} + c^{2} − ab − bc − ca = \frac{1}{2}((a−b)^{2} + (b−c)^{2} + (c−a)^{2})$. Latvijas olimpiādēs šī tehnika parādās tikai dažos uzdevumos (LV.AMO.2022B.11.4 ir tuvākais piemērs), bet starptautiski JBMO/IMO Junior Shortlist tā ir standarta.  
**(5) Piemēri.**
- `LV.AMO.2022B.11.4` (jau pieminēts) — pierāda $(x−y)^{2} + (y−z)^{2} + (z−x)^{2} \leq 2$, no kā izriet sākotnējā nevienādība. Šeit tieši šī ir izmantotā tehnika.
- *JBMO 2017 stila uzdevums (8.–9.kl.):* reāliem $a, b, c$ pierādīt $a^{2} + b^{2} + c^{2} \geq ab + bc + ca$. Pierādījums viena rinda: $2(a^{2} + b^{2} + c^{2} − ab − bc − ca) = (a−b)^{2} + (b−c)^{2} + (c−a)^{2} \geq 0$.
- *IMO Junior Shortlist stila:* pierādīt, ka jebkura trijstūra malām $a, b, c$ izpildās $a^{2} + b^{2} + c^{2} < 2(ab + bc + ca)$. Pamatojas uz trijstūra nevienādību $a < b + c$ u.tml.; iznāk no $(b+c−a)(c+a−b)(a+b−c) > 0$, ko pamato ar SOS-tipa pārveidojumiem.  
*Piezīme:* Šī metode nav uzskatāma par jaunu (tā loģiski izriet no #4 un #16), bet starptautiski tā parādās tik bieži un ar tik atpazīstamu pierakstu, ka ir vērts to izcelt atsevišķi. Latvijas materiālos to varētu pievienot kā “3-mainīgo paplašinājumu” metodei #4.

---

## 24. FunctionalSubstitutionForRecurringExpression

**(1)** No 9.klases. 
**(2)** Funkcionāla substitūcija atkārtotai izteiksmei  
**(3)** Functional substitution for self-referring expressions
**(4) Apraksts.** Ja vienādojumā vai sistēmā nezināmais ir iekšā kādā saliktā izteiksmē (sakne, daļa, kvadrātsakne, kāpināšana), pielieto sākotnējo vienādojumu rekursīvi paša iekšā un iegūst vienkāršāku, ekvivalentu vienādojumu. Tipiska forma: $x = \sqrt{a + \sqrt{a + \sqrt{a + \ldots}}}$ → ar bezgalīgu rekursiju vienādojums kļūst 
$x = \sqrt{a + x}$, no kā $x^{2} = a + x$ un atrisina kā
kvadrātvienādojumu. Variants: $x = a + a/(a + a/(a + \ldots))$ 
utml. ar daļām. Šī metode prasa diezgan precīzu izpratni par 
konverģences nosacījumiem, tāpēc Latvijas pamatizglītības 
programmā tā nav iekļauta, taču junioru olimpiādēs (sevišķi krievu un austrumeiropas tradīcijā 8.–9.kl.) parādās diezgan regulāri.  
**(5) Piemēri.**
- *Krievija 8.kl. olimpiādes:* 
atrast $x = \sqrt{2 + \sqrt{2 + \sqrt{2 + \ldots}}}$ vērtību. 
Pielietojot rekursīvi, $x^{2} = 2 + x$, tātad $x^{2} − x − 2 = 0$, no kā $x = 2$ (otra sakne negatīva, neder).
- *Polija/Ungārija 9.kl. stila:* atrisināt $x + 1/(x + 1/(x + 1/x)) = 2$. Saliktās daļas saīsināšana ar substitūciju.
- `LV.NOL.2023.6.1`: vienādības $2 + 1/(x + 1/(y + 1/z)) = 37/13$ atrisināšana naturālos skaitļos — kaut arī uzdevumā skaidri jautāts vienkārši “atrod vienu piemēru”, *Piezīmes* daļā ir parādīts šis pats substitūcijas paņēmiens ($37/13 = 2 + 11/13$, tātad 
$1/(x + \ldots) = 11/13$, no kā $x + \ldots = 13/11 = 1 + 2/11$, 
un tā tālāk). Tas faktiski ir vienīgais piemērs Latvijas
materiālos, kur šī metode parādās — un pat tur tikai komentāra veidā.

*Piezīme:* Junioru olimpiāžu praksē šī metode ir piemērojama arī tā saucamajām nemainīgo punktu situācijām: ja $f(f(x)) = f(x)$, tad $f(x)$ ir $f$ nemainīgs punkts, ko atrod no $f(t) = t$. Latvijas materiālos šis loks parādās tikai netieši — caur periodisku virkņu metodi.

---

## 25. DetectPeriodInRecursiveSequence

**(1)** No 7.–8. klases.
**(2)** Periodisks raksturs rekurentā virknē ar galīgu stāvokļu kopu.
**(3)** Detecting a period in a recursive sequence.
**(4) Apraksts.** Ja virknē katrs nākamais loceklis viennozīmīgi noteikts ar iepriekšējo (vai
ar galīgu skaitu iepriekšējo locekļu vai citu galīgu stāvokli), un visi iespējamie stāvokļi pieder
galīgai kopai, tad virkne agrāk vai vēlāk sāk atkārtoties — izveidojas periods. Pēc periodicitātes
atklāšanas patvaļīgi tālu virknes locekli iegūst, atrodot tā indeksa atlikumu pa moduļa $T$
(perioda), kur $T$ ir perioda garums. Metode strādā gan ar skaitliskām virknēm, gan ar
stāvokļu virknēm (piem., šaha figūras pozīcijas, atlikumu virknes pa moduli). Atšķirībā no
parastās invariantu metodes, te svarīga ir tieši stāvokļu galīgā kopa un determinētība — bez
tiem periodicitāte nav garantēta.
**(5) Piemēri.** LV.AMO.2018.7.2 (virkne ar pirmo locekli $4$ un rekurenci $x \mapsto \tfrac{1}{1-x}$
— pārrēķinot, $4 \to -\tfrac{1}{3} \to \tfrac{3}{4} \to 4$, periods $3$; tādēļ $2018.$ loceklis ir
tas pats, kas $2018 \bmod 3 = 2$ pozīcijā, t.i., $-\tfrac{1}{3}$, un summa $2018$ locekļiem ir
$672 \cdot (4 - \tfrac{1}{3} + \tfrac{3}{4}) + 4 + (-\tfrac{1}{3})$); GRAMATA piemērs par virkni
$1, 2, 3, 5, 8, 3, 1, 4, 5, 9, \ldots$, kur katrs nākamais ir iepriekšējā kvadrāta ciparu summa —
ar galīgu stāvokļu kopu virkne kļūst periodiska; klasisks uzdevums par pakāpes $2^n$ pēdējo
ciparu (periods $4$: $2, 4, 8, 6, 2, 4, \ldots$).

---

## 26. SlopesOnCoordinatePlane

**(1)** No 8.–9. klases.
**(2)** Virziena koeficients koordinātu plaknē.
**(3)** Slopes (gradients) on the coordinate plane.
**(4) Apraksts.** Taisnei caur diviem dažādiem punktiem $A(x_1, y_1)$ un $B(x_2, y_2)$ virziena
koeficients ir $k_{AB} = \tfrac{y_2 - y_1}{x_2 - x_1}$ (ja $x_1 \neq x_2$). Divas taisnes ir paralēlas
tad un tikai tad, ja to virziena koeficienti ir vienādi; perpendikulāras tad un tikai tad, ja
koeficientu reizinājums ir $-1$. Metode ir centrāla koordinātu ģeometrijas uzdevumos ar
punktu kolinearitāti, taisņu paralēlismu, viduspunktu un nogriežņu krustpunktu īpašībām.
Bieži apvienota ar viduspunkta formulu $M = (\tfrac{x_1+x_2}{2}, \tfrac{y_1+y_2}{2})$ vai ar
nogriežņu sadalīšanu noteiktā attiecībā.
**(5) Piemēri.** LV.AMO.2010.9.2 (četri dažādi punkti uz parabolas $y = x^2$ — punktiem
$P_i = (a_i, a_i^2)$ uz parabolas hordas $PQ$ virziena koeficients ir $\tfrac{a^2 - b^2}{a - b}
= a + b$; ja $E$ būtu gan $AB$, gan $CD$ viduspunkts, tad $\tfrac{x_A + x_B}{2} = \tfrac{x_C + x_D}{2}$
un $\tfrac{y_A + y_B}{2} = \tfrac{y_C + y_D}{2}$, no kā secina $x_A + x_B = x_C + x_D$ un
$x_A^2 + x_B^2 = x_C^2 + x_D^2$ — pretruna ar punktu dažādību); LV.NOL.2022.10.1 (taisne caur
$C(10, 2)$ paralēli taisnei $AB$ ar $A(21, 1)$ un $B(20, 22)$ — autors iegūst $k_{AB} = -21$ no
divu punktu starpības un raksta meklēto taisni formā $y = -21x + b$); GRAMATA 5.3.4. uzdevumi
par lineārām funkcijām $y = ax + k$ un $y = bx + m$ (no grafiku slīpuma salīdzina koeficientus
$a$ un $b$).



---

## Citas metodes

Metodes, kuras neizmanto Latvijas pamatskolā, bet 
varētu būt starptautiskās junioru līmeņa olimpiādēs:

* Cauchy-Schwarz inequality
* Power mean inequality
* Bernoulli inequality
* Polynomial division
* Mathematical induction
* Newton's identities, systems with symmetry. 
