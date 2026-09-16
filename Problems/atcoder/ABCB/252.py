N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B  =list(map(int, input().split()))
B = set([x-1 for x in B])


mx = max(A)

for i in range(len(A)):
    if A[i] == mx and i in B:
        exit(print("Yes"))
print("No")