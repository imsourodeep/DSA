# Last updated: 05/09/2026, 21:04:20
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest = 127
        for i in letters:
            if ord(i)>ord(target) and ord(i)<smallest:
                smallest = ord(i)
        if smallest == 127:
            return letters[0]
        return chr(smallest)
        