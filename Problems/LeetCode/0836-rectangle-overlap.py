class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1,ay1,ax2,ay2 = rec1
        tx1,ty1,tx2,ty2 = rec2
        lossFromA = max(0,(min(ax2, tx2)-max(ax1, tx1))) * max(0,(min(ay2, ty2)- max(ay1,ty1)))
        return bool(lossFromA)
