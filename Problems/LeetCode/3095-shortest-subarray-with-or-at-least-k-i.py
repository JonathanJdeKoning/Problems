class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def sublists(lst):
            n = len(lst)
            sublists = []

            for start in range(n):
                for end in range(start + 1, n + 1):
                    sublists.append(lst[start:end])

            return sublists
        
        mn = 999999999
        for lst in sublists(nums):
            if reduce(lambda a,b:a|b,lst) >= k:
                mn = min(mn, len(lst))
        if mn == 999999999:
            return -1
        return mn