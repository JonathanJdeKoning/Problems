from math import factorial
N = int(input())

ans = 0

while N:
    for i in range(1, 10000000):
        if factorial(i+1) > N:
            N -= factorial(i)
            ans += 1
            break

print(ans)
            