# Problem: Design Task Manager
# LeetCode: https://leetcode.com/problems/design-task-manager/
# Difficulty: Medium

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.users = defaultdict(set)
        self.tasks = defaultdict(tuple)
        self.heap = SortedList()

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.users[userId].add((taskId, priority))
        self.tasks[taskId] = (userId, priority)
        self.heap.add((priority, taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, priority = self.tasks[taskId]
        self.rmv(taskId)
        self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        userId, priority = self.tasks[taskId]
        self.users[userId].discard((taskId, priority))
        del self.tasks[taskId]
        self.heap.discard((priority, taskId, userId))

    def execTop(self) -> int:
        if not self.heap:
            return -1
        _, taskId, userId = self.heap[-1]
        self.rmv(taskId)
        return userId