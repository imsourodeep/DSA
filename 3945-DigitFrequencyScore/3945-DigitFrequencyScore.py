# Last updated: 05/09/2026, 12:51:19
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        trav = []
        ans = 0 
        n1 = str(n)
        while n != 0:
            ld = n%10
            n = n//10
            if ld not in trav:
                c = n1.count(str(ld))
                ans += ld * c
                trav.append(ld)
        return ans