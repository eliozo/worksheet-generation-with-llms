#!/bin/bash 

export PYTHONPATH=..

# 1.komanda - iesūta pirmo reizi lietotāja vaicājumu; izveido JSON
# OpenAI ģenerē darba lapas virsrakstu; izvēlas, kura klase (klases) būs
# Izvēlas tēmas, metodes (citu metainformāciju - questionType) -- SPARQL filtri
# Kuru Jinja2 šablonu vajadzēs lietot
# (visu šo saraksta JSON failā - no kura Jinja2 var aizpildīt)
# Visu ko ģenerē ar nejaušo skaitļu ģeneratoru, tam pievieno "seed" (piemēram, 42). 
python3 eliozo_client.py create-task "**Vajadzīgais saturs:** Darba lapa 90 minūšu nodarbībai pirms novada olimpiādes. **Apmācāmie:** 8.klases skolēni, nav daudz patstāvīgi gatavojušies, bet izgājuši Rīgas ģimnāziju iestājeksāmenus pēc 6.klases. Viņiem patīk neformāla valoda, animācijas seriāls Arcane. **Mācību tēmas:**  Dirihlē princips ar piemēriem par kombinatoriku, kombinatorisko ģeometriju vai skaitļu teoriju. Olimpiāžu stila uzdevumiem jābūt ar dažādu tipu jautājumiem (pierādījumi, piemēri, optimizācijas uzdevumi), lai skolēni vingrinātos ievērot pareizu, uzdevuma prasībām atbilstošu atrisinājuma struktūru. **Atbildes formāts:** Lūdzu izveidot pavisam 10 uzdevumu komplektu aprakstītajai situācijai: Vispirms 2 ievaduzdevumus, tad īsu teorijas pārskatu (komplektam nepieciešamās prasmes - par Dirihlē principu un dažādām atrisinājumu struktūrām). Visbeidzot 8 uzdevumus ar pieaugošu grūtības pakāpi. Visu 10 uzdevumu atrisinājumus (konspektīvus, kas nav domāti kā paraugs atrisinājumu noformēšanai olimpiādē) ievietot darba lapas beigās." --reference task.json 


# Lietotājs tagad var caurskatīt šo task.json - paskatīties, vai viss izskatās normāli.
# Lietotājs var arī pielabot kaut ko, ja izrādās, ka OpenAI ir viņa query pārpratis
# (Var redzēt, vai klase, tēma utml. ir pareizi uzminēta no lietotāja vaicājuma/query.)
# No task.json izvelk pilnu lietotāja vaicājumu un meklē Weaviate uzdevumus, kas saturiski līdzīgi šim vaicājumam
# Uzdevumus noglabā failā worksheet.json, kuru pēc tam var pārveidot par word doc
python eliozo_client.py get-problems --output worksheet.json --reference task.json 

python eliozo_client.py convert-worksheet worksheet.json tests_word/pigeonhole-test01.docx --reference tests_word/twocolumn.json

python eliozo_client.py convert-worksheet tests_word/questiontype_problems.rst tests_word/questiontype_problems.docx --reference tests_word/twocolumn.json

python eliozo_client.py convert-worksheet tests_word/questiontype_problems4.rst tests_word/questiontype_problems.docx --reference tests_word/twocolumn.json

python eliozo_client.py get-problems --output worksheet.json --reference task.json 

python eliozo_client.py get-problems-fuseki --output worksheet.json --reference task.json 


exit 0

add-metadata ../../qualification-project/migration-script/resources/LV-AMO-2004-content.md questionType --mode text --provider OpenAI

