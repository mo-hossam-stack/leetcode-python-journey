# Problem: Design Spreadsheet
# LeetCode: https://leetcode.com/problems/design-spreadsheet/
# Difficulty: Medium


from collections import defaultdict

class Spreadsheet:

    def __init__(self, _rows: int):
        self.spreadsheet = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.spreadsheet[cell] = 0

    def getValue(self, formula: str) -> int:
        return sum(
            self.spreadsheet[term] if term[0].isalpha() else int(term)
            for term in formula[1:].split('+')
        )