from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = list(Counter(nums).values())
        return sum([(x+2)//3 for x in count]) if 1 not in count else -1