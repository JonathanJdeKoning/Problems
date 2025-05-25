x,a,b = map(int, input().split())

after = b-a


if after <= 0:
    print("delicious")
else:
    if after <= x:
        print("safe")
    else:
        print("dangerous")
