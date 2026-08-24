# Last updated: 24/08/2026, 21:01:55
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
        