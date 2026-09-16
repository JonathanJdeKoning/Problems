def solve():
    N = int(input())
    S = input()
    if S == S[::-1]:
        print("0\n")
        return 
    
    for mask in range(1 << N):
        idx = []
        for j in range(N):
            if (mask & (1 << j)):
                idx.append(j)

        rem = [S[i] for i in idx]
        idx = set(idx)
        if rem != sorted(rem):
            continue
        new = [S[i] for i in range(len(S)) if i not in idx]
        if new == new[::-1]:
            print(len(idx))
            print(*sorted([i+1 for i in idx]))
            return
    print(-1)

T = int(input())
for _ in range(T):
    solve()

