# Last updated: 05/09/2026, 12:51:58
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums),max(nums))