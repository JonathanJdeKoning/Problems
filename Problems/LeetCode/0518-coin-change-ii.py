class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        coins.sort()
        ans = 0
        @cache
        def ways_to_make(i, tot):
            if i >= len(coins): return 0
            if tot < 0: return 0
            if tot == 0: return 1

            take = ways_to_make(i, tot - coins[i])
            skip = ways_to_make(i+1, tot)
            return take + skip

   

        return ways_to_make(0, amount)