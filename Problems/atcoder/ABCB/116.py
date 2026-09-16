steps = 0
seen = set()
N = int(input())
while True:
    steps += 1
    if N in seen:
        exit(print(steps))
    seen.add(N)
    if N%2==0:
        N //= 2
        continue
    else:
        N = 3*N + 1
