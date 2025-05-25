a,b,c = list(map(int, input().replace(","," ").split()))
nums = sorted([a,b,c])
if len(set(nums)) == 1 or nums[0] + nums[1] == nums[2]:
    print("Yes")
else:
    print("No")
