N, X = map(int, input().split())
A = list(map(int, input().split()))

for num in A:
    if num < X:
        X = num
        print(1)
    else:
        print(0)

        

