set PYTHONPATH=..
set RDFPATH="C:\Users\eozolina\Documents\workspace-private\qualification-project\migration-script\resources"

rem python eliozo_client.py drop-rdf abc --reference problemdata.json
rem python eliozo_client.py create-rdf-dataset abc --reference problemdata.json
rem python eliozo_client.py ingest-rdf abc %RDFPATH%/LV-NOL-2004-content.ttl --reference problemdata.json

rem python eliozo_client.py create-schema-vectors eliozo-model --reference problemdata.json
rem python eliozo_client.py ingest-classifiers eliozo-model topic %RDFPATH%/skos_topic.ttl  --reference problemdata.json
python eliozo_client.py get-classifiers "**Vajadzīgais saturs:** Darba lapa 90 minūšu nodarbībai pirms novada olimpiādes. **Apmācāmie:** 8.klases skolēni, nav daudz patstāvīgi gatavojušies, bet izgājuši Rīgas ģimnāziju iestājeksāmenus pēc 6.klases. Viņiem patīk neformāla valoda, animācijas seriāls Arcane. **Mācību tēmas:**  Dirihlē princips ar piemēriem par kombinatoriku, kombinatorisko ģeometriju vai skaitļu teoriju. Olimpiāžu stila uzdevumiem jābūt ar dažādu tipu jautājumiem (pierādījumi, piemēri, optimizācijas uzdevumi), lai skolēni vingrinātos ievērot pareizu, uzdevuma prasībām atbilstošu atrisinājuma struktūru. **Atbildes formāts:** Lūdzu izveidot pavisam 10 uzdevumu komplektu aprakstītajai situācijai: Vispirms 2 ievaduzdevumus, tad īsu teorijas pārskatu (komplektam nepieciešamās prasmes - par Dirihlē principu un dažādām atrisinājumu struktūrām). Visbeidzot 8 uzdevumus ar pieaugošu grūtības pakāpi. Visu 10 uzdevumu atrisinājumus (konspektīvus, kas nav domāti kā paraugs atrisinājumu noformēšanai olimpiādē) ievietot darba lapas beigās." --reference ../tests/get-classifiers/task.json