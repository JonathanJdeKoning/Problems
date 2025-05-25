a,b,c=  map(int, input().split())


if c==0:
    while True:
        a -=1
        if a==-1:
            print("Aoki"); exit()
        b -=1
        if b==-1:
            print("Takahashi");exit()
else:
    while True:
        b -=1
        if b==-1:
            print("Takahashi");exit()
        a-=1
        if a == -1:
            print("Aoki");exit()
