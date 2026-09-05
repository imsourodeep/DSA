# Last updated: 05/09/2026, 12:51:27
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for i in nums: 
            if i%2 == 0:
                if nums.count(i) == 1:
                    return i
        return -1
        