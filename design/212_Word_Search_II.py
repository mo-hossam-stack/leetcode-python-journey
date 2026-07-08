# Problem: 212. Word Search II
# LeetCode: https://leetcode.com/problems/word-search-ii/
# Difficulty: Hard

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        self.result = set()
        self.rows, self.cols = len(board), len(board[0])
        self.visited = set()

        def backtrack(r, c, node, path):
            if node.is_end_of_word:
                self.result.add(path)
                node.is_end_of_word = False 
            
            self.visited.add((r, c))
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < self.rows and 0 <= new_c < self.cols and (new_r, new_c) not in self.visited:
                    next_char = board[new_r][new_c]
                    if next_char in node.children:
                        backtrack(new_r, new_c, node.children[next_char], path + next_char)

            self.visited.remove((r, c))

        for r in range(self.rows):
            for c in range(self.cols):
                start_char = board[r][c]
                if start_char in trie.root.children:
                    backtrack(r, c, trie.root.children[start_char], start_char)

        return list(self.result)
