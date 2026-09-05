# Last updated: 05/09/2026, 12:51:38
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        pd = 1
        num = n
        while n>0:
            pd = pd* (n%10)
            n=n//10
        if pd%t == 0:
            return num
        else:
            return self.smallestNumber(num+1,t)


        