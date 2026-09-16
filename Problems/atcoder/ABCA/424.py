a, b,c = map(int, input().split())

if a+b>c and b+c>a and c+a>b and (a==b or b==c or c==a):
    print("Yes")
else:
    print("No")
