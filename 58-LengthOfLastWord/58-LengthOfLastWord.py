# Last updated: 16/08/2026, 12:33:49
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        word = list(s.split())
        return len(word[0])

        