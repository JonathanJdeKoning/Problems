a,b = list(map(int, input().replace(","," ").split()))

x = a/b


from math import ceil, floor

if abs(floor(x) - x) < abs(ceil(x) - x):
    print(floor(x))
else:
    print(ceil(x))