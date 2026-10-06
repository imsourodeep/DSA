# Last updated: 07/10/2026, 00:10:27
1class Solution:
2    def minAddToMakeValid(self, s: str) -> int:
3        stack =[]
4        count = 0
5        if s == "":
6            return 0
7        for i in s:
8            if i == "(":
9                stack.append(i)
10                count += 1
11            elif i ==")" and stack != []:
12                count -= 1
13                stack.pop()
14            elif i ==")" and stack == []:
15                count += 1
16        return abs(count)
17        