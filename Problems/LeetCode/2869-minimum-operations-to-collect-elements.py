class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        count = 0
        while True:
            count += 1
            n = nums.pop()
            if n > k: continue
            seen.add(n)
            if sorted(list(seen)) == list(range(1,k+1)): return count

