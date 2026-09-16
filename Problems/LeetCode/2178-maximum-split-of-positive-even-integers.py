class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2 == 1: return []
        ans = []
        i = 2
        total = 0
        while total+i <= finalSum:
            ans.append(i)
            total += i
            i += 2
        ans[-1] += finalSum-total
        return ans
