X,Y,Z = list(map(int, input().replace(","," ").split()))

print((X*Y*Z)%(int(1e9)+7))