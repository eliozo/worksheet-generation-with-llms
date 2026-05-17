# Tipiskās skaitļu teorijas pamatojumu metodes 5.–9. klases olimpiāžu uzdevumos

Šis dokuments apkopo galvenās skaitļu teorijas pamatojuma metodes, kas parādās
Latvijas (LV.AMO, LV.NOL) un citu junioru līmeņa olimpiāžu uzdevumos 5.–9. klasei. 
Šajā vecuma posmā par “skaitļu teoriju” parasti uzskata aritmētiku par 
dalāmību, skaitļa pierakstu, ciparu summām, sadalīšanu reizinātājos 
un summās; vairākas no metodēm pārklājas ar algebru
un kombinatoriku. Mazākajās klasēs dominē tieša dalāmības pazīmju lietošana, 
skaitļa pieraksts šķiru summā un pilnā pārlase pa atlikumiem; 
8.–9. klasē parādās modulārā aritmētika, sadalīšana reizinātājos 
ar algebrisko identitāšu palīdzību, pierādījums no pretējā un dalītāju
skaita formulas. Tipiskā uzdevumā ir jāizmanto vairākas metodes 
vienlaikus — piemēram, skaitļa pieraksts šķiru summā tiek apvienots 
ar dalāmības pazīmi un gadījumu pārlasi.


## 1. DivisibilityRules

**(1)** No 5. klases.
**(2)** Dalāmības pazīmes (ar $2, 3, 4, 5, 8, 9, 10, 11$).
**(3)** Divisibility rules.
**(4) Apraksts.** Skaitlis dalās ar $2$ vai $5$, ja tā pēdējais cipars dalās; ar $4$ vai $25$ — ja
pēdējie divi cipari; ar $8$ — ja pēdējie trīs cipari; ar $3$ vai $9$ — ja ciparu summa dalās; ar
$11$ — ja pēdējais cipars summas ar pārmaiņus zīmi dalās ar $11$. Tās ir pirmās metodes,
ko apgūst piektklasnieks. Šīs pazīmes bieži kombinē, izmantojot to, ka dalāmība ar saliktu
skaitli izriet no dalāmības ar tā savstarpēji pirmskaitļa reizinātājiem (skat. nākamo metodi).
**(5) Piemēri.** LV.NOL.2011./12. 5. klase 3. uzd. ($7$-ciparu skaitlis no cipariem
$1,2,3,4,5,7,8$, kas dalās ar $7$ — autors izveido $1428357 = 1400000 + 28000 + 350 + 7$,
katra summas locekļa dalāmība ar $7$ acīmredzama); LV.SOL.2016./17. 5. klase 2. uzd. (skaitlis,
kura ciparu summa dalās ar $27$, bet pats nedalās — der $9981$, ciparu summa $27$, bet
$9981 = 369 \cdot 27 + 18$); LV.NOL.2025.5.kl. par sešciparu skaitļu pārlasi pēc dalāmības ar
$2, 5$ un $9$ pazīmēm.


## 2. CoprimeFactorsDivisibility

**(1)** No 6.–7. klases.
**(2)** Dalāmība ar savstarpēji pirmskaitļu reizinātāju.
**(3)** Divisibility by coprime factors.
**(4) Apraksts.** Ja $b$ un $c$ ir savstarpēji pirmskaitļi (lielākais kopīgais dalītājs $1$), tad
skaitlis $a$ dalās ar $bc$ tad un tikai tad, ja tas dalās gan ar $b$, gan ar $c$. Tas ļauj sarežģītu
dalāmību (piem., ar $90$) sadalīt vienkāršās pazīmēs (ar $9$ un ar $10$). Svarīgi atcerēties
nosacījumu par savstarpējo pirmskaitļiem: piemēram, no tā, ka $18$ dalās ar $2$ un ar $6$,
nevar secināt, ka tas dalās ar $12$. Šī metode ir loģisks pamatprincips daudzās zemāka līmeņa
uzdevumos par dalāmību ar saliktiem skaitļiem.
**(5) Piemēri.** LV.NOL.2011./12. 8. klase 1. uzd. (mazākais skaitlis no $123456789\ldots N$,
kas dalās ar $18 = 2 \cdot 9$); LV.AMO.2024.9.5 (Zanes telefona numurs dalās ar $15 = 3 \cdot 5$
— jāpārbauda dalāmība gan ar $3$, gan ar $5$); LV.NOL.2023.8.kl. uzdevums par dalāmību ar
$90$ (jāatdala dalāmība ar $9$ un dalāmība ar $10$).


## 3. PositionalNotation

**(1)** No 5. klases.
**(2)** Skaitļa pieraksts šķiru summā.
**(3)** Positional (place-value) notation.
**(4) Apraksts.** Skaitļa cipari $\overline{ab}$, $\overline{abc}$ utt. tiek izteikti algebriski:
$\overline{ab} = 10a + b$, $\overline{abc} = 100a + 10b + c$ utt. Tas pārvērš “vārdiskos”
uzdevumus par cipariem algebriskos vienādojumos vai izteiksmēs, kuras pēc tam var
pārveidot vai sadalīt reizinātājos. Tipisks pielietojums — uzdevumi par skaitli, kura ciparus
samaina vietām, vai par skaitļa atkārtošanos (piemēram, $\overline{abcabc}$, $\overline{abab}$).
**(5) Piemēri.** LV.SOL.5.kl. par Annu un divciparu skaitļiem: $\overline{ab} + \overline{ba} =
11(a+b)$, kas vienmēr dalās ar $11$; LV.SOL.2011./12. 7. klase 6. uzd. (Pēteris-Jānis sešciparu
skaitļu spēle: izveidojas $\overline{abcabc} = 1001 \cdot \overline{abc} = 7 \cdot 11 \cdot 13 \cdot
\overline{abc}$); LV.NOL piecciparu skaitlim $\overline{abcab}$ ar dalāmību ar $13$: jāpārveido
par $1001 \cdot \overline{ab} + 100c$, kur pirmais saskaitāmais dalās ar $13$.


## 4. PrimeFactorization

**(1)** No 5.–6. klases.
**(2)** Sadalīšana pirmreizinātājos.
**(3)** Prime factorization.
**(4) Apraksts.** Katru naturālu skaitli, kas lielāks par $1$, var viennozīmīgi izteikt kā
pirmskaitļu reizinājumu (kanoniskā forma $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$). Tas ļauj
risināt jautājumus par dalāmību, skaitļa īpašībām, dažādiem skaitļa “garumiem” un dalītāju
struktūru. Olimpiāžu uzdevumos sadalījumu pirmreizinātājos bieži apvieno ar gadījumu
pārlasi (kuri pirmreizinātāji ietilpst, ar kādu pakāpi) vai ar nepieciešamību iegūt konkrētu
dalītāju skaitu.
**(5) Piemēri.** LV.JMK.2011./12. 2. kārta (“skaitļa garums” — pirmreizinātāju skaits; lielākā
četrciparu skaitļa “garums” iegūstams, ņemot pēc iespējas mazākus pirmreizinātājus);
LV.JMK.2015./16. 3. kārta (trīs dažādu naturālu skaitļu reizinājums $36 = 2^2 \cdot 3^2$ —
jāuzskaita visi sadalījumi); LV.SOL.2016./17. 6. klase 2. uzd. (vai naturāla skaitļa ciparu
reizinājums var būt $6930$ — sadala $6930$ pirmreizinātājos un pārbauda, vai katrs $\le 9$).


## 5. NumberOfDivisors

**(1)** No 8.–9. klases.
**(2)** Dalītāju skaita formula.
**(3)** Divisor counting function.
**(4) Apraksts.** Ja $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$, tad pozitīvo dalītāju skaits ir
$\tau(n) = (a_1+1)(a_2+1)\cdots(a_k+1)$. Šī formula ļauj risināt uzdevumus, kuros prasīts
skaitlis ar konkrētu dalītāju skaitu, vai kuros jāanalizē dalītāju struktūra. Bieži formula
parādās kopā ar nosacījumu, ka skaitlis ir dalāms vai nedalāms ar kādu konkrētu pirmskaitli.
**(5) Piemēri.** LV.AMO.2023.12.5 ($26\%$ no skaitļa $3 \cdot 2^{24}$ dalītājiem dod
atlikumu $1$, dalot ar $3$ — autors izmanto, ka kopā ir $2 \cdot 25 = 50$ dalītāji);
LV.NOL.2025.11.kl. (skaitlis ar tieši $111$ dalītājiem un nosacījumi par dalāmību);
GRAMATA atrisinājums uzdevumam “vai eksistē skaitlis ar tieši $12$ dalītājiem” — der
$2^{11}$, jo $\tau(2^{11}) = 12$.


## 6. FactoringAlgebraicExpressions

**(1)** No 8.–9. klases.
**(2)** Algebriska sadalīšana reizinātājos (SRF, binoma kvadrāts).
**(3)** Factoring algebraic expressions.
**(4) Apraksts.** Identitātes $a^2 - b^2 = (a-b)(a+b)$, $(a \pm b)^2 = a^2 \pm 2ab + b^2$,
$a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$, $a^n - b^n$ utt. ļauj izteiksmes pārveidot par
reizinājumiem un pierādīt dalāmību vai to, ka skaitlis nav pirmskaitlis. Šī metode īpaši
labi strādā ar pakāpju izteiksmēm. Bieži pirms identitātes lietošanas izteiksme jāpārveido
(jāizvilkts kopējais reizinātājs, jāpārkārto saskaitāmie utt.).
**(5) Piemēri.** GRAMATA 9.kl. teorijas materiāls: $2^{28} - 3^{14} = (2^{14} - 3^7)(2^{14} + 3^7)$,
tātad nav pirmskaitlis; $2^{16} + 2^9 \cdot 5^{17} + 5^{34} = (2^8 + 5^{17})^2$;
LV.NOL.2011./12. 8. klase 3. uzd.: $3999991 = 4000000 - 9 = 2000^2 - 3^2 = 1997 \cdot 2003$;
LV.NOL.2025.12.kl. par izteiksmi $b^2 - ac$ saistītā ar racionālu skaitli.


## 7. ParityArgument

**(1)** No 5.–6. klases.
**(2)** Paritātes (pāra/nepāra) argumenta lietojums.
**(3)** Parity argument.
**(4) Apraksts.** Paritāte ($\bmod 2$) ir vienkāršākais invariants skaitļu teorijā: pāra plus
pāra ir pāra; nepāra plus nepāra ir pāra; pāra plus nepāra ir nepāra; pāra reizes jebkurš ir
pāra. Tas ļauj ātri pierādīt, ka kāda vienādība nav iespējama vai kāds rezultāts nav
sasniedzams. Tipiska pielietojuma joma — pierādījums no pretējā: pieņem, ka vienādība
izpildās, un atrod, ka vienai pusei jābūt pāra skaitlim, bet otrai — nepāra.
**(5) Piemēri.** GRAMATA uzdevums par eksistenci $8a - 12b = 2023$ naturālos skaitļos —
kreisā puse vienmēr pāra, labā nepāra, tātad nav atrisinājuma; LV.AMO.2024.9.3 (Agnese
darbojas ar $11, 12, 13$ uz tāfeles — paritātes konfigurācija $1$ pāra un $2$ nepāra saglabājas,
tādēļ $20, 24, 25$ nav sasniedzams); GRAMATA uzdevums par naturāliem $a, b, c$ un pāra
skaitļu skaitu starp $a+b, a+c, b+c, ab, ac, bc$ — jāpārbauda visas paritātes kombinācijas.


## 8. ModularArithmetic

**(1)** No 8.–9. klases.
**(2)** Kongruences pēc moduļa (atlikumu aritmētika).
**(3)** Modular arithmetic / congruences.
**(4) Apraksts.** Ja $a \equiv b \pmod{m}$, tad $a$ un $b$ dod vienādus atlikumus, dalot ar $m$.
Šādas kongruences var saskaitīt, atņemt, reizināt un (ar piesardzību) kāpināt. Tas dod
sistemātisku rīku, lai izsekotu skaitļa atlikumam pa moduļa $m$, un parasti tiek pielietots
kopā ar pilno pārlasi pa visiem atlikumiem $\{0, 1, \ldots, m-1\}$. Pamatuzdevums — pierādīt,
ka kāda izteiksme nav vesela skaitļa kvadrāts (kvadrāti dod atlikumus $0, 1$ pēc moduļa $4$
un $0, 1, 4, 7, 9$ pēc moduļa $8$), vai ka kāds skaitlis nedalās ar dotu skaitli.
**(5) Piemēri.** LV.NOL.2023.11.4 (pierādīt, ka divu secīgu naturālu skaitļu reizinājums nav
formā $36n + 8$: pēc $\bmod 9$ kreisā puse vienmēr ir $8$, bet $x(x+1)$ nedod $8 \pmod{9}$);
LV.NOL.2021.10. klase (izteiksme $n^2 - n + 36$ nedalās ar $165$ — pēdējais cipars nedod ne
$0$, ne $5$); LV.AMO.2023.12.5 ($2^a \pmod{3}$ atkarībā no $a$ paritātes).


## 9. DivisibilityByConsecutive

**(1)** No 8. klases.
**(2)** Secīgu skaitļu reizinājuma dalāmība.
**(3)** Divisibility of products of consecutive integers.
**(4) Apraksts.** Reizinājums $n(n+1)$ vienmēr ir pāra skaitlis (viens no diviem secīgiem
skaitļiem ir pāra). Reizinājums $n(n+1)(n+2)$ vienmēr dalās ar $6$. Vispārīgāk, $k$ secīgu
naturālu skaitļu reizinājums dalās ar $k!$. Saistīts rezultāts: ja $p$ ir nepāra pirmskaitlis,
tad $p^2 - 1 = (p-1)(p+1)$ dalās ar $8$ (no diviem secīgiem pāra skaitļiem viens dalās
ar $4$, otrs ar $2$). Šī metode atvieglo daudzu izteiksmju dalāmības pārbaudi.
**(5) Piemēri.** LV.NOL.2022.9.5 ($p^2 - 1$ dalās ar $24$, ja $p$ — nepāra pirmskaitlis: dalās
ar $3$ kā secīgu skaitļu reizinājums un dalās ar $8$, kā parādīts iepriekš); klasisks olimpiāžu
folkloras uzdevums — pierādīt, ka $n^3 - n$ dalās ar $6$ (sadala kā $n(n-1)(n+1)$);
LV.AMO.2024.12.3 ($n^3 \equiv n \pmod{6}$).


## 10. LastDigitAnalysis

**(1)** No 6.–7. klases.
**(2)** Pēdējā cipara (atlikuma pēc $\bmod 10$) analīze.
**(3)** Last digit (mod 10) analysis.
**(4) Apraksts.** Skaitļa pēdējais cipars nosaka atlikumu, dalot ar $10$. Šī ir vienkāršākā
modulārās aritmētikas forma, kas pieejama jau pirms kongruenču formālas apgūšanas.
Sevišķi noderīga, lai izslēgtu vienādību: ja kreisā un labā puse dod dažādus pēdējos ciparus,
vienādība nav iespējama. Noderīgs fakts — naturāla skaitļa kvadrāta pēdējais cipars var būt
tikai $0, 1, 4, 5, 6, 9$ (nekad $2, 3, 7, 8$).
**(5) Piemēri.** GRAMATA 9.kl. atrisinājums: $(x-y)^2 = 6xy + 7$ nav atrisinājuma naturālos
skaitļos, jo kreisā puse ir skaitļa kvadrāts un nevar beigties ar $7$; LV.NOL.2021.10. klase
(pārbauda visus iespējamos pēdējos ciparus skaitļiem $n$ un $n-1$, lai redzētu, kāds ir
$n^2 - n + 36$ pēdējais cipars); LV.NOL.2021TEST.6.15 (vai $20212021$ dalās ar $5$ — atbilde
“nē”, jo nebeidzas ne ar $0$, ne ar $5$).


## 11. CompleteEnumeration

**(1)** No 5. klases.
**(2)** Pilnā pārlase ar gadījumu analīzi.
**(3)** Complete enumeration / case analysis.
**(4) Apraksts.** Ja iespējamo vērtību ir maz, tās visas uzskaita un pārbauda atsevišķi. Šī
metode parādās jau pirmajos olimpiāžu uzdevumos un ir centrāla uzdevumiem, kur prasīts
atrast “visas” derīgās vērtības. Pārlasi var veikt pa skaitļa ciparu summas vērtībām, pa
skaitļa atlikumiem ar kādu moduli, pa visiem pirmskaitļiem līdz dotai robežai utt.
Risinājuma struktūra: visi gadījumi tiek uzskaitīti, un katrā tiek vai nu uzrādīts piemērs, vai
pierādīta neiespējamība.
**(5) Piemēri.** GRAMATA: kā skaitli $50$ izteikt kā divu pirmskaitļu summu — autors pārbauda
visus pirmskaitļus, kas nepārsniedz $50$, un atrod $4$ derīgus pārus; GRAMATA $4$-centu/$9$-centu
pastmarku uzdevums (pārbauda visas iespējamās $9$-centu pastmarku skaita vērtības no
$0$ līdz $4$); LV.AMO.2024.11.3 (četrciparu skaitlis ar īpašību par nodzēstā cipara dalāmību
ar $3$ — jāpārbauda atlikumu kombinācijas pēc moduļa $3$).


## 12. InvariantMethod

**(1)** No 6.–7. klases.
**(2)** Invariantu metode.
**(3)** Invariant method.
**(4) Apraksts.** Lai pierādītu, ka kāds rezultāts nav sasniedzams ar atļautām darbībām,
atrod kādu lielumu, kurš saglabājas (vai mainās paredzami) pie katras atļautās darbības,
bet atšķiras sākuma un beigu konfigurācijā. Skaitļu teorijā kā invariants visbiežāk parādās:
elementu summa, summa $\bmod m$ (paritāte, dalāmība ar $3$, $4$ u.tml.), elementu skaita
paritāte. Atšķirībā no nedalāmības argumenta, šeit invariants tiek izsekots procesa gaitā.
**(5) Piemēri.** GRAMATA klasiskais paritātes piemērs: $10$ papīra gabalu sagriežot $5$ vai
$7$ daļās, kopējais gabalu skaits paliek pāra → nevar iegūt $999$; GRAMATA: skaitlis $18$ uz
tāfeles, pieskaitot $6$ vai atņemot $12$, paliek dalāms ar $3$, tādēļ $2$ nav sasniedzams;
LV.NOL.2023.7.5 (kastes lodīšu uzdevumā ar trim krāsām visu krāsu lodīšu paritāte mainās
katrā gājienā — viens no apgalvojumiem neizpildās).


## 13. PeriodicSequence

**(1)** No 7.–8. klases.
**(2)** Periodiska skaitļu virkne un atlikumi.
**(3)** Periodic sequences modulo $m$.
**(4) Apraksts.** Ja virkni iegūst pēc rekurences un katru locekli aplūko modulo $m$, tad
iespējamo atlikumu daudzums ir ierobežots, un agrāk vai vēlāk atlikumu kombinācija
atkārtojas — virkne kļūst periodiska. Tas ļauj noteikt patvaļīgi tāla virknes locekļa atlikumu
vai paritāti. Bieži šī metode parādās uzdevumos par lielas pakāpes pēdējo ciparu
($2^{n} \pmod{10}$ ir periodisks ar periodu $4$), Fibonači tipa virkņu īpašībām vai virknēm,
kas definētas ar “katrs nākamais loceklis ir...”
**(5) Piemēri.** GRAMATA piemērs par virkni, kur pirmais loceklis ir $11$ un katrs nākamais —
iepriekšējā kvadrāta ciparu summa; pēc dažiem soļiem virkne kļūst periodiska un var noteikt
$2018$-o locekli; klasisks uzdevums par pēdējo ciparu skaitlim $2^{2018}$; LV.AMO.2024.7.3
(skaitļu virkne $12, \ldots$ ar darbībām reizināt vai dalīt ar $2$ vai $3$ — pirmreizinātāju skaita
paritāte ir periodiska, tāpēc $61.$ loceklis nevar būt $54$).


## 14. DiophantineEquations

**(1)** No 8.–9. klases.
**(2)** Vienādojumi veselos skaitļos (Diofanta).
**(3)** Diophantine equations.
**(4) Apraksts.** Vienādojumu, kura nezināmie ir veseli (vai naturāli) skaitļi, parasti risina
ar vienu no šādiem paņēmieniem: (a) sadala vienādojumu reizinātājos un izmanto skaitļa
sadalījumu reizinātājos veselos skaitļos; (b) izsaka vienu nezināmo caur otru un izmanto
dalāmības argumentu; (c) pierāda neiespējamību ar modulāro aritmētiku vai paritāti.
Tipiskā uzdevuma struktūra: konstatēt, ka kreisā un labā puse jāizsaka kā vienāda formas
reizinājumi, un pārlasīt visus iespējamos veidus.
**(5) Piemēri.** GRAMATA uzdevums par $(x-2)(y-2) = 4$ veselos skaitļos — autors uzskaita
visus $6$ veidus, kā $4$ sadalāms kā divu veselu skaitļu reizinājums, un iegūst $6$ atrisinājumu
pārus; LV.AMO.2024.10.1 (pareizinājuma uzdevums $n^4 + 2n = m^2 + 2m^3$ — sadalāms par
$n(n^3 - 2n^2 - n + 2) = 0$ un tālāk meklē dalāmību ar $-2$); LV.NOL.2025.12.2 (vienādojums
$972^a \cdot 32^b \cdot 9^c = 1$ — pēc sadalīšanas pirmreizinātājos kļūst par lineāru
vienādojumu sistēmu kāpinātājos).


## 15. PigeonholeInNT

**(1)** No 7.–8. klases.
**(2)** Dirihlē princips skaitļu teorijā.
**(3)** Pigeonhole principle in number theory.
**(4) Apraksts.** Klasiskais Dirihlē princips: ja $n+1$ skaitļus sadala $n$ klasēs (piem., pēc
atlikuma ar $n$), tad vismaz divi nonāks vienā klasē. Skaitļu teorijā tas dod tūlītēju
secinājumu: starp jebkuriem $n+1$ veseliem skaitļiem ir divi, kuru starpība dalās ar $n$.
Vispārīgāks variants: ja vairāk nekā $mn$ objekti tiek sadalīti $n$ grupās, tad kādā grupā ir
vismaz $m+1$ objekti. Bieži kombinēta ar pilno pārlasi vai sadalījumu pa atlikumiem.
**(5) Piemēri.** GRAMATA 2.15.: no jebkuriem $8$ naturāliem skaitļiem var izvēlēties divus,
kuru starpība dalās ar $7$ ($7$ iespējamie atlikumi, $8$ skaitļi); LV.AMO.2024.10.2 ($15$
trīsciparu skaitļu vidū — vai nu divi ar vienādu ciparu summu, vai divi ar ciparu summu
summu $28$: izveido $14$ kopas un piemēro Dirihlē principu); LV.AMO.2024.10.4 (par
skolēnu atzīmēm — $28$ skolēnu vidū vai nu četri ar vienādu atzīmi, vai četri ar atzīmi
$> 7$).


## 16. BoundingArgument

**(1)** No 8.–9. klases.
**(2)** Novērtējumi no augšas un no apakšas.
**(3)** Bounding (estimation) argument.
**(4) Apraksts.** Lai pamatotu, ka skaitlis ir vienāds ar konkrētu vērtību, var pierādīt divas
nevienādības — ka tas nav lielāks par šo vērtību un ka tas nav mazāks par to. Tipiska
pielietojuma situācija — skaitlis ir nezināms, bet ar dotajiem nosacījumiem var iegūt gan
augšējo, gan apakšējo robežu, kas izrādās tuvu (vai vienāda). Skaitļu teorijā šis paņēmiens
parādās gan optimizācijas uzdevumos (kāds ir lielākais/mazākais skaitlis ar dotām īpašībām),
gan tādos, kur nezināmā vērtība ir noteikta, jo veselu skaitļu starp augšējo un apakšējo
robežu ir tikai viens.
**(5) Piemēri.** LV.AMO.2019.10.1 (dimantu uzdevums — masu summa $S$ tiek novērtēta no
augšas un apakšas, iegūstot $6\tfrac{13}{42} \le n-3 \le 7\tfrac{31}{35}$, tādēļ $n-3 = 7$);
LV.NOL.2021.10.5 (skaitļu pāros — vispirms pierāda $a_{125} + a_{376} > 2000$, pēc tam
izmanto, ka skaitļi ir dažādi un naturāli, lai iegūtu $a_{146} \ge a_{125} + 21$);
GRAMATA 5.kl. uzdevums par mazāko sešciparu skaitli no cipariem $\{0, 1, 2, 3\}$ ar ciparu
summu, kas dalās ar $9$.


## 17. ProofByContradiction

**(1)** No 7.–8. klases.
**(2)** Pierādījums no pretējā.
**(3)** Proof by contradiction.
**(4) Apraksts.** Lai pierādītu, ka kāds apgalvojums ir patiess vai kāds rezultāts nav
sasniedzams, pieņem pretējo un parāda, ka tas noved pie pretrunas (ar doto, ar zināmu
faktu vai ar pašu pieņēmumu). Skaitļu teorijā tipisks scenārijs: pieņem, ka kāda izteiksme
pieņem konkrētu vērtību, un atrod, ka tā labās un kreisās puses dalāmība neatbilst.
Pierādījumu no pretējā bieži apvieno ar paritātes argumentu, modulāro aritmētiku vai
ekstremālo elementu izvēli.
**(5) Piemēri.** LV.NOL.2023.11.4 (pieņem, ka $x(x+1) = 36n+8$ ir iespējams, un caur
$(2x+1)^2 = 144n + 33$ iegūst pretrunu ar dalāmību ar $9$); LV.NOL.2021.11.kl. (uzdevumā
par $a+b$ un $ab+1$ pirmskaitļiem — pieņem, ka abi dalās ar pirmskaitli $p \ge 3$, un noved
pie pretrunas); LV.NOL.2021.11.kl. par $n^2 - n + 36$ nedalāmību ar $169$.


## 18. AlgebraicManipulationForInteger

**(1)** No 8.–9. klases.
**(2)** Algebriska pārveidošana, lai iegūtu paritātes vai dalāmības argumentu.
**(3)** Algebraic rearrangement to expose divisibility.
**(4) Apraksts.** Bieži vien sākotnējais vienādojums vai izteiksme tieši neuzrāda paritāti vai
dalāmību, bet pēc pārveidošanas (pārkārtošanas, pilnā kvadrāta atdalīšanas, kopīga
reizinātāja iznešanas) tā kļūst skaidri redzama. Šī metode darbojas kā tilts starp algebru
un skaitļu teoriju — algebrisko pārveidojumu mērķis ir radīt formu, kurā parādās modulārais
arguments.
**(5) Piemēri.** GRAMATA 9.kl. par $20x^3 - 17y^2 + 1 = 2018$: pēc pārkārtošanas
$20(x^3 - 100) = 17(1 + y^2)$; kreisā puse pāra, tādēļ $y$ ir nepāra, $y = 2k+1$, un iegūstam
$20(x^3 - 100) = 17(2 + 4k^2 + 4k)$, kur kreisā dalās ar $4$, bet labā ne; LV.NOL.2024.9.5
($9x = 10x - x = \overline{x0} - x$, kas ļauj iegūt ciparu summas dalāmību ar $9$);
LV.NOL.2021.11. klase ($n^2 - n + 36 = (n-7)^2 + 13(n-1)$ — sadalījums, kas atklāj dalāmību
ar $13$).


## 19. TelescopingAndIdentity

**(1)** No 8.–9. klases.
**(2)** Identitāšu un teleskopējošu summu izmantošana.
**(3)** Telescoping sums and algebraic identities.
**(4) Apraksts.** Daudzas skaitļu teorijas izteiksmes pārveidojamas, izmantojot identitātes
$a = a + b - b$, $n = 10n - 9n$, $\tfrac{1}{n(n+1)} = \tfrac{1}{n} - \tfrac{1}{n+1}$, vai sadalot
summas tā, ka blakus locekļi savstarpēji iznīcinās. Šis paņēmiens ir noderīgs gan summu
aprēķināšanā, gan dalāmības pierādīšanā: ja $a = b + c$ un divi no trim dalās ar $d$, tad arī
trešais dalās ar $d$.
**(5) Piemēri.** LV.AMO.2023.10.5 ($\tfrac{1+2+\ldots+99}{99} = \tfrac{50 \cdot 99}{99} = 50$
— izmantojot summas formulu); GRAMATA uzdevums par četrciparu skaitli un tā ciparu
permutāciju — abu skaitļu starpība dalās ar $9$, jo $abcd = 999a + 99b + 9c + (a+b+c+d)$
un ciparu summa pie permutācijas nemainās; LV.NOL.2024.9.kl. uzdevumi par ciparu summu
caur identitāti $9 \cdot \overline{abc} = \overline{abc0} - \overline{abc}$.


## 20. NumberConstruction

**(1)** No 5.–6. klases.
**(2)** Skaitļa konstruēšana ar dotām īpašībām.
**(3)** Constructing a number with required properties.
**(4) Apraksts.** Lai pierādītu, ka skaitlis ar dotām īpašībām eksistē, pietiek to konkrēti
uzrādīt. Tomēr “konstruēšana” parasti nav uzminēšana — to veic sistemātiski, izmantojot
dalāmības pazīmes vai algebriskās identitātes. Tipiska struktūra: skaitlis tiek izteikts kā
saskaitāmo summa, kur katrs saskaitāmais atsevišķi dalās ar prasīto skaitli; vai arī tiek
piemērota viena no Latvijas olimpiāžu “folkloras” konstrukcijām, piem., $\overline{abcabc}$
formas skaitlis, kas dalās ar $7, 11, 13$.
**(5) Piemēri.** LV.NOL.2011./12. 5. klase 3. uzd. (septiņciparu skaitlis no cipariem
$1, 2, 3, 4, 5, 7, 8$, kas dalās ar $7$ — autors konstruē $1428357 = 1400000 + 28000 + 350 + 7$,
katra summas locekļa dalāmība ar $7$ ir tieša); GRAMATA: vai eksistē skaitlis ar $12$
dalītājiem — der $2^{11}$; LV.AMO.2024.11.3 (četrciparu skaitlis, kuram, nodzēšot vienu
ciparu, atlikušais nedalās ar $3$ — konstruē, izmantojot atlikumus pēc moduļa $3$).


## 21. GameInvariantsInNT

**(1)** No 7.–8. klases.
**(2)** Skaitļu teorijas invarianti spēļu uzdevumos.
**(3)** Number-theoretic invariants in game problems.
**(4) Apraksts.** Spēļu uzdevumos uzvarētāja stratēģijas vai gala stāvokļa sasniedzamības
analīze bieži balstās uz skaitļu teorētisku invariantu: kopīgais skaitlis dalās/nedalās ar
dotu skaitli, summa $\bmod m$, pirmreizinātāju skaita paritāte u.tml. Atšķirībā no
parastās invariantu metodes, te invariants jāizmanto, lai uzrādītu konkrētu uzvaras
stratēģiju (kā vienam spēlētājam saglabāt invariantu, vai kā otrs to noteikti pārkāps).
**(5) Piemēri.** LV.SOL.2011./12. 7. klase 6. uzd. (Pēteris-Jānis sešciparu spēle, kur Pēteris
veido $\overline{abcabc} = 1001 \cdot \overline{abc}$, kurš vienmēr dalās ar $13$);
LV.AMO.2024.9.3 (Agneses uzdevumā uz tāfeles vienmēr saglabājas $1$ pāra un $2$ nepāra
skaitļi); LV.AMO.2024.7.3 (skaitļu virkne ar reizināšanu/dalīšanu ar $2, 3$ — invariants ir
pirmreizinātāju skaita paritāte).


## 22. SumOfArithmeticOrTriangularNumbers

**(1)** No 7.–8. klases.
**(2)** Aritmētiskās progresijas vai trijstūru skaitļu summas formula.
**(3)** Sum of arithmetic progression / triangular numbers.
**(4) Apraksts.** Pirmo $n$ naturālo skaitļu summa $1 + 2 + \ldots + n = \tfrac{n(n+1)}{2}$ un
aritmētiskās progresijas summa $S_n = \tfrac{n(a_1 + a_n)}{2}$ ir bāzes rīki, kas pirmoreiz
parādās jau 6.–7. klases olimpiādēs. Tie ļauj salīdzināt kopējās summas, pierādīt
neiespējamību (ja kopējā summa nedalās ar nepieciešamo skaitu klašu), un risināt uzdevumus
ar zīmēm “$+$” un “$-$” pirms skaitļiem.
**(5) Piemēri.** LV.NOL.2022.10.5 (izteiksme $\pm 1 \pm 2 \ldots \pm 120$ — kopējā summa
$1 + \ldots + 120 = 7260$; ja zīmes maina, tad $P - M$ var iegūt ne katrru vērtību; konkrēti
$2023$ neder, jo $P$ un $M$ ir ar vienādu paritāti un to starpība ir pāra); LV.AMO.2024.11.2
(festivāla dalībnieku punktu summa $5(0 + \tfrac{1}{2} + \ldots + 9) = 5 \cdot 85.5 = 427.5$ —
nav vesels, tādēļ pretruna); GRAMATA: Daina veido desmitciparu skaitli no visiem cipariem
— ciparu summa $0 + 1 + \ldots + 9 = 45$ vienmēr dalās ar $3$.


## 23. WellOrderingPrinciple

**(1)** No 9. klases.
**(2)** Mazākā elementa princips.
**(3)** Well-ordering / minimal counterexample.
**(4) Apraksts.** Naturālo skaitļu apakškopā vienmēr eksistē mazākais elements. To bieži
izmanto pierādījumos no pretējā: pieņem, ka kāds apgalvojums neizpildās, un izvēlas
mazāko pretpiemēru. No šī izvēlēta mazākā elementa īpašībām iegūst pretrunu, parasti
konstruējot vēl mazāku pretpiemēru vai parādot, ka mazākais elements pats par sevi noved
pie pretrunas. Šī ir matemātiskās indukcijas un “bezgalīgās noaiziešanas” loģiskā pamatne.
**(5) Piemēri.** LV.AMO.2019.10.1, LV.AMO.2019.12.5 (kombinēti ar novērtējumiem — izvēlas
ekstrēmu un iegūst pretrunu); LV.NOL olimpiāžu uzdevumi, kuros izvēlas mazāko skaitli ar
dotām īpašībām un pierāda, ka tā eksistence ir pretrunīga (klasiska struktūra arī starptautisku
olimpiāžu uzdevumos, piem., USAMO un Balkānu olimpiāžu junioru sērijās).


## 24. CountingWithDigitalConstraints

**(1)** No 6.–7. klases.
**(2)** Skaitīšana ar nosacījumiem par cipariem.
**(3)** Counting numbers with digit constraints.
**(4) Apraksts.** Šī ir kombinatoriski–skaitļu teorētiska metode: jāsaskaita visi skaitļi, kuri
atbilst noteiktiem ciparu nosacījumiem (dalāmība, ciparu summa, atkārtošanās utt.).
Risināšana parasti notiek pa ciparu pozīcijām, ievērojot reizināšanas principu un nepāra
gadījumu izdalīšanu. Bieži apvienots ar pirmā vai pēdējā cipara ierobežojumu (lai garantētu
dalāmību) un ar atlikumu pārlasi pēc moduļa $3$, ja prasīta dalāmība ar $3$ vai $9$.
**(5) Piemēri.** LV.AMO.2024.9.5 (Zanes deviņciparu tālruņa numurs ar atšķirīgiem cipariem,
dalāms ar $15$, un kvadrātu konfigurācijām uz tālruņa pogu izkārtojuma — atbilde $12$);
LV.SOL.2015./16. 5. klase 5. uzd. (lielākais piecciparu skaitlis ar dažādiem cipariem, kas
dalās ar $3$); klasiskās palindromu uzdevums no LV.SOL.2011./12. 6. klases ($2011.$ pēc
kārtas septiņciparu palindroms).


## 25. PrimePropertiesAndUniqueness

**(1)** No 7.–8. klases.
**(2)** Pirmskaitļu īpašības un viennozīmīga sadalīšana.
**(3)** Properties of primes and unique factorization.
**(4) Apraksts.** Pirmskaitlim $p$ ir tikai divi pozitīvi dalītāji: $1$ un $p$. Ja $p$ — pirmskaitlis
un $p \mid ab$, tad $p \mid a$ vai $p \mid b$ (Eiklīda lemma). Pirmskaitļu viennozīmīgas
sadalīšanas teorēma garantē, ka katra naturāla skaitļa $n > 1$ pirmreizinātāju sadalījums
ir unikāls. Šīs īpašības atļauj “atrisināt vienādības pa pirmreizinātājiem”, salīdzinot abu pušu
$p$-pakāpes katram pirmskaitlim $p$.
**(5) Piemēri.** LV.NOL.2023.8.1 (uzdevums, kurā katrā rūtiņā jāieraksta pirmskaitlis tā, lai
četru pēc kārtas summa būtu vienāda — autors izmanto, ka pirmskaitļu summa $127$ noved
pie konkrētas periodiskas konfigurācijas); LV.NOL.2025.12.2 ($972^a \cdot 32^b \cdot 9^c = 1$ —
salīdzinot kāpinātājus pie pirmskaitļiem $2$ un $3$, iegūst lineāru sistēmu); LV.NOL.2021.11.kl.
($a^2 + b$ pirmskaitlis un secinājumi par $a, b$ paritāti).
