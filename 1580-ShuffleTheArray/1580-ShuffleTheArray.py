# Last updated: 16/08/2026, 12:33:23
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans =[]

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans
