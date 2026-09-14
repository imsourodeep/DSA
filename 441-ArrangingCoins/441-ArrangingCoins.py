# Last updated: 14/09/2026, 18:35:57
class Solution:
    def arrangeCoins(self, n: int) -> int:
        staircoins = 0
        if n ==1:
            return 1
        for i in range(1,n+1):
            staircoins += i
            if n<staircoins:
                return i-1
                


