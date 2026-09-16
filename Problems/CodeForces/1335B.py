from collections import Counter
def solve():
    N, A, B = list(map(int, input().split()))
    letters = set(list(map(chr, range(97, 97+26))))
    ans = []
    for i in range(B):
        ans.append(chr(97+i))
    while len(ans) != A: ans.append(ans[-1])
    
    while len(ans) != N:
        last = Counter(ans[-(A-1):])
        if len(last) == B:
            ans.append(ans[-1])
        else:
            ans.append((letters - set(last.keys())).pop())

    return "".join(ans)

for _ in range(int(input())):
    print(solve())