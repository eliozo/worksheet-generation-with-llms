export PYTHONPATH=".."

python eliozo_client.py create-task --query ../tests/master-demo/query-modular.txt --reference ../tests/master-demo/task-modular.json

python eliozo_client.py get-classifiers --reference ../tests/master-demo/task-modular.json

python eliozo_client.py get-problems --worksheet ../tests/master-demo/worksheet-modular.json  --reference ../tests/master-demo/task-modular.json

python eliozo_client.py convert-worksheet ../tests/master-demo/worksheet-modular.json ../tests/master-demo/worksheet-modular.rst --reference ../tests/master-demo/task-modular.json
python eliozo_client.py convert-worksheet ../tests/master-demo/worksheet-modular.rst ../tests/master-demo/worksheet-modular.docx --reference ../tests/master-demo/task-modular.json