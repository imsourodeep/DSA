# Last updated: 16/08/2026, 12:33:56
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            elif i == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif i == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif i == "]":
                if not stack or stack.pop() != "[":
                    return False
        return not stack