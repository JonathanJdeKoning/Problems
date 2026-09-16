N = int(input())

for c in range(100):
    for d in range(100):
        if 4*c + 7*d == N:
            exit(print("Yes"))
print("No")
