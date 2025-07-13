#!/bin/bash

export PYTHONPATH=../..

python eliozo_client.py md-repository-to-turtle \
    "https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Il_-qJURh8sZHRN1oJSwok4kRUjcA7VCOhDfg1PnTUC14k4skRRl3NrUDEbd1vELQq_ALwEU9Ltx/pub?output=csv" \
    temp --reference ../tests/md-to-turtle/task.json

