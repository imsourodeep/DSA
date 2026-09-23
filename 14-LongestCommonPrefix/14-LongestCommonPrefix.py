# Last updated: 24/09/2026, 00:13:00
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans =""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i]==strs[-1][i]:
                ans += strs[0][i]
            else :
                break
        return ans
            