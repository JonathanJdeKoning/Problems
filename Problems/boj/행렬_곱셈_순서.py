N = int(input())

ans = 0


A = []
D= []
for _ in range(N):
    X, Y= list(map(int, input().split()))
    A.append((X,Y))
D.append(A[0][0])
D.append(A[0][1])
for x,y in A[1:]:
    D.append(y)
dp = [[-1]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
#print(D)
for j in range(1, N):
    for i in range(N-j):
        y = i
        x = j+i
        #print(y,x)
        dp[y][x] = min(dp[y][k]+dp[k+1][x]+D[y-1]*D[k]*D[x] for k in range(y,x))


#for row in dp:
#    print(row)
print(dp[0][-1])
