N = int(input())
A = list(map(int, input().split()))


ans = 0
for i in range(len(A)-2):
    a = A[i]
    for j in range(i+1, len(A)-1):
        b = A[j]
        if b == a: continue
        for k in range(j+1, len(A)):
            c = A[k]
            if c == a or c == b: continue

            if c+a > b and a+b > c and c+b > a:
                ans += 1
print(ans)
