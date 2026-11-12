# Problem: 420. Strong Password Checker
# LeetCode: https://leetcode.com/problems/strong-password-checker/
# Difficulty: Hard
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = (not has_lower) + (not has_upper) + (not has_digit)

        if n < 6:
            return max(6 - n, missing_types)

        repeats = []
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                repeats.append(length)
            else:
                i += 1

        if n <= 20:
            replace = sum(L // 3 for L in repeats)
            return max(replace, missing_types)

        delete_cnt = n - 20
        d = delete_cnt

        for idx in range(len(repeats)):
            if d > 0 and repeats[idx] % 3 == 0:
                repeats[idx] -= 1
                d -= 1

        for idx in range(len(repeats)):
            if d >= 2 and repeats[idx] % 3 == 1:
                repeats[idx] -= 2
                d -= 2

        total_replace = sum(L // 3 for L in repeats)
        saved_by_3 = min(total_replace, d // 3)
        total_replace -= saved_by_3

        return delete_cnt + max(total_replace, missing_types)
