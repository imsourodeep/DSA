# Last updated: 05/09/2026, 12:51:35
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumation = 0
        digitsum = 0
        digitprod = 1
        temp = n
        while temp != 0:
            digitsum += temp%10
            digitprod *= temp%10
            summation = digitsum + digitprod
            temp //=10
        return n%summation ==0
        