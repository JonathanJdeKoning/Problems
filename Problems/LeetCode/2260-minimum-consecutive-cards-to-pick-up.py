class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mp = {}
        mn = 99999999
        for i,c in enumerate(cards):
            if c in mp:
                mn = min(mn, 1+(i - mp[c]))
            mp[c] = i
        if mn == 99999999: return -1
        return mn