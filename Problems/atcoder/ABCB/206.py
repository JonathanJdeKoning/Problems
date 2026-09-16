N = int(input())

t = 0
for i in range(1,10000000):
    t += i
    if t >= N:
        exit(print(i))
