set PYTHONPATH=..
rem cp ../tests/adapt-worksheet/worksheet_original.json ../tests/adapt-worksheet/worksheet.json 
rem cp ../tests/adapt-worksheet/task_original.json ../tests/adapt-worksheet/task.json 

rem python eliozo_client.py adapt-worksheet extend Theory --reference ../tests/adapt-worksheet/task.json
rem python eliozo_client.py adapt-worksheet extend Title --reference ../tests/adapt-worksheet/task.json
rem python eliozo_client.py adapt-worksheet extend StyleRules --reference ../tests/adapt-worksheet/task.json

rem python eliozo_client.py convert-worksheet ../tests/adapt-worksheet/worksheet.json ../tests/adapt-worksheet/worksheet.rst --reference ../tests/adapt-worksheet/task.json
rem python eliozo_client.py convert-worksheet ../tests/adapt-worksheet/worksheet.rst ../tests/adapt-worksheet/worksheet.docx --reference ../tests/adapt-worksheet/task.json

python eliozo_client.py create-task "**Vajadzīgais saturs:** Darba lapa 90 minūšu nodarbībai pirms novada olimpiādes. **Apmācāmie:** 8.klases skolēni, nav daudz patstāvīgi gatavojušies, bet izgājuši Rīgas ģimnāziju iestājeksāmenus pēc 6.klases. Viņiem patīk neformāla valoda, animācijas seriāls Arcane. **Mācību tēmas:**  Dirihlē princips ar piemēriem par kombinatoriku, kombinatorisko ģeometriju vai skaitļu teoriju. Olimpiāžu stila uzdevumiem jābūt ar dažādu tipu jautājumiem (pierādījumi, piemēri, optimizācijas uzdevumi), lai skolēni vingrinātos ievērot pareizu, uzdevuma prasībām atbilstošu atrisinājuma struktūru. **Atbildes formāts:** Lūdzu izveidot pavisam 10 uzdevumu komplektu aprakstītajai situācijai: Vispirms 2 ievaduzdevumus, tad īsu teorijas pārskatu (komplektam nepieciešamās prasmes - par Dirihlē principu un dažādām atrisinājumu struktūrām). Visbeidzot 8 uzdevumus ar pieaugošu grūtības pakāpi. Visu 10 uzdevumu atrisinājumus (konspektīvus, kas nav domāti kā paraugs atrisinājumu noformēšanai olimpiādē) ievietot darba lapas beigās." --reference ../tests/create-task/task.json
python eliozo_client.py get-problems --worksheet ../tests/get-problems/worksheet.json  --reference ../tests/get-problems/task.json
python eliozo_client.py convert-worksheet ../tests/get-problems/worksheet.json ../tests/get-problems/worksheet.rst --reference ../tests/get-problems/task.json
python eliozo_client.py convert-worksheet ../tests/get-problems/worksheet.rst ../tests/get-problems/worksheet.docx --reference ../tests/get-problems/task.json