class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        ans = 0
        l, r = 0, k
        tot = sum(calories[l:r])
        while True:
            if tot < lower: ans -= 1
            elif tot > upper: ans += 1

            if r == len(calories): break
            tot -= calories[l]
            l += 1
            tot += calories[r]
            r += 1
            
        return ans
