def solve():
    N = int(input())
    M = [] 
    M.append(list(map(int, input().split()))) 
    M.append(list(map(int, input().split()))) 
    
    mn = min(M[0][0], M[-1][-1])
    mx = max(M[0][0], M[-1][-1])
    
    negVar = [[0]*N for _ in range(2)]
    posVar = [[0]*N for _ in range(2)]
    dp = [[0]*N for _ in range(2)]
    for i in range(2):
        for j in range(N):
            v = M[i][j]
            if v >= mn and v <= mx: 
                continue
            if v < mn:
                negVar[i][j] = mn - v
            if v > mx:
                posVar[i][j] = v - mx
    
    for i in range(1, N):
        dp[0][i] = max(dp[0][i-1], negVar[0][i] + posVar[0][i])

    dp[1][0] = negVar[1][0] + posVar[1][0]

    for i in range(1, N):
        dp[1][i] = max(min(dp[1][i-1], dp[0][i]), posVar[1][i] + negVar[1][i])

    
for _ in range(int(input())):
    print(solve())