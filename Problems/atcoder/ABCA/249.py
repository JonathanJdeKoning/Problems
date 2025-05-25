a,b,c,d,e,f,x = map(int, input().split())
tToRest = a
restLeft = c
tMeters = 0
aMeters = 0
for i in range(x):
    if tToRest ==0:
        restLeft -= 1
        if restLeft == 0:
            restLeft = c
            tToRest = a
    else:
        tToRest -= 1
        tMeters += b


aToRest = d
restLeft = f
for i in range(x):
    if aToRest ==0:
        restLeft -= 1
        if restLeft == 0:
            restLeft = f
            aToRest = d
    else:
        aToRest -= 1
        aMeters += e

if tMeters > aMeters:
    print("Takahashi")
elif aMeters > tMeters:
    print("Aoki")
else:print("Draw")
