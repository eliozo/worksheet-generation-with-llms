#!/bin/bash

dir=../../math/problembase/LV.VOL/lv-vol-2019
python eliozo_client.py add-metadata $dir/content_lv.md hasSolutionConcept --mode text --provider gpt-4o --output $dir/content_lv2.md --reference $dir/problemdata.json

