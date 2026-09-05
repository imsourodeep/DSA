# Last updated: 05/09/2026, 12:51:41
class Solution:
    def minElement(self, nums: List[int]) -> int:
        sumarray = []
        for i in nums:
            s = 0
            ld = 0
            while i !=0:
                ld = i%10
                s += ld
                i//=10
            sumarray.append(s)
        return min(sumarray)

