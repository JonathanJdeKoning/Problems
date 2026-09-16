class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dom, x = Counter(nums).most_common()[0]
        domCount = 0
        for i in range(len(nums)):
            if nums[i] == dom: domCount += 1
            if domCount > (i+1)/2 and x - domCount > (len(nums) - i - 1) / 2:
                return i
        return -1