def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    for a in range(min(N, 500) - 1):
        for b in range(a+1, min(N, 500)):
            if (A[b] % A[a]) % 2 == 0:
                return f"{A[a]} {A[b]}"
    return -1


for _ in range(int(input())):
    print(solve())