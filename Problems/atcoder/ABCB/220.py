K = int(input())
A, B = list(map(list, input().split()))

a = 0
b = 0

i = 0
while A:
    a += K**i * int(A.pop())
    i += 1
i = 0
while B:
    b += K**i * int(B.pop())
    i += 1
print(a*b)
