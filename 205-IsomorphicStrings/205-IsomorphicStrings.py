# Last updated: 18/08/2026, 11:05:19
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        reverse = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in mapping and mapping[a] != b:
                return False

            if b in reverse and reverse[b] != a:
                return False

            mapping[a] = b
            reverse[b] = a

        return True