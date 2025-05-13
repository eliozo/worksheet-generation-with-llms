set PYTHONPATH=..
rem cp ../tests/adapt-worksheet/worksheet_original.json ../tests/adapt-worksheet/worksheet.json 
rem cp ../tests/adapt-worksheet/task_original.json ../tests/adapt-worksheet/task.json 

rem python eliozo_client.py adapt-worksheet extend Theory --reference ../tests/adapt-worksheet/task.json
rem python eliozo_client.py adapt-worksheet extend Title --reference ../tests/adapt-worksheet/task.json
rem python eliozo_client.py adapt-worksheet extend StyleRules --reference ../tests/adapt-worksheet/task.json

rem python eliozo_client.py convert-worksheet ../tests/adapt-worksheet/worksheet.json ../tests/adapt-worksheet/worksheet.rst --reference ../tests/adapt-worksheet/task.json
rem python eliozo_client.py convert-worksheet ../tests/adapt-worksheet/worksheet.rst ../tests/adapt-worksheet/worksheet.docx --reference ../tests/adapt-worksheet/task.json

python eliozo_client.py create-task "**Vajadzīgais saturs:** Darba lapa 90 minūšu nodarbībai pirms novada olimpiādes. **Apmācāmie:** 8.klases skolēni. Viņiem patīk neformāla valoda, animācijas seriāls Arcane. **Mācību tēmas:**  Grafu teorija, virsotņu pakāpes, grafu apstaigāšana, planāri grafi bez šķautņu krustošanās, ceļi un cikli grafos, koki. Olimpiāžu stila uzdevumiem jābūt ar dažādu tipu jautājumiem (pierādījumi, piemēri, optimizācijas uzdevumi). **Atbildes formāts:** Lūdzu izveidot pavisam 10 uzdevumu komplektu aprakstītajai situācijai: Vispirms 2 ievaduzdevumus, tad īsu teorijas pārskatu. Visbeidzot 8 uzdevumus ar pieaugošu grūtības pakāpi. Visu 10 uzdevumu atrisinājumus (konspektīvus, kas nav domāti kā paraugs atrisinājumu noformēšanai olimpiādē) ievietot darba lapas beigās." --reference ../tests/get-problems/task.json 
python eliozo_client.py get-classifiers --reference ../tests/get-problems/task.json
python eliozo_client.py get-problems --worksheet ../tests/get-problems/worksheet.json  --reference ../tests/get-problems/task.json
python eliozo_client.py convert-worksheet ../tests/get-problems/worksheet.json ../tests/get-problems/worksheet.rst --reference ../tests/get-problems/task.json
python eliozo_client.py convert-worksheet ../tests/get-problems/worksheet.rst ../tests/get-problems/worksheet.docx --reference ../tests/get-problems/task.json