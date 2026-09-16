ans = 0

S = input()
for a, b in zip(S, S[::-1]):
    if a != b:
        ans += 1
print(ans//2)