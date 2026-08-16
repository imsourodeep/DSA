# Last updated: 16/08/2026, 12:33:27
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mymax = 0
        secmax = 0
        for i in nums:
            if i>mymax:
                secmax = mymax
                mymax = i
            elif i>secmax:
                secmax = i
        return (mymax-1)*(secmax-1)
        