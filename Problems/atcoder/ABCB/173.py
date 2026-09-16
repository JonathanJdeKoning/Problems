from collections import defaultdict
mp = defaultdict(int)
N = int(input())
for _ in range(N):
    s = input()
    mp[s] += 1


for s in ["AC", "WA", "TLE", "RE"]:
    print(f"{s} x {mp[s]}")