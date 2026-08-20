# Last updated: 20/08/2026, 19:52:24
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        i = 0
        j = n-1
        while (j<len(haystack)):
            if haystack[i:j+1]==needle:
                return i
            else:
                i+=1
                j+=1
        return -1