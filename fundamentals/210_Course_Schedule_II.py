# Problem: 210. Course Schedule II
# LeetCode: https://leetcode.com/problems/course-schedule-ii/
# Difficulty: Medium

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = {i:set() for i in range(numCourses)}
        graph = collections.defaultdict(set)
        for i,j in prerequisites:
            preq[i].add(j)
            graph[j].add(i)
        
        q = collections.deque([])
        for k, v in preq.items():
            if len(v) == 0:
                q.append(k)
        taken = []
        while q:
            course = q.popleft()
            taken.append(course)
            if len(taken) == numCourses:
                return taken
            for cor in graph[course]:
                preq[cor].remove(course)
                if not preq[cor]:
                    q.append(cor)
        return []
