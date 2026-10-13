# Last updated: 13/10/2026, 19:55:59

class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        ans = [-1, -1]
        prod = float('-inf')

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target and nums[i] > nums[j]:
                    if nums[i] * nums[j] > prod:
                        prod = nums[i] * nums[j]
                        ans = [i, j]

                elif nums[i] + nums[j] == target and nums[j] > nums[i]:
                    if nums[i] * nums[j] > prod:
                        prod = nums[i] * nums[j]
                        ans = [j, i]

        return ans
