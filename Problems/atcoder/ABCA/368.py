N, K = list(map(int, input().replace(","," ").split()))

A = list(map(int, input().replace(","," ").split()))

print(" ".join(map(str, A[-K:] + A[:-K])))