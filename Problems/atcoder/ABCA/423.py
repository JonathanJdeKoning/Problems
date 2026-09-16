X, C = map(int, input().split())
ans = 0
for i in range(X):
    W = 1000*i  + i*C
    if W > X:
        exit(print(ans))
    ans = W - (i*C)
print(0)
