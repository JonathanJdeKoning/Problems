W, H, N = list(map(int, input().replace(","," ").split()))
area = W*H
L = 0
U = H
R = W
D = 0
for _ in range(N):
    x, y, op = list(map(int, input().replace(","," ").split()))

    if op == 1:
        L = max(L, x)
    elif op == 2:
        R = min(R, x)
    elif op == 3:
        D = max(D, y)
    else:
        U = min(U, y)

if (L >= R or D >= U) :
    print(0)
else:
    print(abs(L - R) * abs(D - U))



    
    
    