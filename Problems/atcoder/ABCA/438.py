D, F = map(int, input().split())
T = F
while T <= D:
    T += 7

ans = T%D
if ans == 0: ans = 7
print(ans)
