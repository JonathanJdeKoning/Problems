class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        return len([x for x in rectangles if min(x) == max([min(x) for x in rectangles])])
