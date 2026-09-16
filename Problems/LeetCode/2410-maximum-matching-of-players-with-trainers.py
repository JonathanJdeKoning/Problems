class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p = 0
        t = 0
        ans = 0
        while p < len(players) and t < len(trainers):
            if trainers[t] >= players[p]:
                ans += 1
                p += 1
            t += 1

        return ans