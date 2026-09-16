class Solution:
    def minElement(self, nums: List[int]) -> int:
        def f(n):
            return sum(int(c) for c in str(n))

        return f(min(nums, key = f))