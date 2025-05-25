v,t,s,d = map(int, input().split())
invis = set()

start = v*t
end = v*s
if start<= d<=end:
    print("No")
else:
    print("Yes")

