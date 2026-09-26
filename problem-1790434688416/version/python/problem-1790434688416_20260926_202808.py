# Last updated: 26/09/2026, 20:28:08
'''
If the source and target square is same, then there is no need to move.
If the squares are different, then at-max only 2 moves will be required by the queen to reach their, but if it is in the diagonal, then only 1 move is required.
For diagonal finding: if absolute difference in the row co-ordinate and column co-ordinate are equal, then the squares are in a diagonal.
'''

1class Solution:
2    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
3        
4        if (source == target):
5            return 0
6        elif abs(source[0]-target[0]) == abs(source[1]-target[1]):
7            return 1
8        
9        elif (source[0] == target[0]) or (source[1] == target[1]):
10            return 1
11        
12        return 2
13        