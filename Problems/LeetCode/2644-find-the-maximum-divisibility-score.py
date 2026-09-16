class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = []
        mx = -1
        for div in divisors:
            score = len([x for x in nums if x%div==0])
            if score > mx:
                mx = score
                ans = [div]
            elif score == mx:
                ans.append(div)
        return min(ans)