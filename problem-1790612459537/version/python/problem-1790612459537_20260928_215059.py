# Last updated: 28/09/2026, 21:50:59
# If number is less than 0, then return False, otherwise, check if by repeated divisions by 2, if the value reduces to 1, then the number is power of 2, otherwise not.
1class Solution:
2    def isPowerOfTwo(self, n: int) -> bool:
3        if (n<1):
4            return False
5        while (n%2 == 0):
6            n/=2
7        return n == 1