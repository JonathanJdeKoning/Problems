s,t = input().split()
poss = []

for i in range(len(s)-1):
    for j in range(1,i+2):
        poss.append(s[j-1:len(s)+1:i+1])
if t in poss:
    print("Yes")
else:
    print("No")

#jonathanjdekoning
