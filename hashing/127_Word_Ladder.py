# Problem: Word Ladder
# LeetCode: https://leetcode.com/problems/word-ladder/
# Difficulty: Hard

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "qwertyuioplkjhgfdsazxcvbnm":
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet:
                        queue.append((newWord, length + 1))
                        wordSet.remove(newWord)

        return 0