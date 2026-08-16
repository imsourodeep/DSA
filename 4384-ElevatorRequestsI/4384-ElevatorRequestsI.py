# Last updated: 16/08/2026, 12:32:58
class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        time = 0
        prev = 0
        for i in range(len(requests)):
            if requests[i] != prev:
                time += max(requests[i],prev) - min(requests[i],prev)
                prev = requests[i]

        return time