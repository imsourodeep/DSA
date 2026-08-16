# Last updated: 16/08/2026, 12:33:01
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            if s[i] == s[n-i-1]:
                return i
        return -1
        