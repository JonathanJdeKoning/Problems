class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for c in moves:
            if c == "U": y -=1
            if c == "D": y += 1
            if c == "L": x -= 1
            if c == "R": x += 1
        return x ==0 and y ==0