h, w, l, c = map(int, input().split())

if h*w*l < c:
    print("TOO TIGHT")
elif h*w*l > c:
    print("SO MUCH SPACE")
else:
    print("COZY")