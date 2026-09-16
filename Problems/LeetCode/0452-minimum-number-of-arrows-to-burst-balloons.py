class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort balloons by their end position
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        end = points[0][1]
        
        for balloon in points:
            start, end_of_balloon = balloon
            # If the balloon starts after the current end point, it needs a new arrow
            if start > end:
                arrows += 1
                end = end_of_balloon  # Update the end point
        return arrows
        