class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res = [False]*len(candies)
        for i, kid in enumerate(candies):
            if kid+extraCandies >= mx:
                res[i]=True
        return res