# Last updated: 07/10/2026, 00:15:04
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack =[]
        count = 0
        if s == "":
            return 0
        for i in s:
            if i == "(":
                stack.append(i)
                count += 1
            elif i ==")" and stack != []:
                count -= 1
                stack.pop()
            elif i ==")" and stack == []:
                count += 1
        return abs(count)
        