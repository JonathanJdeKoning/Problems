class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal, greater = [], [], []
        for num in nums:
            if num < pivot:  less.append(num)
            if num == pivot: equal.append(num)
            if num > pivot:  greater.append(num)
        return less + equal + greater