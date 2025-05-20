

Arcane Grafu Teorija: Iesildošā darba lapa 8.klasei
=====================================================================




Ievaduzdevumi
-------------------------------------------------------------------------




*Sākumā – divi viegli uzdevumi, kas palīdz atcerēties galvenos jēdzienus grafu pasaulē. Jūties kā Vi, kas sāk trenēt prātu pirms īstas misijas Piltover!*




Arcane pilsētā Hexportā starp sešām galvenajām apkaimēm ved ceļi, bet ne visi ceļi ir savienoti. Ja katru apkaimi var sasniegt no jebkuras citas (staigājot pa ceļiem), vai šis grafis ir noteikti saistīts? Nosauc piemēru vai pierādi!
(sk. NEW)






Vai pa apli var uzrakstīt skaitļus :math:`0;\;1;\;2;\;3;\;4;\;5;\;6;\;7;\;8;\;9` tā, lai katri divi blakus esoši atšķirtos par :math:`3`, :math:`4` vai :math:`5`?
(sk. LV.AMO.2022B.8.4)






Teorijas pārskats
-------------------------------------------------------------------------




XXXXX theory: 1) Virsotnes pakāpe: cik šķautnes (ceļi, tilti) iziet no virsotnes (punkta vai vietas)\n2) Grafa apstaigāšana (traversēšana): grafu var iziet pa noteiktu maršrutu (ceļu vai ciklu)\n3) Planārs grafs: var uzzīmēt uz plaknes, tā lai šķautnes nekrustotos\n4) Ceļi un cikli: ceļš – virknē nav atkārtotu šķautņu, bet ciklā sākuma un beigu virsotne sakrīt\n5) Koki: grafs, kas ir saistīts un kurā nav ciklu. Parasti noder shēmošanā, piemēram, Hextech iekārtu ķēdēs!




Grūtākie uzdevumi (Arcane olimpiādes stilā!)
-------------------------------------------------------------------------




*8 uzdevumi ar arvien lielāku sarežģītību. Te būs gan piemēri, gan pierādījumi, gan optimizācijas!*




60 pensionāri katru dienu Arcane sociālajā tīklā apmainās ziņām. Katrs kungs sarakstās ar tieši :math:`17` dāmām, katra dāma ar tieši :math:`13` kungiem. Cik ir kungu un cik dāmu?
(sk. LV.AMO.2011.6.2)






Piltoverā ir dots koks ar :math:`15` virsotnēm. Cik šķautņu koks var maksimāli saturēt? Kā šo vispār noteikt jebkuram koka virsotņu skaitam?
(sk. NEW)






Kādu lielāko daudzumu dažādu ciparu var izrakstīt pa apli tā, lai katri divi blakus uzrakstīti cipari, lasot jebkurā virzienā, veidotu pirmskaitļa pierakstu?
(sk. LV.AMO.2007.7.1)






Dotam sešstūra tīklam (katra virsotne savienota ar 3 'kaimiņiem'), kāda var būt mazākā iespējamā un lielākā iespējamā virsotnes pakāpe? Un cik šķautnes kopā ir šādā tīklā ar :math:`12` virsotnēm?
(sk. NEW)






Hextech izgudrotāji vēlas zīmēt planāru grafu ar :math:`8` virsotnēm un :math:`15` šķautnēm. Vai tas ir iespējams? Pamato, izmantojot planāru grafu formulu :math:`v-e+f=2`.
(sk. NEW)






Izveido nedivdaļīgu ciklisku grafu uz :math:`5` virsotnēm un parādi, kāpēc tas nav divdaļīgs.
(sk. NEW)






Arcane džungļos Summoner's Rift var pārvietoties tikai pa vienvirziena tiltiem no ciema uz ciemu (nav nevienas kopīgas atpakaļceļa saites). Vai šo grafu var saukt par koku? Pastāsti, kādiem nosacījumiem koks atbilst.
(sk. NEW)






Atrisinājumi (konspektīvi)
-------------------------------------------------------------------------




XXXXX solutions_header: Katram uzdevumam – galvenā doma (vērtējams pēc idejas, nevis noformējuma):




XXXXX solution: Grafis ir saistīts, ja starp katrām divām virsotnēm eksistē ceļš. Ja ir sasniedzamība, grafā nav atdalītu 'nostūru'.




XXXXX solution: Nav iespējams, jo dažām virsotnēm (skaitļiem) vispār nav starpā pieļaujamu kaimiņu, nesanāk apļveida 'kaimiņu' sadale.




XXXXX solution: Izmantojam virsotņu pakāpju vienādojumu – rezultātā sanāk 26 kungi un 34 dāmas.




XXXXX solution: Kokam ar :math:`n` virsotnēm ir :math:`n-1` šķautnes, neatkarīgi no formas. Tātad ar :math:`15` virsotnēm – :math:`14` šķautnes.




XXXXX solution: Maksimums – :math:`3` cipari. Vairākiem noteikti parādās sadursme ar pirmskaitļa prasībām.




XXXXX solution: Katrs no :math:`12` virsotnēm ar 3 šķautnēm, kopā :math:`18` šķautnes. Visas virsotnes ar pakāpi 3 – regulars grafs. Pakāpes vienādas.




XXXXX solution: Planāram grafam :math:`e \leq 3v-6`, šeit :math:`15 < 3\cdot8 - 6 = 18`, līdz ar to – var eksistēt planārs grafs.




XXXXX solution: :math:`C_5` cikls nav divdaļīgs, jo tajā ir cikls ar nepāra garumu – divdaļīgam grafam ciklu garumiem jābūt pāra.




XXXXX solution: Vienvirziena malām nav piemērojama koka definīcija, jo parasts koks ir nesaistīts ar orientāciju – tajā nav orientētu šķautņu.




Atrisinājumi
-----------------------------------------------















**NEW**
Jā, ja katru apkaimi var sasniegt no jebkuras citas, tad grafis ir saistīts pēc definīcijas. Ja piemērs – apkaimes A, B, C, D, E, F un starp tām ceļi, kas veido apli, tad visas sasniedzamas.





**LV.AMO.2022B.8.4**
Nav iespējams. Dažas no skaitļiem (:math:`0,1,2,8,9`) nevar likt blakus nevienam no pārējiem noteiktā veidā, tāpēc rakstīt ap apli šādi nav iespējams.





















**LV.AMO.2011.6.2**
Vienādojums: :math:`a+b=60`, :math:`17a=13b`. Ris. :math:`a=26` (kungi), :math:`b=34` (dāmas).





**NEW**
Kokam ar :math:`n` virsotnēm ir :math:`n-1` šķautne. Tātad ar :math:`15` virsotnēm – :math:`14` šķautnes.





**LV.AMO.2007.7.1**
Maksimālais – :math:`3` cipari: :math:`1`, :math:`3`, :math:`7` jebkurā secībā, jo lielākiem vai citiem iespējami atkārtojas nepirmpāra ciparu pāri.





**NEW**
Ja katram ir :math:`3` kaimiņi, katras šķautnes gals pieskaitīts divreiz: šķautņu skaits :math:`E=\frac{12\cdot3}{2}=18`. Mazākā un lielākā pakāpe visiem ir :math:`3`, jo regulars grafs.





**NEW**
Planārajam grafam ar :math:`v` virsotnēm un :math:`e` šķautnēm nepieciešams :math:`e\leq3v-6`. Šeit :math:`3\cdot8-6=18`, :math:`15<18`, tāpēc – jā, iespējams.





**NEW**
Cikls ar :math:`5` virsotnēm (:math:`C_5`) nav divdaļīgs, jo tajā ir nepāra garuma cikls. Divdaļīgā grafā nedrīkst būt nepāra garuma cikli.





**NEW**
Nē, jo kokā šķautnes nav orientētas, koks ir saistīts un bez cikliem. Ja vienvirziena (orientēts) – tad tas ir vairs nav koks pēc parastās definīcijas.














































