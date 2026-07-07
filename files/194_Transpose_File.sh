# Problem: 194. Transpose File
# LeetCode: https://leetcode.com/problems/transpose-file/
# Difficulty: Medium

awk '
{
    for (i = 1; i <= NF; i++)
        a[i] = a[i] ? a[i] FS $i : $i
}
END {
    for (i = 1; i <= NF; i++)
        print a[i]
}' file.txt
