class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points= set()
        for wack in nums:
            for i in range(wack[0], wack[1]+1):
                points.add(i)
        return len(points)