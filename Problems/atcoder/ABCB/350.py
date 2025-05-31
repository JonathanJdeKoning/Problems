n,q=input().split()
a=[1]*int(n)
for x in input().split():
    a[int(x)-1]^=1
print(sum(a))
