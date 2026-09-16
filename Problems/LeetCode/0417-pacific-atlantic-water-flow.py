class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        canReachP = set()
        canReachA = set()

        qp = deque()
        qa = deque()

        for i in range(R):
            for j in range(C):
                if i == 0 or j == 0:
                    qp.append((i,j))
                if i == R-1 or j==C-1:
                    qa.append((i,j))

        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        seenP = set()
        seenA = set()
        while qp:
            cy, cx = qp.popleft()
            ch = heights[cy][cx]
            seenP.add((cy, cx))

            for dy, dx in dirs:
                ny, nx = dy+cy, dx+cx
                if (ny, nx) in seenP: continue
                if ny<=-1 or nx<=-1 or ny>=R or nx>=C: continue
                if heights[ny][nx] < ch: continue
                qp.append((ny, nx))

        while qa:
            cy, cx = qa.popleft()
            ch = heights[cy][cx]
            seenA.add((cy, cx))

            for dy, dx in dirs:
                ny, nx = dy+cy, dx+cx
                if (ny, nx) in seenA: continue
                if ny<=-1 or nx<=-1 or ny>=R or nx>=C: continue
                if heights[ny][nx] < ch: continue
                qa.append((ny, nx))

        return list(seenP.intersection(seenA))

        
        