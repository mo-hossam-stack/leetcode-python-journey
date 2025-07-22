#!/bin/bash

echo "Enter folder name (e.g., arrays,fundamentals,two_pointers,hashing,sliding_window,bit_manipulation):"
read folder

files=$(git status --porcelain | grep -E "^\?\?|^ M" | awk '{print $2}' | grep "^$folder/.*\.py$")

if [ -z "$files" ]; then
  echo "🚫 No new or modified .py files found in $folder/"
  exit 0
fi

echo "📝 Files to commit:"
echo "$files"

for file in $files; do
  filename=$(basename "$file" .py)
  git add "$file"
  git commit -m "feat($folder): add solution for '$filename'"
done

echo "🔄 Pulling latest changes with rebase..."
if git pull --rebase; then
  echo "✅ Pull successful. Now pushing..."
  git push origin main
else
  echo "❌ Pull failed. Please resolve conflicts and run the script again."
fi
