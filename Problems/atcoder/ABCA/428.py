S, A ,B , X = map(int, input().split())

ans = 0
M = [S]*A + [0]*B

print(sum(M[i%len(M)] for i in range(X)))
