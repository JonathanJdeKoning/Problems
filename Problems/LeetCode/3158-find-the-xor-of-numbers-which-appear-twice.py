class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        arr = list(set([x for x in nums if nums.count(x) == 2]))
        if len(arr) == 0: return 0

        start = arr[0]
        for i in arr[1:]:
            start = start^i
        return start