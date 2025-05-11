

Dirihlē princips
=====================================================================




.. class:: center

**Teorija un piemēri, gatavojoties Atklātajai matemātikas olimpiādei 2024./2025. m.g.**



 
Apskatīsim pavisam vienkāršu uzdevumu.





*Pēterim ir* :math:`3` *truši un* :math:`2` *būri. Visi truši atrodas būros. Vai noteikti kādā no šiem būriem ir vismaz divi truši?*




**Teorēma:** Ja vairāk nekā :math:`n` objekti jāsadala :math:`n` grupās, tad noteikti būs tāda grupa, kurā atradīsies vismaz :math:`2` objekti.




*Pierādījums:* Pieņemsim pretējo, ka nevienā grupā nav vairāk kā viens objekts. Tā kā grupu pavisam ir :math:`n`, tad kopā nav izvietoti vairāk kā :math:`n` objekti, bet grupās ir jāsadala vairāk nekā :math:`n` objekti. Tātad pieņēmums ir aplams un noteikti ir grupa, kurā vairāk nekā viens, tas ir, vismaz :math:`2` objekti, kas arī bija jāpierāda.



 
Bieži vien Dirihlē principu formulē šādā veidā:





**Teorēma:** Ja vairāk nekā :math:`n` truši jāizvieto :math:`n` būros, tad vismaz vienā būrī nonāks vairāk nekā viens (tātad vismaz :math:`2`) truši.



 
Lietojot Dirihlē principu uzdevumu risināšanā, galvenais ir izdomāt, kas katrā uzdevumā būs 'būri' un kas -- 'truši'. Uzdevumu risinājumā var gan atsaukties uz Dirihlē principu, gan arī atrisinājumu veidot, piemēram, līdzīgi kā pierādot 1. teorēmu. Abi šādi risinājumi ir pareizi (skat., piem., nākamo uzdevumu)





Uzdevumu piemēri
-------------------------------------------------------------------------




1. Pulciņā ir :math:`13` skolēni. Pierādīt, ka no tiem var atrast tādus divus, kas dzimuši vienā un tajā pašā mēnesī!




*Atrisinājums:* Ja katrā mēnesī būtu dzimis ne vairāk kā viens skolēns, tad visos mēnešos kopā būtu dzimuši ne vairāk kā :math:`12` skolēnu, bet pulciņā ir :math:`13` skolēni. Tātad noteikti ir tāds mēnesis, kurā dzimuši vismaz divi no šī pulciņa skolēniem.





*Atrisinājums:* Šajā uzdevumā :math:`13` skolēni ir jāsadala :math:`12` grupās (mēnešos). Pēc Dirihlē principa noteikti būs mēnesis, kurā ir dzimuši vismaz divi skolēni, kas arī bija jāpierāda.





2. Doti naturāli skaitļi no :math:`1` līdz :math:`8`. Pierādīt, ka, izvēloties jebkurus piecus no tiem, varēs atrast tādus divus, kuru summa ir :math:`9`.




*Atrisinājums:* Jebkuri no pieciem izvēlētajiem skaitļiem ietilpst vienā no šādām grupām (grupas veidotas no skaitļiem, kuru summa ir :math:`9`): „:math:`1` un :math:`8`”, „:math:`2` un :math:`7`”, „:math:`3` un :math:`6`”, „:math:`4` un :math:`5`”. Ar katru grupu būtu pa ne vairāk kā viens skaitlis, tad viss pārējais kopā būtu ne vairāk kā četri skaitļi, bet ir jāizvēlas pieci skaitļi, tātad noteikti ir tāds pāris, kuru ir divi skaitļi, un šo skaitļu summa ir :math:`9`.





*Atrisinājums:* Jebkuri no pieciem izvēlētajiem skaitļiem ietilst vienā no šādiem četriem 'būriem': „1 un 8”; „2 un 7”, „3 un 6”, „4 un 5”. Tāpēc pēc Dirihlē principa vismaz vienā būrī nonāks vismaz 2 „truši” jeb 2 skaitļi, kuru summa ir deviņi.





3. Izliektā 100-stūru virsotnes kaut kādā secībā sanumurētas ar naturālajiem skaitļiem no :math:`1` līdz :math:`100`, katra virsotne ar citu skaitli. Katrai malai aprēķina tās galu numuru starpību (no lielākā skaitļa atņemot mazāko). Pierādīt, ka vismaz divām malām šīs starpības ir vienādas!




*Atrisinājums:* Ir iespējamas tikai :math:`99` dažādas starpības: :math:`1; 2; \ldots; 99`; tie ir „būri”. Ir 100 malas, kam aprēķinātas starpības; tie ir „truši”. Pēc Dirihlē principa vismaz vienā būrī būs vismaz :math:`2` truši jeb vismaz divām malām šīs starpības ir vienādas.





4. Sniegbaltīte uzdāvināja katram no 7 rūķīšiem pa 5 konfektēm: 'Vāverīti', 'Margrietiņu' un 'Lācīti', pie tam katrs rūķītis saņēma vismaz vienu katra veida konfekti. Pierādīt, ka ir divi tādi rūķīši, kam viņa uzdāvināja vienādus konfekšu komplektus!




*Atrisinājums:* Ievērosim, ka skaitli 5 var izteikt kā trīs naturālu skaitļu summu tikai divos veidos: :math:`3 + 1 + 1` un :math:`2 + 2 + 1` (ja nav būtiska saskaitāmo secība). Taču, ņemot vērā arī to, kura no konfetēm pirmajā gadījumā ir dāvināta 3 eksemplāros un kura no konfektem otrajā gadījumā -- vienā eksemplārā, iegūstam 6 dažādas iespējas:

.. figure:: ../tests/worksheets/pigeonhole_2025_page2A.png
   :width: 246px

Tā kā ir 7 rūķīši un 6 dažādas iespējas, kā uzdāvināt konfektes, tad pēc Dirihlē principa noteikti ir tādi divi rūķīši, kam Sniegbaltīte uzdāvināja vienādas konfekšu komplektus.





5. Taisne nokrāsota :math:`10` dažādās krāsās. Pierādīt, ka uz tās var atrast divus punktus, kas nokrāsoti vienā krāsā un starp kuriem attālums centimetros ir vesels skaitlis!




*Atrisinājums:* Izvēlamies uz taisnes :math:`11` punktus tā, lai attālums starp katriem diviem no tiem būtu vesels skaitlis. Tā kā ir izvēlēti :math:`11` punkti un ir :math:`10` dažādas krāsas, tad pēc Dirihlē principa vismaz divi no šiem punktiem ir vienā krāsā.





6. Pierādīt, ka starp jebkuriem sešiem naturāliem skaitļiem, kas nedalās ar :math:`10`, var atrast divus tādus, kuru summa vai starpība dalās ar :math:`10`.




*Atrisinājums:* Apskatām divus iespējamos gadījumus.  
**(1)** Ja starp apskatāmajiem skaitļiem ir divi tādi, kam pēdējie cipari vienādi, tad to starpība dalās ar :math:`10`.  
**(2)** Ja nu tādu divu skaitļu nav, tad pēdējie cipari ir vienādi, tad sadalām skaitļus 5 grupās atbilstoši to pēdējiem cipariem: "1 un 9"; "2 un 8"; "3 un 7"; "4 un 6"; "5". Tā kā ir :math:`6` skaitļi un piecas grupas, tad divi skaitļi noteikti ieies vienā grupā, to summa dalās ar :math:`10`.





7. Pierādīt, ka starp septiņiem naturāliem skaitļiem var izvēlēties tādus divus, kuru starpība dalās ar :math:`7`.




*Atrisinājums:* Naturālis skaitlis, dalot ar :math:`7`, var dot kādu no sekojošiem atlikumiem: :math:`0; 1; 2; 3; 4; 5; 6`. Dotos astoņus skaitļus uzskatām par „trušiem”, savukārt vienā 'būri' ievietosim tos skaitļus, kad vienādās atlikumu dalījumi ar :math:`7`, tādai ir :math:`7` 'būru' principi: pēc Dirihlē principa 'būri' nonāks vismaz divi 'truši' jeb vismaz divi skaitļi dod vienādus atlikumus, dalot ar :math:`7`. Šo skaitļu starpība dalās ar :math:`7` (skat. nākamo teorēmu).





**Teorēma:** Teorēma par starpības dalīšanos. Dots, ka :math:`a, b` un :math:`n` -- veseli skaitļi, turklāt :math:`n > 0`. Starpība :math:`(a - b)` dalās ar :math:`n` tad un tikai tad, ja :math:`a un b` dod vienādus atlikumus, dalot ar :math:`n`.



 
Apskatīsim vēl vienu uzdevumu par Pēteri un viņa trušiem.





*Pēterim ir* :math:`5` *truši un* :math:`2` *būri. Visi truši atrodas būros. Vai noteikti kādā no šiem būriem ir vismaz* :math:`3` *truši?*



 
Risināsim šo uzdevumu līdzīgi, kā iepriekšējo uzdevumu par trušiem. Ja šāda būra nebūtu, tad Pēterim katrā būrī būtu ne vairāk kā :math:`2` truši. Tātad abos būros kopā būtu ne vairāk kā 4 truši, bet Pēterim ir 5 truši. Līdz ar to noteikti ir tāds būris, kurā atrodas vismaz :math:`3` truši.





*Un, ja Pēterim būtu* :math:`10` *truši un* :math:`3` *būri? Vai mēs varētu apgalvot, ka noteikti ir tāds būris, kurā ir vismaz* :math:`4` *truši?*



 
Atbilde atkal ir apstiprinoša. Ja katrā būrī būtu ne vairāk kā :math:`3` truši, tad visos būros kopā būtu izvietoti ne vairāk kā :math:`9` truši, bet Pēterim ir :math:`10` truši. Tātad noteikti ir tāds būris, kurā atrodas vismaz 4 truši.





*Šajos piemēros varēja lietot tālāk doto Dirihlē principa vispārinājumu.*




**Teorēma:** **(Dirihlē princips)**: Ja vairāk nekā :math:`m \cdot n` objektì jāsadala :math:`n` grupās, tad noteikti būs grupa, kurā atradīsies vismaz :math:`(m + 1)` objekts.




*Pierādījums:* Pieņemsim pretējo, ka nevienā grupā nav vairāk kā :math:`m` objekti. Tā kā grupu pavisam ir :math:`n`, tad kopā nav izvietoti vairāk kā :math:`m \cdot n` objekti, bet grupās ir jāsadala vairāk nekā :math:`m \cdot n` objekti. Tātad pieņēmums ir aplams un noteikti ir grupa, kurā ir vairāk nekā :math:`m`, tas ir, vismaz :math:`(m + 1)` objekts.




Uzdevumu piemēri
-------------------------------------------------------------------------




8. Mākslinieku darbnīcā izgatavotas 36 skulptūras, kuru masa ir :math:`490~\text{kg}`, :math:`495~\text{kg}`, :math:`500~\text{kg}`, :math:`\ldots`, :math:`665~\text{kg}`. Vai visas šīs skulptūras var aizvest ar :math:`7` automašīnām, ja katrai no tām kravasnīša ir :math:`3` tonnas, ar katru automašīnu drīkst veikt tikai vienu reisu un automašīnas nedrīkst pārslogot?




*Atrisinājums:* Pamatotsim, ka prasītais nav iespējams. Ja katrā no septiņām automašīnām iekrautu ne vairāk kā :math:`5` skulptūras, tad kopā pa visām mašīnām būtu izvietotas ne vairāk kā :math:`35` skulptūras, bet jāizveto ir :math:`36` skulptūras. Tātad noteikti ir tāda mašina, kurā būtu jāiekrauj vismaz sešas skulptūras. Taču pat sešu vieglāko skulptūru kopējā masa ir :math:`490 + 495 + 500 + 505 + 510 + 515 = 3015` kilogrami, tātad ir lielāka par masu, kādu pieļaujams iekraut vienā automašīnā. Tas nozīmē, ka uzdevuma prasības nav izpildāmas.





*Atrisinājums:* Pamatotsim, ka prasītais nav iespējams. Šajā uzdevumā „truši” ir skulptūras, „būri” -- automašīnas. Ievērosim, ka :math:`36 = 7 \cdot 5 + 1` skulptūras jāsadala pa 7 automašīnām. Tādā pēc Dirihle principa vismaz vienā automašīnā jāiekrauj vismaz 6 skulptūras. Taču pat sešu vieglāko skulptūru kopējā masa ir :math:`490 + 495 + 500 + 505 + 510 + 515 = 3015` kilogrami, tātad ir lielāka par masu, kādu pieļaujams iekraut vienā automašīnā. Tas nozīmē, ka uzdevuma prasības nav izpildāmas.





9. Profesora Ciparina olimpiādē bija :math:`3` uzdevumi. Tajā piedalījās :math:`100` skolēni. Pierādīt, ka atradīsies vismaz :math:`13` skolēni, kas izrēķināja vienu un to pašu uzdevumu (vai arī neizrēķināja neievienu uzdevumu)! Katrs skolēns katru uzdevumu vai nu izrēķināja, vai neizrēķināja, daļēji risinājumi netika iesniegti.




*Atrisinājums:* No trīs uzdevumiem var tikt izveidoti 8 dažādi atrisināto uzdevumu „komplekti” (t.s.k., neviens atrisināts uzdevums), tabulā ar "+" atzīmēti tie uzdevumi, kuru skolēns izrēķināja.

.. figure:: ../tests/worksheets/pigeonhole_2025_page3A.png
   :width: 246px

Ja katru „komplektu” būtu atrisinājuši ne vairāk kā :math:`12` skolēni, tad skolēnu kopējais skaits būtu ne vairāk kā :math:`12 \cdot 8 = 96 < 100`. Tātad ir vismaz :math:`13` skolēni, kas atrisinājuši vienus un tos pašus uzdevumus.





10. Rūtiņu virsotnēs atzīmēti 16 balti punkti (skat. 1. att.). Vai tieši septiņus punktus var nokrāsot melnus tā, lai nekādi trīs vienā krāsā nokrāsoti punkti neatrastos uz vienas taisnes?

![](pigeonhole_2025_page3B.png)




*Atrisinājums:* Nē, to nevar izdarīt. Ja melnā krāsā nokrāsoti tieši septiņi punkti, tad paliek deviņi balti punkti. Tā kā visi punkti izvietoti četrās rindās, tad pēc Dirihlē principa kādā no šīm rindām būs vismaz trīs balti punkti, bet tas ir pretrunā ar uzdevuma nosacījumiem.





11. Maisiņā bija :math:`10` sarkanas, :math:`10` dzeltenas un :math:`10` zaļas lentes. Tautas deju kolektīva astoņas meitenes katra izvēlējās vienu lenti no šī maisiņa.
**(A)** Vai var apgalvot, ka tieši četras meitenes izvēlējās vienādas krāsas lentes?
**(B)** Vai noteikti ir vismaz trīs meitenes, kas izvēlējās vienādas krāsas lentes?
**(C)** Kāds mazākais skaits lenšu būtu jāizņem no maisiņa, lai varētu apgalvot, ka vismaz četras no tām ir vienā krāsā?




*Atrisinājums:* **(A)** Nē, piemēram, varētu gadīties, ka 1 meitene izvēlējās sarkanu lenti, 1 meitene -- dzeltenu lenti un :math:`6` meitenes -- zaļu lenti.  
**(B)** Jā, noteikti. Ja katras krāsas lenti būtu izvēlējušās ne vairāk kā :math:`2` meitenes, tad kopā būtu ne vairāk kā :math:`2 \cdot 3 = 6` meitenes, bet tā ir pretruna ar doto, ka lentes izvēlējās :math:`8` meitenes. Tātad noteikti ir vismaz :math:`3` meitenes, kas izvēlējās vienas krāsas lentes. (Izmantots Dirihle princips.)  
**(C)** Pamatotsim, ka mazākais skaits lenšu, kas jāizņem no maisiņa, ir :math:`10`, un ka mazāk izņemt nevar. Ar deviņām (vai mazāk) lentēm nepietiktu, jo būtu iespējams, ka no katras krāsas ir pa :math:`3` lentām (vai mazāk). Tātad, ja no maisiņa izņemt :math:`10` lentes, tad pēc Dirihle principa noteikti vismaz četras no tām būtu vienā krāsā.





*Tālāk dotais materiāls paredzēts galvenokārt 9.-12. klašu skolēniem.*




12. Skolas ēdnīcas pusdienu piedāvājumā ir divas dažādas zupas, divi dažādi pamatēdieni un divi dažādi deserti. Pusdienās aizgāja :math:`200` skolēni, no katra ēdienu veida (zupa, pamatēdiens, deserts) katrs skolēns izvēlējās ne vairāk kā vienu ēdienu, pie tam nebija tāda skolēna, kurš neēda vispār neko. Kāds ir lielākais skaits skolēnu, kas noteikti pasūtīja vienu un to pašu?




*Atrisinājums:* Pamatot, ka lielākais skolēnu skaits, kas noteikti pasūtīja vienu un to pašu, ir :math:`8`. Ievērojam, ka katra veida ēdienu var izvēlēties par vai nu neiekļaut komplektā, vai izvēlēties vienu ēdienu. Tātad katram ēdiena veidam ir :math:`3` dažādas iespējas. Tā kā katrs skolēns izvēlējās vismaz vienu no piedāvātajiem ēdieniem (nevar gadīties, ka no katra ēdiena veida neizvēlas nevienu), ir iespējamas :math:`3 \cdot 3 \cdot 3 - 1 = 26` dažādas pusdienu komplektu iespējas.





*Atrisinājums:* Ja katru no šīm komplektiem būtu izvēlējušies ne vairāk kā :math:`7` skolēni, tad pusdienās būtu aizgājuši ne vairāk kā :math:`7 \cdot 26 = 182` skolēni, kas ir pretrunā ar uzdevuma nosacījumiem. Tātad noteikti ir :math:`8` skolēni, kas pasūtīja vienu un to pašu. Nevar apgalvot, ka vairāk kā :math:`8` skolēni pasūtīja vienu un to pašu, jo ir iespējams, ka pirmos :math:`18` no :math:`26` dažādajiem pusdienu komplektiem izvēlējās pa :math:`8` skolēniem un atlikušos :math:`8` pusdienu komplektus -- pa :math:`7` skolēniem (tas ir, :math:`18 \cdot 8 + 8 \cdot 7 = 200`).




 
*Piezīme.* Treknrakstā izcelta teksta vietā var būt, piemēram, arī šāds spriedums: tā kā skolēnu skaits ir :math:`200 = 7 \cdot 26 + 18`, tad pēc Dirihlē principa noteikti ir 8 skolēni, kas pasūtīja vienu un to pašu.





13. Pierādīt, ka starp jebkuriem :math:`78` trīsciparu skaitļiem var atrast četrus tādus skaitļus, kuru ciparu summas ir vienādas!




*Atrisinājums:* Pavisam iespējamas :math:`27` dažādās ciparu summas vērtības:

.. figure:: ../tests/worksheets/pigeonhole_2025_page4A.png
   :width: 246px

Ievērojam, ka  
**(1)** ciparu summa 1 un 27 katra ir tikai vienam skaitlim (100 un 999),
**(2)** ciparu summa 2 un 26 katra ir tikai trīs skaitļiem (:math:`101; 110; 200` un :math:`899; 989; 998`). Tādēļ šajās grupās varētu būt ne vairāk kā to, kurus :math:`78` trīsciparu skaitļus iezīmēs. Pieņemsim, ka šīs četras grupas ir maksimāli piepildītas -- tajās kopā ievietoti :math:`8` skaitļi. Tād atlikušajās :math:`23` grupās jāievieto :math:`78 - 8 = 70` skaitļi.




 
Ja katrā no šīm 23 grupām būtu ievietoti ne vairāk kā 3 skaitļi, tad kopā būtu izvietoti ne vairāk kā :math:`3 \cdot 23 = 69` skaitļi -- pretruna tam, ka :math:`78` skaitļi jāizvieto :math:`70` skaitļi. Līdz ar to noteikti ir tāda grupa, kurā ir vismaz četri skaitļi -- tie arī ir meklētie četri skaitļi, kuru ciparu summas ir vienādas.




 
Piezīme. Treknrakstā izcelta teksta vietā var būt, piemēram, arī šāds spriedums: tā kā :math:`70 = 3 \cdot 23 + 1`, tad pēc Dirihlē principa noteikti ir tāda grupa, kurā ir vismaz četri skaitļi -- tie arī ir meklētie četri skaitļi, kuru ciparu summas ir vienādas.





14. Sporta zālē trenējas 32 cilvēki, kuri visi ir vismaz 21 gadu veci. Pierādīt, ka no šiem cilvēkiem var atrast divus tādus, kuriem ir vairāk nekā 30 gadi vai 4 tādus, kuru gadu skaits ir vienāds!




*Atrisinājums:* Pieņemam pretējo tam, kas jāpierāda, tas ir, nav divu cilvēku, kuriem ir vairāk nekā 30 gadi un nav četru cilvēku, kuriem ir vienāds gadu skaits. Sadalām cilvēkus grupās pēc to gadu skaita:

.. math::

    \{21\}; \{22\}; \{23\};\ldots;\{29\}; \{30\}; \{\text{vairāk nekā 30}\}.

Tad pirmajās 10 grupās katrā ir ne vairāk kā 3 cilvēki un pēdējā -- ne vairāk kā viens cilvēks. Tātad sporta zālē ir vismaz :math:`3 \cdot 10 + 1 = 31` cilvēks. Tādēļ pieņēmums ir aplams un esam pierādījuši, ka var atrast divus tādus cilvēkus, kuriem ir vairāk nekā 30 gadi vai 4 tādus, kuru gadu skaits ir vienāds.





*Atrisinājums:* Sadalām cilvēkus grupās pēc to gadu skaita:

.. math::

    \{21\}; \{22\}; \{23\};\;\ldots\;\{29\}; \{30\}; \{\text{vairāk nekā 30}\}.

Apskatām divus iespējamos gadījumus. 1) Ja pēdējā grupā ir vismaz divi cilvēki, tad prasītais izpildās. 2) Ja pēdējā grupā ir mazāk nekā divi cilvēki, tad pa atlikušajām 10 grupām jāsadala vismaz 31 cilvēks. Tā kā ir 10 grupas un vismaz :math:`31 = 3 \cdot 10 + 1` cilvēks, tad pēc Dirihle principa kādā no šīm grupām ir vismaz 4 cilvēki, tātad tiem gadu skaits ir vienāds.





Uzdevumi treniņam
-------------------------------------------------------------------------




1. Kāds mazākais skaits cilvēku ir nepieciešams, lai garantētu to, ka a) 2 cilvēkiem, b) 3 cilvēkiem dzimšanas diena sakrīt?




2. Doti 12 dažādi divciparu skaitļi. Pamatot, ka var izvēlēties divus no tiem, lai to starpība būtu divciparu skaitlis, kura abi cipari ir vienādi!




3. Vairākās kaudzītēs kopā ir 58 sērkociņi; nevienā kaudzītē nav mazāk kā 1 sērkociņš un nav vairāk kā 12 sērkociņi. Pierādīt, ka ir divas kaudzītes, kurās ir vienāds sērkociņu skaits, vai ir divas kaudzītes, kurās kopā ir tieši 13 sērkociņi!




4. Katrā no 16 mazajiem trijstūriem (skat. 3. att.) ir ierakstīts viens skaitlis, pavisam ierakstīti septiņi trijnieki un deviņi piecinieki. Pierādīt, ka var izvēlēties tādu trijstūri, kā parādīts 4. att., kurā ierakstīto skaitļu summa ir vismaz 18.




*Tālāk dotie uzdevumi paredzēti galvenokārt 9.-12. klašu skolēniem.*




5. No pirmajiem 100 naturālajiem skaitļiem izvēlēts 51 skaitlis. Pierādīt, ka no tiem var izvēlēties divus, no kuriem viens dalās ar otru!




6. Pierādīt, ka no septiņiem patvaļīgiem naturāliem skaitļiem var izvēlēties divus tādus skaitļus, kuru kvadrātu starpība dalās ar 11.




7. Pēterītim bija 100 aplīši, uz kuriem uzrakstīti naturālie skaitļi no 1 līdz 100 (uz katra aplīša cits skaitlis). Skolotāja lika izvēlēties 4 aplīšus un izvietot tos tā, lai būtu patiesa vienādība :math:`O + O = O + O`. Aplīši bija izbērti uz grīdas, un līdz šī uzdevuma saņemšanai Pēteris bija paguvis savākt tikai 21 aplīti. Vai ar tiem viņam noteikti pietika, lai izpildītu skolotājas uzdevumu?




8. Pierādīt, ka starp jebkuriem 35 divciparu skaitļiem var atrast trīs tādus skaitļus, kuru ciparu summas ir vienādas!




9. Dots naturāls skaitlis :math:`n`, kas nedalās ar 2 un 5. Pamatot, ka pastāv tāds skaitļa :math:`n` daudzskaitlis, kas sastāv tikai no vieniniekiem!




Uzdevumu atrisinājumi
=====================================================================




1. Cik cilvēki ir nepieciešami, lai garantētu to, ka **(A)** 2 cilvēkiem, **(B)** 3 cilvēkiem dzimšanas diena sakrīt?




*Atrisinājums:* **(A)** Mazākais skaits cilvēku ir 367. Pamatosim, ka ar mazāk cilvēkiem nepietiek. Ja būtu ne vairāk kā 366 cilvēki, tad varētu gadīties, ka katram dzimšanas diena ir citā dienā (ieskaitot 29. februāri), tāpēc ir nepieciešami vismaz 367 cilvēki, lai, izmantojot Dirihlē principu, garantētu to, ka vismaz 2 cilvēkiem dzimšanas diena sakrīt.
**(B)** Līdzīgi, izmantojot Dirihlē principu, varam spriest, ka būtu nepieciešami vismaz :math:`2 \cdot 366 + 1 = 733` cilvēki, lai garantētu to, ka vismaz 3 cilvēkiem dzimšanas diena sakrīt.





2. Katrā no 16 mazajiem trijstūriem (skat. 
5. att. un 6. att.) ir ierakstīts viens skaitlis, pavisam ierakstīti septiņi trijnieki un deviņi piecinieki. Pierādīt, ka var izvēlēties tādu trijstūri, kā parādīts 6. att., kurā ierakstīto skaitļu summa ir vismaz 18.




*Atrisinājums:* Sadalīsim sākotnējo trijstūri četros trijstūros ar malas garumu 2 (skat 7. att.). Tā kā ir četri šādi trijstūri (kas nepārklājas), un tajos ierakstīti 9 piecinieki, tāpēc Dirihlē principa kādā no šiem trijstūriem būs vismaz trīs piecinieki, tāpēc tajā ierakstīto skaitļu summa ir vismaz :math:`5 + 5 + 5 + 3 = 18`, kā bija jāpierāda.





3. Vairākās kaudzītēs kopā ir 58 sērkociņi; nevienā kaudzītē nav mazāk kā 1 sērkociņš un nav vairāk kā 12 sērkociņi. Pierādīt, ka ir divas kaudzītes, kurās ir vienāds sērkociņu skaits, vai ir divas kaudzītes, kurās kopā ir tieši 13 sērkociņi!




*Atrisinājums:* Pieņemsim pretējo tam, kas jāpierāda, tas ir, nav divu kaudzīšu, kurās ir vienāds sērkociņu skaits un nav divu kaudzīšu, kurās kopā ir tieši 13 sērkociņi. Tad no naturālu skaitļu pāra :math:`(1; 12), (2; 11), (3; 10), (4; 9), (5; 8), (6; 7)` ne vairāk kā viens skaitlis kādā kaudzītē. Tāpēc sērkociņu nav vairāk kā :math:`7 + 8 + 9 + 10 + 11 + 12 = 57` (no katra skaitļu pāra izvēlējās lielāko skaitli) -- pretruna. Tātad pieņēmums ir aplams un, ja ir divas kaudzītes, kurās ir vienāds sērkociņu skaits, vai ir divas kaudzītes, kurās kopā ir tieši 13 sērkociņi.





4. Doti 12 dažādi divciparu skaitļi. Pamatojot, ka var izvēlēties divus no tiem, lai to starpībā būtu divciparu skaitlis, kura abi cipari ir vienādi!




*Atrisinājums:* Apskatīsim vispirms tos divciparu skaitļus, kuriem abi cipari ir vienādi. Tie ir:

.. math::

    11; 22; 33; 44; 55; 66; 77; 88; 99.

Ievērojam, ka tie ir visi divciparu skaitļi, kas dalās ar 11. Atliek pamatot, ka no dotajiem 12 divciparu skaitļiem var atrast 2 tādus, kuru starpība dalās ar 11. Tā kā ir doti 12 skaitļi, bet skaitlim, dalot ar 11, ir iespējami tikai 11 dažādi atlikumi, tad pēc Dirihlē principa noteikti būs divi tādi skaitļi, kuru dos vienādu atlikumu, dalot ar 11. Tātad vienmēr varēs atrast divus skaitļus no dotajiem 12 skaitļiem, lai to starpība dalītos ar 11. Turklāt šī starpība noteikti būs divciparu skaitlis, jo pēc dotā visi skaitļi ir dažādi un tāpēc nav iespējams iegūt vienīgo skaitli, kas dalās ar 11, kas ir mazāks par divciparu skaitli, tas ir, skaitli 0.





5. No pirmajiem 100 naturālajiem skaitļiem izvēlēt 51 skaitlis. Pierādīt, ka no tiem var izvēlēties divus, no kuriem viens dalās ar otru!




*Atrisinājums:* Visus naturālos skaitļus no 1 līdz 100 sadalīsim 50 grupās: katru nepāra skaitli ievietosim citā grupā (pavisam ir 50 nepāra skaitļi). Ievērojam, katru pāra skaitli p var izteikt kā nepāra skaitļa n un divnieka pakāpes reizinājumu, tas ir, :math:`p = n \cdot 2^k`, kur k ir kāds naturāls skaitlis. Pāra skaitli p ievietosim vienā grupā ar tam atbilstošo nepāra skaitli n. Pirmās grupas ir

.. math::

    \{1; 2; 4; 8; 16; 32; 64\},\;\; \{3; 6; 12; 24; 48; 96\},\;\; \{5; 10; 20; 40; 80\}\;\;\text{utt.}

Izvēloties jebkurus divus skaitļus no vienas grupas, lielākais skaitlis dalās ar mazāko (dalījums ir divnieka pakāpe).





6. Pierādīt, ka no septiņiem patvaļīgiem naturāliem skaitļiem var izvēlēties divus tādus skaitļus, kuru kvadrātu starpība dalās ar :math:`11`.




*Atrisinājums:* Aprēķinām, kādus atlikumus pēc moduļa 11 dod naturālu skaitļu kvadrāti:

.. figure:: ../tests/worksheets/pigeonhole_2025_page7A.png
   :width: 246px

Tātad naturāla skaitļa kvadrāts, dalot ar :math:`11`, var dot tikai sešus dažādus atlikumus: :math:`0`, :math:`1`, :math:`3`, :math:`4`, :math:`5` vai :math:`9`. Tā kā doti septiņi skaitļi, tad no Dirihlē principa izriet, ka divu skaitļu kvadrāti, dalot ar :math:`11`, dod vienādus atlikumus. Izvēloties šos skaitļus, iegūstam vajadzīgo -- to kvadrātu starpība dalās ar :math:`11`.





7. Pēterītim bija :math:`100` aplīši, uz kuriem uzrakstīti naturālie skaitļi no 1 līdz 100 (uz katra aplīša cits skaitlis). Skolotāja lika izvēlēties 4 aplīšus un izvietot tos tā, lai būtu patiesa vienādība :math:`O + O = O + O`. Aplīši bija izbrūzīti uz grīdas, un līdz šī uzdevuma saņemšanai Pēteris bija paguvis savākt tikai :math:`21` aplīti. Vai ar tiem vienmēr noteikti pietika, lai izpildītu skolotājas uzdevumu?




*Atrisinājums:* No Pēterīša salasītajiem aplīšiem var izveidot :math:`\binom{21}{2} = 210` dažādu skaitļu pārus (pārus, kas atšķiras tikai ar aplīšu secību, uzskatām par vienādiem). Šos pārus tālākajā spriedumā uzskatīsim par "trušiem". Apskatām, kādas var būt vienā pārī ietilpstošo skaitļu summas. Mazākā summas vērtība ir :math:`1 + 1 = 2`; lielākā summas vērtība ir :math:`99 + 100 = 199`. Tātad pavisam iespējamas 197 dažādas summas vērtības: :math:`3; 4; 5; \ldots; 197; 198; 199`. Šīs dažādās vērtības uzskatām par "būrīem". Tā kā "trušu" ir vairāk nekā "būru", tad pēc Dirihlē principa kādā "būrī" ir vismaz divi "truši". Tas nozīmē, ka Pēterītim ir divi aplīšu pāri, kuros ietilpstošo skaitļu summas ir vienādas; pieņemsim, ka :math:`A + B = C + D` (pāri ir A, B un C, D). Pamatosim, ka neviens skaitlis neietilpst abos pāros. Ja, pieņemot, :math:`A = C`, tad no :math:`A + B = C + D` sekotu arī :math:`B = D` un pāri :math:`A, B` un :math:`C, D` nebūtu dažādi. Tāpat arī, ja atrastu aplīšus :math:`A, B, C, D` ir dažādi, tāpēc Pēterītim no tiem var izvietot vienādību :math:`A + B = C + D`.





8. Pierādīt, ka starp jebkuriem 35 divciparu skaitļiem var atrast trīs tādus skaitļus, kuru ciparu summas ir vienādas!




*Atrisinājums:* Izveidosim tabulu -- gar tās horizontālo rindu ierakstīsim visas iespējamās skaitļa pirmā cipara vērtības un gar vertikālo rindu -- pēdējā cipara vērtības. Tabulas rūtiņās ierakstīsim kolonnas un rindiņas numuru summu (sk. att.). Esam izveidojuši atbilstību starp skaitļiem un to ciparu summām.

.. figure:: ../tests/worksheets/pigeonhole_2025_page7B.png
   :width: 246px

Tabulā atrodami visi divciparu skaitļi no 10 līdz 99. Pavisam iespējamas 18 dažādas ciparu summas vērtības (varam izveidot 18 dažādas grupas). Ievērojam, ka
1) ciparu summa 1 un 18 katra ir tikai vienam skaitlim (10 un 99),
2) ciparu summa 2 un 17 katra ir tikai diviem skaitļiem (11; 20 un 89; 98). Tātad šajās grupās varāk skaitļu nevar būt neatkarīgi no tā, kādus 35 skaitļus izvēlamies.




 
Pieņemsim, ka šīs 4 grupas ir maksimāli piepildītas -- tajās kopā ievietoti 6 skaitļi. Tad atlikušajās 14 grupās jāievieto 29 skaitļi. Bet pēc Dirihlē principa noteikti ir tāda grupa, kurā ir vismaz trīs skaitļi -- tie arī ir meklētie trīs skaitļi, kuru ciparu summas ir vienādas.





9. Dots naturāls skaitlis :math:`n`, kas nedalās ar :math:`2` un :math:`5`. Pamatojiet, ka pastāv tāds skaitļa :math:`n` daudzkārtnis, kas sastāv tikai no vieniniekiem.




*Atrisinājums:* Apskatīsim :math:`n` skaitļus :math:`1`; :math:`11`; :math:`111`; :math:`1111`; :math:`\ldots` ; :math:`11 \cdots 1`. Šiem skaitļiem ir :math:`n` iespējamie atlikumi, dalot ar :math:`n`, tas ir, :math:`0, 1, 2, \ldots, n - 1`. Ja kādam no skaitļiem atlikums ir :math:`0`, tad tas ir meklētais daudzkārtnis. Pretējā gadījumā ir iespējami :math:`n-1` atlikumi un pēc Dirihlē principa būs divi tādi skaitļi, kuru starpība dalīsies ar :math:`n`. Šī starpība būs izskatā :math:`111 \cdots 100 \cdots 0`. Tā kā :math:`n` nedalās ar :math:`2` un :math:`5`, tad :math:`n` nevar saturēt nevienu 10-nieka pakāpi, tāpēc no skaitļa :math:`111 \cdots 100 \cdots 0` varam nodzēst nulles un tas vēl joprojām dalīsies ar :math:`n`. Rezultātā iegūstam skaitli, kas sastāv tikai no vieniniekiem un kas dalās ar :math:`n`, t. i., ir skaitļa n daudzkārtnis.




