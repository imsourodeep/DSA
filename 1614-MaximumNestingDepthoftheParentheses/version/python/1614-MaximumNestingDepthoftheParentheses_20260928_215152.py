# Last updated: 28/09/2026, 21:51:52
1class Solution:
2    def maxDepth(self, s: str) -> int:
3        stack =[]
4        all = 0
5        for i in s:
6            if i == "(":
7                stack.append(i)
8                now = stack.count("(")
9            elif i == ")":
10                if now > all:
11                    all = now
12                stack.pop()
13        return all
14