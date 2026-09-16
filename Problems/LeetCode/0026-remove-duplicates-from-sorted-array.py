class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        swp = 0
        place = 0
        while swp != len(nums):
            if nums[swp] not in seen:
                seen.add(nums[swp])
                nums[place], nums[swp] = nums[swp], nums[place]
                place += 1
            swp += 1
        print(nums)
        return place 

            
