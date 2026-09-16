A = list(map(int, input().split()))
A.sort()
K = int(input())

for _ in range(K):
    A[-1] *= 2
print(sum(A))