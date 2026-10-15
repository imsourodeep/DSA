# Last updated: 15/10/2026, 10:45:49
1
2class Solution:
3    def sumCounts(self, nums: List[int]) -> int:
4        l = len(nums)
5
6        subarrays = []
7        for i in range(l):
8            for j in range(i, l):
9                subarrays.append(nums[i:j+1])
10
11        ans = 0
12
13        for subarray in subarrays:
14            distinct = len(set(subarray))
15            ans += distinct * distinct
16
17        return ans
18