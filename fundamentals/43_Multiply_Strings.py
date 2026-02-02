# Problem:  Multiply Strings
# LeetCode: https://leetcode.com/problems/multiply-strings/
# Difficulty: Medium

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        first_number = num1[::-1]
        second_number = num2[::-1]

        results = []
        for index, digit in enumerate(second_number):
            results.append(self.multiply_one_digit(digit, index, first_number))

        answer = self.sum_results(results)

        return "".join(str(digit) for digit in reversed(answer))

    def multiply_one_digit(
        self, digit2: str, num_zeros: int, first_number: List[str]
    ) -> List[int]:
        current_result = [0] * num_zeros
        carry = 0

        for digit1 in first_number:
            multiplication = int(digit1) * int(digit2) + carry
            carry = multiplication // 10
            current_result.append(multiplication % 10)

        if carry != 0:
            current_result.append(carry)
        return current_result

    def sum_results(self, results: List[List[int]]) -> List[int]:
        answer = results.pop()

        for result in results:
            new_answer = []
            carry = 0
            for digit1, digit2 in zip_longest(result, answer, fillvalue=0):
                curr_sum = digit1 + digit2 + carry
                carry = curr_sum // 10
                new_answer.append(curr_sum % 10)

            if carry != 0:
                new_answer.append(carry)

            answer = new_answer

        return answer
