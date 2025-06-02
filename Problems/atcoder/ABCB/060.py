A, B, C = map(int, input().split())

seen = set()
mul = 1
while True:
    rem = (A*mul)%B
    if rem == C:
        exit(print("YES"))
    else:
        if rem in seen:
            exit(print("NO"))
        else:
            seen.add(rem)
            mul += 1