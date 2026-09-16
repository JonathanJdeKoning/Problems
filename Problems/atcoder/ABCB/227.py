N = int(input())

ans = 0

A = list(map(int, input().split()))

for num in A:
    good = False
    for a in range(1, 334):
        for b in range(1, 334):
            if 4*a*b + 3*a + 3*b == num:
                good = True

    if not good: ans += 1
print(ans)
