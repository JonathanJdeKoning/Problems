n = int(input())
nums = list(map(int, input().split()))

s = sorted(nums)
var = s[-2]

for i, num in enumerate(nums, start=1):
    if num == var:
        print(i); break
