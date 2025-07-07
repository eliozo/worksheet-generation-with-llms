

Invariantu metode Vinnija Pūka pasaulē (8.–9. klase)
=====================================================================




Kas ir invariantu metode?
-------------------------------------------------------------------------




*Invariants matemātikā ir vērtība vai īpašība, kas kaut kādā procesā nemainās — lai arī pārējie nosacījumi mainās, invariants paliek nemainīgs. Problēmas ar invariantiem bieži atrisina, meklējot šādas vērtības, lai noteiktu, vai kāda situācija ir iespējama vai cik soļi vajadzīgi rezultāta sasniegšanai.*




*Vinnijs Pūks savas dzimšanas dienas svinībās vēlas sadalīt :math:`30` burciņas medus sev un draugiem (Rū, Iā, Tigrs, Sivēns). Katru reizi, kad Pūks dala medu, viņš iedod 1 burciņu katram draugam, bet sev paņem :math:`2` burciņas. Vai pēc vairākām dalīšanas reizēm var gadīties, ka burciņas izbeidzas tieši tā, lai pēc pēdējās reizes Pūkam būtu tikpat daudz medus, cik katram draugam?*




theory: Padoms: saskaiti, cik burciņas medus kopā sadalās katrā dalīšanas reizē un kā mainās Pūka un draugu skaits. Mēģini atrast invariantu — piemēram, atšķirību starp Pūka un draugu burciņu skaitu.




Iesildīšanās uzdevums
-------------------------------------------------------------------------




Vinnijs Pūks un Sivēns spēlē spēli ar 12 akmeņiem. Katrs pēc kārtas paņem 1 vai 2 akmeņus. Pūks vienmēr sāk. Kurš no viņiem var vienmēr uzvarēt (paņemt pēdējo akmeni), ja abi vienmēr spēlē vislabāk? Pamato atbildi ar invariantu.
(sk. `NEW <https://www.dudajevagatve.lv/eliozo/problem?problemid=NEW>`_)




Galvenie uzdevumi
-------------------------------------------------------------------------




Āpsītis lasa 64 ozolzīles pa grupām: katrā solī viņš var paņemt vai nu 1, 3 vai 5 zīles. Vai obligāti kādā brīdī zīles beigsies tieši pēc kāda viņa soļa, ja viņš turpina līdz vairs nevar paņemt atļauto daudzumu?
(sk. `NEW <https://www.dudajevagatve.lv/eliozo/problem?problemid=NEW>`_)




Uz galda atrodas :math:`k` konfektes. Andris un Juris pamīšus izdara gājienus: Andris - pirmo, trešo, piekto u.t.t., Juris - otro, ceturto, sesto u.t.t. Ar :math:`n`-to gājienu (:math:`n=1, 2, 3, \ldots`) jāapēd vismaz viena, bet ne vairāk par :math:`n` konfektēm. Kas apēd pēdējo konfekti, uzvar. Kurš uzvar, pareizi spēlējot, ja (A) :math:`k=8`; (B) :math:`k=64`?
(sk. `LV.AMO.2003.9.5 <https://www.dudajevagatve.lv/eliozo/problem?problemid=LV.AMO.2003.9.5>`_)




Jānis un Anna spēlē šādu spēli. Uz tāfeles ir uzrakstīts naturāls skaitlis. Spēlētāji pēc kārtas veic gājienu: no uzrakstītā skaitļa atņem kādu šī skaitļa ciparu (izņemot :math:`0`), nodzēš uz tāfeles esošo skaitli un tās vietā uzraksta iegūto starpību. Uzvar tas, kurš pēc sava gājiena iegūst :math:`0`. Sākumā ir uzrakstīts skaitlis :math:`2011`, pirmo gājienu izdara Anna. Kurš no spēlētājiem, pareizi spēlējot, uzvarēs? Apraksti, kā uzvarētājam jārīkojas!
(sk. `LV.AMO.2011.8.5 <https://www.dudajevagatve.lv/eliozo/problem?problemid=LV.AMO.2011.8.5>`_)




Divi spēlētāji pamīšus raksta uz tāfeles skaitļa :math:`216` dabiskos dalītājus. Katrā gājienā jāievēro šādi noteikumi:
- nedrīkst atkārtoti rakstīt jau uzrakstītu dalītāju;
- nedrīkst rakstīt dalītāju, kurš ir tieši :math:`2` vai :math:`3` reizes lielāks vai mazāks nekā kāds jau uzrakstītais dalītājs.
Zaudē tas spēlētājs, kurš nevar izdarīt gājienu. Kurš spēlētājs - pirmais vai otrais - vienmēr var uzvarēt?
(sk. `LV.AMO.2019.11.2 <https://www.dudajevagatve.lv/eliozo/problem?problemid=LV.AMO.2019.11.2>`_)




Divi spēlētāji pamīšus raksta uz tāfeles pa vienam naturālam skaitlim no :math:`1` līdz :math:`9` ieskaitot. Nedrīkst rakstīt skaitļus, ar kuriem dalās kaut viens jau uzrakstīts skaitlis. Kurš nevar izdarīt gājienu, zaudē. Parādiet, kā tas, kas izdara pirmo gājienu, var uzvarēt.
(sk. `LV.AMO.2003.7.3 <https://www.dudajevagatve.lv/eliozo/problem?problemid=LV.AMO.2003.7.3>`_)




Izmanto invariantu! (Atrisināšanas padomi)
-------------------------------------------------------------------------




*1. Mēģini noteikt, kura lieta uzdevumā nemainās, neskatoties uz darbībām! 2. Saskaiti atšķirības (pāru, ciparu, atlikumu u.c.). 3. Vienmēr mēģini veidot tabulu vai pierakstu par visiem stāvokļiem, īpaši, ja spēlē esi kopā ar Pūku vai draugiem!*




Atrisinājumi
-----------------------------------------------



























**NEW**
Uzvarēt var tas, kurš pēc savas gājiena secības nodrošina, ka pēc katra sava gājiena uz galda vienmēr paliek pāra skaits akmeņu. Ja Pūks vienmēr paņem tā, lai pēc viņa gājiena paliek pāra skaits akmeņu, viņš uzvarēs. Invariants — akmeņu skaita atlikums, dalot ar 3.









**NEW**
Invariants – atlikums, dalot ar 2. Katru reizi izņemot 1, 3 vai 5 zīles, atlikums mainās, bet, ja sāk ar pāra skaitu, pēc pārīšu gājieniem var beigties tieši pēc soļa. Šajā gadījumā 64 ir pāra skaitlis, viņam vienmēr izdosies.





**LV.AMO.2003.9.5**
<strong>(A)</strong> uzvar Juris. Viņš ar otro gājienu ēd :math:`2` konfektes. Kopā tagad apēstas :math:`3` konfektes. Andris var ēst :math:`1, 2` vai :math:`3` konfektes. Andris ēd attiecīgi :math:`4, 3` vai :math:`2` konfektes un uzvar. <br/>
<strong>(B)</strong> uzvar Andris. Viņš spēlē tā, lai pēc viņa gājieniem būtu apēsti :math:`1^2, 2^2, 3^2, 4^2, \ldots` konfektes. Šāds skaits veido invariantu (kvadrātu secība), līdz ar to viņš var nodrošināt uzvaru.





**LV.AMO.2011.8.5**
Uzvar pirmais spēlētājs, katrā gājienā atņemot no skaitļa tā pēdējo ciparu, tādējādi pēc sava gājiena iegūstot skaitli, kura pēdējais cipars ir :math:`0`. Otrais spēlētājs nevar atņemt :math:`0`, tātad paliek tikai skaitļi, kur pēdējais cipars nav :math:`0`. Līdz ar to pirmais spēlētājs vienmēr varēs veikt gājienu un beigu beigās uzvarēt.





**LV.AMO.2019.11.2**
Vienmēr var uzvarēt otrais spēlētājs. Dalītājus var sapārot tā, ka katra pāra dalītāju reizinājums ir :math:`216`. Pirmais spēlētājs izvēlas jebkuru dalītāju, otrais – attiecīgo pāra dalītāju. Tā kā pāra skaitļu attiecība nav :math:`2` vai :math:`3`, šī stratēģija saglabā invariantu – nevienu dalītāju nevar izvēlēties atkārtoti, līdz ar to otrais spēlētājs vienmēr var atbildēt, un beigās uzvar.





**LV.AMO.2003.7.3**
Pirmais spēlētājs ar :math:`1.` gājienu uzraksta :math:`2`. Uz otrā spēlētāja katru 1. gājienu viņš atbild pēc šādas shēmas: :math:`5 \rightarrow 7`, :math:`7 \rightarrow 5`, :math:`3 \rightarrow 8`, :math:`8 \rightarrow 3`, :math:`9 \rightarrow 4`, :math:`6 \rightarrow 4`, :math:`4 \rightarrow 6`. Šis ir invarianta piemērs – atbilstoši piespēlē, kad otrs izvēlas, un saglabā iespēju uzvarēt.










