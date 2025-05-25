a, b = map(int, input().split())

solids = a+b
fat = b
if solids >= 15 and fat >= 8:
    print(1)
elif solids >= 10 and fat >= 3: 
    print(2)
elif solids >= 3:
    print(3)
else:
    print(4)
