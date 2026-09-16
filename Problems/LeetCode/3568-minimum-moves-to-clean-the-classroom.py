class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        orig =  energy
        R, C = len(classroom), len(classroom[0])
        sy, sx = None, None
        rests = set()
        litters = 0 
        bitmap = {}
        for i, row in enumerate(classroom):
            for j, cell in enumerate(row):
                if cell == "S":
                    sy = i
                    sx = j
                if cell == "R":
                    rests.add((i,j))
                if cell == "L":
                    litters += 1
                    bitmap[(i,j)] = 2**len(bitmap)
            
                    
        q = deque([(energy, set(), sy, sx)])
        steps = -1
        best= {}


        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            steps += 1
            for _ in range(len(q)):
                ce, l, cy, cx = q.popleft()
                #print(ce, l, cy, cx)

                id = sum(bitmap[ll] for ll in l)
                #print(f"{id=}")
                #print(f"{best=}")
                if id not in best:
                    best[id] = defaultdict(int)
                    best[id][(cy, cx)] = ce
                    #print("Added")
                else:
                    if (cy, cx) in best[id] and best[id][(cy,cx)] >= ce:
                        continue
                    best[id][(cy,cx)] = ce
                    #print("Added")
                

                if classroom[cy][cx] == "R": ce = orig
                
                if classroom[cy][cx] == "L" and (cy, cx) not in l:
                    l.add((cy, cx))
                    id = id + bitmap[(cy, cx)]
                    if id not in best:
                        best[id] = defaultdict(int)
                        best[id][(cy, cx)] = ce
                    else:
                        if (cy, cx) in best[id] and best[id][cy, cx] >= ce:
                            continue
                        best[id][(cy, cx)] = ce
                        
                if len(l) == litters: return steps
                
                if ce == 0: continue    
                for dy, dx in directions:
                    ny, nx = dy+ cy, dx+cx

                    if min(ny, nx) == -1 or ny == R or nx == C: continue
                    if classroom[ny][nx] == "X": continue
                    if (ny, nx) in best[id] and best[id][(ny,nx)] >= ce: continue

                    q.append((ce - 1, l.copy(), ny, nx))

        return -1
                    


                
                
                