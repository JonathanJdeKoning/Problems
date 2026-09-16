ans = 0
for i in range(1, int(input()) + 1):
    if i %3 == 0 or i%5 ==0: continue
    ans += i
print(ans)