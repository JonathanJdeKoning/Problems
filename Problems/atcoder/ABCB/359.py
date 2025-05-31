n = int(input())
nums = list(map(int, input().split()))
tot = 0
for i,c in enumerate(nums[:-2]):
    if nums[i+2] == c:
        tot += 1
print(tot)

