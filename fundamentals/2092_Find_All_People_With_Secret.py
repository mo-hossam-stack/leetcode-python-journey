# Problem: Find All People With Secret
# LeetCode: https://leetcode.com/problems/find-all-people-with-secret/
# Difficulty: Hard

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])

        adj = [[] for _ in range(n)]

        meetings.append([0, firstPerson, 0])

        for x, y, t in meetings:
            adj[x].append((t, y))
            adj[y].append((t, x))

        INF = 10**18
        minVisitedTime = [INF] * n

        def dfs(person: int, time: int):
            if time >= minVisitedTime[person]:
                return

            prev_min = minVisitedTime[person]
            minVisitedTime[person] = time

            meetings_list = adj[person]
            start_idx = bisect.bisect_left(meetings_list, (time, -1))

            for i in range(start_idx, len(meetings_list)):
                meeting_time, neighbor = meetings_list[i]

                if meeting_time >= prev_min:
                    break

                if time <= meeting_time < prev_min:
                    dfs(neighbor, meeting_time)

        dfs(0, 0)

        return [i for i in range(n) if minVisitedTime[i] != INF]
