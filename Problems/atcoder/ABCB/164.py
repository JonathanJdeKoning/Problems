A, B, C, D = list(map(int, input().split()))

while True:
    C -= B
    if C <= 0:
        print("Yes")
        exit()
    A -= D
    if A <= 0:
        print("No")
        exit()