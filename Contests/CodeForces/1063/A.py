def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(1, len(A), 2):
        if i == len(A)-1: break
        if A[i] != A[i+1]: return "NO"
    return "YES"
for _ in range(int(input())):
    print(solve())