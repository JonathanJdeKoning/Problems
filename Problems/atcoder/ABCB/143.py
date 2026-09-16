N = int(input())
A = list(map(int, input().split()))

ans = 0 

for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        ans += A[i] * A[j]
print(ans)