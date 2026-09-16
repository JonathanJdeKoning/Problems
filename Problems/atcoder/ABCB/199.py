N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mx = max(A)
mn = min(B)

if mx > mn:
    exit(print(0))

print(mn - mx + 1)