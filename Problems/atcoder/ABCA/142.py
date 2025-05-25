n = int(input())
poss = []
for i in range(1, n+1):
    poss.append(i)

print(len([x for x in poss if x%2==1])/len(poss))
