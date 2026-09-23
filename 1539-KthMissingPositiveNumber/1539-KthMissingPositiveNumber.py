# Last updated: 24/09/2026, 00:12:27
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        miss =[]
        n = len(arr)
        for i in range(1,n+k+1):
            if i not in arr:
                miss.append(i)
        return miss[k-1]