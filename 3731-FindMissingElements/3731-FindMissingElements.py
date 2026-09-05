# Last updated: 05/09/2026, 12:51:34
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        num_set = set(nums)
        mini = min(nums)
        maxi = max(nums)
        for i in range(mini,maxi+1):
            if i not in num_set:
                ans.append(i)
        return ans