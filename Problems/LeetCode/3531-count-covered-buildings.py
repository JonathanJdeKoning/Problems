class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        yMap = {}
        xMap = {}

        for x, y in buildings:
            if y not in xMap:
                xMap[y] = [x,x]
            else:
                mn, mx = xMap[y]
                mn = min(mn, x)
                mx = max(mx, x)
                xMap[y] = [mn, mx]
            if x not in yMap:
                yMap[x] = [y,y]
            else:
                mn, mx = yMap[x]
                mn = min(mn, y)
                mx = max(mx, y)
                yMap[x] = [mn, mx]
        ans = 0
        for x, y in buildings:
            mnX, mxX = xMap[y]
            mnY, mxY = yMap[x]
            if x in range(mnX+1, mxX) and y in range(mnY+1, mxY):
                ans += 1
        print(xMap)
        print(yMap)
        return ans

