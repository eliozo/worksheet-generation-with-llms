# Set environment variable
$env:PYTHONPATH = ".."

# Copy files (commented out)
# Copy-Item ../tests/adapt-worksheet/worksheet_original.json ../tests/adapt-worksheet/worksheet.json
# Copy-Item ../tests/adapt-worksheet/task_original.json ../tests/adapt-worksheet/task.json

# Execute python scripts (commented out)
# python eliozo_client.py adapt-worksheet extend Theory --reference ../tests/adapt-worksheet/task.json
# python eliozo_client.py adapt-worksheet extend Title --reference ../tests/adapt-worksheet/task.json
# python eliozo_client.py adapt-worksheet extend StyleRules --reference ../tests/adapt-worksheet/task.json

# python eliozo_client.py convert-worksheet ../tests/adapt-worksheet/worksheet.json ../tests/adapt-worksheet/worksheet.rst --reference ../tests/adapt-worksheet/task.json
# python eliozo_client.py convert-worksheet ../tests/adapt-worksheet/worksheet.rst ../tests/adapt-worksheet/worksheet.docx --reference ../tests/adapt-worksheet/task.json

# Execute active python commands
python eliozo_client.py create-task '**Ģenerē darba lapu 7.–8. klases skolēniem par Dirihlē principu, izmantojot Vinnija Pūka tēlu un viņa draugus kā kontekstu. Darba lapa paredzēta vienai 45 minūšu matemātikas stundai. Tā satur 1 iesildīšanās uzdevumu, 5 galvenos uzdevumus (1 ģenerē LLM, 4 nāk no Jena Fuseki, bet adaptēti), definīcijas un Dirihlē principa formulējumu. Darba lapas apjomam jāiekļaujas 2 A4 lapās. Darba lapas beigās pievieno 1–2 ieteikumus skolēniem par katru uzdevumu. Uzdevumiem jābūt atraktīviem un sasaistītiem ar stāstu par Vinniju Pūku.' --reference ../tests/get-problems/task.json

python eliozo_client.py get-classifiers --reference ../tests/get-problems/task.json
python eliozo_client.py get-problems --worksheet ../tests/get-problems/worksheet.json --reference ../tests/get-problems/task.json
python eliozo_client.py convert-worksheet ../tests/get-problems/worksheet.json ../tests/get-problems/worksheet.rst --reference ../tests/get-problems/task.json
python eliozo_client.py convert-worksheet ../tests/get-problems/worksheet.rst ../tests/get-problems/worksheet.docx --reference ../tests/get-problems/task.json
