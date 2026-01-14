# Problem: Separate Squares II
# LeetCode: https://leetcode.com/problems/separate-squares-ii/
# Difficulty: Hard

class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)
    
    def update(self, idx, l, r, ql, qr, delta):
        if ql >= r or qr <= l:
            return
        if ql <= l and r <= qr:
            self.count[idx] += delta
        else:
            mid = (l + r) // 2
            self.update(idx * 2, l, mid, ql, qr, delta)
            self.update(idx * 2 + 1, mid, r, ql, qr, delta)

        if self.count[idx] > 0:
            self.covered[idx] = self.xs[r] - self.xs[l]
        else:
            if r - l == 1:
                self.covered[idx] = 0
            else:
                self.covered[idx] = self.covered[idx * 2] + self.covered[idx * 2 + 1]

class Solution:

    def separateSquares(self, squares):
        events = []
        x_coords = set()
        
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            x_coords.add(x)
            x_coords.add(x + l)
        
        events.sort(key=lambda e: (e[0], e[1]))
        xs_sorted = sorted(x_coords)
        mapping = {x: i for i, x in enumerate(xs_sorted)}
        
        seg_tree = SegmentTree(xs_sorted)
        
        segments = []  
        prefix_area = 0.0
        prev_y = events[0][0]
        i = 0
        N = len(events)
        
        while i < N:
            cur_y = events[i][0]
            if cur_y > prev_y:
                cur_union = seg_tree.covered[1]
                segments.append((prev_y, cur_y, cur_union, prefix_area))
                prefix_area += cur_union * (cur_y - prev_y)
                prev_y = cur_y
            while i < N and events[i][0] == cur_y:
                y, typ, x1, x2 = events[i]
                left_idx = mapping[x1]
                right_idx = mapping[x2]
                seg_tree.update(1, 0, seg_tree.n, left_idx, right_idx, typ)
                i += 1
        
        total_area = prefix_area
        target_area = total_area / 2.0

        for (y_start, y_end, union_length, seg_prefix) in segments:
            seg_area = union_length * (y_end - y_start)
            if seg_prefix + seg_area >= target_area - 1e-10:
                delta_y = (target_area - seg_prefix) / union_length
                return float(y_start + delta_y)
