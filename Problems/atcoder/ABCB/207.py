A, B, C, D = list(map(int, input().split()))

cyan = A + B
red = C

steps = 1
while True:
    if steps > 1000000: exit(print(-1))
    if cyan/red <= D:
        exit(print(steps))


    steps += 1
    cyan += B
    red += C