def solve():
    N, S = list(map(int, input().split()))
    A = list(map(int, input().split()))
    if S in A: A.remove(S)
    if not A: return 0
    mn = min(A)
    mx = max(A)
    if S > mx:
        return abs(S-mn)
    elif S < mn:
        return abs(S-mx)
    else:
        return  min(abs(S- mn), abs(S-mx)) * 2 + max(abs(S-mn), abs(S-mx))


for _ in range(int(input())):
    print(solve())