a,b = map(int, input().split())


if a==b:
    print("Draw");exit()

if a ==1:
    print("Alice");exit()
elif b ==1:
    print("Bob"); exit()

if a >b:
    print("Alice")
else:
    print("Bob")
