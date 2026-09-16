class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        ans = 0
        weight.sort(reverse=True)
        n = 5000
        while  weight and n >= weight[-1]:
            ans += 1
            n -= weight.pop()
        return ans