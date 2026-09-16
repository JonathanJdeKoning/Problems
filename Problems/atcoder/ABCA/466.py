N = int(input())
A = list(map(int, input().split()))

if all(map(lambda x:x<0, A)):
    print("Yes")
else:
    print("No")
    
