class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0

        def maxUnits(box):
            return box[-1]

        boxTypes.sort(key=maxUnits)

        while boxTypes and truckSize:
            numBoxes, numUnits = boxTypes.pop()
            useable = min(truckSize, numBoxes)

            truckSize -= useable
            ans += useable * numUnits
        
        return ans
