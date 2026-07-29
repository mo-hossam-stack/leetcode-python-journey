# Problem: 3518. Smallest Palindromic Rearrangement II
# LeetCode: https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/
# Difficulty: Hard

class Solution:
    def count_perms(self, freq, cap: int) -> int:
        n = sum(freq)
        if n == 0:
            return 1

        ways = 1
        remaining = n
        for f in freq:
            if f == 0:
                continue
            choose = f if f <= remaining - f else remaining - f
            for i in range(choose):
                ways = ways * (remaining - i) // (i + 1)
                if ways >= cap:
                    return cap

            remaining -= f

        return ways

    def kth_permutation(self, freq: List[int], k: int) -> Optional[str]:
        if self.count_perms(freq, k) < k:
            return None

        result = []
        remaining = sum(freq)

        while remaining > 0:
            for c in range(26):
                if freq[c] == 0:
                    continue

                freq[c] -= 1
                ways = self.count_perms(freq, k)

                if k > ways:
                    k -= ways
                    freq[c] += 1
                else:
                    result.append(chr(ord('a') + c))
                    remaining -= 1
                    break
            else:
                return None

        return ''.join(result)

    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        if n == 1:
            return s if k == 1 else ""

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        half = [0] * 26
        mid = ""
        for c in range(26):
            if freq[c] % 2 == 1:
                mid = chr(ord('a') + c)
            half[c] = freq[c] // 2

        if sum(half) == 0:
            return mid if k == 1 else ""

        left = self.kth_permutation(half, k)
        if left is None:
            return ""

        return left + mid + left[::-1]
