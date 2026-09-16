class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ymake = {0:0,1:0,2:0}
        gridmake = {0:0,1:0, 2:0}
        for i in range(rows):
            for j in range(cols):
                gridmake[grid[i][j]] += 1
        mid = cols//2
        tail = [x[mid] for x in grid[mid:]]
        left = [grid[i][i] for i in range(mid)]
        right = [grid[i][-(i+1)] for i in range(mid)]
        myy = tail + left + right
        for num in myy:
            ymake[num] += 1
        outmake = {}
        for i in range(3):
            outmake[i] = gridmake[i] - ymake[i]
        #print(ymake)
        #print(outmake)
        
        mn = math.inf
        #ynum = None
        #outnum =  None
        #yops =0
        #outops = 0
        for i in range(3):
            for j in range(3):
                if i == j: continue
                turny = 0
                turnout =0
                for key, val in ymake.items():
                    if key != i:
                        turny += ymake[key]
                for key, val in outmake.items():
                    if key != j:
                        turnout += outmake[key]
                #oldmn = mn
                mn = min(mn, turny+turnout)
                #if oldmn != mn:
                    #yops = turny
                    #outops = turnout
                    #ynum = i
                    #outnum = j
        #print(f"{yops=}")
        #print(f"{outops=}")
        #print(f"{ynum=}")
        #print(f"{outnum=}")
        return mn
                        