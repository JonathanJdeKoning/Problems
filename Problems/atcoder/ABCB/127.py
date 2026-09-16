r, d, k2 = list(map(int, input().split()))

for i in range(10):
    k2 = r*k2 - d

    print(k2)    