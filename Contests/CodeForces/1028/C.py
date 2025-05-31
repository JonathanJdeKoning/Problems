from math import gcd
def solve():
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    if N == 1: return 0
    GCD = gcd(A[0], A[1])
    for num in A[2:]:
        GCD = gcd(num, GCD)
    
    if GCD in A:
        return(N - A.count(GCD))
    
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if gcd(A[i], A[j]) == GCD:
                return N
    return N + 1


for _ in range(int(input())):
    print(solve())