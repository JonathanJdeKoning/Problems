a, b = map(int, input().split())
dist = abs(a-b)

if dist ==1 or dist%2==1:print("IMPOSSIBLE")
else:
    print((a+b)//2)
