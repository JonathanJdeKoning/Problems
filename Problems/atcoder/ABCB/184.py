N, X = list(map(int, input().split()))

for c in input():
    if c == 'o': X += 1
    else: X = max(0, X-1)
print(X)