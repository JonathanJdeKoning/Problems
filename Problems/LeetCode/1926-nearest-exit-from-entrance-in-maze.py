class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        seen = set()
        R,C = len(maze), len(maze[0])
        q = deque([tuple(entrance)])
        steps = -1
        while q:
            steps+= 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr in seen: continue
                seen.add(curr)
                if curr != tuple(entrance):
                    if min(curr[0],curr[1]) == 0 or curr[0]==R-1 or curr[1] == C-1:
                        return steps

                for dy, dx in directions:
                    y=curr[0]+dy
                    x=curr[1]+dx
                    if min(y,x) ==-1 or y==R or x==C or (y,x) in seen: continue
                    if maze[y][x] == "+": continue
                    q.append((y,x))
        return -1



