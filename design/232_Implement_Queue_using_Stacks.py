# Problem: 232. Implement Queue using Stacks
# LeetCode: https://leetcode.com/problems/implement-queue-using-stacks/
# Difficulty: Easy

class MyQueue(object):
    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    def push(self, x):
        self.in_stk.append(x)

    def pop(self):
        self.peek()
        return self.out_stk.pop()

    def peek(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]

    def empty(self):
        return not self.in_stk and not self.out_stk

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
