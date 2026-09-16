A, B = input().split() 

X = int(A + B)

if (X**0.5).is_integer() :
    print("Yes")
else:
    print("No")