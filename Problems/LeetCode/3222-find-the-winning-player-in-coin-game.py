class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        player = 0

        while True:
            if x==0 or y <4: break
            x -= 1
            y -= 4
            player = abs(player-1)

        if player == 0:
            return("Bob")
        return "Alice"
        
