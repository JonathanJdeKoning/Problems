N = int(input())
A = list(map(int, input().split()))

tot = 0

for tree in A:
    if tree <= 10: continue
    tot += tree - 10
print(tot)