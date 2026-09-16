N = int(input())

s = set(list(map(int, input().split())))
for _ in range(N-2):
    x, y= list(map(int, input().split()))
    s = s.intersection({x, y})

if s:
    print("Yes")
else:
    print("No")
