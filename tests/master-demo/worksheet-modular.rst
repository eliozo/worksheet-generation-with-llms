

Modulārā aritmētika caur pasaku piemēriem
=====================================================================




Iesildīšanās: Kas notiek ar atlikumiem?
-------------------------------------------------------------------------




Vinnijs Pūks atrada 17 medus burciņas un katru dienu spēj apēst tikai veselu burciņu. Pēc cik dienām viņam būs palikušas tieši :math:`3` burciņas, ja viņš katru dienu apēd :math:`4` burciņas (un nekā neslēpj)? Kādu darbību šeit vajadzētu izmantot?
(sk. `NEW <https://www.dudajevagatve.lv/eliozo/problem?problemid=NEW>`_)




Noderīgas definīcijas un likumi
-------------------------------------------------------------------------




**Teorēma:** Modulārā aritmētika: Sacīsim, ka divi skaitļi ir kongruenti pēc moduļa :math:`n`, ja tiem dalot ar :math:`n`, atlikumi ir vienādi (piem., :math:`15 \equiv 3 \pmod{12}`, jo abiem atlikums ir :math:`3`).




**Teorēma:** Atlikums: Sadala skaitli :math:`a` ar veselu :math:`n`, iegūst dalījumu :math:`a=qn+r`, kur atlikums :math:`r` vienmēr ir :math:`0 \leq r < n`.




**Teorēma:** Paritāte: Skaitļi ir vai nu pāra (dalās ar :math:`2`, atlikums :math:`0`) vai nepāra (saliekot jebkuru skaitli ar :math:`2`, atlikumā ir :math:`1`).




**Teorēma:** Periodiskums decimāldaļās: Ja veidojam dalījuma :math:`1/n` decimāldaļu, decimālpieraksta cipari pēc brīža sāk atkārtoties ar noteiktu periodu, kas saistīts ar modulāro aritmētiku.




Galvenie uzdevumi — Vai Sniegbaltīte arī prot atlikumus?
-------------------------------------------------------------------------




Tumšā rudens vakarā Māris izdomāja saskaitīt visus naturālos skaitļus no :math:`1` līdz :math:`n`, kur :math:`n` ir kāds naturāls skaitlis. Vai var gadīties, ka Māris ieguva summu, kuras pēdējais cipars ir (A) :math:`8`, (B) :math:`9`?
(sk. `LV.AMO.2022B.6.3 <https://www.dudajevagatve.lv/eliozo/problem?problemid=LV.AMO.2022B.6.3>`_)




Vai var atrast tādus veselus skaitļus :math:`a` un :math:`b`, kuriem izpildās vienādība :math:``a \cdot (3a+5b)\cdot 7b = 7654321:math:``?
(sk. `LV.AMO.2014.7.2 <https://www.dudajevagatve.lv/eliozo/problem?problemid=LV.AMO.2014.7.2>`_)




Sniegbaltītei un 7 rūķīšiem patīk dejot aplī. Katrreiz pēc :math:`5` dziesmas notīm, dejo nākamais rūķītis. Ja mūzika atskan :math:`23` reizes, kurš rūķītis ir pie Sniegbaltītes beigās, ja sākumā pirmais rūķītis bija blakus?
(sk. `NEW <https://www.dudajevagatve.lv/eliozo/problem?problemid=NEW>`_)




Triju veselu pozitīvu skaitļu summa ir :math:`407`. Ar kādu lielāko daudzumu nullīšu var beigties šo skaitļu reizinājums?
(sk. `LV.AMO.2005.7.4 <https://www.dudajevagatve.lv/eliozo/problem?problemid=LV.AMO.2005.7.4>`_)




Vinnijs Pūks vāra burkā medu. Viņš lieto tikai :math:`2`, :math:`3`, :math:`7` un :math:`8` kā pēdējos ciparus saviem burku kodiem. Vai iespējams, ka viens burkas numurs ir tieši trīs reizes lielāks par kādu citu, ja abus kodus veido tikai šie cipari?
(sk. `NEW <https://www.dudajevagatve.lv/eliozo/problem?problemid=NEW>`_)




Atrodi naturālu skaitli, kuru, dalot ar :math:`2010`, atlikumā iegūst :math:`13`, bet, dalot ar :math:`2011`, atlikumā iegūst :math:`3`.
(sk. `LV.AMO.2011.7.3 <https://www.dudajevagatve.lv/eliozo/problem?problemid=LV.AMO.2011.7.3>`_)




Norādes uzdevumu risināšanai
-------------------------------------------------------------------------




*1. Ievaduzdevumā vari pārbaudīt atlikumu dažādas dienas, domājot par dalījumu ar atlikumu. 2. Skaties tabulā, kā periodiski atkārtojas pēdējie cipari summām! 3. Atrodi vismaz vienu atlikuma īpašību vai spried par pāra/nepāra rezultātu. 4. Iedomājies rūķīšus kā skaitļu pulku, kas rotē aplī — mēģini aprēķināt atlikumus! 5. Par reizinājuma nullēm — aprēķini, cik $2$ un $5$ reizinātāju ir kopā. 6. Skaitļu kodi: dari līdzīgi kā ar pirkstu cipariem — pārbaudi iespējamās vērtības! 7. Sistēmām ar diviem moduļiem — atrodi tādu skaitli, kas abās dalīšanās reizēs dod izteikto atlikumu.*




Atrisinājumi
-----------------------------------------------











**NEW**
Atbildi var iegūt, dalot :math:`17` ar :math:`4` – atlikumā būs :math:`1` (jo :math:`4 \cdot 4 = 16`, atlikums :math:`1`), bet viņš grib lai atlikumā būtu :math:`3`. To var atrast, izsekojot atlikumiem: pēc :math:`1` dienas – :math:`13`, pēc :math:`2` – :math:`9`, pēc :math:`3` – :math:`5`, pēc :math:`4` – :math:`1`, pēc :math:`5` – nav iespējams (negatīvs atlikums). Tātad Pūks nevar tieši iegūt :math:`3` burciņas šādā veidā.





























**LV.AMO.2022B.6.3**
(A) Jā, piemēram, :math:`1+2+\cdots+7=28`. (B) Nē, neatkarīgi no :math:`n` pēdējais cipars nevar būt :math:`9`. Skaitīšanas laikā pēdējie cipari summām veido periodisku virkni.





**LV.AMO.2014.7.2**
Nē, nevar. Pa kreisi reizinājums vienmēr ir pāra skaitlis (jo vismaz viens no reizinātājiem ir pāra vai arī :math:`3a+5b` kļūst pāra, ja abi :math:`a` un :math:`b` ir nepāra), bet :math:`7654321` ir nepāra skaitlis.





**NEW**
Katra :math:`5` nots pārbīda kārtību, pēc :math:`23` reizēm ieņemto vietu var atrast, dalot :math:`23` ar :math:`7` (jo rūķu ir :math:`7`). :math:`23 \div 7 = 3` pilni apļi un atlikums :math:`2`, tādēļ tas ir :math:`1+2=3` rūķītis.





**LV.AMO.2005.7.4**
Atbilde: ar :math:`6` nullēm. Piemērs :math:`250 \cdot 125 \cdot 32=1000000`. Nevar iegūt vairāk nullīšu, jo ar :math:`5` dalāmo pakāpe visiem saskaitāmajiem kopā nepārsniedz :math:`6`.





**NEW**
Nē, jo, ja reizina ar :math:`3` šos ciparus, rezultātā pēdējais cipars (attiecīgi :math:`6`, :math:`9`, :math:`1`, :math:`4`) nevar būt kādā no atļautajiem.





**LV.AMO.2011.7.3**
Tāds skaitlis ir :math:`20113`, jo :math:`20113 = 2010 \cdot 10 + 13 = 2011 \cdot 10 + 3`.










