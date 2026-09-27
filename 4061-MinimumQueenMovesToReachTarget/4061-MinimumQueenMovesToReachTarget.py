# Last updated: 27/09/2026, 12:57:11
class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        
        if (source == target):
            return 0
        elif abs(source[0]-target[0]) == abs(source[1]-target[1]):
            return 1
        
        elif (source[0] == target[0]) or (source[1] == target[1]):
            return 1
        
        return 2
        