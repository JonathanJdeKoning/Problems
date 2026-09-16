ans = 0
M = []


def rowNums(i,j):
    nums = set(M[i])
    nums.discard(0)
    return nums

def colNums(i,j):
    nums = set([row[j] for row in M])
    nums.discard(0)
    return nums

def boxNums(i, j):
    boxI = (i//3)*3
    boxJ = (j//3)*3
    nums = set()
    for y in range(boxI, boxI+3):
        for x in range(boxJ, boxJ+3):
            nums.add(M[y][x])
    nums.discard(0)
    return nums

def allAllowed(i,j):
    baseNums = {1,2,3,4,5,6,7,8,9}
    return baseNums - allDisallowed(i,j)

def allDisallowed(i,j):
    return rowNums(i, j) | colNums(i,j) | boxNums(i, j)

def solveSudoku():
    zeros = []
    done = False
    for i in range(9):
        for j in range(9):
            if M[i][j] == 0: 
                zeros.append((i, j))

    def dfs(k):
        global ans
        global M
        nonlocal zeros
        nonlocal done
        if done: return
        if k == len(zeros):
            ans += extractEuler()
            done = True
            return

        y, x = zeros[k]
        allowed = allAllowed(y, x)
        if not allowed: return
        for num in allowed:
            M[y][x] = num
            dfs(k+1)

        M[y][x] = 0
    dfs(0)
        
def extractEuler():
    return 100*M[0][0] + 10*M[0][1] + M[0][2]

with open("c:/Users/jj720/Documents/PythonScripts/CompetitiveProgramming/Problems/Problems/Euler/sudoku.txt", "r") as file:
    for line in file.readlines():
        
        if line.startswith("Grid"):
            if not M: continue
            solveSudoku()
            
            M = []
            continue
        M.append([int(x) for x in line.strip()])

solveSudoku() 
print(ans)
