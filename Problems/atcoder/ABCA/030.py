a,b,c,d = map(int, input().split())


x = a/b
y = c/d


if x < y:
    print("TAKAHASHI")
elif y < x:
    print("AOKI")
else:
    print("DRAW")
