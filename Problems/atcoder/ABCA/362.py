c = list(map(int, input().split()))

s = input()
if s=="Blue":
    print(min(c[:2]))
elif s == "Red":
    print(min(c[1:]))
else:
    print(min(c[0],c[1]))
