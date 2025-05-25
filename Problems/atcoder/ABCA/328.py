n, x = map(int, input().split())
arr = list(map(int, input().split()))

print(sum([f for f in arr if f <= x]))
