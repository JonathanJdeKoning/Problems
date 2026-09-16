from functools import cache
from math import sqrt, ceil

N = 10_000_000
good = set()
print("filling good...")
for i in range(ceil(sqrt(N))):
    j = i
    while True:
        num = i**2 + j**2 + i*j
        if num > N:
            break
        good.add(num)
        j += 1

isGood = [1 if i in good else 0 for i in range(N)]

reqLen = 35
def checkRange(reqLen, k):
    for i in range(N):

        for j in range(reqLen):
            idx = i+k*j
            if idx >= len(isGood): break
            if not isGood[i+k*j]: break
        else:
            print(f"FOUND!: Start: {i}, Step: {k}")


for stepSize in range(9990, N, 10):
    if stepSize%10 == 0:
        print(f"Checking stepsize >={stepSize}")
    checkRange(26, stepSize)