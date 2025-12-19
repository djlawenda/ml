#!/usr/bin/env bash
set -e
cd "/home/lukasz/Documents/code/py/ml"
# Stage new/modified files but ignore caches if you used .gitignore
git add .
# Auto message with timestamp; edit as you like
git commit -m "Logseq sync: $(date +'%Y-%m-%d %H:%M:%S')"
git push origin main
