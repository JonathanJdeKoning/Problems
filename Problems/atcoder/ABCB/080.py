N = int(input())

if N % sum([int(x) for x in str(N)])==0:
    print("Yes")
else:
    print("No")