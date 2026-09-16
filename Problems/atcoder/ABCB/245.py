N = int(input())
A = list(map(int, input().split()))

A = set(A)

for i in range(5000):
    if i not in A:
        print(i)
        exit()