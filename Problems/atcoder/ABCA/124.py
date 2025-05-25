a,b = map(int, input().split())
total = 0
for _ in range(2):
    if a > b:
        total += a
        a -= 1
    else:
        total += b
        b -= 1
print(total)

