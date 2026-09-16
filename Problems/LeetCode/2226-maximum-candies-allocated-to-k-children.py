class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canGetKCandies(amount):
            if amount == 0: return True
            kidsLeft = k
            curr = 0
            while curr != len(candies):
                currCand = candies[curr]
                canFeed = currCand // amount
                kidsLeft -= canFeed
                if kidsLeft <= 0: return True
                curr += 1
            return False

        return bisect_right(range(max(candies)+1), 0, key=lambda x: not canGetKCandies(x)) - 1
