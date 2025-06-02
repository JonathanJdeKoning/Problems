k,s = map(int, input().split())
total = 0
for i in range(min(k+1,s+1)):
    left = s-i
    
    if k*2 < left:
        continue

    if k > left:
        total += left+1
        continue

    poss = left+1
    total += poss - (left-k)*2


print(total)

