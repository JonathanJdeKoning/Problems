from itertools import takewhile
def solve():
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    if N == 1: return 0
    
    A.sort()
    A = [x%2 for x in A]
    if A[0] == A[-1]: return 0 
    x = len(list(takewhile(lambda z: z==A[0], A)))
    y = len(list(takewhile(lambda z: z==A[-1], A[::-1])))
    return min(x,y)
    



T = int(input())
for _ in range(T):
    print(solve())
