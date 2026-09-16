def solve():
    R, C = list(map(int, input().split()))
    
    mat = [list(input()) for _ in range( R )]

    need = "vika"
    need = list(need[::-1])
    curr = need.pop()
    for colIDX in range(C):
        col = [row[colIDX] for row in mat]
        if curr in col:
            if not need:
                return "YES"
            curr = need.pop()

    return "NO"


for _ in range(int(input())):
    print(solve())
        
    