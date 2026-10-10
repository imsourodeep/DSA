# Last updated: 10/10/2026, 21:06:38
1
2class Solution:
3    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
4        ans = [-1, -1]
5        prod = float('-inf')
6
7        for i in range(len(nums) - 1):
8            for j in range(i + 1, len(nums)):
9                if nums[i] + nums[j] == target and nums[i] > nums[j]:
10                    if nums[i] * nums[j] > prod:
11                        prod = nums[i] * nums[j]
12                        ans = [i, j]
13
14                elif nums[i] + nums[j] == target and nums[j] > nums[i]:
15                    if nums[i] * nums[j] > prod:
16                        prod = nums[i] * nums[j]
17                        ans = [j, i]
18
19        return ans
20