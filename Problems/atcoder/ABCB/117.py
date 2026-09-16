N = int(input())
Sides = list(map(int, input().split()))
Sides.sort()

if Sides.pop() < sum(Sides):
    print("Yes")
else:
    print("No")