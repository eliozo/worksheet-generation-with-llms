

Grafu teorijas pamati
=====================================================================




Ievaduzdevumi
-------------------------------------------------------------------------




*Divi viegli uzdevumi, lai iesildītos un atcerētos grafu teorijas pamatidejas. Lūgums problēmas risināt ar nelielu sarunu stilu ― ja vēlies, izmanto fantāziju no Arcane pasaules!*




Piltover pilsētā ir 6 tilti, kas savieno 4 dažādas salas. Vai vienmēr būs vismaz viena sala, pie kuras pienāk vismaz 3 tilti?
(sk. NEW)




Viktors vēlas pavadīt Jinku ekskursijā pa pilsētas automatizēto tramvaja tīklu. Ja katrā pieturā uz tāfeles uzrakstīts, cik tramvaja līniju no šīs pieturas iet tālāk, vai kopā visu pieturu norādītie skaitļi vienmēr būs pāra skaitlis?
(sk. NEW)




Teorijas pārskats
-------------------------------------------------------------------------




**Teorēma:** Grafā var pētīt virsotnes (:math:`v`), šķautnes (:math:`e`), un dažādas īpašības, piemēram, virsotņu pakāpes (cik šķautņu pieiet pie katras). Grafu var zīmēt arī plaknē (par planāru sauc tad, ja to var izdarīt bez šķautņu krustošanās). Svarīgi ir meklēt ceļus, ciklus, pa kuriem iespējams pārvietoties, un īpašu grafu veidu – kokus (grafi bez cikliem un savienotiem mezgliem). Dažreiz noder arī "roku paspiešanas lemmas" – kopējais visu virsotņu pakāpju skaitlis vienmēr dalās ar divi.




Uzdevumi ar pieaugošu grūtību
-------------------------------------------------------------------------




*Galvenās darba daļas uzdevumi: īsti piemēri, pierādījumi, optimizācijas uzdevumi. Progresīvi sarežģītāki, daži var būt saistīti ar Arcane pasaules pilsētvides problēmām!*




Vai pa apli var uzrakstīt skaitļus<br /> (A) :math:`0, 1, ..., 9`; <br /> (B) :math:`0, 1, ..., 13`; <br /> tā, lai katri divi blakus esoši skaitļi atšķirtos par :math:`3`, :math:`4` vai :math:`5`?
(sk. LV.AMO.2022B.8.4)




Arcane rajonā Jayce zīmē grafu ar 8 virsotnēm, katrai no kurām ir nepāra pakāpe. Vai tas ir iespējams? Pamato!
(sk. NEW)




Sešdesmit pensionāri katru dienu sociālajā tīklā sarakstās savā starpā. Katrs kungs sarakstās ar tieši :math:`17` dāmām, bet katra kundze sarakstās ar tieši :math:`13` kungiem. Cik šeit ir kungu un cik – kundžu?
(sk. LV.AMO.2011.6.2)




Vi ir izplānojis ķēdes pastu Jaunajā Piltoverā. Vi vēlas katrai mājai izsūtīt vēstules tā, lai, sākot no jebkuras mājas, vēstuli varētu aiznest uz visām mājām (t.i., grafā nav izolētu salu). Kādu minimālo šķautņu (savienojumu) skaitu viņai vajadzēs, ja ir :math:`n` mājas?
(sk. NEW)




Grafā ar :math:`7` virsotnēm un :math:`12` šķautnēm, vai var būt iespējams grafu uzkrāsot ar :math:`2` krāsām, lai nevienai šķautnei nebūtu vienādas krāsas galapunktu?
(sk. NEW)




Jinx mēģina uzzīmēt planāru grafu (bez šķautņu krustošanās) ar 7 virsotnēm, kur katrai virsotnei pieiet vismaz 4 šķautnes. Vai tas iespējams?
(sk. NEW)




Kāds ir visīsākais cikls, kas var būt kādā no grafiem, kas sastāv no 10 virsotnēm un 22 šķautnēm? Kā to varētu atrast?
(sk. NEW)




Echo grib, lai visi viņa draugi apmainās ar kartēm tā, lai katrs varētu nonākt pie jebkura cita drauga – un nav nekādu lieku loku (cikli). Kāda veida grafu viņš uzzīmēs šādam nolūkam? Nosauc šī objekta nosaukumu un galvenās īpašības.
(sk. NEW)




Īsie risinājumu konspekti
-------------------------------------------------------------------------




*Atrisinājums:* 1. Katram tiltam ir divi gali, tātad kopā ir :math:`2 \cdot 6 = 12` galu uz 4 salām. Vidēji :math:`12/4=3` tilti uz salu, tāpēc vismaz vienai salai būs vismaz 3 tilti (pēc Dirihlē principa).





*Atrisinājums:* 2. Katrā pieturā norādītais skaitlis ir tās pakāpe (kādas šķautnes). Kopā visu virsotņu pakāpju summa ir :math:`2 \cdot` šķautņu skaits, tātad pāra skaitlis ('roku paspiešanas lemma').





*Atrisinājums:* 3. Sk. vispirms dažādus gadījumus. (A) ar 0--9 tas ir iespējams, ja grafu uzskata par ciklisku un pārbauda atšķirības. (B) ar 0--13 nē, jo nav iespējams abpusēji savienot katru tā, lai nosacījums par atšķirību pārsniegtu nepieciešamo šķautņu kopu.





*Atrisinājums:* 4. Rokas paspiešanas lemma: grafā nepāra pakāpes virsotņu skaitam jābūt pāra skaitlim. 8 ir pāra skaitlis, bet var, piem., katru savienot ar 3 citiem – ne visas konfigurācijas iespējamas, bet, ja mēģina izveidot precīzi, rodas pretruna ar virsotņu pakāpju summu – nav iespējams.





*Atrisinājums:* 5. Lai varētu noteikt kungu un kundžu skaitu, apzīmējam :math:`x` – kungu, :math:`y` – kundžu. :math:`17x = 13y` un :math:`x + y = 60`. Atrod :math:`x = 39`, :math:`y = 21`.





*Atrisinājums:* 6. Minimālais šķautņu skaits savienotam grafam ar :math:`n` virsotnēm ir :math:`n-1` (minimums savienotam kokam).





*Atrisinājums:* 7. 2-krāsojamība (bipartītie grafi) nozīmē, ka nav nepāra ciklu. 7 virsotnes un 12 šķautnes nozīmē, ka varētu būt cikli ar 3 šķautnēm, tātad nav iespējama 2-krāsojamība.





*Atrisinājums:* 8. Planārs grafam ar :math:`n` virsotnēm un šķautņu skaitu :math:`e \leq 3n-6`. Ja :math:`n=7`, :math:`d \geq 4`, :math:`4 \cdot 7 / 2 = 14` šķautnes, bet :math:`3\cdot 7-6 = 15`, krustošanās vēl nav liegta, bet :math:`d \geq 4` padara par grūtu bez krustošanās, tātad nav iespējams.





*Atrisinājums:* 9. Ja grafā ir :math:`n` virsotnes un :math:`e` šķautnes, tad īsākais cikls var tikt meklēts, izmantojot ciklu teoriju. 22 šķautnes ar 10 virsotnēm norāda, ka cikla garums nevar būt mazāks par 3 (trijstūris).





*Atrisinājums:* 10. Echo uzzīmēs koku – tas ir savienots grafiks bez cikliem. Koka īpašības: katras divas virsotnes savieno tieši viens ceļš; ja ir :math:`n` virsotņu, tad ir :math:`n-1` šķautne.




