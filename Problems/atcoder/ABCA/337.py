n = int(input())
t, a = 0,0

for _ in range(n):
    x,y = map(int, input().split())
    t+=x
    a += y
if t >a:
    print("Takahashi")
elif a >t:
    print("Aoki")
else:
    print("Draw")
