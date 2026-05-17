# Tipiskas kļūdas skaitļu teorijas spriedumos 5.–9. klases olimpiāžu uzdevumos

Šis dokuments apkopo tipiskākās kļūdas, kuras skolēni pieļauj, risinot skaitļu teorijas
(Domain:NT) uzdevumus Latvijas (LV.AMO, LV.NOL) un citu valstu junioru olimpiādēs.
Daudzas no šīm kļūdām nav saistītas ar tehnisku aritmētisku neuzmanību, bet ar loģisku
spriedumu nepilnīgumu, jēdzienu sajaukšanu vai metodes nepareizu pielietojumu — piemēram,
nepareizu dalāmības pazīmes lietojumu, skaitļu kopas neievērošanu (naturāli pret veseliem),
nepilnīgu atlikumu pārlasi modulārajā aritmētikā vai sadalīšanas reizinātājos veikšanu, kad
priekšnoteikums (savstarpēji pirmskaitļi, veseli reizinātāji) nav ievērots. Bieži vien skolēns
iegūst pareizu skaitlisko atbildi, bet risinājums nav uzskatāms par pilnvērtīgu pierādījumu.


## 1. NonCoprimeFactorDivisibility

**(1)** No 6.–7. klases.
**(2)** Dalāmība ar reizinātāju, kas nav savstarpēji pirmskaitļi.
**(3)** Divisibility by a non-coprime product.
**(4) Apraksts.** Skolēns no tā, ka skaitlis dalās ar $a$ un dalās ar $b$, secina, ka tas dalās
ar $a \cdot b$ — neievērojot, ka teorēma izpildās tikai tad, kad $a$ un $b$ ir savstarpēji
pirmskaitļi (LKD vienāds ar $1$). Piemēram, $18$ dalās gan ar $2$, gan ar $6$, bet nedalās
ar $12$. Tipiskākais šīs kļūdas variants — dalāmības pazīmes “konstruēšana” skaitlim $12$
kā “dalās ar $2$ un $6$”, lai gan pareizā pazīme būtu “dalās ar $3$ un $4$”. GRAMATA šo
īpaši uzsver kā kritisko nianci 2.12. nodaļā.
**(5) Piemēri.** GRAMATA 2.12.: $18$ dalās ar $2$ un $6$, bet nedalās ar $12 = 2 \cdot 6$ —
priekšnoteikums “savstarpēji pirmskaitļi” netika izpildīts; LV.NOL.2011./12. 8. klase 1. uzd.
analoģijā — dalāmība ar $18$ pareizi tiek pamatota ar dalāmību ar $2$ un $9$ (ne ar $3$ un
$6$); klasisks olimpiāžu folkloras piemērs — pierādīt dalāmību ar $24$: ja kāds saka “dalās
ar $4$ un $6$”, tas nav pietiekami, jo $\text{LKD}(4,6) = 2 \neq 1$; pareizi būtu “dalās ar $3$
un $8$” (kā LV.NOL.2022.12.4 atrisinājumā par $p^4 - 1$ dalāmību ar $240 = 3 \cdot 5 \cdot 16$).


## 2. UnstatedNumberSetAssumption

**(1)** No 7.–8. klases.
**(2)** Nenorādīts pieņēmums par skaitļu kopu (naturāli/veseli/racionāli).
**(3)** Implicit assumption about the number set.
**(4) Apraksts.** Skolēns sadala skaitli reizinātājos, neievērojot, vai uzdevums atļauj negatīvus
veselos skaitļus. Tipiska situācija: vienādojums $(x-a)(y-b) = N$ veselos skaitļos pieprasa
uzskaitīt visus sadalījumus, ieskaitot $N = (-1) \cdot (-N) = (-2) \cdot (-N/2) \ldots$, bet skolēns
parasti atrod tikai pozitīvos pārus. Pretējais variants: ja uzdevumā prasīts atrast naturālu
atrisinājumu, bet skolēns iekļauj negatīvas vērtības — vai aizmirst, ka $0$ nav naturāls
skaitlis. Šīs kļūdas pamatcēlonis ir nepietiekama uzmanība uzdevuma formulējumam un
piezīmēm par skaitļu kopām, ko Latvijas olimpiāžu materiālos īpaši uzsver GRAMATA.
**(5) Piemēri.** GRAMATA 3.4. uzdevums par $(x-2)(y-2) = 4$ veselos skaitļos — pavisam ir
$6$ derīgi pāri, jo $4 = 1 \cdot 4 = 2 \cdot 2 = (-1) \cdot (-4) = (-2) \cdot (-2) = 4 \cdot 1 = (-4) \cdot (-1)$;
GRAMATA piezīme tieši brīdina, ka “spriedumu par skaitļa sadalīšanu reizinātājos var veikt
tikai tad, ja zināms, ka abi reizinātāji ir veseli skaitļi”; LV.AMO.2022B.9.2 ($x > y > 3$
nosacījums) — bez šī ierobežojuma, izteiksme $(xy-9)(x-y)$ varētu būt negatīva un
secinājums neizpildītos.


## 3. IncompleteResidueCases

**(1)** No 8.–9. klases.
**(2)** Nepilna atlikumu pārlase modulārajā aritmētikā.
**(3)** Incomplete case analysis modulo $m$.
**(4) Apraksts.** Lai pierādītu, ka kāda izteiksme nedalās ar $m$ (vai vienmēr dalās), jāpārbauda
visi $m$ iespējamie atlikumi mainīgajam pēc $\bmod m$. Skolēns bieži pārbauda tikai dažus
gadījumus (piem., $n$ pāra un $n$ nepāra), aizmirstot, ka pa moduļa $5$ jāpārbauda visi pieci
atlikumi $0, 1, 2, 3, 4$. Cita variants — pārbauda atlikumus pēc nepareiza moduļa: ja jāpierāda
dalāmība ar $9$, bet skolēns pārbauda tikai $\bmod 3$ atlikumus. Trešais variants — pārbauda
tikai daļu no nepieciešamajiem moduļiem, ja dalāmība pieprasa vairākus.
**(5) Piemēri.** LV.NOL.2022.12.4 ($p^4 - 1$ dalāmība ar $240$ — autoram jāpārbauda visi $4$
atlikumi $1, 2, 3, 4$ pa moduļa $5$; ja kādu izlaiž, pierādījums nav pilnvērtīgs); LV.NOL.2023.11.4
(otrā risinājuma variantā par $x(x+1) \pmod 9$ — uzskaita visus $9$ atlikumus $0, 1, \ldots, 8$;
ja izlaistu kādu, varētu trūkt pretrunas); LV.NOL.2021.10. klase ($n^2 - n + 36$ pēdējais
cipars — jāuzskaita visi $10$ pēdējie cipari, lai redzētu, ka nevienā gadījumā tas nav $0$ vai $5$).


## 4. WrongDivisibilityRule

**(1)** No 5.–6. klases.
**(2)** Nepareizi formulēta vai lietota dalāmības pazīme.
**(3)** Misstating a divisibility rule.
**(4) Apraksts.** Skolēns sajauc dalāmības pazīmes vai pielieto tās nepareizi: piemēram,
“dalāms ar $4$, ja pēdējais cipars dalās ar $4$” (pareizi — ja pēdējo divu ciparu skaitlis dalās
ar $4$); “dalāms ar $7$, ja ciparu summa dalās ar $7$” (pazīme ar ciparu summu darbojas tikai
$3$ un $9$); “dalāms ar $11$, ja ciparu summa dalās ar $11$” (pareizi — ja ciparu summa pa
nepāra un pa pāra pozīcijām starpība dalās ar $11$). Bieži skolēni paši “izgudro” pazīmes,
kas tā arī nav patiesas.
**(5) Piemēri.** Klasiska kļūda LV.NOL un LV.AMO 5.–6. klases uzdevumos par dalāmību ar $4$:
piem., $\overline{a543b}$ — daži skolēni pārbauda tikai $b$, lai gan jāpārbauda pāra ciparu
skaitlis $\overline{3b}$ (no GRAMATA 2.12. uzdevuma); $\overline{abcabc}$ dalāmība ar $7$ —
nepareiza pazīme būtu “katra trijnieka ciparu summa”, pareizi — izmantot $\overline{abcabc}
= 1001 \cdot \overline{abc}$ un $1001 = 7 \cdot 11 \cdot 13$ (LV.SOL.2011./12. 7. klase);
LV.NOL.2025 piezīme — dalāmība ar $15$ pārbaudāma kā $3$ un $5$, ne kā “dalāms ar $3$ un
nepāra cipars beigās”.


## 5. PrimeOnePointConfusion

**(1)** No 5.–6. klases.
**(2)** Skaitļa $1$ uzskatīšana par pirmskaitli vai $2$ izlaišana no pirmskaitļiem.
**(3)** Confusing 1, or omitting 2, as a prime.
**(4) Apraksts.** Pirmskaitļa definīcija: naturāls skaitlis, kuram ir tieši divi dažādi dalītāji
($1$ un pats skaitlis). Skaitlis $1$ NAV pirmskaitlis, jo tam ir tikai viens dalītājs. Skolēni
mēdz: (a) iekļaut $1$ pirmskaitļu sarakstā, kas noved pie nepareizām atrisinājumiem; vai
(b) aizmirst, ka $2$ ir vienīgais pāra pirmskaitlis, un to izlaist (piem., uzdevumos par “divu
pirmskaitļu summu”). Latvijas materiālos GRAMATA tieši brīdina par neprecīzu pirmskaitļa
definīciju (“tikai divi dalītāji — pats skaitlis un $1$”), kas neizslēdz $1$.
**(5) Piemēri.** GRAMATA piezīme 22. uzdevumā par skaitļa $50$ izteikšanu kā divu
pirmskaitļu summu — autors brīdina par neprecīzu definīciju; ja skolēns iekļautu $1$ kā
pirmskaitli, viņš pievienotu nepareizu sadalījumu $50 = 1 + 49$ (lai gan $49 = 7^2$ arī nav
pirmskaitlis); LV.AMO.2022A.5.4 (Laine un Raimonds — divciparu pirmskaitļi ar pirmskaitļa
cipariem; skolēni, kas $1$ uzskata par pirmskaitli, varētu pievienot nepareizu skaitli, lai gan
$1$ pat nav viencipara dalītāju struktūrā); klasisks Goldbaha tipa uzdevums “katrs pāra
skaitlis $> 2$ kā divu pirmskaitļu summa” — ja izlaiž $2$ no pirmskaitļu saraksta, summas
kā $5 = 2 + 3$ tiek aizmirstas.


## 6. ConfusingDivisorAndMultiple

**(1)** No 5.–6. klases.
**(2)** “Dalītāja” un “dalāmā” sajaukšana.
**(3)** Confusing divisor and multiple.
**(4) Apraksts.** Skolēni, īpaši piektklasnieki, sajauc terminus “dalītājs” un “dalāmais”
(arī “daudzkārtnis”). Skaitļa $12$ dalītāji ir $1, 2, 3, 4, 6, 12$, savukārt $12$ dalāmie (vai
daudzkārtņi) ir $12, 24, 36, \ldots$ Šī kļūda var izpausties arī kā “dalāmā” formulas
neuzmanība vienādojumos: piemēram, $b$ dalās ar $c$ nozīmē, ka pastāv $k$ tāds, ka
$b = kc$ (tātad $c$ ir dalītājs, $b$ ir dalāmais). Bieži kļūda parādās uzdevumos par
mazāko kopīgo dalāmo (MKD) un lielāko kopīgo dalītāju (LKD), kuri tiek sajaukti savā
starpā.
**(5) Piemēri.** Klasisks olimpiāžu uzdevums “atrast naturālu skaitli, kuram ir tieši $12$
dalītāji” — skolēns var sajaukt, ka jāatrod skaitlis ar tieši $12$ dalāmajiem, kas ir bezgalīgi
daudz (jebkurš skaitlis); GRAMATA uzdevums par MKD un LKD lietojumu “divu veidu
objektu komplektēšanā” — sajaucot dalāmo ar dalītāju, atbilde sanāk principiāli citāda;
LV.NOL.5. klases uzdevumi par “lielāko skaitli, kas ir gan dalītājs $36$, gan $48$”.


## 7. FactoringWithoutIntegerCondition

**(1)** No 8.–9. klases.
**(2)** Sadalīšana reizinātājos bez veselu skaitļu nosacījuma.
**(3)** Factoring without ensuring integer factors.
**(4) Apraksts.** Sadalot vienādojumu reizinātājos, lai pielietotu dalāmības argumentu,
jāievēro, ka abi reizinātāji ir veseli skaitļi (vai vismaz, ka pats argumentācijas tips to atļauj).
Piemēram, no $ab = N$ ar $N$ veselu nevar tieši secināt, ka $a$ un $b$ ir veseli, ja vien tas
nav iepriekš dots vai pierādīts. GRAMATA šo brīdinājumu izvirza tieši ($x-2)(y-2) = 4$
uzdevumā: “Spriedumu par skaitļa sadalīšanu reizinātājos var veikt tikai tad, ja zināms, ka
abi reizinātāji ir veseli skaitļi.” Bez šī nosacījuma būtu bezgalīgi daudz “atrisinājumu”.
**(5) Piemēri.** Klasisks gadījums no LV.AMO un Krievijas olimpiādēm: vienādojums $xy + x + y
= 100$ — pārveido par $(x+1)(y+1) = 101$, un tikai tāpēc, ka $x, y$ veseli, $(x+1)(y+1)$
ir veseli, un $101$ ir pirmskaitlis, ir maz iespējamību; ja nebūtu nosacījuma par veseliem,
risinājumu būtu bezgalīgi daudz; LV.AMO.2024.10.1 (sadala $n(n^3 - 2n^2 - n + 2) = 0$ un
secina, ka $-2$ dalās ar $n$ — tas pareizi tikai tāpēc, ka $n$ ir naturāls); GRAMATA 2.13.
piemēri par $(x-y)^2 = 6xy + 7$ — risinājums balstās uz to, ka $x, y$ ir naturāli un izteiksme
ir naturāla skaitļa kvadrāts.


## 8. WrongDivisibilityDirection

**(1)** No 8.–9. klases.
**(2)** Dalāmības “virziena” sajaukšana.
**(3)** Confusing direction of divisibility.
**(4) Apraksts.** Skolēns sajauc apgalvojumus “$a$ dalās ar $b$” un “$b$ dalās ar $a$”, vai pielieto
implikāciju nepareizā virzienā. Pareizi: ja $p$ — pirmskaitlis un $p \mid ab$, tad $p \mid a$ vai
$p \mid b$ (Eiklīda lemma). Šis fakts NEIZPLDĀS, ja $p$ nav pirmskaitlis: piemēram, $6 \mid
4 \cdot 9 = 36$, bet $6 \nmid 4$ un $6 \nmid 9$. Cita kļūda — pielietot dalāmības “tranzitivitāti”
greizi: ja $a \mid b$ un $b \mid c$, tad $a \mid c$ (tas ir pareizi), bet skolēni mēdz to izmantot
nepareizajā secībā.
**(5) Piemēri.** Klasisks pretpiemērs Eiklīda lemmai bez pirmskaitļa nosacījuma: $4 \cdot 9 = 36$
dalās ar $6$, bet ne $4$, ne $9$ atsevišķi nedalās ar $6$; LV.NOL.2021.11.kl. par $a^2 + b$
pirmskaitlību — argumentācija būtiski balstās uz to, ka tieši pirmskaitlis $p$ dala $ab+1$ un
$a+b$ (ne otrādi); GRAMATA piezīmes par pakāpju īpašībām — $2^a$ dalāmība ar $3$ atkarīga
no $a$ paritātes, bet skolēns mēdz pierakstīt apgriezto secinājumu.


## 9. CarelessModularComputation

**(1)** No 8.–9. klases.
**(2)** Neuzmanīga aritmētika ar atlikumiem.
**(3)** Careless modular arithmetic.
**(4) Apraksts.** Modulārās aritmētikas paliekā kļūdas: nepareizi sareizināti atlikumi, izmantotas
īsinātās formulas, ko nedrīkst (piemēram, mēģinājums “atcelt” reizinātāju kongruencē, kad
tas nav savstarpēji pirmskaitlis ar moduli), vai nepareizi noteiktas pakāpes atlikumi.
Tipisks gadījums: skolēns pareizi nosaka, ka $2^2 \equiv 1 \pmod 3$, bet pēc tam nepareizi
secina, ka $2^a \equiv 1 \pmod 3$ visiem $a$, neredzot atšķirību starp pāra un nepāra $a$.
Cits variants: kongruence $a \equiv b \pmod m$ nedrīkst tikt “dalīta” ar $k$, ja $\text{LKD}(k, m)
\neq 1$.
**(5) Piemēri.** LV.AMO.2023.12.5 (uzdevumā par $3 \cdot 2^{24}$ dalītājiem — autors korekti
nodala $a$ pāra un nepāra gadījumus: $2^{2k} \equiv 1 \pmod 3$ un $2^{2k+1} \equiv 2 \pmod 3$;
ja skolēns to izlaistu, viņš secinātu, ka visi $2^a$ dalītāji dod $1$ vai visi dod $2$, kas ir nepareizi);
LV.NOL.2023.11.4 (otrā risinājuma variantā skolēns nepareizi secinātu $x(x+1) \equiv 2 \pmod 9$,
ja kopētu pareizinājumu nepareizi); klasiska kļūda — pakāpe $7^{2025} \pmod {10}$:
skolēns var aizmirst, ka $7^4 \equiv 1 \pmod {10}$ (periods $4$), un nokļūt pie nepareizā
pēdējā cipara.


## 10. ExampleInsteadOfProof

**(1)** No 5.–6. klases.
**(2)** Konkrēts piemērs vietā vispārīga pierādījuma.
**(3)** Example instead of universal proof.
**(4) Apraksts.** Šī ir uzdevuma struktūras kļūda, kas īpaši izteikti parādās skaitļu teorijā.
Uzdevumos formā “Pierādi, ka visiem naturāliem $n$ izpildās ...” skolēns parāda dažus
konkrētus piemērus (piem., pārbauda $n = 1, 2, 3$) un secina, ka apgalvojums izpildās
vispārīgi. Tāpat: uzdevumā “Vai noteikti...?” pozitīva atbilde prasa vispārīgu pierādījumu,
bet negatīva pietiek ar pretpiemēru; uzdevumā “Vai iespējams...?” otrādi. Skolēni mēdz
sajaukt šos uzdevumu tipus un sniegt piemēru tur, kur vajadzīgs pierādījums.
**(5) Piemēri.** GRAMATA uzdevums “Vai vienmēr divu naturālu skaitļu summa $\overline{ab}
+ \overline{ba}$ dalās ar $11$?” — pozitīvā atbilde prasa pierādījumu $\overline{ab} +
\overline{ba} = 11(a+b)$; nepietiek ar “$12 + 21 = 33 = 3 \cdot 11$”; LV.AMO.2018.kl. tipa
uzdevums “pierādīt, ka katrs nepāra pirmskaitlis ir formā $4k \pm 1$” — vajag vispārīgu
spriedumu, nevis pārbaudi $p = 3, 5, 7, 11$; LV.NOL.2022.12.4 ($p^4 - 1$ dalāmība ar $240$ —
nepareizs risinājums būtu “pārbaudīsim $p = 7, 11, 13$ un redzēsim, ka dalās”, kas nav
pilnvērtīgs pierādījums vispārīgam apgalvojumam).


## 11. MissingBoundOrExample

**(1)** No 6.–7. klases.
**(2)** Trūkst piemērs vai trūkst novērtējums optimizācijas uzdevumā.
**(3)** Missing the example or the bound in optimization problems.
**(4) Apraksts.** Skaitļu teorijas uzdevumi “Kāds ir lielākais/mazākais skaitlis ar īpašību...”
prasa divus soļus: (a) konkrētu piemēru, kurā prasītā vērtība tiek sasniegta; (b) pamatojumu,
ka labāku vērtību sasniegt nav iespējams. Skolēni bieži aprobežojas ar vienu no šiem
soļiem. Tipiska variants: uzrakstīt piemēru un teikt “tas ir lielākais” bez argumenta, kāpēc
lielāks nav iespējams. Vai otrādi — pierādīt augšējo robežu, neuzrādot konkrētu piemēru,
kas to sasniedz.
**(5) Piemēri.** LV.AMO.2024.10.3 (mazākā $n$ vērtība, lai katrs cipars no $0$ līdz $9$ parādītos
kā pāra summas pēdējais cipars — autors abus soļus veic: pirmkārt, ar nevienādību $n(n-1)/2
\geq 10$ iegūst $n \geq 5$, tad ar paritātes argumentu izslēdz $n = 5$, beigās uzrāda piemēru
$\{1, 2, 3, 4, 5, 6\}$ ar $n = 6$); LV.AMO.2022A.5.4 (lielākais divciparu pirmskaitlis ar
pirmskaitļa cipariem — autors pārbauda $77, 75, 73$ un pamato, ka pirmie divi nav
pirmskaitļi); klasisks GRAMATA tipa uzdevums “Kāds ir mazākais sešciparu skaitlis no cipariem
$0, 1, 2, 3$, kas dalās ar $9$?” — vajag gan piemēru ($100233$), gan pamatojumu, ka mazāks
neder.


## 12. WrongDigitSumRange

**(1)** No 5.–6. klases.
**(2)** Nepareizi noteikts ciparu summas iespējamais diapazons.
**(3)** Wrong range for digit sum.
**(4) Apraksts.** Risinot uzdevumus, kur ciparu summa ir mainīgais lielums (parasti dalāmības
ar $3$ vai $9$ kontekstā), skolēni mēdz nepareizi noteikt ciparu summas iespējamo diapazonu.
$k$-ciparu skaitļa ciparu summa ir intervālā $[1, 9k]$ (pirmajam ciparam jābūt vismaz $1$),
nevis $[0, 9k]$. Bieži tiek aizmirsts, ka pirmais cipars nav nulle: piem., $4$-ciparu skaitļa
mazākā ciparu summa ir $1$ (no $1000$), nevis $0$. Vai otrādi — uzdevumos par ciparu
permutācijām aizmirst, ka samainot ciparus, var iegūt skaitli, kas “sākas ar nulli”, kas
parasti nav atļauts.
**(5) Piemēri.** GRAMATA uzdevums par lielāko ciparu summu septiņciparu skaitlim, kas dalās
ar $8$ — autors izmanto, ka ciparu summa nepārsniedz $7 \cdot 9 = 63$; LV.AMO.2024.10.2
(par trīsciparu skaitļu ciparu summām — mazākā ir $1$ atbilstoši $100$, lielākā ir $27$ atbilstoši
$999$; ja skolēns ņemtu summu starp $0$ un $27$, kopu skaits Dirihlē principa lietošanai
sanāktu nepareizs); LV.SOL.2015./16. 5. klase 5. uzd. (lielākais piecciparu skaitlis ar dažādiem
cipariem, kas dalās ar $3$ — autors izmanto, ka pirmā cipara minimums ir $1$, nevis $0$, kad
meklē “mazāko atskaitāmo summu”).
