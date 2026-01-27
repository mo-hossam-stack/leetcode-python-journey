# Problem: Substring with Concatenation of All Words
# LeetCode: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Difficulty: Hard

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        count = {}
        for i in words:
            count[i] = count.get(i, 0) + 1
        length = len(words[0]) * len(words)
        single = len(words[0])
        res = []
        for offsets in range(single):
            left = offsets
            curr = {}
            window = 0
            for right in range(offsets, len(s), single):
                slices = s[right:right+single]
                if slices in count:
                    curr[slices] = curr.get(slices, 0) + 1
                    window += 1
                    while curr[slices] > count[slices]:
                        left_word = s[left:left + single]
                        curr[left_word] -= 1
                        if curr[left_word] == 0:
                            del curr[left_word]
                        left += single
                        window -= 1
                    if window * single == length:
                        if count == curr:
                            res.append(left)
                else:
                    left = right + single
                    curr.clear()
                    window = 0

        return res
