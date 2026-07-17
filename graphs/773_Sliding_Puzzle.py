# Problem: 773. Sliding Puzzle
# LeetCode: https://leetcode.com/problems/sliding-puzzle/
# Difficulty: Hard
class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        start = "".join(str(num) for row in board for num in row)
        target = "123450"
        
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        queue = deque([(start, start.index('0'), 0)])
        visited = {start}
        
        while queue:
            state, zero_idx, moves = queue.popleft()
            
            if state == target:
                return moves
            
            for next_idx in neighbors[zero_idx]:
                state_arr = list(state)
                state_arr[zero_idx], state_arr[next_idx] = state_arr[next_idx], state_arr[zero_idx]
                next_state = "".join(state_arr)
                
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, next_idx, moves + 1))
                    
        return -1
