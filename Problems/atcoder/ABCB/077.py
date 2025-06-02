N =int(input())


for i in range(1000000):
    if i*i > N:
        print((i-1) * (i-1))
        exit()