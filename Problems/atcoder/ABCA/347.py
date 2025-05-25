n, k = map(int, input().split())

nums = list(map(int, input().split()))

out = sorted([num//k for num in nums if num%k==0])
print(" ".join(map(str, out)))

