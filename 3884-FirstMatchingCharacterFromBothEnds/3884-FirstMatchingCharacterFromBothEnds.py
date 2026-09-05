# Last updated: 05/09/2026, 12:51:22
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            if s[i] == s[n-i-1]:
                return i
        return -1
        