# Last updated: 08/09/2026, 20:41:39
class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        return (n-1000)+1