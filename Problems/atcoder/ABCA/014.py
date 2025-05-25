c = int(input())
k = int(input())

ans = 0
while c%k != 0:
    ans += 1
    c += 1
print(ans)
