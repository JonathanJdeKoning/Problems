class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        curr = inf
        ans = 0
        for num in maximumHeight:
            if num < curr:
                curr = num
            else:
                curr -= 1
            if curr <=0: return -1
            ans += curr
        return ans