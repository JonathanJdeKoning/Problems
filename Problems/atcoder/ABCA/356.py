n, l, r = map(int, input().split())
nums = list(range(1,n+1))
l -=1
r -= 1
print(" ".join(map(str, nums[:l] + nums[l:r+1][::-1] + nums[r+1:])))
