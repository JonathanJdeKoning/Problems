class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guarded = set(())
        guards = set([tuple(pos) for pos in guards])
        walls = set([tuple(pos) for pos in walls])

        for i in range(m):
            guarding = False
            for j in range(n):
                if (i,j) in guards:
                    guarding = True
                if (i,j) in walls:
                    guarding = False
                    continue
                if guarding:
                    guarded.add((i,j))
                
            guarding = False
            for j in range(n-1, -1, -1):
                if (i,j) in guards:
                    guarding = True
                if (i,j) in walls:
                    guarding = False
                    continue
                if guarding:
                    guarded.add((i,j))

        for j in range(n):
            guarding = False
            for i in range(m):
                if (i,j) in guards:
                    guarding = True
                if (i,j) in walls:
                    guarding = False
                    continue
                if guarding:
                    guarded.add((i,j))
                
            guarding = False
            for i in range(m-1, -1, -1):
                if (i,j) in guards:
                    guarding = True
                if (i,j) in walls:
                    guarding = False
                    continue
                if guarding:
                    guarded.add((i,j))

        return (m*n) - (len(guarded) + len(walls))

            
            