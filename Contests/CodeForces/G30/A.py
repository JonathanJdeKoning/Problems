def solve():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    mn = min(A)
    mx = max(A)
    if X >= mn and X <= mx:
        return "YES"
    else:
        return "NO"


for _ in range(int(input())):
    print(solve())