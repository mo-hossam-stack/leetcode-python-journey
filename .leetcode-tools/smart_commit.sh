#!/bin/bash

echo "Enter folder name (e.g., array):"
read folder

# نجيب الملفات الجديدة أو المعدّلة فقط داخل المجلد المطلوب
files=$(git status --porcelain | grep "^??\|^ M" | awk '{print $2}' | grep "^$folder/")

if [ -z "$files" ]; then
  echo "No new or modified .py files found in $folder/"
  exit 0
fi

for file in $files; do
  if [[ "$file" == *.py ]]; then
    filename=$(basename "$file" .py)
    git add "$file"
    git commit -m "feat($folder): add solution for '$filename'"
  fi
done

git push origin main
