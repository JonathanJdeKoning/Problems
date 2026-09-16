N = int(input())
poss = set()
for base in range(1, 1001):
    for power in range(2,11):
        if base**power <= 1000:
            poss.add(base**power)
        else:
            break
ans = 1
for i in range(1, N+1):
    if i in poss:
        ans = i

print(ans)