# Last updated: 28/09/2026, 21:26:46
class Solution:
    def maxDepth(self, s: str) -> int:
        stack =[]
        all = 0
        for i in s:
            if i == "(":
                stack.append(i)
                now = stack.count("(")
            elif i == ")":
                if now > all:
                    all = now
                stack.pop()
        return all
