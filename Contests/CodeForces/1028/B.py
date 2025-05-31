mod = 998244353
def solve():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    R = []
    bestP = -1
    bestQ = -1
    bestPIdx = -1
    bestQIdx = -1
    for i in range(N):
        newP = P[i]
        newQ = Q[i]

        if newP > bestP:
            bestP = newP
            bestPIdx = i

        if newQ > bestQ:
            bestQ = newQ
            bestQIdx = i

        pComp = i - bestPIdx
        qComp = i - bestQIdx

        if P[bestPIdx] > Q[bestQIdx]:
            ans = (pow(2, P[bestPIdx], mod) + pow(2, Q[pComp], mod))%mod
        elif Q[bestQIdx] > P[bestPIdx]:
            ans = (pow(2, Q[bestQIdx], mod) + pow(2, P[qComp], mod))%mod
        else:
            if Q[pComp] > P[qComp]:
                ans = (pow(2, P[bestPIdx], mod) + pow(2, Q[pComp], mod))%mod
            else:
                ans = (pow(2, Q[bestQIdx], mod) + pow(2, P[qComp], mod))%mod

        R.append(ans)
    return R
    

for _ in range(int(input())):
    print(" ".join([str(x) for x in solve()]))