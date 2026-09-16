class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        total = 0
        d = {}
        for i, (player, color) in enumerate(pick):
            if player not in d:
                d[player] = [0]*101
            d[player][color] += 1

        for player, picks in d.items():
            if max(picks) >player:
                total += 1
        return total
