# Last updated: 16/08/2026, 12:33:20
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums),max(nums))