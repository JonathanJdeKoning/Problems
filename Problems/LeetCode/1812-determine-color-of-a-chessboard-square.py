class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letters = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
        x = int(letters[coordinates[0]]) - 1
        y = int(coordinates[1])-1

        if (x+y) %2 == 0:
            return False
        return True