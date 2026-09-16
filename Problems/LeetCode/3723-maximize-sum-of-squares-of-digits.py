class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num*9 < sum: return ""
        ans = []
        while sum >= 9:
            sum -= 9
            ans.append(9)
            
        if sum:
            ans.append(sum)
        while len(ans) != num:
            ans.append(0)
        
        zeros = ans.count(0)
        reg = [x for x in ans if x != 0]

        return "".join(map(str, sorted(reg, reverse=True))) + "0"*zeros