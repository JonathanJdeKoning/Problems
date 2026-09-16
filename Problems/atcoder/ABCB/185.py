N, M, T = list(map(int, input().split()))
currCharge = N
currTime = 0
for i in range(M):
    A, B = list(map(int, input().split()))

    currCharge = max(0, currCharge - (A - currTime))
    if currCharge == 0:
        exit(print("No"))
    currCharge = min(currCharge + (B - A), N)

    currTime = B

chargeAtHome = max(0, currCharge - (T - currTime))
if chargeAtHome == 0:
    exit(print("No"))
print("Yes")