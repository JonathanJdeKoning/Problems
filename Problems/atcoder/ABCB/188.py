N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

if 0 == sum([a*b for a,b in zip(A, B)]):
    print("Yes")
else:
    print("No")