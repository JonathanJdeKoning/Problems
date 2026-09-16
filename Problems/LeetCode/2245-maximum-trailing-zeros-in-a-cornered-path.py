class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        H, W = len(grid), len(grid[0])

        for i in range(H):
            for j in range(W):
                cell = grid[i][j]
                twos = 0
                fives = 0
                while cell%2==0:
                    twos += 1
                    cell //= 2
                while cell %5==0:
                    fives += 1
                    cell //= 5
                grid[i][j] = (twos, fives)

        prefixLR = copy.deepcopy(grid)
        prefixUD = copy.deepcopy(grid)
        for i in range(H):
            twos = 0
            fives = 0
            for j in range(W):
                t, f = grid[i][j]
                twos += t
                fives += f
                prefixLR[i][j] = (twos, fives)


        for j in range(W):
            twos = 0
            fives = 0
            for i in range(H):
                t, f = grid[i][j]
                twos += t
                fives += f
                prefixUD[i][j] = (twos, fives)

        def queryL(i, j):
            return prefixLR[i][j]
        def queryR(i, j):
            base = prefixLR[i][W-1]
            bt, bf = base
            if j == 0: return base
            pt, pf = prefixLR[i][j-1]
            return (bt - pt, bf-pf)

        def queryU(i, j):
            return prefixUD[i][j]

        def queryD(i, j):
            base = prefixUD[H-1][j]
            bt, bf = base
            if i == 0: return base
            pt, pf = prefixUD[i-1][j]
            return (bt -pt, bf-pf)

        def trailers(state):
            twos = state[1][0] + state[2][0] - state[0][0]
            fives = state[1][1] + state[2][1] - state[0][1]
            return min(twos, fives)

        ans = 0
        for i in range(H):
            for j in range(W):
                X = grid[i][j]
                L = queryL(i,j)
                R = queryR(i,j)
                U = queryU(i,j)
                D = queryD(i,j)

                LU = trailers([X, L, U])
                LD = trailers([X, L, D])
                RU = trailers([X, R, U])
                RD = trailers([X, R, D])
                ans = max(ans, max(LU, LD, RU, RD))
        return ans

        