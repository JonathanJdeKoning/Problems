N = int(input())
A = []
mp = {}
for i in range(N):
    name, score = input().split()
    score = int(score)
    mp[(name, score)] = i+1
    A.append((name, score))
A.sort(key = lambda x: (x[0], -x[1]))
for a in A:
    print(mp[a])
