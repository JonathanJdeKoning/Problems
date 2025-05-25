n = int(input())


x,y = divmod(n,1000)

if y == 0:
    print(0)
else:

    print(1000-y)
