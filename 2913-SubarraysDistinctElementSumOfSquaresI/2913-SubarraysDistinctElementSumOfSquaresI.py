# Last updated: 15/10/2026, 10:47:19

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        l = len(nums)

        subarrays = []
        for i in range(l):
            for j in range(i, l):
                subarrays.append(nums[i:j+1])

        ans = 0

        for subarray in subarrays:
            distinct = len(set(subarray))
            ans += distinct * distinct

        return ans
