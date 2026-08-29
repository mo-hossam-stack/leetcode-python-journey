# Problem: 2948. Make Lexicographically Smallest Array by Swapping Elements
# LeetCode: https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/
# Difficulty: Medium
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        org_index = []
        for i in range(len(nums)):
            org_index.append([nums[i], i])

        org_index.sort(key=lambda x: x[0])

        org_index.append([2 * 10**9 + 1, 0])

        group = [org_index[0][0]]
        group_idx = [org_index[0][1]]

        for pair in range(1, len(org_index)):
            num = org_index[pair][0]
            idx = org_index[pair][1]
            prev = org_index[pair - 1][0]

            if num - prev > limit:

                group_idx.sort()

                for i in range(len(group)):
                    nums[group_idx[i]] = group[i]

                group, group_idx = [], []

            group.append(num)
            group_idx.append(idx)

        return nums
