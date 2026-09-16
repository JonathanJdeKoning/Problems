good = set(["ABC", "ARC", "AGC", "AHC"])
for _ in range(3):
    good.discard(input())

print(good.pop())