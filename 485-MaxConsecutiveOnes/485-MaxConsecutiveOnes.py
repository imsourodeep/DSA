# Last updated: 16/08/2026, 12:33:37
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans =[]
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                ans.append(count)
                count = 0
        ans.append(count)
        return max(ans)