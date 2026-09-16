from math import inf
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    S = list(input())
    X = list("0"*N)
    if S[0] == "1" or S[-1] == "1": return -1
    
    mn = A.index(1)
    mx = A.index(N)
    if S[mn] == "1": return -1
    if S[mx] == "1": return -1

    for i in range(min(mn, mx)+1, max(mx, mn)):
        X[i] = "1"

    start = A[0]
    end = A[-1]
    for i in range(1, mn):
        if A[i] < start:
            X[i] = "1"
    for i in range(1, mx):
        if A[i] > start:
            X[i] = "1"
    
    for i in range(mn+1, N):
        if A[i] < end:
            X[i] = "1"
    for i in range(mx+1, N):
        if A[i] > end:
            X[i] = "1"
    
    for i in range(N):
        if S[i] == "0": continue
        if X[i] != "1": return -1
    return f"5\n{1+min(mn,mx)} {1+max(mn,mx)}\n1 {1+mn}\n1 {1+mx}\n{1+mn} {N}\n{1+mx} {N}"


for _ in range(int(input())):
    print(solve())