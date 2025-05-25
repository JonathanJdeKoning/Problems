n,k,a = map(int, input().split())
a -= 1
for _ in range(k-1):
    a = (a+1)%n
print(a+1)
