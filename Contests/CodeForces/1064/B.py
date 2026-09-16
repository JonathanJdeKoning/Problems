def solve():
    A, B, N = list(map(int, input().split()))
    if N == 1 or N*B <= A or B >= A:
        print(1)
        return
    
    if (A/N == B):
        print(1)
        return
    else:
        print(2)
        return
for _ in range(int(input())):
    solve()