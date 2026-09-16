class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        R, C = len(picture), len(picture[0])
        ans = 0
        rows = defaultdict(int)
        cols = defaultdict(int)
        for i in range(R):
            for j in range(C):
                if picture[i][j] == "B":
                    rows[i] += 1
                    cols[j] += 1

        for i in range(R):
            for j in range(C):
                if picture[i][j] == "W": continue
                if rows[i] == 1 and cols[j] == 1: ans += 1
        return ans