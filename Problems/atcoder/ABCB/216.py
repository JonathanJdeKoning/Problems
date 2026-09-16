N = int(input())

seen = set()

for _ in range(N):
    s = input()
    if s in seen:
        exit(print("Yes"))
    seen.add(s)
print("No")