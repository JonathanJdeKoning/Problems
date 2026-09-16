N ,M, X = list(map(int, input().split()))
tolls = set(list(map(int, input().split())))
NCost = 0
OCost = 0
for i in range(X, N+1):
    if i in tolls:
        NCost += 1

for i in range(X, -1, -1):
    if i in tolls:
        OCost += 1
print(min(NCost, OCost))
