echo "Enter folder name (e.g., arrays,fundamentals,two_pointers,hashing,sliding_window,bit_manipulation,linked_list,dp):"
read folder

# Add -u to show files inside completely untracked directories
files=$(git status --porcelain -u | awk '{print $2}' | grep -E "^$folder/.*\.(py|sql|sh)$")

if [ -z "$files" ]; then
  echo "No new or modified .py, .sql, or .sh files found in $folder/"
  exit 0
fi

echo "Files to commit:"
echo "$files"

for file in $files; do
  # Extract filename with its extension directly
  filename=$(basename "$file")
  git add "$file"
  git commit -m "feat($folder): add solution for '${filename}'"
done

# Also add -u here for the extra changes check
extra_changes=$(git status --porcelain -u | awk '{print $2}' | grep -vE "^$folder/.*\.(py|sql|sh)$")

stash_needed=false
if [ -n "$extra_changes" ]; then
  echo "Extra changes found (outside $folder):"
  echo "$extra_changes"
  read -p "Do you want to commit them as 'chore: update project files'? (y/n): " confirm
  if [ "$confirm" == "y" ]; then
    git add $extra_changes
    git commit -m "chore: update project files"
  else
    echo "Skipped committing extra changes. Stashing them temporarily..."
    git stash push -u -k -m "smart_commit_auto_stash"
    stash_needed=true
  fi
fi

echo "Pulling latest changes with rebase..."
if git pull --rebase; then
  echo "Pull successful. Now pushing..."
  git push origin main
else
  echo "Pull failed. Please resolve conflicts and run the script again."
fi

if [ "$stash_needed" = true ]; then
  echo "Restoring your skipped changes..."
  git stash pop
fi