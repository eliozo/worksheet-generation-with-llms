# Tipiskās ģeometrijas pamatojumu metodes 5.–9. klases olimpiāžu uzdevumos

Šis dokuments apkopo galvenās ģeometriskās pamatojuma metodes, kuras parādās Latvijas
(LV.AMO, LV.NOL) un citu junioru līmeņa olimpiāžu uzdevumos 5.–9. klasei. Mazākajās klasēs
dominē kombinatoriskās ģeometrijas, krāsojumu un simetrijas metodes, savukārt 8.–9. klasē
pakāpeniski parādās tradicionālie ģeometrijas pierādījumi par vienādiem un līdzīgiem
trijstūriem, paralelogramu īpašībām, Pitagora teorēmu utt. Tipiskā olimpiādes uzdevumā vienlaikus
tiek lietoti vairāki paņēmieni — leņķu meklēšana parasti ir tikai viens no soļiem.


## 1. AngleChasing

**(1)** No 7. klases.
**(2)** Leņķu meklēšana (izteikšana ar mainīgajiem).
**(3)** Angle chasing.
**(4) Apraksta.** Galvenais paņēmiens, ar ko sāk gandrīz katru ģeometrijas uzdevumu, kurā
parādās leņķi. Vienu vai vairākus nezināmos leņķus apzīmē ar mainīgo (piem., $\alpha$, $\beta$)
un pakāpeniski izsaka pārējos leņķus, izmantojot trijstūra leņķu summu ($180^\circ$),
četrstūra leņķu summu ($360^\circ$), blakusleņķus, krustleņķus, vienādsānu trijstūra leņķus pie
pamata un vienādu malu/leņķu īpašības. Bieži leņķu meklēšanas mērķis ir parādīt, ka kāds
trijstūris ir vienādsānu (divi vienādi leņķi), atrast leņķi konkrētā punktā vai pierādīt, ka divi
leņķi ir vienādi (gatavojot līdzīgu/vienādu trijstūru izmantošanai).
**(5) Piemēri.** LV.NOL.2017./18. 7. klase 1. uzd. (leņķis $\angle AGE$ vienādsānu trijstūru
konstrukcijā); LV.NOL.2011./12. 8. klase 2. uzd. (trijstūrī $ABC$ ar $\sphericalangle ABC = 30^\circ$
un vienādmalu $\triangle CEF$ jāparāda, ka $F$ ir $BC$ viduspunkts); LV.AMO.2023.10.3.
(ieliekta četrstūra leņķu sakarību kombinēšana ar trijstūru vienādību).


## 2. ParallelLinesAngleProperties

**(1)** No 7. klases.
**(2)** Leņķi pie paralēlām taisnēm.
**(3)** Parallel lines and transversal angles.
**(4) Apraksta.** Ja divas paralēlas taisnes krusto trešā taisne, tad iekšējie šķērsleņķi ir
vienādi, kāpšļu leņķi ir vienādi un iekšējie vienpusleņķi summējas $180^\circ$. Šī sakarība
sniedz iespēju leņķus, kas atrodas dažādās zīmējuma vietās, “pārvietot” pie viena un tā paša
trijstūra; bieži apvienojas ar palīglīniju vilkšanu paralēli kādai esošai taisnei. Apgrieztais
apgalvojums (ja attiecīgie leņķi ir vienādi, tad taisnes paralēlas) tiek izmantots, lai pierādītu
taišņu paralelitāti.
**(5) Piemēri.** LV.NOL.2017./18. 7. klase 1. uzd. (caur vairākiem punktiem velk taisnes
paralēli $AB$ un summē leņķus $\alpha$ un $\beta$); LV.AMO.2019.8.3. (paralelogramā $ABCD$
bisektrises leņķis ir iekšējais šķērsleņķis pie $AB \parallel CD$); LV.NOL.2024.10.1. (lai
pierādītu $AC \parallel BD$, izmanto, ka iekšējo vienpusleņķu summa ir $180^\circ$).


## 3. TriangleAngleSum

**(1)** No 7. klases.
**(2)** Trijstūra (un daudzstūra) leņķu summa.
**(3)** Triangle and polygon angle sum.
**(4) Apraksta.** Trijstūra iekšējo leņķu summa ir $180^\circ$, četrstūra — $360^\circ$, un
patvaļīga $n$-stūra leņķu summa ir $(n-2)\cdot 180^\circ$. Ārējais leņķis ir vienāds ar abu
neblakus iekšējo leņķu summu. Šī formulas tiek lietota gan, lai aprēķinātu nezināmo leņķi,
gan, lai izteiktu leņķus ar parametriem $\alpha, \beta$. Bieži apvienojas ar iepriekšējām divām
metodēm. Regulāra $n$-stūra leņķis ir $\frac{(n-2)\cdot 180^\circ}{n}$ — piemēram, regulāra
astoņstūra leņķis ir $135^\circ$.
**(5) Piemēri.** LV.AMO.2009./10. 8. klase 4. uzd. (regulāra astoņstūra leņķis $135^\circ$
izmantots, lai parādītu, ka $BDFH$ ir kvadrāts); LV.AMO.2023.10.3 (pilnais leņķis ap punktu
$B$: $360^\circ$); LV.NOL.2024.10.1. (četrstūra $CAXY$ ievilkta četrstūra leņķu summa).


## 4. IsoscelesTriangleProperties

**(1)** No 7. klases.
**(2)** Vienādsānu trijstūra īpašības un pazīmes.
**(3)** Isosceles triangle properties.
**(4) Apraksta.** Vienādsānu trijstūrī leņķi pie pamata ir vienādi; bisektrise, kas vilkta no
virsotnes pret pamatu, ir arī mediāna un augstums. Apgriezti — ja divi trijstūra leņķi ir
vienādi, tad trijstūris ir vienādsānu (tā saucamā “pazīme”). Ļoti bieži uzdevumā saskata
vienādsānu trijstūri ar leņķu meklēšanas palīdzību un tad iegūst secinājumus par malu
vienādību (vai otrādi). Vienādmalu trijstūris ir vienādsānu trijstūra speciālgadījums ar visiem
leņķiem $60^\circ$.
**(5) Piemēri.** LV.NOL.2017./18. 8. klase 2. uzd. (atliek $PT = PS$ un secina, ka $\triangle RTP$
un $\triangle PQT$ ir vienādsānu); LV.AMO.2019.8.3 ($\triangle ADF$ ir vienādsānu, jo
$\sphericalangle DAF = \sphericalangle AFD$, tāpēc $AD = DF$); LV.AMO.2022A.9.3.
(paralelograma $ABDE$ konstrukcijā tiek izmantotas vienādu leņķu sakarības).


## 5. CongruentTriangles

**(1)** No 7. klases.
**(2)** Vienādu trijstūru pazīmes (mlm, lml, mmm, hl, hℓ).
**(3)** Triangle congruence (SAS, ASA, SSS, RHS).
**(4) Apraksta.** Lai parādītu, ka divi nogriežņi vai leņķi ir vienādi, viens no
visizplatītākajiem ceļiem ir parādīt vienādību divos trijstūros, kuriem šie nogriežņi (leņķi) ir
atbilstošie elementi. Pazīmes ir: malu–leņķis–mala (mlm/SAS), leņķis–mala–leņķis (lml/ASA),
mala–mala–mala (mmm/SSS) un taisnleņķa trijstūriem hipotenūza–katete (hℓ/RHS) vai
hipotenūza–leņķis. Praktiskos uzdevumos vispirms tiek meklēti vienādi elementi (no
dotā, no paralelograma īpašībām, no vienādsānu trijstūra, no bisektrises u.c.), tad piemērojama
attiecīgā pazīme.
**(5) Piemēri.** LV.NOL.2015./16. 8. klase 3. uzd. (taisnstūra ABCD diagonāļu krustpunktā
$\triangle AOP = \triangle COQ$ pēc ℓmℓ); LV.AMO.2022A.9.3. ($\triangle BCD = \triangle EFA$ pēc
ℓmℓ sešstūrī ar paralēlām pretmalām); LV.AMO.2023.10.3. (trīs taisnleņķa trijstūri
$\triangle ABE = \triangle CBF = \triangle CDF$ pēc hℓ).


## 6. AuxiliaryLines

**(1)** No 7. klases (vienkāršās konstrukcijās), izteikti no 8. klases.
**(2)** Palīglīniju vilkšana.
**(3)** Auxiliary lines / constructions.
**(4) Apraksta.** Sākotnējais zīmējums bieži nepieder pietiekamu informāciju — risinājuma
atrašanai jāpapildina ar palīgnogriezni vai taisni. Standartiski paņēmieni: novilkt taisni paralēli
kādai citai, novilkt perpendikulu (augstumu), savienot kādus divus punktus (piem., diagonāli),
pagarināt nogriezni. Mērķis parasti ir radīt jaunu vienādsānu/vienādmalu trijstūri,
paralelogramu, taisnleņķa trijstūri vai radīt situāciju, kurā lietojama Pitagora teorēma vai
trijstūru līdzība.
**(5) Piemēri.** LV.NOL.2015./16. 8. klase 3. uzd. (vienādsānu trijstūrī $PQD$ velk augstumu
$QH$, kas ir arī mediāna); LV.NOL.2017./18. 7. klase 1. uzd. (caur visiem punktiem velk
paralēlas $AB$); LV.NOL.2024.10.3. (no $B$ velk augstumu $BD$ pret $AC$, lai izmantotu
Pitagora teorēmu).


## 7. PointOnSegmentConstruction

**(1)** No 7. klases.
**(2)** Punkta atlikšana uz nogriežņa (malas vai pagarinājuma).
**(3)** Marking a point on a segment.
**(4) Apraksta.** Speciāls palīgkonstrukcijas paveids — uz dotās malas vai uz tās
pagarinājuma atliek punktu tā, lai iegūtu zināmu nogriežņa garumu (piem., $AE = AB$, vai
$PT = PS$). Tas rada vienādsānu trijstūri un/vai jaunus vienādus trijstūrus, kas savieto
zīmējumā jau esošos elementus. Īpaši efektīvs, ja uzdevumā parādās summas vai starpības
nosacījumi par malām (piem., $AD = AB + CD$).
**(5) Piemēri.** LV.AMO.2018./19. 7. klase 4. uzd. (uz $AD$ atliek $E$ tā, ka $AE = AB$, tad
$ED = CD$ — bisektrises kļūst par vidusperpendikuliem); LV.NOL.2020./21. 8. klase 5. uzd.
(atliek $G$ uz $AD$ ar $AG = AB$, lai pierādītu, ka $\triangle BCD$ ir vienādmalu); LV.NOL.2017./18.
8. klase 2. uzd. (uz $QR$ atliek $T$ ar $PT = PS$).


## 8. PerpendicularBisector

**(1)** No 7.–8. klases.
**(2)** Nogriežņa vidusperpendikuls.
**(3)** Perpendicular bisector property.
**(4) Apraksta.** Punkts atrodas uz nogriežņa $XY$ vidusperpendikula tad un tikai tad, ja
tas atrodas vienādā attālumā no $X$ un $Y$. Bieži vidusperpendikuls rodas no vienādsānu
trijstūra bisektrises/mediānas, vilktas no virsotnes pret pamatu. Šo īpašību izmanto, lai
pierādītu, ka divi nogriežņi ir vienādi (parādot, ka kāds punkts atrodas uz vidusperpendikula),
vai lai konstruētu nepieciešamo punktu.
**(5) Piemēri.** LV.AMO.2018./19. 7. klase 4. uzd. (četrstūrī ABCD ar $AD = AB + CD$:
bisektrises $AM$ un $DM$ kļūst par $BE$ un $CE$ vidusperpendikuliem); klasiskās konstrukcijās
ap trijstūri apvilktas riņķa līnijas centrs ir trīs malu vidusperpendikulu krustpunkts.


## 9. PythagoreanTheorem

**(1)** No 8. klases.
**(2)** Pitagora teorēma.
**(3)** Pythagorean theorem.
**(4) Apraksta.** Taisnleņķa trijstūrī ar katetēm $a, b$ un hipotenūzu $c$ izpildās $a^2 + b^2 = c^2$.
Lieto, lai aprēķinātu nezināmo nogriežņa garumu, kad zināmas divas taisnleņķa trijstūra malas;
bieži kombinē ar palīglīniju vilkšanu (augstuma novilkšana pret malu, lai izveidotu divus
taisnleņķa trijstūrus), kā arī ar saīsinātās reizināšanas formulām un kvadrātvienādojumiem.
Apgrieztā teorēma ļauj parādīt, ka trijstūris ir taisnleņķa.
**(5) Piemēri.** LV.NOL.2024.10.3. (no $B$ velk augstumu $BD$ pret $AC$, izmanto
$AB^2 - AD^2 = BC^2 - DC^2$, lai atrastu $AD = 1$); klasisks uzdevums — aprēķināt taisnstūra
diagonāli, ja zināmas malas; vairāki LV.NOL un LV.AMO uzdevumi 9. klasē, kur jāatrod
nogrieznis daudzstūrī.


## 10. SimilarTriangles

**(1)** No 9. klases.
**(2)** Līdzīgi trijstūri un to īpašības.
**(3)** Similar triangles.
**(4) Apraksta.** Divi trijstūri ir līdzīgi, ja to atbilstošie leņķi ir vienādi (pietiek ar diviem)
vai ja atbilstošās malas ir proporcionālas. Tad arī visi atbilstošie elementi (augstumi, mediānas,
bisektrises, perimetri) ir proporcionāli ar tādu pašu līdzības koeficientu $k$, bet laukumi
proporcionāli $k^2$. Bieži saskata, novelkot palīglīniju paralēli kādai malai, izveidojot
taisnleņķa trijstūru ar kopīgu leņķi vai izmantojot $90^\circ$ leņķus ar kopīgu šauro leņķi.
**(5) Piemēri.** LV.AMO.2015./16. 9. klase 2. uzd. ($\triangle BMN \sim \triangle CDN$ pēc
ℓℓ pazīmes ar koeficientu $\tfrac{1}{2}$); LV.NOL.2014./15. 9. klase (taisnleņķa trijstūra
sadalīšana līdzīgos taisnleņķa trijstūros, velkot augstumu pret hipotenūzu); LV.SOL.2012./13.
8. klase 3. uzd. (līdzīgi taisnleņķa trijstūri rūtiņu lapā $\Rightarrow$ vienādi leņķi).


## 11. ParallelogramProperties

**(1)** No 8. klases.
**(2)** Paralelograma (taisnstūra, romba, kvadrāta) īpašības un pazīmes.
**(3)** Parallelogram properties.
**(4) Apraksta.** Paralelogramā pretējās malas un pretējie leņķi ir vienādi, diagonāles
krustojoties dalās uz pusēm. Pazīmes: ja četrstūrim pretējās malas ir paralēlas (vai vienādas un
paralēlas), tad tas ir paralelograms. Tālāk specializētas īpašības: rombā diagonāles ir
perpendikulāras, taisnstūrī tās ir vienāda garuma, kvadrāts apvieno abas šīs īpašības.
Daudzos uzdevumos jāpierāda, ka kāds četrstūris (no zīmējuma) ir paralelograms vai kāds no
tā speciālgadījumiem.
**(5) Piemēri.** LV.AMO.2017./18. 8. klase 3. uzd. (paralelograma diagonāle sadala to divos
vienādos trijstūros, laukuma aprēķins); LV.AMO.2019.9.3. ($QNBC$ ir paralelograms, jo
$CQ \parallel BN$ un $CB \parallel QN$, pēc tam papildus $CB = BN$ dod rombu); LV.AMO.2024.12.4.
(parādīts, ka $BCMH$ ir paralelograms, jo $BC \parallel MH$ un $BC = MH$).


## 12. CyclicQuadrilateral

**(1)** No 9. klases (parasti 9. klases otrajā pusē vai augstākā līmenī).
**(2)** Ievilkts četrstūris riņķa līnijā.
**(3)** Cyclic quadrilateral.
**(4) Apraksta.** Četrstūris ir ievilkts riņķa līnijā tad un tikai tad, ja tā pretējo leņķu summa
ir $180^\circ$. Ekvivalenti — ja divi leņķi, kas “redz” vienu un to pašu nogriezni no vienas puses,
ir vienādi, tad attiecīgie četri punkti atrodas uz vienas riņķa līnijas. Šī sakarība bieži ļauj
“pārcelt” leņķus pa riņķa līniju un atrast slēptu leņķu vienādību. Klasiski izmantošanas
varianti: pierādīt punktu kolineāru izvietojumu uz riņķa līnijas vai pierādīt taišņu paralelitāti
caur ievilkta četrstūra leņķu sakarību. Riņķa līnijā ar diametru kā vienu malu trijstūris
ir taisnleņķa (Tales teorēma).
**(5) Piemēri.** LV.NOL.2024.10.1. (krustojošos riņķa līniju konstrukcijā divi ievilkti
četrstūri dod $AC \parallel BD$); LV.NOL.2025.11.3. (taisnstūra konstrukcijā parāda, ka
$\sphericalangle AHC = \sphericalangle AFC$, tāpēc $AHFC$ ir ievilkts).


## 13. AreaInvarianceAndDecomposition

**(1)** No 5.–6. klases (rūtiņu līmenī), nopietni no 8. klases.
**(2)** Laukums kā invariants, sadalīšana un savietošana.
**(3)** Area invariance and decomposition.
**(4) Apraksta.** Figūras laukums nemainās, ja to sadala daļās un pārvieto. Lai aprēķinātu
sarežģītas figūras laukumu, to var sadalīt taisnstūros un taisnleņķa trijstūros vai papildināt līdz
zināmai figūrai. Trijstūri, kuriem ir kopīgs pamats un kuru virsotnes atrodas uz vienas taisnei
paralēlas līnijas, ir vienlieli. Trijstūra mediāna sadala to divos vienlielos trijstūros. Šo
principu bieži lieto, lai pierādītu laukumu attiecības bez konkrētu garumu aprēķināšanas.
**(5) Piemēri.** LV.AMO.2017./18. 8. klase 3. uzd. (paralelogramā $ABCD$, ja $E$, $F$ ir $BC$
un $AD$ viduspunkti, tad četrstūra $FGEH$ laukums ir $\tfrac{1}{4}$ no $ABCD$ laukuma, izmanto
vienlielus trijstūrus); 5.–6. klases uzdevumi par kombinētām figūrām rūtiņu lapā.


## 14. AreaCounting

**(1)** No 6.–7. klases.
**(2)** Laukuma summas/divkārtīga ieskaitīšana.
**(3)** Double-counting of areas.
**(4) Apraksta.** Vienu un to pašu laukumu izsaka divos dažādos veidos, iegūstot
vienādību. Piemēram, trijstūra laukums $S = \tfrac{1}{2}\cdot a \cdot h_a = \tfrac{1}{2}\cdot b \cdot h_b$,
no kā izriet $a\cdot h_a = b\cdot h_b$. Vai arī figūra ir sadalīta vairākās daļās, tāpēc to laukumu
summa ir vienāda ar visas figūras laukumu. Šī tehnika ļauj aprēķināt nogriežņus
(piemēram, augstumu pret hipotenūzu) bez Pitagora teorēmas vai trigonometrijas.
**(5) Piemēri.** Tipisks 9. klases uzdevums: izteikt taisnleņķa trijstūra augstumu pret
hipotenūzu, izmantojot, ka laukums vienāds gan caur katetēm, gan caur hipotenūzu un
augstumu pret to; LV.NOL.2024.10.3. piezīmē minēts šis paņēmiens (augstumu var aprēķināt
caur trijstūra laukumu pēc Hērona formulas).


## 15. TriangleInequality

**(1)** No 7. klases.
**(2)** Trijstūra nevienādība.
**(3)** Triangle inequality.
**(4) Apraksta.** Patvaļīgā trijstūrī katras malas garums ir mazāks nekā pārējo divu malu
garumu summa: $a + b > c$, $b + c > a$, $a + c > b$. Tikpat svarīga ir starpības forma:
$|a - b| < c$. Šo nevienādību lieto, lai pierādītu citas nevienādības ar trijstūra malām, lai
parādītu, ka trīs nogriežņi nevar veidot trijstūri, kā arī kombinatorisku uzdevumu
risinājumos, kur jānosaka, no kādu nogriežņu komplektiem var izveidot trijstūri.
**(5) Piemēri.** LV.NOL.2022.8.3. ($\triangle ABC$ vienādsānu platleņķa ar $\sphericalangle ABC = 20^\circ$:
pierāda, ka $3 \cdot AC > AB$, izmantojot $BC + AC > AB$ kombinācijā ar gadījumu analīzi);
LV.AMO.2024.11.1. (trijstūra nevienādības $a + b > c$ kvadrāts dod $a^2 + 2bc > b^2 + c^2$);
LV.AMO.2024.12.1. (no $a + b > c$ secina $c(a + b + c) > 2c^2$, saskaita trīs nevienādības).


## 16. ColoringInvariant

**(1)** No 6.–7. klases.
**(2)** Krāsojuma invariants.
**(3)** Coloring invariant.
**(4) Apraksta.** Lai pierādītu, ka figūru nevar noklāt ar dotām figūriņām (vai citu līdzīgu
neiespējamību), tabulu izkrāso šaha galdiņa veidā, joslās, diagonālēs vai 3–4 krāsās tā, lai
katra figūriņa pārklātu fiksētu skaitu katras krāsas rūtiņu. Ja kopējais krāsas rūtiņu skaits
figūrā un izkrāsotā skaita summa figūriņās nesakrīt, iegūta pretruna. Visbiežāk krāsojums ir
divkrāsains, bet sarežģītākos uzdevumos lieto 3 vai 4 krāsas.
**(5) Piemēri.** LV.AMO.2014./15. 8. klase 4. uzd. ($10 \times 9$ tabulu nevar pārklāt ar
dotām figūrām — pierādīts ar šaha galdiņa krāsojumu); LV.AMO.2022A.9.5. (sākotnējais
$8 \times 8$ kvadrāta sadalījums šūnās $2 \times 2$, kas tiek lietots arī laukumu aprēķinos);
klasiskie uzdevumi par $4 \times 11$ taisnstūra pārklāšanu.


## 17. ParityInvariant

**(1)** No 5.–6. klases.
**(2)** Paritātes invariants.
**(3)** Parity invariant.
**(4) Apraksta.** Daudzos ģeometrijas uzdevumos par norisēm vai konfigurācijām atrod
lielumu, kura paritāte (pāra/nepāra) saglabājas pēc katras darbības. Ja sākotnējais lielums
ir pāra, bet vēlamais — nepāra (vai otrādi), prasītā transformācija nav iespējama. Ģeometriskos
uzdevumos paritāti bieži saista ar krāsoto/nekrāsoto rūtiņu skaitu, ar nogriežņu galu skaitu
(katram nogrieznim ir $2$ gali — pāra skaitlis) vai ar attālumu izmaiņām pēc katra
soļa.
**(5) Piemēri.** Klasisks rokasspiediena lemma: ja katrs no $m$ rūķīšiem ir pazīstams ar
nepāra skaitu citiem rūķīšiem, tad $m$ ir pāra (LV.AMO.2019.8.4); uzdevumos par $1 \times 5$
figūru sašķidrināšanu šaha galdiņā paritāte tiek skaitīta uz iekrāsotām rūtiņām (LV.AMO.2014./15.
8. klase).


## 18. SymmetryStrategy

**(1)** No 6.–7. klases.
**(2)** Simetrijas izmantošana (spēlēs un konstrukcijās).
**(3)** Symmetry strategy.
**(4) Apraksta.** Daudzos kombinatoriskās ģeometrijas un spēļu uzdevumos otrais (vai
pirmais) spēlētājs uzvar, atbildot uz pretinieka gājieniem simetriski — vai nu attiecībā pret
figūras centru, vai attiecībā pret simetrijas asi. Šī metode darbojas, kad figūrai piemīt centrāla
vai axsiāla simetrija. Tipisks plāns: ja figūrai ir centrs/ass, otrais spēlētājs garantē, ka pēc
viņa gājiena situācija paliek simetriska — līdz ar to viņš vienmēr var atbildēt, ja pretinieks
var iet. Ne-ģeometriskās spēlēs simetrija parādās arī kā skaitļu sadalīšana pa pāriem.
**(5) Piemēri.** LV.AMO.2019.8.2 (spēle $6 \times 6$ tabulā ar simetriju pret centru — uzvar
otrais spēlētājs); klasiskie AMO 6.–7. klases uzdevumi par riņķa sadalīšanu $16$ daļās;
LV.AMO.2022B.12.5. (līdzīga simetrijas izmantošana lielākiem tabulām).


## 19. PigeonholePrinciple

**(1)** No 6.–7. klases.
**(2)** Dirihlē princips.
**(3)** Pigeonhole principle.
**(4) Apraksta.** Ja vairāk nekā $n$ objektus jāsadala $n$ grupās, tad vismaz vienā grupā ir
vairāk nekā viens objekts. Ģeometrijas kontekstā objekti var būt punkti, nogriežņi vai citi
elementi, savukārt grupas — kvadrāti, rindas, kolonnas, krāsu klases vai citas pēc iespējas
veiklīgi izvēlētas īpašības. Bieži lieto kopā ar pierādīšanu no pretējā.
**(5) Piemēri.** Klasisks 16 punktu rūtiņu virsotnē uzdevums (3 punkti uz vienas taisnes
neeksistēs — Dirihlē); LV.NOL.2023.12.2 (sešu šahistu turnīrā vienmēr eksistē monohromā
trijstūra konstrukcija); LV.AMO.2022A.9.5 ($8 \times 8$ tabulu $1 \times 5$ taisnstūru kontekstā).


## 20. ProofByContradiction

**(1)** No 7. klases.
**(2)** Pierādījums no pretējā.
**(3)** Proof by contradiction.
**(4) Apraksta.** Lai pierādītu apgalvojumu $P$, pieņem, ka spēkā ir $\neg P$ (pretējais), un
no šī pieņēmuma izvada pretrunu ar dotajiem vai ar zināmiem faktiem. Ģeometrijas
uzdevumos bieži saistīts ar nemainības (invariantu) un Dirihlē principa lietošanu, kā arī
ar gadījumu apskates pamatošanu. Tipiski mērķi: pierādīt, ka kaut kas nav iespējams, vai
pierādīt, ka kaut kas obligāti ir.
**(5) Piemēri.** LV.AMO.2023.12.4 (par taisnstūri $2 \times 4$ rūtiņās — pieņemot pretējo,
nonāk pie pretrunas); LV.AMO.2024.12.5 (Jānītis mežā — pretrunas pierādījums caur
laukuma sakarību); plaši lietots ar Dirihlē principu (sk. iepriekš).


## 21. ReflectionAndCentralSymmetry

**(1)** No 8.–9. klases.
**(2)** Simetriska punkta atlikšana (atspoguļošana).
**(3)** Reflection / central symmetry construction.
**(4) Apraksta.** Lai izveidotu pārskatāmāku konfigurāciju, atliek figūras vai punkta
simetrisko attēlu pret kādu taisni vai punktu. Tas bieži pārveido sākotnējo uzdevumu
ekvivalentā, bet vienkāršākā uzdevumā, jo simetriski izveidotie objekti ir vienādi (vai
veido vienādsānu/vienādmalu trijstūrus). Klasiska tehnika problēmās ar ieliektu
četrstūri vai ar minimālu ceļu garumu.
**(5) Piemēri.** LV.AMO.2024.10.4. (kvadrāta $ABCD$ iekšienē atliek $E'$, lai $\triangle BEC$
būtu vienāds ar simetriskā konfigurācijā $\triangle AE'B$ — iegūst regulāru trijstūri);
LV.AMO.2023.10.3. otrais atrisinājums (punktu $B$ un $C$ atspoguļo pret taisni $AD$,
iegūst vienādmalu trijstūri).


## 22. CaseAnalysis

**(1)** No 5.–6. klases (vienkāršos veidos), no 7. klases pierādījumos.
**(2)** Gadījumu analīze (pilnā pārlase).
**(3)** Case analysis (exhaustive consideration).
**(4) Apraksta.** Ja uzdevuma nosacījumi pieļauj dažādas konfigurācijas (piemēram, kurš
no leņķiem ir virsotnes leņķis vienādsānu trijstūrī, vai punkts atrodas konkrētā vai pretējā pusē
no taisnes), risinājumu sadala vairākos gadījumos un apskata katru atsevišķi. Svarīgi ir
pamatot, ka apskatīti visi iespējamie gadījumi un ka citu nav. Bieži lieto kopā ar simetriju —
ja divi gadījumi ir savstarpēji simetriski, var apskatīt tikai vienu.
**(5) Piemēri.** LV.NOL.2009./10. 8. klase 6. uzd. / LV.NOL.2022.8.3. (vienādsānu trijstūris ar
$\sphericalangle ABC = 20^\circ$: trīs iespējamie virsotņu izkārtojumi, katrs apskatīts atsevišķi);
LV.AMO.2024.11.2 (gadījumi pēc punktu skaita); klasiski LV.SOL un LV.NOL uzdevumi
par taišņu krustošanos plaknē.


## 23. CountingByDoubleCounting

**(1)** No 7. klases.
**(2)** Divkārša ieskaitīšana (kombinatoriski ģeometriskos uzdevumos).
**(3)** Double counting.
**(4) Apraksta.** Vienu un to pašu lielumu (piemēram, punktu un nogriežņu pāru skaitu,
incidenču skaitu starp figūrām vai virsotnēm) ieskaita divos dažādos veidos, iegūstot
vienādību. Tipiska forma — rokasspiedienu lemma: grafā summa par visu virsotņu pakāpēm
ir $2 \cdot |E|$, tāpēc nepāra pakāpes virsotņu skaits ir pāra. Ģeometrijas uzdevumos
bieži saistīts ar nogriežņu galu skaitu, krustojumu skaitu, figūras virsotņu saskaiti.
**(5) Piemēri.** LV.AMO.2019.8.4. (rūķīšu drauguzību grafā — kāpēc nevar būt 7 rūķīši, no
kuriem katram ir 1 draugs); klasiski uzdevumi par $n$ taišņu krustpunktu skaita formulu un par
plaknes sadalīšanu daļās.


## 24. EquilateralTriangleConstruction

**(1)** No 8. klases.
**(2)** Vienādmalu (regulāra) trijstūra konstruēšana ārpus zīmējuma.
**(3)** Equilateral triangle augmentation.
**(4) Apraksta.** Pie dota nogriežņa pievelk vienādmalu trijstūri (vai vairākus tādus
trijstūrus pa virkni). Tas rada vienādus malu garumus un $60^\circ$ leņķus, kurus var izmantot,
lai pierādītu kāda cita objekta vienādmalu trijstūra īpašības vai lai pielietotu trijstūra
nevienādību garām figūrām. Bieži tiek izmantots arī gadījumā, kad konfigurācijā parādās
$30^\circ$, $60^\circ$ vai $120^\circ$ leņķi.
**(5) Piemēri.** LV.NOL.2009./10. 8. klase 6. uzd. (pie vienādsānu trijstūra $ABC$ ar
$\sphericalangle ABC = 20^\circ$, kur $AB = BC$, pievelk vēl divus tādus pašus trijstūrus, iegūstot
vienādmalu trijstūri $ABE$, no kā $3 \cdot AC > AB$); LV.AMO.2024.10.4. (vienādmalu
trijstūra konstruēšana ar simetriskā punkta palīdzību kvadrātā).


## 25. AngleAtCenterAndCircumference

**(1)** No 9. klases (parasti otrās puses tēma).
**(2)** Centra leņķis un ievilkts leņķis, $30^\circ$–$60^\circ$–$90^\circ$ taisnleņķa trijstūra īpašības.
**(3)** Inscribed angle and special right triangles.
**(4) Apraksta.** Riņķa līnijas centra leņķis ir divreiz lielāks par to pašu loku skaitošo
ievilkto leņķi (ja vēl nav apgūts pilnā mērā, tad spēkā speciālgadījums: trijstūris, kas balstīts
uz diametra, ir taisnleņķa). Taisnleņķa trijstūrī mediāna, vilkta pret hipotenūzu, ir vienāda
ar pusi no hipotenūzas (iet caur centru ap trijstūri apvilktajā riņķa līnijā). Taisnleņķa
trijstūrī ar šaurleņķi $30^\circ$ katete pret šo leņķi ir puse no hipotenūzas. Šīs sakarības bieži
parādās konfigurācijās ar vienādu malu summām un perpendikuliem.
**(5) Piemēri.** LV.AMO.2024.12.4. (taisnleņķa trijstūra mediāna pret hipotenūzu ir
$\tfrac{1}{2}$ no $CD$, no kā $HM = BC$, kas ļauj parādīt paralelogramu $BCMH$);
LV.AMO.2023.10.3. (taisnleņķa trijstūrī $BED$ leņķis pret kateti, kas ir divreiz īsāka par
hipotenūzu, ir $30^\circ$); LV.AMO.2015./16. 9. klase 2. uzd. (katete pret $30^\circ$ leņķi).
