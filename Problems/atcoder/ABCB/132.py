N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(1, len(A)-1):
    if (A[i-1] < A[i] and A[i] < A[i+1]) or (A[i-1] > A[i] and A[i] > A[i+1]): ans += 1
print(ans)