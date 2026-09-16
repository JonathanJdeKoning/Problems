class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat = 0
        while True:
            if not nums: break
            if len(nums) == 1:
                concat += nums.pop()
                break
            else:
                one = nums[0]
                two = nums[-1]
                nums = nums[1:-1]
                concat += int(str(one)+str(two))
        return concat
