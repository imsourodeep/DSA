# Last updated: 11/10/2026, 09:54:48
1class Solution:
2    def threeFibonacciSum(self, n: int) -> bool:
3        i = 0
4        j = 1
5        k = 1
6        t = j+k
7        while(t <= n):
8            if (i+j+k == n):
9                return True
10            i = j
11            j = k
12            k = t
13            t = j+k
14        return False
15            