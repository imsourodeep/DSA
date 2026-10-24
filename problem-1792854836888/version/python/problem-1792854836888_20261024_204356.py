# Last updated: 24/10/2026, 20:43:56
1class Solution:
2    def peakValleyDifference(self, nums: list[int]) -> int:
3        peaksum = 0
4        valleysum = 0
5        n = len(nums)
6        for i in range(1,n-1):
7            if i>0 and i<n-1 and nums[i] > nums[i-1] and nums[i] > nums[i+1]:
8                peaksum += nums[i]
9            elif i>0 and i<n-1 and nums[i] < nums[i-1] and nums[i] < nums[i+1]:
10                valleysum += nums[i]
11
12        return peaksum-valleysum