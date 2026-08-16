# Last updated: 16/08/2026, 12:33:59
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        original = x
        if x<0:
            return False
        while x!=0 :
            num = (num*10) + (x%10)
            x //=10
        return original == num