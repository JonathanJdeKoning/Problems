X, Y = map(int, input().split())

new = (X + Y) % 12
if new == 0: new = 12

print(new)

