# Problem: 192. Word Frequency
# LeetCode: https://leetcode.com/problems/word-frequency/
# Difficulty: Medium

awk '{for(i=1;i<=NF;i++) cnt[$i]++}
END {
    for(w in cnt) print w, cnt[w]
}' words.txt | sort -k2,2nr
