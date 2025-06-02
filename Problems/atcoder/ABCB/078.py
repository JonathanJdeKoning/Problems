X, Y, Z = map(int, input().split())


check = 1
while True:
    if check*Y + Z*(check+1) > X:
        exit(print(check-1))
    else:
        check += 1

