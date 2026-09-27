# Last updated: 27/09/2026, 12:57:31
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            sum = 0
            while (nums[i]!=0):
                sum += nums[i] % 10
                nums[i]//=10
            # print(sum)
            if i == sum:
                return i
        return -1
