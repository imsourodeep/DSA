# Last updated: 18/08/2026, 11:05:01
class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        rows = len(drones)
        cols = len(drones[0])
        mini = float('inf')
        index = -1
        for i in range(rows):
            dist = 0
        
            for j in range(cols - 1):
                dist += abs(drones[i][j] - target[j])
        
            if dist <= drones[i][2] and dist < mini:
                mini = dist
                index = i
        
        return index