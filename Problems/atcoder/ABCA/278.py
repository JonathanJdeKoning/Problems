n, k = map(int, input().split())
a = list(map(int, input().split()))
a = a[k:] + [0]*min(k, len(a))
print(" ".join(map(str, a)))

