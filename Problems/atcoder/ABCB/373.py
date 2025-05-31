s = input()
ans = 0
mp = {c: i+1 for i,c in enumerate(s)}

curr = mp["A"]
for c in "BCDEFGHIJKLMNOPQRSTUVWXYZ":
    loc = mp[c]
    ans += abs(curr-loc)
    curr = loc

print(ans)