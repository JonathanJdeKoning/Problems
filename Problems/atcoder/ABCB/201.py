N = int(input())

mp = {}
for _ in range(N):
    name, height = input().split()
    height = int(height)
    mp[name] = height


good = (sorted(mp.values())[-2])

for k in mp:
    if mp[k] == good:
        print(k)