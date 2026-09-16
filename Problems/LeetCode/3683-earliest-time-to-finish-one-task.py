class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min([sum(t) for t in tasks])