
def upto(N): return N*(N+1)//2


def solve():
    N, K, X = list(map(int, input().split()))
    mn = upto(K)
    mx = upto(N) - upto(N-K)
    if X >=mn and X <= mx:
        return("YES")
    else:
        return("NO")
    

for _ in range(int(input())):
    print(solve())