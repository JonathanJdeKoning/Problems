A, B, C = list(map(int, input().replace(","," ").split()))

while B != C:
    if B == A:
        print("No")
        exit()
    B = (B+1) % 24
print("Yes")