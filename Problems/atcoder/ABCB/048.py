a, b, x = list(map(int, input().replace(","," ").split()))

print(b // x - (a-1) // x)