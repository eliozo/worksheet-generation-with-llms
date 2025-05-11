

*Invariants – tas, kas paliek nemainīgs (kādā norisē, kādos apstākļos).*



 
Piemēram,
• mašīnas braukšanas ātrums visā ceļa posmā nav nemainīgs lielums, jo, uzsākot braucienu, tas ātrums ir nulle, bet kaut kādā ceļa posmā tas ir nemainīgs jeb invariants;
• pulksteņa rādītāja spicā gala attālums līdz centram, kur tas ir piestiprināts, ir nemainīgs jeb invariants, bet spicā gala attālums līdz skaitlim 12, pulksteņa rādītājam kustoties, nav nemainīgs.




 
Invariantu metode bieži ir lietojama tādu uzdevumu risināšanā, kuros tiek aplūkots kāds process – noteiktu darbību izpilde ar dotajiem lielumiem, un ir jāpierāda, ka no sākotnējiem datiem norādīto rezultātu NAV iespējams iegūt. Tad uzdevuma risinājumā var rīkoties pēc tālāk aprakstītā plāna.





**Teorēma:** Invariantu metode
Atrast piemērotu īpašību, kura
1) piemīt sākumā dotajiem lielumiem;
2) ir invarianta, tas ir, saglabājas, veicot pieļaujamās darbības;
3) nepiemīt tam lielumam, kas būtu jāiegūst galarezultātā.



 
Invariants atkarībā no uzdevuma var būt, piemēram, elementu skaits, summa, starpība, reizinājums, paritāte (būt pārā vai nepāra skaitlim), dalāmība ar 3, dalāmība ar 4, periodiskums.





Uzdevumu piemēri
-------------------------------------------------------------------------




1. Sākumā bija 10 papīra gabali. Dažus no tiem sagrieza vai nu 5, vai 7 daļās. Visus iegūtos gabalus sajauca un dažus no tiem atkal sagrieza vai nu 5, vai 7 daļās. Vai, tādā veidā turpinot, var iegūt tieši 999 papīra gabalus?




*Atrisinājums:* Atsinājums. Aplūkosim, kā izmainās kopējais gabalu skaits, atkarībā no tā, cik daļās tiek sagriezts viens gabals.

.. figure:: ../tests/worksheets/page1_a.png
   :width: 246px






 
Ievērojam, ka sākumā bija doti 10 papīra gabali – pāra skaitlis.
Ja papīra gabalu sagriež
• 5 daļās, tad kopējais gabalu skaits palielinās par 4 (par pāra skaitli), tātad tas bija pāra skaitlis un paliek pāra skaitlis, jo, saskaitot divus pāra skaitļus, iegūst pāra skaitli;
• 7 daļās, tad kopējais gabalu skaits palielinās par 6 (par pāra skaitli), tātad tas bija pāra skaitlis un paliek pāra skaitlis, jo, saskaitot divus pāra skaitļus, iegūst pāra skaitli.




 
Tātad kopējais papīra gabalu skaits vienmēr būs pāra skaitlis. Tā kā 999 ir nepāra skaitlis, tad tieši 999 papīra gabalus iegūt nevarēs. Uzdevums atrisināts.
INVARIANTS – kopējais papīra gabalu skaits vienmēr ir pāra skaitlis.





2. Uz tāfeles uzrakstīti skaitļi 1; 2; 3; ...; 10. Vienā gājienā var izvēlēties jebkurus divus no tiem un abiem pieskaitīt pa vieniniekam. Vai, atkārtojot šādus gājienus, var panākt, lai visi skaitļi kļūtu vienādi?




*Atrisinājums:* Atsinājums. Sākumā doto skaitļu summa ir nepāra skaitlis:

.. math::

    1+2+3+4+5+6+7+8+9+10=55

Katrā gājienā, pieskaitot pa vieniniekam diviem skaitļiem, visu skaitļu summa palielinās par 2 (par pāra skaitli). Pie nepāra skaitļa pieskaitot pāra skaitli, iegūst nepāra skaitli. Tātad visu skaitļu summa pēc katra gājiena paliek nepāra skaitlis.

Beigās prasīts iegūt desmit vienādus skaitļus, bet desmit vienādu skaitļu summa :math:`10 \cdot x` ir pāra skaitlis. Tātad nevar panākt, lai visi skaitļi kļūtu vienādi. Uzdevums atrisināts.

INVARIANTS – visu skaitļu summa vienmēr ir nepāra skaitlis.





3. Pamestā mājā dzīvo 2016 spoki. Spoku ķērājs vienā reizē var noķert vai nu tieši 33, vai tieši 17 spokus, bet tad uzreiz uzrodas attiecīgi vai nu 48, vai 14 jauni spoki. Vai iespējams, ka kādā brīdī šajā mājā būs tieši viens spoks?




*Atrisinājums:* Atsinājums. Aplūkosim, kā izmainās kopējais spoku skaits, atkarībā no tā, cik spoki tiek noķerti.

.. figure:: ../tests/worksheets/page2_a.png
   :width: 246px

Ievērojam, ka kopējais spoku skaits izmainās par skaitli, kas dalās ar 3.




 
**Atceries!**
Viens skaitlis dalās ar otru skaitli, ja šos skaitļus var izdalīt bez atlikuma.




 
Sākumā bija 2016 spoki – skaitlis, kas dalās ar 3, jo skaitļa 2016 ciparu summa ir :math:`2+0+1+6=9`, kas dalās ar 3, tātad arī pats skaitlis dalās ar 3.
Ja pie skaitļa, kas dalās ar 3, pieskaita vai no tā atņem skaitli, kas dalās ar 3, vienmēr iegūst skaitli, kas dalās ar 3, jo :math:`3k \pm 3m = 3 \cdot (k \pm m)`.
Tātad kopējais spoku skaits pēc katra ķēriena dalās ar 3. Tā kā skaitlis 1 nedalās ar 3, tad nav iespējams, ka kādā brīdī mājā būs tieši viens spoks. Uzdevums atrisināts.
INVARIANTS – kopējais spoku skaits vienmēr dalās ar 3.




 
**Iegaumē!**
Ja uzdevumā ir jautājums „Vai var...?”, „Vai iespējams...?” un atbilde ir
• **JĀ**, tad risinājumā jāpārāda piemērs, kurā visas uzdevuma prasības ir izpildītas;
• **NĒ**, tad ar dažu atsevišķu piemēru apskati, kuros neizdodas panākt vēlamo, nepietiek, bet ir vajadzīgs pierādījums, kas balstās uz vispārīgiem spriedumiem, ka tiešām nekādā gadījumā prasīto nebūs iespējams iegūt.





Paritāte
-------------------------------------------------------------------------




*Apskatīsim uzdevumus, kuru atrisināšanas pamatā ir viens apsvērums – "būt pāra vai nepāra skaitlim".*




4. Kvadrāts sastāv no :math:`4 \times 4` rūtiņām. Četras rūtiņas nokrāsotas melnas tā, ka katrā rindā un katrā kolonnā ir tieši viena melna rūtiņa. Vienā gājienā atļauts izvēlēties vienu rindu vai vienu kolonnu un mainīt tajā krāsojumu uz pretējo — melnās rūtiņas pārkrāsot baltas, bet baltās — melnas. Vai var gadīties, ka kvadrātā paliek tieši 3 melnas rūtiņas?




*Atrisinājums:* Atsinājums. Uzdevuma risinājumā gan rindas, gan kolonnas sauksim par līnijām.
Pieņemsim, ka kādā gājienā tiek izmainīts rūtiņu krāsojums līnijā :math:`t`. Tabulā apskatīsim, kā gājiena rezultātā mainās melno rūtiņu skaits līnijā :math:`t` un arī visā kvadrātā.
Apskatīsim visus gadījumus, kā var izvietot melnās rūtiņas uz līnijas :math:`t`:

.. figure:: ../tests/worksheets/page3_a.png
   :width: 246px

Secinām, ka jebkura gājiena rezultātā melno rūtiņu skaits kvadrātā mainās par pāra skaitli. Tā kā uzdevuma sākumā ir 4 melnās rūtiņas (pāra skaitlis), tad melno rūtiņu skaits nevar kļūt vienāds ar 3 (nepāra skaitlis). Uzdevums atrisināts.
INVARIANTS – melno rūtiņu skaits ir pāra skaitlis.





5. Uz tāfeles rindā uzrakstīti skaitļi 1, 2, 3, ..., 2014. Vienā gājienā atļauts nodzēst jebkurus divus blakus esošus skaitļus un to vietā uzrakstīt šo skaitļu starpību. Vai iespējams, ka, veicot atļautos gājienus, uz tāfeles paliek tikai viens vienīgs skaitlis 0?




*Atrisinājums:* Atsinājums. Izmantojot aritmētiskās progresijas locekļu summas formulu, aprēķinām uz tāfeles uzrakstīto skaitļu summu:

.. math::

    1+2+\cdots+2014=\frac{(1+2014)\cdot 2014}{2}=2015\cdot 1007

Šī summa ir nepāra skaitlis.
Ja tiek nodzēsti divi blakus esoši skaitļi :math:`a` un :math:`b`, un to vietā uzrakstīta šo skaitļu starpība :math:`(a-b)`, tad uz tāfeles uzrakstīto skaitļu summa samazinās par :math:`(a+b)-(a-b)=a+b-a+b=2b`, tas ir, par pāra skaitli.

Ja visu sākumā doto skaitļu summa ir NEPĀRA skaitlis, bet, nodzēšot divus blakus esošus skaitļus, uz tāfeles uzrakstīto skaitļu summa samazinās par pāra skaitli, tad, katrreiz atņemot no nepāra skaitļa pāra skaitli, iegūsim NEPĀRA skaitli. Līdz ar to skaitli 0 nevar iegūt, jo nulle ir pāra skaitlis. Uzdevums atrisināts.

INVARIANTS – skaitļu summa ir nepāra skaitlis.





6. Uz displeja ekrāna uzrakstīta burtu virkne XXOXOO. Burtu grupu XO var aizstāt ar OOXXOO, bet burtu grupu OOX var aizstāt ar burtu X. Vai, izpildot šādas operācijas, var iegūt burtu virkni OXOXOXOXOXOXOXO?




*Atrisinājums:* Atsinājums. Aplūkosim burtu X un burtu O skaita starpību.
Sākumā virknē šī burtu skaita starpība ir nulle, bet beigu virknē tā ir :math:`(-1)`.
Izdarot pirmā veida aizvietošanu, šī starpība samazinās par 2, bet, izdarot otrā veida aizvietošanu, tā palielinās par 2 (skat. tabulu).

.. figure:: ../tests/worksheets/page3_b.png
   :width: 246px

Redzam, ka ar katru pieļaujamo operāciju starp burtu O skaitu un burtu X skaitu mainās par pāra skaitli. Tā kā sākotnējā burtu virknē šī starpība ir nulle (pāra skaitlis), tad tā nevar beigu virknē kļūt vienāda ar nepāra skaitli (:math:`-1`). Uzdevums atrisināts.

INVARIANTS – X un O skaita starpība virknē, kas var iegūt uz ekrāna, ir pāra skaitlis.




 
**Dalāmība un specifiskas atlikumu vērtības**

Dažreiz par invarianto īpašību var izvēlēties, piemēram, īpašību “dalīties ar 3”, “dalot ar 3, dot atlikumu 1”, “dalot ar 3, dot atlikumu 2”, “dalīties ar 4” utt.

**Iegaumē!**

**Dalāmības pazīmes:**
- skaitlis dalās ar 2 (vai 5), ja tas beidzas ar pāra ciparu (ar 0 vai 5);
- skaitlis dalās ar 3 (vai 9), ja tā ciparu summa dalās ar 3 (vai 9);
- skaitlis dalās ar 11, ja tā ciparu summas, kas atrodas pāra pozīcijās, un ciparu summas, kas atrodas nepāra pozīcijās, starpība dalās ar 11.

Atlikums, ko iegūst, dalot naturālu skaitli ar 3 (vai 9), ir vienāds ar atlikumu, ko iegūst, dalot ar 3 (vai 9) šī skaitļa ciparu summu.





7. Ar naturālu skaitli drīkst izdarīt šādas operācijas:
a) reizināt ar 2;
b) dalīt ar 2, ja skaitlis ir pāra skaitlis;
c) pierakstīt galā to pašu skaitli (piemēram, ar šo operāciju no skaitļa 2015 var iegūt skaitli 20152015).
Vai ar šīm operācijām, izdarat tās vairākas reizes, no skaitļa 24 var iegūt skaitli 2015?




*Atrisinājums:* Atsinājums. Izpētīsim vispirms abus skaitļus: doto un to, kuru jāiegūst. Skaitlim 24 izpildās īpašība “dalās ar 3”, bet skaitlim 2015 šī īpašība nepiemīt.

Pierādīsim: ja kāds skaitlis dalās ar 3, tad skaitlis, kas no tā tiek iegūts ar šajā uzdevumā pieļaujamajām operācijām, arī dalīsies ar 3. Tiešām:

a) ja :math:`n` dalās ar 3, tad arī :math:`2n` dalās ar 3,
b) ja pāra skaitlis :math:`2n` dalās ar 3, tad :math:`n` dalās ar 3,
c) apgalvojums par trešo operāciju izriet no dalāmības pazīmes ar 3. Ja skaitļa :math:`n` ciparu summa dalās ar 3, tad arī jauniegūtā skaitļa :math:`nn` ciparu summa dalās ar 3, jo tā ir divreiz lielāka nekā sākotnējā skaitļa :math:`n` ciparu summa. Tātad arī pats jauniegūtais skaitlis :math:`nn` dalās ar 3.

Tā kā uzdevumā dotais skaitlis 24 dalās ar 3, tad arī visi skaitļi, kurus var iegūt no 24, dalās ar 3. Bet skaitlis 2015 ar 3 nedalās, tādēļ ar uzdevumā dotajām operācijām skaitli 2015 nevarēs iegūt. Uzdevums atrisināts.

INVARIANTS – visi iegūtie skaitļi dalās ar 3.





8. Uz tāfeles ir uzrakstīti cipari 2, 3, 4, 5. Atļauts izvēlēties dažus no tiem un sastādīt no tiem skaitli A. Pēc tam skaitli A reizināt ar 13, un ciparus, kurus iegūst reizināšanas rezultātā, uzraksta uz tāfeles izvēlēto ciparu vietā. (Piemēram, izvēloties ciparus 2, 3, 4, varam no tiem sastādīt skaitli A = 324 un iegūt skaitli 13 \cdot A = 13 \cdot 324 = 4212, pie tam cipars 2 tiek iegūts divas reizes. Tagad uz tāfeles ir uzrakstīti cipari 1, 2, 2, 4, 5). Vai var aprakstīto operāciju palīdzību var panākt, ka uz tāfeles būs uzrakstīti cipari: 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7?




*Atrisinājums:* Atsinājums. Izmantosim, ka naturāls skaitlis, dalot to ar 3, dod tādu pašu atlikumu, kādu dod šī skaitļa ciparu summa, dalot to ar 3.

Ja vienas operācijas izpildes sākumā izvēlēto ciparu summa, dalot ar 3, dod atlikumu :math:`r`, tad tādu pašu atlikumu :math:`r` dod arī no šiem cipariem izveidotais skaitlis :math:`A`. Tā kā :math:`13A = A + 12A` un :math:`12A` dalās ar 3, tad tādu pašu atlikumu :math:`r`, dalot ar 3, dod arī jauniegūtais skaitlis :math:`13A`; tātad tādu pašu atlikumu :math:`r`, dalot ar 3, dod arī to ciparu summa, kurus pēc operācijas izpildes beigās uzraksta uz tāfeles sākumā izvēlēto ciparu vietā. Tātad operācijas izpildes gaitā nemainās uz tāfeles uzrakstīto ciparu summas atlikums, dalot ar 3.

Ievērosim, ka sākumā uzrakstīto ciparu summa ir 14, un tā dod atlikumu 2, dalot ar 3. Tātad visām ciparu virk­nēm, kas parādās uz tāfeles, ir atlikums 2, dalot to summu ar 3.

Bet galarezultātā prasītās virknes ciparu summa ir:

.. math::

    (2+2+3+3+4+4+5+5+6+6+7+7)=2\cdot 27=54;

tā dod atlikumu 0, dalot ar 3.

Tātad prasīto ciparu virkni nevar iegūt. Uzdevums atrisināts.

INVARIANTS – uz tāfeles esošo ciparu summa, dalot to ar 3, dod atlikumu 2.





Periodiskums
-------------------------------------------------------------------------




9. Bezgalīgu skaitļu virkni 1; 2; 3; 5; 8; 3; 1; 4; 5; 9; 4; 3; 7; 0; 7; 7; ... veido pēc šāda likuma: pirmie divi skaitļi ir 1 un 2, bet katrs nākamais skaitlis, sākot ar trešo, ir divu iepriekšējo skaitļu summas pēdējais cipars. Vai šajā skaitļu virknē kaut kur blakus atrodas skaitļi 2 un 4?




*Atrisinājums:* Atsinājums. Pāra skaitļus apzīmēsim ar :math:`p`, bet nepāra skaitļus – ar :math:`n`.
Ievērojam, ka :math:`n+n=p`; :math:`n+p=n`; :math:`p+n=n`; :math:`p+p=p`.
Tā kā virknes locekļus nosaka divu iepriekšējo skaitļu summas pēdējais cipars, tad tā veidojas šādi:

.. math::

    n; p; n; p; n; p; n; p; n; p; n; p; n; p; n; p; \ldots

Šajā virknē periodiski atkārtojas grupa :math:`(n; p; n)`. Virknē nekur blakus neatrodas divi pāra skaitļi, tādēļ šajā virknē nekur blakus neatradīsies skaitļi 2 un 4. Uzdevums atrisināts.

INVARIANTS – virknē periodiski atkārtojas grupa :math:`(n; p; n)`.





Sarežģītāki invarianti
-------------------------------------------------------------------------




10. Rindā uzrakstīti 2015 vieninieki. Atļauts nodzēst jebkurus divus uzrakstītus skaitļus :math:`a` un :math:`b` un to vietā uzrakstīt vienu jaunu skaitli :math:`\frac{a+b}{4}`. Tā turpina, kamēr paliek uzrakstīts viens skaitlis. Vai var gadīties, ka tas ir mazāks nekā 0,0001?




*Atrisinājums:* Atsinājums. Pieņemsim, ka tiek nodzēsti skaitļi :math:`a` un :math:`b` un to vietā uzrakstīts skaitlis :math:`\frac{a+b}{4}`.

Pierādīsim, ka

.. math::

    \frac{1}{a}+\frac{1}{b} \geq \frac{1}{\frac{a+b}{4}} \quad (1)

tas ir, katra gājiena rezultātā visu uzrakstīto skaitļu apgriezto lielumu summa nepalielinās.

Veicot ekvivalentus pārveidojumus, pakāpeniski iegūstam:

.. math::

    \frac{a+b}{ab} \geq \frac{4}{a+b}

:math:``(a+b)^2 \geq 4ab:math:``

.. math::

    a^2+2ab+b^2 \geq 4ab

:math:``a^2-2ab+b^2 \geq 0:math:``

.. math::

    (a-b)^2 \geq 0

Pēdējā nevienādība ir patiesa, jo izteiksmes kvadrāts vienmēr ir nenegatīvs. Tā kā tika veikti ekvivalentie pārveidojumi, tad arī nevienādība (1) ir patiesa.

Sākumā visu uzrakstīto skaitļu apgriezto lielumu summa ir :math:`2015 \cdot \frac{1}{1}=2015`; tātad arī beigās tā nav lielāka kā 2015.

Ja beigās palikušo vienīgo skaitli apzīmējam ar :math:`x`, tad šī summa ir :math:`\frac{1}{x}`; tāpēc :math:`\frac{1}{x} \leq 2015` un

.. math::

    x \geq \frac{1}{2015} > \frac{1}{10000}=0,0001.

Tātad beigās uz tāfeles uzrakstītais skaitlis nevar būt mazāks kā 0,0001. Uzdevums atrisināts.

INVARIANTS – visu ierakstīto skaitļu apgriezto lielumu summa vienmēr lielāka vai vienāda ar 2015.




 
**Par kādu bieži sastopamu kļūdu**

Gadījumos, kad zināms, ka kāda īpašība piemīt sākotnējam lielumam, saglabājas izpildāmo gājienu rezultātā un piemīt arī beigās vajadzīgajam rezultātam, tad šī informācija vien vēl **neļauj secināt**, vai vajadzīgais beigu rezultāts iegūstams no sākotnējā lieluma, izpildot pieļautos gājienus. Tādos gadījumos uzdevuma risināšanai jāmeklē citi invarianti, varbūt veids, kā iegūt vajadzīgo gala rezultātu, utt.

Ja izdodas atrast īpašību, kas
- **piemīt** sākumā dotajiem lielumiem,
- ir invarianta, t.i., **saglabājas**, veicot pieļaujamās operācijas,
- **piemīt** tiem lielumiem, kuri jāiegūst gala rezultātā,

tad no tā vien vēl **nevar secināt**, ka gala rezultātā vajadzīgos lielumus tiešām varēs iegūt.





11. Uz tāfeles uzrakstīts skaitlis 2016. Ar vienu gājienu tam var vai nu pieskaitīt 12, vai atņemt 18. Vai, daudzkārt izdarat šādus gājienus, var iegūt skaitli 1000?



 
**Kurš no risinājumiem ir pareizs?**

**Jānīša risinājums.** Sākumā dotais skaitlis ir pāra skaitlis. Gan 12, gan 18 arī ir pāra skaitļi. Pāra skaitlim pieskaitot vai no tā atņemot pāra skaitli, iegūst pāra skaitli. Tātad uz tāfeles visu laiku parādīsies tikai pāra skaitļi. Arī beigās iegūstamais skaitlis 1000 ir pāra skaitlis. Tātad to **var** iegūt ar norādītajām darbībām.

**Pēterīša risinājums.** Sākumā dotais skaitlis dalās ar 3. Gan 12, gan 18 arī dalās ar 3. Ja skaitlim, kas dalās ar 3, pieskaita vai no tā atņem skaitli, kas dalās ar 3, tad atkal iegūst skaitli, kas dalās ar 3. Tātad uz tāfeles visu laiku parādīsies tikai tādi skaitļi, kas dalās ar trīs. Bet beigās iegūstamais skaitlis 1000 ar 3 nedalās. Tātad to **nevar** iegūt ar norādītajām darbībām.

**Pēterīša spriedums ir pareizs, bet Jānīša spriedums ir kļūdains.**
Jānītis savā risinājumā koncentrējās uz īpašību “būt pāra skaitlim”. Viņš atzīmēja, ka šī īpašība piemīt gan visiem skaitļiem, kurus var iegūt, gan arī skaitlim 1000, par kura iegūšanas iespējamību jautāts uzdevumā. Tādējādi Jānītis konstatēja, ka ar skaitļa paritāti saistīti apsvērumi **netraucē** skaitļa 1000 iegūšanai. Bet no tā vēl neizriet, ka 1000 iegūšanai netraucē nekādi citi apsvērumi! Gluži otrādi, kā to savā risinājumā atradis Pēterītis, dalāmība ar 3 ir apsvērums, kas parāda, ka 1000 ar atļautajiem gājieniem nevar iegūt.

Situācija ir apmēram tāda pati, kāda rastos, ja Jānītim un Pēterītim būtu uzdots noskaidrot, vai celiņu cauri džungļiem no Mumbo ciema uz Tumbo ciemu neapdraud nekādas briesmas. Jānītis, ķīmiski analizējot gaisa sastāvu, neklūdīgi noskaidro, ka ceļā tuvumā nav neviena lauvas, un no tā secina, ka var droši doties ceļā. Turpretī Pēterītis koncentrējas uz jaguāru meklēšanu un konstatē, ka 10 metrus no celiņa guļ veselā jaguāru saime. Kādi no šiem secinājumiem ir pareizs, varat saprast paši.





Uzdevumi treniņam
=====================================================================




5.-8. klasei
-------------------------------------------------------------------------




1. Niknajam jūras laupītājam Smuīdim ir četras kaudzes ar zelta monētām. Viņš māk vienu kaudzi sadalīt 3 vai 5 mazākās kaudzēs. Vai, atkārtoti izpildot šādas darbības, Smuīdirs varēs iegūt tieši 2015 kaudzes, ko piešķirt saviem palīgiem?




2. Bagātajai Austrumu princesei Smuidrai zem gultas ir 6 lādes. Sākumā lādēs ir attiecīgi 1, 5, 0, 0, 2, 3 zelta monētas. Katru stundu viņa izvēlas 2 lādes un katrā no tām pieliek klāt 1 monētu. Vai, atkārtoti izpildot šādas darbības, var panākt, ka kādā brīdī visās lādēs būs vienāds skaits monētu?




3. Sensenos laikos saimnieciskajam Gotfrīdam bija 99 aitas un 21 kamielis, un viņa mājlopu Gotfrīdam nebija. Bagdadē par 4 kamieļiem pretī varēja saņemt 8 aitas, bet Damaskā par 5 aitām pretī varēja saņemt 3 kamieļus. Vai, atkārtoti mainot dzīvniekus tikai šajās divās pilsētās, Gotfrīds varēja iegūt tieši 2015 mājlopus?




4. Autoserviss „Šrotiņš” ir 39 mašīnas. Naskais Maigonis katra mēneša 20. datumā vienu pārdod 7 restaurētas mašīnas un to vietā nopērk 16 vecas mašīnas, vai arī 19 mašīnas nodedz metāllūžņos un to vietā nopērk 4 vecas mašīnas. Nekādas citas darbības, kas maina mašīnu skaitu, netiek veiktas. Vai iespējams, ka „Šrotiņā” kādā mēneša 21. datumā būs tieši 2015 mašīnas?




9.-12. klasei
-------------------------------------------------------------------------




5. Regulārā astoņstūra virsotnēs pēc kārtas uzrakstīti skaitļi 7, 15, 3, 17, 1, 9, 5, 11. Ar skaitļiem atļauts veikt šādas darbības:
- pieskaitīt kādam skaitlim divus skaitļus, kas atrodas blakus virsotnēs;
- atņemt no skaitļa divkāršotu pretējā virsotnē uzrakstīto skaitli, ja starpība ir pozitīva.

Vai, atkārtoti izpildot šīs darbības, var panākt, ka vienā no virsotnēm būs ierakstīts skaitlis 2014?




6. Ar naturālu skaitli atļauts veikt šādas darbības:
- pieskaitīt 6;
- dalīt ar 4, ja skaitlis dalās ar 4;
- mainīt vietām skaitļa ciparus (skaitļa sākumā nedrīkst atrasties nulle).

Vai, atkārtoti izpildot šīs darbības, no skaitļa 30 var iegūt skaitli 2015?




7. Vienā gājienā no 1. att. dotās figūras var izvēlēties jebkuru 2. att. redzamo figūru (var arī pagriezt) un tajā ierakstītajiem skaitļiem vai nu pieskaitīt 1, vai arī atņemt 1. Vai, atkārtoti izpildot šādus gājienus, var panākt, ka visās šūnās ir ierakstīts skaitlis 2015?

.. figure:: ../tests/worksheets/page7_a.png
   :width: 246px

![](page7_b.png)






8. Ar naturālu skaitli atļauts izdarīt šādas darbības:
- pieskaitīt skaitlim tā ciparu summu;
- atņemt no skaitļa tā ciparu summu.

Vai, atkārtoti izpildot šīs darbības, no skaitļa 139 var iegūt skaitli a) 63; b) 193?




Uzdevumu atrisinājumi
=====================================================================




1. Niknajam jūras laupītājam Smuīdim ir četras kaudzes ar zelta monētām. Viņš māk vienu kaudzi sadalīt 3 vai 5 mazākās kaudzēs. Vai, atkārtoti izpildot šādas darbības, Smuīdirs varēs iegūt tieši 2015 kaudzes, ko piešķirt saviem palīgiem?




*Atrisinājums:* Atsinājums. Ievērojam, ka sākumā bija 4 kaudzes — pāra skaitlis.
Ja vienu kaudzi sadala:
- 3 daļās, tad kopējais kaudzīšu skaits palielinās par 2 (par pāra skaitli);
- 5 daļās, tad kopējais kaudzīšu skaits palielinās par 4 (par pāra skaitli).
Tātad kopējais kaudzīšu skaits vienmēr būs pāra skaitlis. Tā kā 2015 ir nepāra skaitlis, tad tieši 2015 kaudzēs iegūt nevarēs.





2. Bagātajai Austrumu princesei Smuidrai zem gultas ir 6 lādes. Sākumā lādēs ir attiecīgi 1, 5, 0, 0, 2, 3 zelta monētas. Katru stundu viņa izvēlas 2 lādes un katrā no tām pieliek klāt 1 monētu. Vai, atkārtoti izpildot šādas darbības, var panākt, ka kādā brīdī visās lādēs būs vienāds skaits monētu?




*Atrisinājums:* Atsinājums. Sākumā lādēs esošo monētu kopējais skaits ir nepāra skaitlis:

.. math::

    1+5+0+0+2+3=11

Katru stundu, pieliekot pa vienai monētai katrā no divām izvēlētajām lādēm, visu monētu kopējais skaits palielinās par 2 (par pāra skaitli). Neviena skaita pieaugšana par pāra skaitli nepārvērtīs nepāra skaitli pāra skaitlī. Tātad visos lādēs vienāds monētu skaits nevar tikt sasniegts, jo tas prasītu pāra skaitli.





3. Sensenos laikos saimnieciskajam Gotfrīdam bija 99 aitas un 21 kamielis, cu mājlopu Gotfrīdam nebija. Bagdadē par 4 kamieļiem pretī varēja saņemt 8 aitas, bet Damaskā par 5 aitām pretī varēja saņemt 3 kamieļus. Vai, atkārtoti mainot dzīvniekus tikai šajās divās pilsētās, Gotfrīds varēja iegūt tieši 2015 mājlopus?




*Atrisinājums:* Atsinājums. Ievērojam, ka sākumā kopējais mājlopu skaits ir

.. math::

    99+21=120

— pāra skaitlis.
Ja par 4 kamieļiem var saņemt 8 aitas, kopējais mājlopu skaits palielinās par 4 (par pāra skaitli);
Ja par 5 aitām pretī saņem 3 kamieļus, kopējais mājlopu skaits samazinās par 2 (par pāra skaitli).
Tātad kopējais mājlopu skaits vienmēr būs pāra skaitlis. Tā kā 2015 ir nepāra skaitlis, tad tieši 2015 mājlopus iegūt nevarēs.





4. Autoserviss „Šrotiņš” ir 39 mašīnas. Naskais Maigonis katra mēneša 20. datumā vienu pārdod 7 restaurētas mašīnas un to vietā nopērk 16 vecas mašīnas, vai arī 19 mašīnas nodedz metāllūžņos un to vietā nopērk 4 vecas mašīnas. Nekādas citas darbības, kas maina mašīnu skaitu, netiek veiktas. Vai iespējams, ka „Šrotiņā” kādā mēneša 21. datumā būs tieši 2015 mašīnas?




*Atrisinājums:* Atsinājums. Aplūkosim, kā izmainās kopējais mašīnu skaits, atkarībā no, kuru darbību Maigonis veic:
- pārdod 7 restaurētas mašīnas un nopērk 16 vecas mašīnas: kopējais skaits palielinās par 9;
- nodedzina 19 mašīnas un nopērk 4 vecas mašīnas: kopējais skaits samazinās par 15.

Gan 9, gan -15 ir skaitļi, kas dalās ar 3.
Sākotnēji mašīnu skaits ir 39, kas dalās ar 3.
Veicot katru no pieļaujamām darbībām, kopējais skaits mainās par skaitli, kas dalās ar 3.
Tātad visos gadījumos mašīnu skaits dalās ar 3.
Skaitlis 2015 ar 3 nedalās, jo :math:`2+0+1+5=8` un :math:`8 \mod 3 = 2`.
Tātad nav iespējams, ka „Šrotiņā” kāda mēneša 21. datumā būs tieši 2015 mašīnas.





5. Regulārā astoņstūra virsotnēs pēc kārtas uzrakstīti skaitļi 7, 15, 3, 17, 1, 9, 5, 11. Ar skaitļiem atļauts veikt šādas darbības:
- pieskaitīt kādam skaitlim divus skaitļus, kas atrodas blakus virsotnēs;
- atņemt no skaitļa divkāršotu pretējā virsotnē uzrakstīto skaitli, ja starpība ir pozitīva.

Vai, atkārtoti izpildot šīs darbības, var panākt, ka vienā no virsotnēm būs ierakstīts skaitlis 2014?




*Atrisinājums:* Atsinājums. Visi skaitļi, kas uzrakstīti regulārā astoņstūra virsotnēs, sākumā ir nepāra skaitļi.
Ievērojam, ja:
1) nepāra skaitlim pieskaita divus nepāra skaitļus, iegūst nepāra skaitli;
2) nepāra skaitlim atņem pāra skaitli, iegūst nepāra skaitli.
Tāpēc neatkarīgi no tā, cik reizes abas darbības tiek izpildītas, virsotnēs vienmēr būs nepāra skaitļi.
Tā kā 2014 ir pāra skaitlis, tas nevar tikt ierakstīts kādā virsotnē.





6. Ar naturālu skaitli atļauts veikt šādas darbības:
- pieskaitīt 6;
- dalīt ar 4, ja skaitlis dalās ar 4;
- mainīt vietām skaitļa ciparus (skaitļa sākumā nedrīkst atrasties nulle).

Vai, atkārtoti izpildot šīs darbības, no skaitļa 30 var iegūt skaitli 2015?




*Atrisinājums:* Atsinājums. Skaitlim 30 īpašība "dalās ar 3", bet skaitlim 2015 šī īpašība nepieder.
Pierādīsim: ja kāds skaitlis dalās ar 3, tad veicot jebkuru no uzdevumā dotajām darbībām, arī rezultāts dalās ar 3.
Ievērojam, ja:
- skaitlis k dalās ar 3, tad arī (k+6) dalās ar 3 (jo katrs saskaitāmais dalās ar 3, tad arī summa dalās ar 3);
- ja skaitlis dalās ar 4 un ar 3, tad arī k/4 dalās ar 3 (jo piemērojami reizinātāji);
- apgalvojums "mainīt vietām skaitļa ciparus" ir no dalāmības pazīmes ar 3 (ja skaitļa ciparu summa dalās ar 3, tad arī paša skaitļa ciparu permutācija dod skaitli, kas dalās ar 3).
Tātad, ja dots skaitlis dalās ar 3, tad arī pēc darbību atkārtotas pielietošanas jauniegūtais skaitlis dalās ar 3.
Tā kā 2015 ar 3 nedalās, tad to nevar iegūt.





7. Vienā gājienā no 1. att. dotās figūras var izvēlēties jebkuru 2. att. redzamo figūru (var arī pagriezt) un tajā ierakstītajiem skaitļiem vai nu pieskaitīt 1, vai arī atņemt 1. Vai, atkārtoti izpildot šādus gājienus, var panākt, ka visās šūnās ir ierakstīts skaitlis 2015?

.. figure:: ../tests/worksheets/page7_a.png
   :width: 246px

![](page7_b.png)






*Atrisinājums:* Atsinājums. Šūnās ierakstītie skaitļi 1, 2, ..., 19 veido aritmētisko progresiju ar diferenci 1.
Izmantojot aritmētiskās progresijas locekļu summas formulu, aprēķinām sākumā šūnās ierakstīto skaitļu summu:

.. math::

    \frac{(1+19) \cdot 19}{2}=190.

Ja katrā šūnā ir ierakstīts skaitlis 2015, tad visu šūnu summa ir

.. math::

    2015 \times 19=38285.

Ievērosim, ka ar katru izdarīto gājienu, pie trim vai četrām blakus esošām šūnām pieskaita vai atņem 1, un tā rezultātā visu šūnu kopējā summa palielinās vai samazinās par 3 vai 4. Tā kā skaitļi 3 un 4 dalās ar 1, tad kopējā summa var mainīties par jebkuru naturālu skaitli.
Tādēļ var atrast tādu gājienu virkni, kas sākotnējo summu 190 pārvērš summā 38285 un tālāk, ja nepieciešams, sadala korekti skaitļus šūnās.





8. Ar naturālu skaitli atļauts izdarīt šādas darbības:
- pieskaitīt skaitlim tā ciparu summu;
- atņemt no skaitļa tā ciparu summu.

Vai, atkārtoti izpildot šīs darbības, no skaitļa 139 var iegūt skaitli a) 63; b) 193?




*Atrisinājums:* Atsinājums. a) Skaitli 63 var iegūt šādi:

.. math::

    139-13=126-9=117-9=108-9=99-18=81-18=63.

b) Atlikums, ko iegūst, dalot naturālu skaitli ar 9, ir vienāds ar atlikumu, ko iegūst, dalot ar 9 šī skaitļa ciparu summu. Tāpēc naturāla skaitļa un tā ciparu summas starpība noteikti dalās ar 9. Kaut vienu reizi izpildot atņemšanas variantu, visu starpā iegūstamie skaitļi dalīsies ar 9.

Tā kā sākumā dots skaitlis 139, tas ar 9 nedalās, tāpēc, ja skaitlim visu laiku pieskaita tā ciparu summu, skaitlis palielināsies. Skaitļi pārvērtīsies šādi:

.. math::

    139+13=152+8=160+7=167+14=181+11=192+12=204+6=210+3=213\rightarrow \dots

Visi tālāk iegūstamie skaitļi ir lielāki nekā 193, tātad skaitli 193 nevarēs iegūt.




