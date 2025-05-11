Consider the following style rules how to improve a math worksheet in Latvian: 
```
[
    {
        "id": "P006A",
        "original": "*Kāds ir mazākais* (1) sešciparu skaitlis, kas sastāv tikai no cipariem 2, 0, 1, 3 un dalās ar 9?",
        "modified": "Atrodiet  mazāko sešciparu skaitli, kas sastāv tikai no cipariem 2, 0, 1, 3 un dalās ar 9.",
        "explanations": "(1) \"Kāds ir mazākais\" should be replaced by \"Atrodiet mazāko\" since there is a unique object the problem talks about."
    },
    {
        "id": "P006B",
        "original": "Vai eksistē tādi naturāli skaitļi a un b, *ka* (1): 8⋅a−12⋅b=2023.",
        "modified": "Vai eksistē tādi naturāli skaitļi a un b, lai 8⋅a−12⋅b=2023.",
        "explanations": "(1) Replace \"ka\" by \"lai\" to express intention."
    },
    {
        "id": "P006C",
        "original": "Cik *4-centu* (1) pastmarku *nepieciešams* (2), lai izveidotu *vērtību 35 centi* (3), izmantojot tikai 4-centu (1) un 9-centu (1)  pastmarkas?",
        "modified": "Cik 4 centu pastmarku var izmantot, lai izveidotu 35 centu vērtību, izmantojot tikai 4 centu un 9 centu pastmarkas?",
        "explanations": "(1) Expression \"4 centu pastmarka\" (space with no hyphen) is a correct usage.\n(2) \"nepieciešams\" is ambiguous here -- either write \"cik pastmarku minimāli nepieciešams\" (what is the least necessary number of postage stamps), or \"cik pastmarku var izmantot\" (how. many postage stamps can be used). \n(3) \"35 centu vērtība\" is the appropriate word order. "
    },
    {
        "id": "P006D",
        "original": "*Cik ir* (1) lielākā iespējamā ciparu summa septiņciparu naturālam skaitlim, kas dalās ar 8?",
        "modified": "Kāda ir lielākā iespējamā ciparu summa septiņciparu naturālam skaitlim, kas dalās ar 8?",
        "explanations": "(1) Regarding \"summa\" (a sum) one should say \"kāda ir\" rather than \"cik ir\"."
    },
    {
        "id": "P006E",
        "original": "Vai skaitļa kvadrāts *noteikti ir* (1)  lielāks *nekā* (2) pats skaitlis?",
        "modified": "Vai skaitļa kvadrātam noteikti jābūt lielākam par pašu skaitli?",
        "explanations": "(1) \"noteikti jābūt\" is better here compared to \"noteikti ir\" as it is about the necessity (not about already existing numbers).\n(2) \"lielāks par\" is better compared to \"lielāks nekā\" as \"nekā\" points to a certain, defined number (rather than a square that is a variable quantity)."
    },
    {
        "id": "P006F",
        "original": "Vai vienmēr, *negatīvam skaitlim pieskaitot* (1) tā kvadrātu, iegūst pozitīvu skaitli (2)?",
        "modified": "Vai vienmēr, pieskaitot negatīvam skaitlim tā kvadrātu, iegūst pozitīvu rezultātu?",
        "explanations": "(1) In \"pieskaitot negatīvam skaitlim\" the word order focuses on the action verb \"pieskaitīt\".\n(2) Avoid repetition of \"skaitlis\""
    },
    {
        "id": "P006G",
        "original": "*Kāds* (1) mazākais skaits punktu jānodzēš, lai *nekādi trīs* (2) no atlikušajiem punktiem neatrastos uz vienas taisnes?",
        "modified": "Kāds ir mazākais punktu skaits, kas jānodzēš, lai nevieni trīs no atlikušajiem punktiem neatrastos uz vienas taisnes?",
        "explanations": "(1) \"Kāds ir\" (instead of \"kāds\") emphasizes our need to know the value.\n(2) As all the points are given, we can use \"neviens\" in plural -- \"nevieni trīs punkti\" would mean \"no three points (out of the given ones) ...\" "
    },
    {
        "id": "P006H1",
        "original": "*Tabulā ar izmēriem 6×6 rūtiņas* (1) ierakstīti skaitļi 1, 0 un 1, katrā rūtiņā *viens skaitlis* (2). ",
        "modified": "Tabulā, kuras izmērs ir 6×6 rūtiņas, ierakstīti skaitļi 1, 0 un 1, katrā rūtiņā pa skaitlim.",
        "explanations": "(1) For clarity use a clause and separate it with commas.\n(2) \"pa skaitlim\" would be better as it avoids using \"viens\" too much."
    },
    {
        "id": "P006H2",
        "original": "Guna aprēķināja katrā rindā, katrā kolonnā un abās galvenajās diagonālēs ierakstīto skaitļu summas. Vai *noteikti* (1) starp iegūtajām summām *ir* (1) vismaz divas vienādas?",
        "modified": "Guna aprēķināja katrā rindā, katrā kolonnā un abās galvenajās diagonālēs ierakstīto skaitļu summas. Vai starp iegūtajām summām noteikti jābūt vismaz divām vienādām?",
        "explanations": NaN
    },
    {
        "id": "P006I",
        "original": "Pirtiņā ir četras lāvas. *Pirtī* (1) pērties iegāja deviņi cilvēki. Vai noteikti būs tāda lāva, uz kuras *sēdēs* (2) vismaz trīs cilvēki *tad, kad* (3) visi būs apsēdušies?",
        "modified": "Pirtiņā ir četras lāvas. Tur pērties iegāja deviņi cilvēki. Kad visi būs apsēdušies (2), vai noteikti būs tāda lāva, uz kuras sēž (3) vismaz trīs cilvēki?",
        "explanations": "(1) Avoid repeating \"pirtī\", \"pirtiņā\".\n(2) Do not use future tense in a subordinate clause \"sēdēs\", if future is clear from \"būs tāda lāva\".\n(3) Replace \"... tad, kad ...\" (too many auxiliary words) by \"Kad ..., ...\" to express adjective clause describing time."
    },
    {
        "id": "P006J",
        "original": "Daina, izmantojot visus ciparus, burtnīcā ierakstīja desmitciparu skaitli. Vai šis skaitlis *noteikti dalās* (1) ar 3?",
        "modified": "Daina, izmantojot visus ciparus, burtnīcā ierakstīja desmitciparu skaitli. Vai šim skaitlim noteikti jādalās ar 3?",
        "explanations": "(1) \"noteikti jādalās\" Is preferable to \"noteikti dalās\" (as \"dalās\" would imply that there is one specific number)."
    },
    {
        "id": "P006K",
        "original": "Vai var atrast tādus četrus dažādus naturālus skaitļus a,b,c,d, *ka* (1) 1a+1b+1c+d1=1?",
        "modified": "Vai var atrast tādus četrus dažādus naturālus skaitļus a,b,c,d, lai 1a+1b+1c+d1=1?",
        "explanations": "(1) Replace \"ka\" by \"lai\" to express intention."
    },
    {
        "id": "P006L",
        "original": "Klasē ir 40 skolēnu. Vai *noteikti ir* (1) tāds mēnesis, kurā savu dzimšanas dienu atzīmē vismaz četri šīs klases skolēni?",
        "modified": "Klasē ir 40 skolēnu. Vai noteikti jābūt tādam mēnesim, kurā savu dzimšanas dienu atzīmē vismaz četri šīs klases skolēni?",
        "explanations": "(1) \"noteikti jābūt\" is better here compared to \"noteikti ir\" as it is about the necessity (not about already existing numbers)."
    },
    {
        "id": "P006M",
        "original": "Ar vienu *„gājienu”* (1) var izvēlēties jebkurus divus no tiem un abiem pieskaitīt vieninieku. Vai, atkārtojot *šādus* (2) „gājienus”, var panākt, *lai* (3) visi skaitļi kļūtu vienādi?",
        "modified": "Uz tāfeles uzrakstīti skaitļi 0; 1; 0; 0. Ar vienu gājienu var izvēlēties jebkurus divus no tiem un abiem pieskaitīt vieninieku. Vai, atkārtojot gājienus, var panākt, ka visi skaitļi kļūst vienādi?",
        "explanations": "(1) Gājiens should not be quoted, as it expresses action. \n(2) For brevity avoid redundant pronoun \"šādus\"\n(3) \"... panākt, ka\" is more appropriate compared to \"... panākt, lai\""
    },
    {
        "id": "P024A",
        "original": "*Tā kā* (1) secība atkārtojas ik pēc 6 kauliņiem un 605=6⋅100+5, *tad* (1) uz 605. kauliņa būs redzami tikpat punktiņi, cik uz 5. kauliņa, tas ir, 5.",
        "modified": "Secība atkārtojas ik pēc 6 kauliņiem, un 6⋅100+5=605, tāpēc uz 605. kauliņa būs redzams tikpat punktiņu, cik uz 5. kauliņa, tas ir, 5.",
        "explanations": "(1) For variety replace construct \"tā kā ... tad ...\" by \"... tāpēc ...\" if the first part of the sentence logically implies the second part."
    },
    {
        "id": "P024B",
        "original": "*Tā kā* (1) katrs nākamais virknes loceklis ir atkarīgs tikai no viena iepriekšējā, *tad* (1), līdzko parādās kāds šajā virknē jau iepriekš bijis skaitlis, izveidojas periods.",
        "modified": "Katrs nākamais virknes loceklis ir atkarīgs tikai no viena iepriekšējā, tāpēc parādoties kādam jau bijušam skaitlim, izveidojas periods.",
        "explanations": "(1) For variety replace construct \"tā kā ... tad ...\" by \"... tāpēc ...\" if the first part of the sentence logically implies the second part."
    },
    {
        "id": "P024C",
        "original": "*Tā kā* (1) 2018 ir pāra skaitlis, *tad* (1) šajā vietā virknē ir skaitlis 13.",
        "modified": "2018 ir pāra skaitlis, tāpēc šajā vietā virknē ir skaitlis 13.",
        "explanations": "(1) For variety replace construct \"tā kā ... tad ...\" by \"... tāpēc ...\" if the first part of the sentence logically implies the second part."
    },
    {
        "id": "P024D",
        "original": "*Tā kā* (1) katrs nākamais virknes loceklis ir atkarīgs tikai no viena iepriekšējā, *tad* (1), līdzko parādās kāds šajā virknē jau iepriekš bijis skaitlis, izveidojas periods.",
        "modified": "Katrs nākamais virknes loceklis ir atkarīgs tikai no viena iepriekšējā, tāpēc parādoties kādam jau bijušam skaitlim, izveidojas periods.",
        "explanations": "(1) For variety replace construct \"tā kā ... tad ...\" by \"... tāpēc ...\" if the first part of the sentence logically implies the second part."
    },
    {
        "id": "P049A",
        "original": "Vai *eksistē tādi* (1) divi dažādi trīsciparu naturāli skaitļi A un B, *ka* (2) ...",
        "modified": "Vai iespējams atrast divus dažādus trīsciparu naturālus skaitļus A un B, lai ...",
        "explanations": "(1) Replace \"vai eksistē\" by \"iespējams atrast\" for variety and informal language.\n(2) Replace \"ka\" by \"lai\" to express intention."
    },
    {
        "id": "P049B",
        "original": "Dagnis no 10 klasesbiedriem ir saņēmis 54 jaunas *īsziņas*, no katra klases biedra vismaz vienu *īsziņu* (1).",
        "modified": "Dagnis no 10 klasesbiedriem ir saņēmis 54 jaunas īsziņas, no katra klases biedra vismaz vienu.",
        "explanations": "(1) Use ellipse for \"īsziņas\" (or a similar repetitive noun) if it is clear from the context."
    },
    {
        "id": "P049C",
        "original": "Vai, izdarot vairākus šādus gājienus, var panākt, *lai* (1) uz tāfeles vienlaicīgi *būtu* (1) uzrakstīti skaitļi 43 ; 45 ; 52 ?",
        "modified": "Vai, veicot vairākus gājienus, var panākt, ka uz tāfeles vienlaicīgi uzrakstīti skaitļi 43 ; 45 ; 52?",
        "explanations": "(1) Start an adjective clause by \"ka\". Once there is no conjunction \"lai\", no need for \"būtu\". "
    },
    {
        "id": "P049D",
        "original": "Vai noteikti šajā rindā *var atrast tādu* (1) skaitli, kam kaimiņš pa kreisi ir mazāks nekā tā kaimiņš pa labi?",
        "modified": "Vai noteikti šajā rindā būs skaitlis, kura “kaimiņš” pa kreisi ir mazāks nekā tā “kaimiņš” pa labi?",
        "explanations": "(1) Unless we ask the problem solver to find something, replace \"var atrast\" by \"būs\" or \"eksistē\". "
    },
    {
        "id": "P050A",
        "original": "*Tā kā* (1) 18+y+y ir jādalās ar 9, *tad* (1) derīgās vērtības ir 27 un 36.",
        "modified": "18+y+y ir jādalās ar 9, tāpēc derīgās vērtības ir 27 un 36.",
        "explanations": "(1) For variety replace construct \"tā kā ... tad ...\" by \"... tāpēc ...\" if the first part of the sentence logically implies the second part."
    },
    {
        "id": "P050B",
        "original": "*Tā kā* (1) 33+y+y ir jādalās ar 9, *tad* (1) derīgās vērtības ir 36 un 45.",
        "modified": "33+y+y ir jādalās ar 9, tāpēc derīgās vērtības ir 36 un 45.",
        "explanations": "(1) For variety replace construct \"tā kā ... tad ...\" by \"... tāpēc ...\" if the first part of the sentence logically implies the second part."
    },
    {
        "id": "P050C",
        "original": "Summu 36 nevar *iegūt* (1), jo, saskaitot divus vienādus ciparus, nevar *iegūt* 3.",
        "modified": "Nevar izveidot summu 36, jo, saskaitot divus vienādus ciparus, nevar iegūt 3. ",
        "explanations": "(1) Replace by a synonym (in our case \"iegūt\" by \"izveidot\"), if the same word repeats in a single sentence."
    },
    {
        "id": "P050D",
        "original": "**Tabulas 3×3** (1) rūtiņās katrā rūtiņā jāieraksta pa vienam naturālam skaitlim tā, lai katrā rindā, *katrā* (2) kolonnā un *katrā* (2) diagonālē ierakstīto skaitļu summas būtu vienādas.",
        "modified": "Tabulā ar izmēriem 3×3 rūtiņas katrā jāieraksta pa naturālam skaitlim tā, lai katrā rindā, kolonnā un diagonālē ierakstīto skaitļu summas būtu vienādas.",
        "explanations": "(1) Avoid \"Tabula 3x3\", if the dimensions of table is meant. Rather write \"tabula ar izmēriem 3x3\".\n(2) Avoid repeating word \"katrs\", \"katrā\"; one such word will apply to every item in the list. "
    }
]
```
(1) "id" is a unique identifier for a style rule; 
(2) "original" shows an example sentence - how some problematic sentence is likely to appear. The most characteristic phrases are highlighted with asterisks and provided with numbers (1), (2), or (3). Sometimes "original" combines several problematic things -- they may appear in isolation as well. 
(3) "modified" shows how to fix the style in this sentence. 
(4) "explanations" provide additional comments - the reasoning behind the replacements in English. 

Consider the following JSON file containing a worksheet: 
```
{
    "snippets": [
        {
            "type": "problem",
            "value": "LV.AMO.2005.7.1. Trijst\u016br\u012b $ABC$ punkti $K$ un $M$ atrodas uz malas $AC$, pie tam $M$ ir $AC$ \nviduspunkts. Ir zin\u0101ms, ka $BM=3,\\ AK=1,\\ MC=2$ un \n$\\sphericalangle BMC=120^{\\circ}$.\n\nPier\u0101d\u012bt, ka $AB=BK$."
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.7.2. K\u0101dam maz\u0101kajam natur\u0101lajam $n$ visas da\u013cas \n$\\frac{5}{n+7},\\ \\frac{6}{n+8},\\ \\frac{7}{n+9},\\ \\ldots,\\ \\frac{35}{n+37},\\ \\frac{36}{n+38}$\nir nesa\u012bsin\u0101mas?"
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.7.3. Pank\u016bka no katras puses j\u0101cep $6$ min\u016btes (varb\u016bt ar p\u0101rtraukumiem). Uz pannas \nvienlaic\u012bgi var atrasties augst\u0101kais $4$ pank\u016bkas. K\u0101d\u0101 \u012bs\u0101kaj\u0101 laik\u0101 var no \nab\u0101m pus\u0113m apcept $5$ pank\u016bkas?\n\nPank\u016bku nomai\u0146ai laiks nav j\u0101paredz."
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.7.4. Triju veselu pozit\u012bvu skait\u013cu summa ir $407$. Ar k\u0101du liel\u0101ko daudzumu nu\u013c\u013cu \nvar beigties \u0161o skait\u013cu reizin\u0101jums?"
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.7.5. Rind\u0101 izrakst\u012bti $10$ da\u017e\u0101di skait\u013ci, kas visi liel\u0101ki par $0$ un maz\u0101ki par \n$1$. To skait\u013cu summa, kas atrodas $2.,\\ 4.,\\ 6.,\\ 8.,\\ 10.$ viet\u0101s, par $1$ \nliel\u0101ka nek\u0101 to skait\u013cu summa, kas atrodas $1.,\\ 3.,\\ 5.,\\ 7.,\\ 9.$ viet\u0101s.\n\nPier\u0101diet: rind\u0101 var atrast t\u0101du skaitli, kas maz\u0101ks par abiem saviem \nkaimi\u0146iem."
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.8.1. Dots, ka kvadr\u0101tvien\u0101dojuma $x^{2}+px+q=0$ saknes ir $x_{1}$ un $x_{2}$, bet \nkvadr\u0101tvien\u0101dojuma $x^{2}+ax+b=0$ saknes ir $x_{1}^{2}$ un $x_{2}^{2}$. Izsac\u012bt\n$a$ un $b$ ar $p$ un $q$ pal\u012bdz\u012bbu."
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.8.2. Par Fibona\u010di skait\u013ciem sauc skait\u013cus $1;\\ 2;\\ 3;\\ 5;\\ 8;\\ 13;\\ 21;\\ \\ldots$ \n(katru n\u0101kamo skaitli \u0161aj\u0101 virkn\u0113 ieg\u016bst, saskaitot divus iepriek\u0161\u0113jos).\n\nVai var past\u0101v\u0113t vien\u0101d\u012bba $a+b=c+d$, ja $a,\\ b,\\ c,\\ d$ ir da\u017e\u0101di Fibona\u010di \nskait\u013ci?"
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.8.3. K\u0101 var sadal\u012bt natur\u0101los skait\u013cus no $1$ l\u012bdz $9$ ieskaitot div\u0101s da\u013c\u0101s t\u0101, lai\nvienas da\u013cas visu skait\u013cu summa b\u016btu vien\u0101da ar otras da\u013cas visu skait\u013cu \nreizin\u0101jumu?"
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.8.4. Trijst\u016br\u012b $ABC$ past\u0101v sakar\u012bbas $AC=BC$ un $\\sphericalangle ACB=20^{\\circ}$. \nLe\u0146\u0137a $CAB$ bisektrise un malas $AC$ vidusperpendikuls krustojas punkt\u0101 $M$. \nApr\u0113\u0137in\u0101t\n\n**(A)** $\\sphericalangle MCB$, **(B)** $\\sphericalangle MBC$."
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.8.5. Kvadr\u0101ts sast\u0101v no $8 \\times 8$ vien\u0101d\u0101m kvadr\u0101tisk\u0101m r\u016bti\u0146\u0101m. Katra r\u016bti\u0146a \nnokr\u0101sota vien\u0101 no $n$ kr\u0101s\u0101m. Ir zin\u0101ms: katrai r\u016bti\u0146ai var atrast vismaz \ndivas kaimi\u0146u r\u016bti\u0146as, kas nokr\u0101sotas t\u0101d\u0101 pa\u0161\u0101 kr\u0101s\u0101 k\u0101 vi\u0146a. (R\u016bti\u0146as sauc \npar kaimi\u0146u r\u016bti\u0146\u0101m, ja t\u0101m ir kop\u012bga mala.)\n\nK\u0101da ir liel\u0101k\u0101 iesp\u0113jam\u0101 $n$ v\u0113rt\u012bba?"
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.9.1. Atrast maz\u0101ko natur\u0101lo skaitli, kas dal\u0101s ar $225$ un kura decim\u0101laj\u0101 pierakst\u0101\nneizmanto nevienu no cipariem $3;\\ 4;\\ 5;\\ 6;\\ 7;\\ 8;\\ 9$."
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.9.2. Trijst\u016bra $ABC$ ievilkt\u0101 ri\u0146\u0137a centrs ir $I$. Dots, ka $CA+AI=CB$. Pier\u0101d\u012bt, ka\n$\\sphericalangle BAC=2 \\sphericalangle CBA$."
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.9.3. Dots, ka $n$ - natur\u0101ls skaitlis. Katrs no $2n+1$ r\u016b\u0137\u012b\u0161iem Lieldien\u0101s vienu \nreizi ierad\u0101s pie Sniegbalt\u012btes un k\u0101du laiku tur uztur\u0113j\u0101s. Ja divi r\u016b\u0137\u012b\u0161i \nvienlaikus bija pie Sniegbalt\u012btes, tad vi\u0146i tur satik\u0101s. Zin\u0101ms, ka katrs \nr\u016b\u0137\u012btis pie Sniegbalt\u012btes satika vismaz $n$ citus r\u016b\u0137\u012b\u0161us.\n\nPier\u0101d\u012bt: ir t\u0101ds r\u016b\u0137\u012btis, kas pie Sniegbalt\u012btes satika visus $2n$ citus \nr\u016b\u0137\u012b\u0161us."
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.9.4. Dots, ka $x^{2}+yz \\leq 2,\\ y^{2}+xz \\leq 2$ un $z^{2}+xy \\leq 2$. Atrast \nizteiksmes $x+y+z$ liel\u0101ko un maz\u0101ko iesp\u0113jamo v\u0113rt\u012bbu."
        },
        {
            "type": "problem",
            "value": "LV.AMO.2005.9.5. Doti $3$ stien\u012b\u0161i. Uz viena no tiem s\u0101kotn\u0113ji uzmaukti $n$ da\u017e\u0101du izm\u0113ru diski \nar caurumiem vid\u016b t\u0101, ka to r\u0101diusi samazin\u0101s no lejas uz aug\u0161u; abi p\u0101r\u0113jie \nstien\u012b\u0161i s\u0101kotn\u0113ji ir tuk\u0161i (skat. 1.z\u012bm., kur $n=6$).\n\n![](LV.AMO.2005.9.5.png)\n\nAr vienu g\u0101jienu var p\u0101rlikt aug\u0161\u0113jo disku no jebkura stien\u012b\u0161a uz jebkuru citu,\nja tikai p\u0101rliekamais disks $D$ nav liel\u0101ks par to disku, kas atrodas pa\u0161\u0101 \napak\u0161\u0101 uz stien\u012b\u0161a, uz kuru p\u0101rliek $D$.\n\nAr k\u0101du maz\u0101ko g\u0101jienu skaitu var pan\u0101kt, lai visi diski atrastos uz stien\u012b\u0161a \n$C$ t\u0101d\u0101 pa\u0161\u0101 k\u0101rt\u012bb\u0101, k\u0101d\u0101 tie s\u0101kotn\u0113ji atrad\u0101s uz stien\u012b\u0161a $A$?"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.7.1. K\u0101du maz\u0101ko daudzumu no skait\u013ciem $1;\\ 2;\\ 3;\\ \\ldots;\\ 12;\\ 13$ var izsv\u012btrot,\nlai katru divu atliku\u0161o summa b\u016btu salikts skaitlis?"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.7.2. Vai funkciju $y=2003x+4197,\\ y=2004x+4198$ un $y=2005x+4199$ grafiki krustojas \nvien\u0101 punkt\u0101?"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.7.3. M\u016bsu r\u012bc\u012bb\u0101 ir $100$ vien\u0101das trijst\u016brveida pl\u0101ksn\u012btes; katras pl\u0101ksn\u012btes malas\ngarums ir $1$. Vai no t\u0101m var salikt fig\u016bru, kuras apk\u0101rtm\u0113rs ir **(A)** $56$, \n**(B)** $57$? J\u0101izmanto visas pl\u0101ksn\u012btes.\n\nSaliekot pl\u0101ksn\u012btes nedr\u012bkst p\u0101rkl\u0101ties. Katras divas pl\u0101ksn\u012btes vai nu \nnesaskaras nemaz, vai saskaras tikai ar vienu st\u016bri, vai saskaras ar vienu \nveselu malu."
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.7.4. Natur\u0101lu skaitli $n$ sauc par \u012bpa\u0161u, ja tas ir vien\u0101ds ar \u010detru savu da\u017e\u0101du \ndal\u012bt\u0101ju summu.\n\n**(A)** atrodiet kaut vienu \u012bpa\u0161u skaitli,  \n**(B)** pier\u0101diet, ka \u012bpa\u0161u skait\u013cu ir bezgal\u012bgi daudz,  \n**(C)** pier\u0101diet, ka visi \u012bpa\u0161i skait\u013ci ir p\u0101ra."
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.7.5. Dotas $8$ p\u0113c \u0101r\u0113j\u0101 izskata vien\u0101das mon\u0113tas. Ir zin\u0101ms, ka vai nu vis\u0101m t\u0101m \nmasas ir vien\u0101das, vai ar\u012b $4$ mon\u0113t\u0101m ir viena masa, bet $4$ mon\u0113t\u0101m - cita \nmasa. K\u0101 ar $3$ sv\u0113r\u0161an\u0101m uz sviras svariem bez atsvariem var noskaidrot, kura \nno iesp\u0113j\u0101m past\u0101v \u012bsten\u012bb\u0101?"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.8.1. Ir zin\u0101ms, ka skait\u013ca $2^{100}$ decim\u0101laj\u0101 pierakst\u0101 ir $431$ cipars. Cik \ndaudziem no skait\u013ciem $2^{1};\\ 2^{2};\\ 2^{3};\\ \\ldots;\\ 2^{99};\\ 2^{100}$ \ndecim\u0101lais pieraksts s\u0101kas ar ciparu $1$?"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.8.2. Kvadr\u0101ts sast\u0101v no $4 \\times 4$ vien\u0101d\u0101m kvadr\u0101tisk\u0101m r\u016bti\u0146\u0101m. R\u016bti\u0146\u0101s \nierakst\u012bti natur\u0101li skait\u013ci no $1$ l\u012bdz $16$ (da\u017e\u0101d\u0101s r\u016bti\u0146\u0101s - da\u017e\u0101di \nskait\u013ci). R\u016bti\u0146u sauc par izcilu, ja taj\u0101 ierakst\u012btais skaitlis maz\u0101ks par \naugst\u0101kais vien\u0101 kaimi\u0146u r\u016bti\u0146\u0101 ierakst\u012btu skaitli (divas r\u016bti\u0146as sauc par \nkaimi\u0146u r\u016bti\u0146\u0101m, ja t\u0101m ir kop\u012bga mala vai kop\u012bgs st\u016bris). K\u0101ds liel\u0101kais \ndaudzums r\u016bti\u0146u var b\u016bt izcilas?"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.8.3. Andris iedom\u0101j\u0101s patva\u013c\u012bgu natur\u0101lu skaitli $n$. Juris ar vienu g\u0101jienu var \npateikt Andrim piecus da\u017e\u0101dus natur\u0101lus skait\u013cus \n$x_{1},\\ x_{2},\\ x_{3},\\ x_{4},\\ x_{5}$, un Andris pateiks Jurim **vienu** no \nskait\u013ciem $nx_{1},\\ nx_{2},\\ nx_{3},\\ nx_{4},\\ nx_{5}$ (bet nepaskaidros, \n**kura** reizin\u0101juma v\u0113rt\u012bbu vi\u0146\u0161 saka).\n\nAr k\u0101du maz\u0101ko jaut\u0101jumu skaitu Juris var noteikti noskaidrot $n$?"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.8.4. Taisne $t$ nav nogrie\u017e\u0146a $AB$ vidusperpendikuls. Cik uz taisnes $t$ var b\u016bt \nt\u0101du punktu $C$, ka $A,\\ B$ un $C$ ir vien\u0101ds\u0101nu trijst\u016bra virsotnes?"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.8.5. Atrisin\u0101t vien\u0101dojumu\n\n$$x^{3}\\left(x^{2}-7\\right)^{2}-36x=0$$"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.9.1. Dots, ka $a$ un $b$ - kaut k\u0101di re\u0101li skait\u013ci. Pier\u0101d\u012bt, ka\n\n$$a^{2}-ab+b^{2} \\geq 5a+5b-25$$"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.9.2. K\u0101da var b\u016bt \u010detru t\u0101du divciparu pirmskait\u013cu summa, kas sast\u0101d\u012bti no cipariem \n$1;\\ 2;\\ 3;\\ 4;\\ 5;\\ 6;\\ 7;\\ 9$, izmantojot katru no tiem tie\u0161i vienu reizi?"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.9.3. Divas ri\u0146\u0137a l\u012bnijas ar r\u0101diusiem $R$ un $r$ \u0101r\u0113ji pieskaras viena otrai punkt\u0101 \n$A$. Taisne $t$ pieskaras ab\u0101m ri\u0146\u0137a l\u012bnij\u0101m punkt\u0101 $A$ un krusto to kop\u0113j\u0101s \n\u0101r\u0113j\u0101s pieskares punktos $K$ un $L$.\n\n**(A)** pier\u0101d\u012bt, ka $MK=KN$ (skat. 1.z\u012bm.);\n\n**(B)** izteikt $KL$ ar $R$ un $r$.\n\n![](LV.NOL.2005.9.3.png)"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.9.4. Vai eksist\u0113 t\u0101di $6$ skait\u013ci, ka, apr\u0113\u0137inot visas iesp\u0113jam\u0101s to summas pa \ndiviem, ieg\u016bst visus natur\u0101los skait\u013cus no $1$ l\u012bdz $15$ ieskaitot?"
        },
        {
            "type": "problem",
            "value": "LV.NOL.2005.9.5. Ciparu virkni veido sekojo\u0161i: t\u0101s pirmie cipari ir $1;\\ 2;\\ 3;\\ 4$, bet katrs \nn\u0101ko\u0161ais vien\u0101ds ar \u010detru iepriek\u0161\u0113jo summas p\u0113d\u0113jo ciparu. (T\u0101tad virkne ir \n$1;\\ 2;\\ 3;\\ 4;\\ 0;\\ 9;\\ 6;\\ 9;\\ \\ldots$)\n\n**(A)** Vai virkn\u0113 k\u0101dreiz p\u0113c k\u0101rtas par\u0101d\u012bsies cipari $2;\\ 0;\\ 0;\\ 5$ tie\u0161i \n\u0161\u0101d\u0101 sec\u012bb\u0101?  \n**(B)** Vai virkn\u0113 k\u0101dreiz p\u0113c k\u0101rtas citur nek\u0101 s\u0101kum\u0101 par\u0101d\u012bsies cipari \n$1;\\ 2;\\ 3;\\ 4$?"
        },
        {
            "type": "problem",
            "value": "LV.VOL.2005.9.1. Uz trapeces $ABCD$ gar\u0101k\u0101 pamata $AD$ \u0146emti t\u0101di divi iek\u0161\u0113ji punkti $M$ un \n$N$, ka $BM \\parallel CN$. Pier\u0101d\u012bt, ka da\u013cu $1,\\ 2$ un $3$ laukumu summa \nvien\u0101da ar da\u013cas $4$ laukumu (skat. 1.z\u012bm.).\n\n![](LV.VOL.2005.9.1.png)"
        },
        {
            "type": "problem",
            "value": "LV.VOL.2005.9.2. Dots, ka $B$ - natur\u0101ls skaitlis, $A=7 \\cdot B$ un $A$ ciparu summa divas \nreizes liel\u0101ka par $B$ ciparu summu. Skaitli $C$ ieg\u016bst, pierakstot skaitlim \n$A$ gal\u0101 skaitli $B$.\n\n**(A)** atrast kaut vienu \u0161\u0101du $C$,  \n**(B)** pier\u0101d\u012bt, ka \u0161\u0101du $C$ ir bezgal\u012bgi daudz,  \n**(C)** pier\u0101d\u012bt, ka katrs \u0161\u0101ds $C$ dal\u0101s ar $9$,  \n**(D)** vai $C$ noteikti dal\u0101s ar $27$?"
        },
        {
            "type": "problem",
            "value": "LV.VOL.2005.9.3. Ap galdu s\u0113\u017e $8$ b\u0113rni. Katriem tr\u012bs p\u0113c k\u0101rtas s\u0113do\u0161iem b\u0113rniem kop\u0101 ir nep\u0101ra\nskaits konfek\u0161u. Pier\u0101d\u012bt, ka katram b\u0113rnam ir vismaz viena konfekte."
        },
        {
            "type": "problem",
            "value": "LV.VOL.2005.9.4. Dots, ka $a$ un $b$ - t\u0101di re\u0101li skait\u013ci, ka $a+b$ ir vesels skaitlis un \n$a^{2}+b^{2}=2$. Atrast visus \u0161\u0101dus $a$ un $b$ p\u0101rus un pier\u0101d\u012bt, ka citu bez \nJ\u016bsu atrastajiem nav."
        },
        {
            "type": "problem",
            "value": "LV.VOL.2005.9.5. Katrs natur\u0101ls skaitlis no $1$ l\u012bdz $2005$ ieskaitot nokr\u0101sots vien\u0101 no $n$ \nkr\u0101s\u0101m. Ir zin\u0101ms: ja $a,\\ b$ un $c$ ir da\u017e\u0101di skait\u013ci, $a$ dal\u0101s ar $b$ un $b$\ndal\u0101s ar $c$, tad $a,\\ b$ un $c$ nav visi nokr\u0101soti vien\u0101 un tai pa\u0161\u0101 kr\u0101s\u0101. \nAtrast maz\u0101ko iesp\u0113jamo $n$ v\u0113rt\u012bbu."
        }
    ]
}
```
If any snippet has "value" that is somewhat similar to the "original" for any of the rules (contains phrases similar to the ones highlighted with the asterisks), please insert that snippet into your response; insert (1), (2), or (3) when appropriate, also provide suggested fix as "value_fixed" and "rule" - which rule was applied. For example, if the original snippet is this: 
```
    { "type": "problem", "value": "Vai pozitīva skaitļa kvadrātsakne noteikti ir mazāka par pašu skaitli?" }
```
then replace it by this: 
```
    { "type": "problem", "value": "Vai pozitīva skaitļa kvadrātsakne noteikti ir (1) mazāka par pašu skaitli?", "value_fixed": "Vai pozitīva skaitļa kvadrātsaknei noteikti jābūt mazākai par pašu skaitli?", rule:"P006E" }
```





Please return just the JSON array containing those snippets which had style fixes like this: 
```
{ "snippets": [
    { "type": "problem", "value": "Vai pozitīva skaitļa kvadrātsakne noteikti ir (1) mazāka par pašu skaitli?", "value_fixed": "Vai pozitīva skaitļa kvadrātsaknei noteikti jābūt mazākai par pašu skaitli?", rule:"P006E" }, 
   // ... 
]}
```
"value" should be taken from the original "snippets" JSON (unchanged). "rule" should point to an existing rule in the given list of style rules.
