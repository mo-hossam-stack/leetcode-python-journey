# Problem: 2213. Longest Substring of One Repeating Character
# LeetCode: https://leetcode.com/problems/longest-substring-of-one-repeating-character/
# Difficulty: Hard

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        tree = [None] * (4 * len(s))

        def merge(left, right):
            left_char = left[0]
            right_char = right[1]

            length = left[2] + right[2]

            best = max(left[5], right[5])

            prefix = left[3]

            if left[3] == left[2] and left[1] == right[0]:
                prefix = left[2] + right[3]

            suffix = right[4]

            if right[4] == right[2] and left[1] == right[0]:
                suffix = left[4] + right[2]

            if left[1] == right[0]:
                best = max(best, left[4] + right[3])

            return (left_char, right_char, length, prefix, suffix, best)

        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, idx, char):
            if l == r:
                tree[node] = (char, char, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, r, idx, char)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, len(s) - 1)

        answer = []

        for i in range(len(queryCharacters)):
            update(
                1,
                0,
                len(s) - 1,
                queryIndices[i],
                queryCharacters[i]
            )

            answer.append(tree[1][5])

        return answer
