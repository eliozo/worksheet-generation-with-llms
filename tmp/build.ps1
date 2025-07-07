$env:PYTHONPATH=".."
python ../scripts/eliozo_client.py convert-worksheet worksheet.json worksheet.rst --template regular.rst.jinja         
python ../scripts/eliozo_client.py convert-worksheet worksheet.rst worksheet.docx