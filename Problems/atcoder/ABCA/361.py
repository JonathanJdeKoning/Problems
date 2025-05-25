n, k, x = map(int, input().split())
a = list(map(int, input().split()))

a.insert(k,x)
print(" ".join(map(str, a)))
