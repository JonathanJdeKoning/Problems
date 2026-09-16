N = int(input())
A = list(map(int, input().split()))

curr = 0
while True:
    if curr != len(A) - 1 and A[curr+1] > A[curr]:
        curr += 1
    else: break

print(A[curr])