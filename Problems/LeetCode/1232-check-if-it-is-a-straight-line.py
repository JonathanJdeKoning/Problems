class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len([x[0] for x in coordinates if x[0] == coordinates[0][0]]) == len(coordinates): return True
        if len([x[1] for x in coordinates if x[1] == coordinates[0][1]]) == len(coordinates): return True


        try:
            slope = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
            for i in range(len(coordinates)-1):
                if (coordinates[i][1] - coordinates[i+1][1]) / (coordinates[i][0] - coordinates[i+1][0]) != slope: return False
            return True
        except: return False
