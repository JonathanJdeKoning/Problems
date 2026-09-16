class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        a,b = start
        x,y = target

        dist = abs(a-x) + abs(b-y)

        return dist%2==0