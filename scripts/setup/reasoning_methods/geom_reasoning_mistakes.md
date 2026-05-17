# Tipiskas kļūdas ģeometrijas spriedumos 5.–9. klases olimpiāžu uzdevumos

Šis dokuments apkopo tipiskākās kļūdas, kuras skolēni pieļauj, risinot ģeometrijas
uzdevumus Latvijas (LV.AMO, LV.NOL) un citu valstu junioru olimpiādēs. Daudzas no šīm
kļūdām nav saistītas ar tehnisko aritmētiku vai algebru, bet ar loģiku, atrisinājuma
struktūru un nepilnīgu spriedumu pamatojumu. Bieži vien skolēns iegūst pareizu skaitlisko
atbildi, bet risinājums nav uzskatāms par pilnvērtīgu pierādījumu — un šādas “puscentu” kļūdas
ir vērtīgi atpazīt un kontrolēt.


## 1. SkippingCaseAnalysis

**(1)** No 7.–8. klases.
**(2)** Trūkst gadījumu analīzes (apskata tikai vienu konfigurāciju).
**(3)** Skipping case analysis.
**(4) Apraksta.** Uzdevuma nosacījumi pieļauj vairākas ģeometriskas konfigurācijas, bet
skolēns apskata tikai vienu — visbiežāk to, kas viņam intuitīvi šķiet “tipiskā” aina. Tipisks
gadījums: vienādsānu trijstūrim dots viens leņķis, bet nav norādīts, vai tas ir virsotnes leņķis
vai pamata leņķis; trijstūrim dots, ka kāda mala ir garākā, bet zīmējumā tā ir attēlota kā īsākā;
punkts atrodas uz nogriežņa “iekšpusē” vai “pagarinājumā”. Korektā risinājumā jāuzskaita
visi iespējamie gadījumi un jāpārliecinās, ka katrā tiek pārbaudīta uzdevuma izpilde — vai arī
korekti jāpamato, kāpēc daži gadījumi automātiski izslēdzas.
**(5) Piemēri.** LV.NOL.2022.8.3 (platleņķa vienādsānu trijstūris ar $\sphericalangle ABC = 20^\circ$
— korekti jāapskata gadījumi $AB = AC$ un $BC = AC$, un atsevišķi jāpamato, ka virsotnes
leņķis $20^\circ$ neder, jo tad trijstūris nebūtu platleņķa); klasisks uzdevums “trijstūrī divas
malas ir vienādas un viena leņķis ir $\alpha$” — bieži tiek apskatīts tikai gadījums, kur dotais
leņķis ir pie vienādajām malām; LV.AMO.2023.10.3 (ieliekts četrstūris — jāspēj atšķirt
iekšējais un ārējais leņķis pie virsotnes $B$).


## 2. RelyingOnDiagramAppearance

**(1)** No 7. klases.
**(2)** Paļaušanās uz zīmējuma izskatu (“tas redzams no attēla”).
**(3)** Relying on the diagram’s appearance.
**(4) Apraksta.** Skolēns no zīmējuma “nolasa” kādu īpašību — piemēram, ka kāds punkts
atrodas uz nogriežņa, ka kāds leņķis ir taisns, ka kādas trīs taisnes krustojas vienā punktā,
ka divas malas ir vienādas vai paralēlas — un izmanto to risinājumā kā pierādītu faktu.
Tomēr zīmējums ir tikai skice; pierādījumā nedrīkst pamatoties uz to, kas “izskatās tā”.
Piezīme. Konkrēti riņķa līnijas centra atrašanās uz noteiktas taisnes, trīs taišņu vienā
krustpunktā vai punkta atrašanās uz noteiktas malas — visi ir spriedumi, kas jāpierāda.
**(5) Piemēri.** Klasiskās viltus “pierādījumus”, ka visi trijstūri ir vienādsānu (Robinsona
paradokss), kur kļūda ir pieņēmums, ka kāds palīgpunkts atrodas trijstūra iekšpusē, bet
patiesībā tas atrodas ārpusē; LV.NOL.2024.10.1 (uzdevumā par divām krustojošām riņķa
līnijām atkarībā no taisnes $t_1$ un $t_2$ novietojuma var rasties dažādas konfigurācijas, un
visā risinājumā nedrīkst izmantot, ka kāds punkts noteikti atrodas konkrētā pusē, ja tas nav
pierādīts); LV.AMO.2024.12.4 (uzdevumā par ievilktu četrstūri — kur atrodas $H$ attiecībā
pret pārējiem punktiem, jāpamato, nevis jāpieņem no zīmējuma).


## 3. ConflatingPropertyAndCriterion

**(1)** No 8.–9. klases.
**(2)** Sajaukt īpašību ar pazīmi.
**(3)** Confusing property with characterization (criterion).
**(4) Apraksta.** Skolēns lieto īpašības apgriezto apgalvojumu kā pazīmi, lai gan apgrieztais
apgalvojums nav patiess. Tipiskākais piemērs: katra paralelograma diagonāle to sadala divos
vienādos trijstūros, bet apgriezti — ja četrstūra diagonāle to sadala divos vienādos trijstūros,
tad četrstūris nav noteikti paralelograms. Tāpat: vienādsānu trijstūrī bisektrise no virsotnes ir
arī mediāna, bet apgriezti — ja trijstūrī kāda bisektrise sakrīt ar mediānu, jāpierāda papildus,
ka trijstūris tiešām ir vienādsānu. Šīs kļūdas mazo klašu kontekstā parādās, jo skolēni vēl tikai
mācās atšķirt jēdzienus “īpašība” un “pazīme”.
**(5) Piemēri.** Klasisks pretpiemērs no Latvijas programmas (skat. 8.5. temata aprakstu):
četrstūris ABCD ar $\sphericalangle A = \sphericalangle D$ — vai tas ir paralelograms? Skolēns,
zinot, ka paralelogramā $\sphericalangle A = \sphericalangle D$ neizpildās (vai dažreiz izpildās
trapecēs), var nekorekti secināt, ka tas ir vai nav paralelograms; uzdevumi ar romba vai
taisnstūra atpazīšanu pēc dažām, bet nepilnīgām īpašībām.


## 4. WrongAngleDecomposition

**(1)** No 7. klases.
**(2)** Nekorekta leņķa “sadalīšana” vai “saskaitīšana”.
**(3)** Incorrect angle addition.
**(4) Apraksta.** Skolēns pieraksta vienādību $\sphericalangle XOZ = \sphericalangle XOY + \sphericalangle YOZ$,
bet patiesībā stars $OY$ neatrodas leņķa $XOZ$ iekšpusē — tāpēc šī vienādība nav spēkā.
Bieži kļūda parādās, kad uzdevumā ir vairāki bisektrises, augstuma vai mediānas nogriežņi,
un to savstarpējais novietojums nav skaidrs no dotā. Tāpat — ja leņķis ir ārējais leņķis pie
virsotnes, tas summējams ar atbilstošu iekšējo leņķi līdz $180^\circ$, nevis $360^\circ$, kā
dažreiz mēdz kļūdaini darīt. Ja leņķis ir “refleksīvs” (lielāks par $180^\circ$), tas vienmēr
jāņem vērā atsevišķi.
**(5) Piemēri.** LV.AMO.2023.10.3 (ieliekts četrstūris $ABCD$ ar $\sphericalangle ABC$ ārpusē
$7\alpha$ — kļūda būtu pieņemt, ka iekšējais leņķis $\sphericalangle ABC = 7\alpha$, lai gan
patiesībā iekšējais leņķis ir $360^\circ - 7\alpha$ vai $\sphericalangle ABC = 7\alpha$ skaitā
kā ārējais — tāpēc paši autori pamato sprieduma korektumu, izmantojot, ka apkārt $B$ visi
četri leņķi summējas $360^\circ$); LV.NOL.2017./18. 7. klase 1. uzdevums (vairāku leņķu
summa pie paralēlām taisnēm — jāuzmanās, lai katrs leņķis tiktu pareizi sadalīts $\alpha$ un
$\beta$ komponentēs un nekas netiktu “divreiz ieskaitīts”).


## 5. UnjustifiedAuxiliaryLineExists

**(1)** No 8. klases.
**(2)** Palīglīnija/punkts tiek konstruēts, neparādot, ka tas patiešām eksistē.
**(3)** Unjustified auxiliary construction.
**(4) Apraksta.** Skolēns risinājumā saka: “Atliksim uz malas $BC$ punktu $X$ tā, ka
$BX = AB$” — un tālāk balstās uz konstrukciju, neparbaudot, vai šāds $X$ tiešām pieder
malai $BC$ (varbūt $AB > BC$ un punkts būtu jāatliek uz $BC$ pagarinājuma). Vai arī:
“Novelksim caur punktu $P$ taisni, paralēlu $AB$, kas krusto $CD$ punktā $Q$”, lai gan
$P$ atrodas tā, ka šāda paralēla taisne nemaz nekrusto $CD$. Korektā risinājumā palīgkonstrukcijas
eksistencei jābūt vai nu acīmredzamai, vai pamatotai. Īpaši nopietns šis aspekts kļūst, kad
konstrukcijas atrašanās vieta atkarīga no nezināmiem leņķiem vai garumiem.
**(5) Piemēri.** LV.AMO.2018./19. 7. klase 4. uzdevums ($AD = AB + CD$ — atliek $E$ uz
$AD$ ar $AE = AB$; šeit eksistence ir acīmredzama, jo $AB < AD$, un autors to pieklusē, bet
skolēnam līdzīgos uzdevumos to vajadzētu atzīmēt); LV.NOL.2020./21. 8. klase 5. uzdevums
($AD = AB + AC$ uz bisektrises — eksistence prasa, ka $AB + AC < AD$ vai cita atbilstoša
sakarība); konstrukcijas ar atspoguļošanu, kur jāpārbauda, vai atspoguļotais punkts patiešām
atrodas vajadzīgajā pusē.


## 6. AreaWithoutPosition

**(1)** No 6.–8. klases.
**(2)** Laukuma aprēķins, neņemot vērā punkta novietojumu.
**(3)** Area computed without checking point location.
**(4) Apraksta.** Aprēķinot laukumus pēc formulām vai sadalot figūras, skolēns var paņemt
nogriežņus ar “zīmi minus” vai uzskatīt, ka kāds laukums atskaitās, lai gan tas atrodas
ārpus dotās figūras. Otrs šīs kļūdas variants: tiek pieņemts, ka mediānas/diagonāles/bisektrises
krustpunkti atrodas figūras iekšpusē, lai gan platleņķa trijstūrim, piemēram, augstumu pamati
var atrasties ārpus malām. Trešais variants: aizmirst, ka augstums platleņķa trijstūrī jāvelk
pret malu vai tās pagarinājumu — pret pagarinājumu pamats var atrasties ārpus malas.
**(5) Piemēri.** Klasiska kļūda — aprēķinot trijstūra laukumu rūtiņu lapā, paņemt nogriežņa
projekciju nevis pašu augstumu (kas atrodas perpendikulāri); LV.AMO.2017./18. 8. klase
3. uzdevums (paralelogramā vidusnogriežņi rada trijstūrus — laukumi tiek aprēķināti pareizi,
jo katrs trijstūris atrodas pilnībā paralelograma iekšpusē, taču modificētā uzdevumā ar
diferencētiem punktiem viegli kļūdīties); šaurleņķa pret platleņķa trijstūra augstuma pamati.


## 7. FromSpecialToGeneral

**(1)** No 5.–7. klases (vienkāršos veidos), turpinās līdz 9. klasei.
**(2)** Vispārinājums no konkrēta piemēra (induktīvs pieņēmums bez pierādījuma).
**(3)** Hasty generalization from a special case.
**(4) Apraksta.** Skolēns uzzīmē konkrētu piemēru, pārbauda, ka tajā prasītā īpašība
izpildās, un secina, ka tā izpildās visos gadījumos. Ģeometrijā tas izpaužas kā uzdevuma
risinājums “ar konkrētiem skaitļiem” vai “ar konkrētu zīmējumu”: skolēns ņem, piemēram,
vienādmalu trijstūri ar malas garumu $1$, izrēķina prasīto un sniedz to kā vispārīgo atbildi.
Vai uzzīmē kvadrātu ar visām virsotnēm rūtiņās un secina, ka prasītais ir patiess vispārīgi.
Korektā risinājumā jāpierāda, ka īpašība izpildās jebkurai dotā tipa figūrai, nevis tikai
izvēlētajā piemērā. Šī kļūda nav tā pati, kas uzdevumiem “Vai eksistē...?”, kuros tieši pietiek
ar vienu piemēru.
**(5) Piemēri.** Klasiska kļūda LV.AMO.2017./18. 8. klase 3. uzd. tipa uzdevumos
(“Aprēķini četrstūra laukumu, ja paralelograma laukums ir $100$”) — skolēns var paņemt
konkrētu paralelogramu (piemēram, kvadrātu ar laukumu $100$) un saskaitīt vidējās
četrstūra laukumu rūtiņās, iegūstot pareizu atbildi, bet bez vispārīga pamatojuma; LV.NOL un
LV.AMO uzdevumi, kuros prasa pierādīt sakarību patvaļīgam trijstūrim/četrstūrim.


## 8. ProofByExampleForUniversalClaim

**(1)** No 5.–6. klases (kombinatoriskajā ģeometrijā).
**(2)** Piemērs vietā pierādījuma uzdevumā par “visiem” vai “noteikti”.
**(3)** Confusing example with proof in universal claims.
**(4) Apraksta.** Šī ir struktūras kļūda, kas saistīta ar uzdevuma jautājuma veidu.
Uzdevumos formā “Vai noteikti...?” vai “Vai vienmēr...?” pozitīva atbilde (“jā”) prasa
vispārīgu pierādījumu, savukārt negatīva atbilde (“nē”) prasa pretpiemēru. Skolēni bieži
sniedz vienu piemēru, kur īpašība izpildās, un secina, ka tā vienmēr izpildās — bet patiesībā
viens piemērs nav pierādījums vispārīgam apgalvojumam. Otrādi — uzdevumos “Vai
iespējams...?” pietiek ar vienu piemēru pozitīvas atbildes pamatošanai, taču negatīvai
atbildei vajadzīgs vispārīgs pierādījums.
**(5) Piemēri.** No olimpiāžu folkloras: “Pierādi, ka jebkurā $4 \times 4$ rūtiņu tabulā ar
$1, 2, 3, 4$ noteikti ir kāds taisnstūris” — piemērs ar vienu konkrētu tabulu nav pierādījums;
LV.AMO.2014./15. 8. klase 4. uzdevums ($10 \times 9$ pārklāšanai jāpierāda neiespējamība
vispārīgi ar krāsojuma invariantu, nevis “es mēģināju vairākus veidus, un nesanāca”);
uzdevums “Vai noteikti trijstūrī iekšējais punkts atrodas tuvāk vienai virsotnei nekā divām
malām?” — atbildei “jā” jāveic pierādījums, atbildei “nē” jāuzrāda pretpiemērs.


## 9. UpperBoundWithoutExample

**(1)** No 6.–7. klases.
**(2)** Norādīta tikai vērtība, bet nav parādīts piemērs (vai otrādi).
**(3)** Missing example or missing upper-bound proof in optimization problems.
**(4) Apraksta.** Uzdevumos veida “Kāds ir lielākais/mazākais...” risinājumam jābūt divām
daļām: (a) konkrēts piemērs, kurā prasītā vērtība tiek sasniegta; (b) pamatojums, ka labāku
vērtību sasniegt nav iespējams. Tipiska kļūda — uzrādīt piemēru un apgalvot, ka labāku
nevar atrast, vai arī pierādīt nevienādību, bet aizmirst parādīt, ka tā ir asa. Bieži vien
skolēni risinājumā “aizmirst” to pusi, kura viņiem šķiet acīmredzama. Ģeometrijā šī kļūda
parādās tādos uzdevumos, kā “Kāds mazākais skaits rūtiņu jāizkrāso, lai...”, “Kāds lielākais
skaits figūru var ietilpt...” un citos optimizācijas uzdevumos.
**(5) Piemēri.** LV.AMO.2022A.9.5 ($8 \times 8$ tabulā jāizkrāso vismaz $12$ rūtiņas, lai
nebūtu $1 \times 5$ neaizkrāsota; risinājumā ir abi soļi — gan zīmējums ar $12$ rūtiņām, gan
pamatojums, ka mazāks skaits nepietiek); LV.AMO.2023.12.4 ($2 \times 4$ un $2 \times 5$
taisnstūri); klasiski uzdevumi par maksimālu figūru skaitu, ko var izgriezt no dotās formas
(piemēram, LV.NOL.2014./15. 6. klase 2. uzdevums) — risinājumā parasti vajag uzrādīt
piemēru un krāsojuma invariantu kā ierobežojumu.


## 10. WrongTriangleSimilarityOrCongruence

**(1)** No 7.–9. klases.
**(2)** Nekorekti lietota vienādu vai līdzīgu trijstūru pazīme.
**(3)** Misapplied congruence/similarity criterion.
**(4) Apraksta.** Skolēns paziņo, ka divi trijstūri ir vienādi vai līdzīgi, atsaucoties uz “pazīmi”,
bet patiesībā vai nu pazīme ir nepareiza, vai arī tā ir lietota nepareizi. Tipiski kļūdu varianti:
(a) izmanto “neeksistējošo” pazīmi mlm tā vietā, kur mlm nedarbojas (piemēram, divām
malām un to nepretleņķim — gadījums “SSA”, kas neviennozīmīgi nosaka trijstūri);
(b) pareizi nosauc malas un leņķus, bet nepareizā secībā/atbilstībā — līdzīgo trijstūru
gadījumā tiek samainītas atbilstošās virsotnes; (c) vienkārši aizmirst pārbaudīt visus
pazīmes nosacījumus. Šī kļūda īpaši mēdz pielīgt taisnleņķa trijstūros, kur ir vienkāršāka
pazīme hℓ (hipotenūza–katete) un kur skolēni dažreiz lieto h$_1$h$_2$ vai cita formā.
**(5) Piemēri.** LV.AMO.2023.10.3 (trīs taisnleņķa trijstūri vienādi pēc hℓ — autori
korekti pārbauda gan hipotenūzas vienādību, gan šaurā leņķa vienādību); klasiska kļūda
LV.AMO.2009./10. 8. klase 4. uzdevumā par astoņstūri (jāuzmanās, kuri leņķi atbilst kuriem
— skolēni mēdz “sakopēt” pazīmi $\ell m\ell$ ar nepareizām atbilstošajām malām);
LV.NOL.2015./16. 9. klase 2. uzdevums ($\triangle BMN \sim \triangle CDN$ — līdzības
koeficients $\tfrac{1}{2}$ jāizseko līdz pareiziem secinājumiem par konkrēto malu attiecību.


## 11. MisuseOfMidpointOrParallel

**(1)** No 8.–9. klases.
**(2)** Nepareizi lietota trijstūra viduslīnijas vai paralelogramu pazīme.
**(3)** Misuse of midsegment / parallel-line criterion.
**(4) Apraksta.** Trijstūra viduslīnijas teorēma saka: ja $M$ un $N$ ir $AB$ un $AC$ viduspunkti,
tad $MN \parallel BC$ un $MN = \tfrac{1}{2} BC$. Apgrieztā teorēma saka: ja $MN \parallel BC$
un $M$ ir $AB$ viduspunkts, tad arī $N$ ir $AC$ viduspunkts. Skolēni bieži lieto tikai daļu no
sakarībām — piemēram, no $MN \parallel BC$ un $MN = \tfrac{1}{2} BC$ secinot, ka $M$ un $N$
ir viduspunkti (kas faktiski ir patiess, bet vajag norādīt, ka tas izriet no Talesa apgrieztās
teorēmas). Saistītas kļūdas: pieņemt, ka trapeces viduslīnija ir vienkārši “vidējais aritmētiskais”
no malām bez pamatojuma vai izmantot pazīmes “divas malas pa pāriem paralēlas” bez
pārbaudes, vai tās tiešām ir pretējās malas.
**(5) Piemēri.** LV.NOL.2025.10.3 (uzdevumā paralelograma pierādījumā tiek izmantots,
ka $2KC = AB = 2CL = KL$ un $AB \parallel KL$ — abi pretējie nosacījumi ir kritiski);
LV.AMO.2024.12.4 (taisnleņķa trijstūra mediāna pret hipotenūzu un secinājumi par paralelitāti
caur paralelogramu); klasiski uzdevumi par taisnstūra/paralelograma diagonāļu krustpunktu.


## 12. UnstatedDirectionAssumption

**(1)** No 7.–9. klases.
**(2)** Implicīts pieņēmums par punkta atrašanās virzienu (pretī, vienā pusē, starp utt.).
**(3)** Implicit positional assumption.
**(4) Apraksta.** Šī ir radniecīga kļūda Nr. 2, bet specifiska gadījumam, kad nepieciešami
ir vairāki konfigurācijas: punkts $E$ var atrasties uz nogriežņa $AB$ vai uz tā pagarinājuma;
punkts $C$ var atrasties vienā vai otrā pusē no taisnes $AB$; lokā “redzamais” leņķis var būt
no centra vai no rāmja pretējās puses. Ja uzdevums nepasaka, ka punkts atrodas konkrētā
pusē, risinājumā vai nu jāpamato attiecīgais novietojums, vai jāapskata abas iespējas.
Bieži šo kļūdu pieļauj uzdevumos par leņķu meklēšanu, kur ir vairāki krustojušies nogriežņi:
skolēns pieņem, ka divi nogriežņi krustojas “iekšpusē”, lai gan patiesībā tie krustojas uz
pagarinājumiem.
**(5) Piemēri.** LV.NOL.2017./18. 8. klase 2. uzdevums (no virsotnes $P$ velkta bisektrise
krusto $QR$ punktā $S$ — uzdevumā ir norādīts, ka $S$ atrodas uz malas, bet skolēnam
analoģiskos uzdevumos vajadzētu pārbaudīt, vai šāds krustpunkts vispār pieder pašai malai);
uzdevumi par krustojošām taisnēm taisnstūrī, kur taisne var krustot vai nu divas blakus
malas, vai divas pretējās malas — abi gadījumi var pieprasīt atsevišķu risinājumu.


## 13. CircularReasoning

**(1)** No 8.–9. klases.
**(2)** Riņķveida argumentācija (apgalvojuma pierādīšana ar to pašu).
**(3)** Circular reasoning.
**(4) Apraksta.** Skolēns pierādījuma sākumā pieņem, ka kāda īpašība izpildās, un beigās
nonāk pie šīs pašas īpašības. Ģeometrijā tas izpaužas kā: lai pierādītu, ka kāds nogrieznis ir
mediāna, tiek pieņemts, ka tas iet caur viduspunktu; vai lai pierādītu, ka trijstūris ir vienādsānu,
tiek pieņemts, ka divi leņķi ir vienādi (kas faktiski ir tieši tas, ko vajadzēja pierādīt). Vēl viens
variants: skolēns sāk ar to, ko vajag pierādīt, izdara pārveidojumus un nonāk pie patiesa
apgalvojuma (piem., $1 = 1$). Tas nav korekts pierādījums, ja vien visi pārveidojumi nav
ekvivalenti un netiek tieši pateikts, ka argumentācija notiek atpakaļgaitā.
**(5) Piemēri.** Klasisks neformālo riņķveida argumentu piemērs: “Trijstūris ir vienādsānu,
jo $\sphericalangle B = \sphericalangle C$. Bet $\sphericalangle B = \sphericalangle C$, jo
trijstūris ir vienādsānu.” Skolēni reti to dara tik nepārklāti, bet pastarpināti caur trim-četriem
spriedumiem var “noslēpt” riņķveida argumentāciju. Piemēram, LV.NOL.2017./18. 7. klase
1. uzdevumā par leņķu summu — ja skolēns iesāktu “pieņemsim, ka $\alpha + \beta$ ir
nezināmā summa, tad katrs leņķis ir...”, viņš nodalītu nezināmo un atrastu vērtību, taču
korekti — caur paralēlu taišņu īpašībām.


## 14. WrongAreaProportionality

**(1)** No 9. klases.
**(2)** Nekorekti lietota laukumu attiecība līdzīgos trijstūros vai sadalītās figūrās.
**(3)** Incorrect area ratio in similar figures or dissections.
**(4) Apraksta.** Līdzīgu trijstūru ar līdzības koeficientu $k$ malu attiecība ir $k$, bet
laukumu attiecība — $k^2$. Skolēni bieži kļūdās un izmanto $k$ tā vietā, lai izmantotu $k^2$
(vai otrādi). Cita variants: skolēns pieņem, ka, ja mala palielinās $2$ reizes, tad arī laukums
palielinās $2$ reizes, lai gan kvadrātam tā nav. Trešs variants: figūrai sadalītā daļā tiek
pielietota nepareiza laukumu attiecība — piemēram, trijstūra mediāna sadala to divos
vienlielos trijstūros, bet bisektrise to dara tikai īpašos gadījumos.
**(5) Piemēri.** Klasisks uzdevums no LV.AMO un IMO talkas: ja trijstūra mediāna sadala
to divos vienlielos trijstūros, kāda ir vidējās trijstūra augstuma un perimetra sakarība?
Skolēni mēdz lietot $k$ tur, kur jālieto $k^2$; LV.AMO.2017./18. 8. klase 3. uzdevumā par
paralelograma laukumu — pareizais arguments balstās uz to, ka mediāna sadala trijstūri
divos vienlielos trijstūros (ne uz līdzības koeficientu).


## 15. ConcludingFromZeroOrEdgeCase

**(1)** No 7.–9. klases.
**(2)** Pieņemt, ka degenerēts gadījums “neeksistē”, vai izlaist robežgadījumu.
**(3)** Missing degenerate or boundary case.
**(4) Apraksta.** Skolēns risina uzdevumu, pieņemot, ka konfigurācija ir “tipiskā” —
trijstūris nav degenerēts, punkts neatrodas uz nogriežņa galapunktiem, divas līnijas nav
paralēlas u.tml. — bet aizmirst pārbaudīt, vai uzdevumā nav arī degenerēti gadījumi, kuri
formāli atbilst nosacījumiem. Tipiski piemēri: vai prasītais izpildās arī tad, kad trijstūris
ir degenerēts (visi trīs punkti uz vienas taisnes)? Vai izpildās, kad četrstūris ir taisnstūris
(speciālgadījums paralelogramam)? Šī kļūda īpaši mēdz parādīties uzdevumos “Vai
noteikti...?”, kuros pretpiemēram var būt arī degenerēta konfigurācija.
**(5) Piemēri.** Klasisks gadījums: uzdevumā prasīts pierādīt sakarību, kas izpildās visiem
trijstūriem ar dotām īpašībām — bet ja viens no leņķiem ir taisns, kāds nogrieznis var
sakrist ar virsotni; uzdevumos par krustojošām taisnēm parasti pieņem, ka tās tiešām
krustojas (un nav paralēlas) — bet jāuzmanās, vai uzdevumā nav prasība analizēt arī tādu
gadījumu; trijstūra nevienādības robežgadījumu $a + b = c$, kas pieļauj degenerētu trijstūri,
parasti uzdevumos izslēdz.
