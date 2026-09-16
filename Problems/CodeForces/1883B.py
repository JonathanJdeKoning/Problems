from collections import Counter
def solve():
    N, K = list(map(int, input().split()))
    S = input()
    if K > len(S):
        print("NO")
        return
    fq = Counter(S)
    vals = list(fq.values())
    odds = sum(1 for num in vals if num % 2 == 1)
    if K < (odds-1): 
        print("NO")
        return
    K -= (odds-1)
    print("YES")
    return






T = int(input())

for _ in range(T):
    solve()