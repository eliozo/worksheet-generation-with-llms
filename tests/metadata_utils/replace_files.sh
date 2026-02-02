#!/bin/bash

MATH_HOME="/Users/kapsitis/workspace-public/math/problembase"

for year in {2004..2025}; do
    src_dir="./lv-vol-$year"
    src_file="$src_dir/content_lv.md"
    # Ensure destination uses the same year structure
    dest_dir="$MATH_HOME/LV.VOL/lv-vol-$year"
    dest_file="$dest_dir/content_lv.md"

    if [ -f "$src_file" ]; then
        # Ensure destination directory exists (optional safety, but good practice)
        # mkdir -p "$dest_dir" 
        
        # Silently overwrite
        cp "$src_file" "$dest_file"
        echo "Copied $src_file to $dest_file"
    else
        echo "Warning: Source file $src_file not found or directory does not exist."
    fi
done