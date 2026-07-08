# Problem: 208. Implement Trie (Prefix Tree)
# LeetCode: https://leetcode.com/problems/implement-trie-prefix-tree/
# Difficulty: Medium

class Trie:

    def __init__(self):
        self.node = {}

    def insert(self, word: str) -> None:
        ro = self.node
        for i in word:
            if i not in ro:
                ro[i] = {}
            ro = ro[i]
        ro['*'] = ''

    def search(self, word: str) -> bool:
        ro = self.node
        for i in word:
            if i not in ro:
                return False
            ro = ro[i]
        if '*' in ro:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        ro = self.node
        for i in prefix:
            if i not in ro:
                return False
            ro = ro[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
