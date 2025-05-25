nums = sorted(map(int, input().split()))
if nums[1]-nums[0] == nums[2]-nums[1]:
    print("Yes")
else:
    print("No")
