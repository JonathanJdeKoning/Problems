N, W = list(map(int, input().split()))

A = list(map(int, input().split()))

while A and A[-1] > W: A.pop()

seen = set()

for num in A:
    seen.add(num)
if len(A) > 1:
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j]  <= W:
                seen.add(A[i] + A[j])
            if len(A) >= 2:
                for k in range(len(A)):
                    if k == i or k == j: continue
                    if A[i] + A[j] + A[k] <= W:
                        seen.add(A[i] + A[j] + A[k])
print(len(seen))
