class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        def signsToDirs(y, x):
            if y < 0 and x < 0: return ( 0,-1)
            if y < 0 and x > 0: return (-1, 0)
            if y > 0 and x < 0: return ( 0, 1)
            if y > 0 and x > 0: return ( 1, 0)

        def dirsToSigns(dy, dx):
            if (dy, dx) == ( 0,-1): return (-1,-1)
            if (dy, dx) == (-1, 0): return (-1, 1)
            if (dy, dx) == ( 0, 1): return ( 1,-1)
            if (dy, dx) == ( 1, 0): return ( 1, 1)

        R, C = len(grid), len(grid[0])
        ey, ex = R-1, C-1

        if k == 0 and 1 not in [R, C]: return -1
        if 1 in [R, C]: return sum(sum(row) for row in grid)

        K  = k + 1        # nk digit width: 0..k
        MY, MX = 2*R+1, 2*C+1   # fy, fx digit widths (biased by R, C)
        BASE = MY * MX * K       # place value of the cost digit

        def encode(cost, fy, fx, nk):
            return cost*BASE + ((fy+R)*MX + (fx+C))*K + nk

        def decode(state):
            cost, low = divmod(state, BASE)
            nk, low = low % K, low // K
            fx, fy = low % MX - C, low // MX - R
            return cost, fy, fx, nk

        heap = [encode(grid[0][0], 1, 1, 0)]
        dirs = [(0,-1),(-1,0),(0,1),(1,0)]
        seen = {}

        while heap:
            state = heappop(heap)
            cc, fy, fx, ck = decode(state)
            cy, cx = abs(fy)-1, abs(fx)-1
            if (cy, cx) == (ey, ex): return cc

            if (fy, fx, ck) in seen and seen[(fy, fx, ck)] <= state: continue
            seen[(fy, fx, ck)] = state

            for dy, dx in dirs:
                ny, nx = dy+cy, dx+cx
                if ny >= R or nx >= C or ny <= -1 or nx <= -1: continue

                nk = ck + 1
                if (cy, cx) == (0,0) or (dy,dx) == signsToDirs(fy, fx):
                    nk = ck
                if nk > k: continue

                fdy, fdx = dirsToSigns(dy, dx)
                nfy, nfx = (ny+1)*fdy, (nx+1)*fdx

                nstate = encode(cc+grid[ny][nx], nfy, nfx, nk)
                if (nfy, nfx, nk) in seen and seen[(nfy, nfx, nk)] <= nstate: continue
                heappush(heap, nstate)
        return -1