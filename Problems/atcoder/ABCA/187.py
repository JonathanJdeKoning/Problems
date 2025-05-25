a,b = input().split()

x = sum([int(z) for z in a])
y = sum([int(z) for z in b])

print(max(x,y))
