# Last updated: 16/08/2026, 12:33:14
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

