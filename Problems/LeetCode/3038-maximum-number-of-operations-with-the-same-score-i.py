class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        count = 0
        initial = nums[0]+ nums[1]
        while True:
            if len(nums) > 1:
                testo = nums[0] + nums[1]
                if testo == initial:
                    count += 1
                    nums = nums[2:]
                else:
                    break
            else:
                break
        return count
            
        