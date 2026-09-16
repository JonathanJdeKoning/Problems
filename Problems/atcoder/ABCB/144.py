N = int(input())
good = set([i*j for i in range(1, 10) for j in range(1, 10)])
if N in good:
    print("Yes")
else:
    print("No")