# Problem: Meeting Rooms III
# LeetCode: https://leetcode.com/problems/meeting-rooms-iii/
# Difficulty: Hard

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        empty_rooms = list(range(n))
        heapify(empty_rooms)
        occupied_rooms = []
        num_meetings = [0] * n
        meetings.sort()

        for s, e in meetings:
            while occupied_rooms and occupied_rooms[0][0] <= s:
                heappush(empty_rooms, heappop(occupied_rooms)[1])

            if empty_rooms:
                start_time = s
                room = heappop(empty_rooms)
            else:
                start_time, room = heappop(occupied_rooms)

            heappush(occupied_rooms, (start_time + (e - s), room))
            num_meetings[room] += 1

        return num_meetings.index(max(num_meetings))
