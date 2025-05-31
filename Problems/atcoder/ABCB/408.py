input()
A = list(map(int, input().split()))
B = [str(x) for x in sorted(set(A))]
print(len(B))
print(" ".join(B))