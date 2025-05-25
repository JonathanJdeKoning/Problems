x, a, b = map(int, input().split())

if abs(x-a) > abs(b-x):
    print("B")
else:
    print("A")
