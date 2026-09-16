N = int(input())
A = list(map(int, input().split()))

B = list(map(int, input().split()))

C = list(map(int, input().split()))

ans =  0
prev = -9999 
for idx in A:
    if idx == prev + 1:
        ans += C[idx - 2]
    ans += B[idx - 1]
    prev = idx

print(ans)
