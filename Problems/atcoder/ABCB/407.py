outcomes = []

for a in range(1,7):
    for b in range(1,7):
        outcomes.append((a,b))

X, Y = list(map(int, input().replace(","," ").split()))


N = len(outcomes)
hits = 0
for a,b in outcomes:
    if a+b >= X or abs(a-b) >=Y:
        hits += 1
print(hits/len(outcomes))