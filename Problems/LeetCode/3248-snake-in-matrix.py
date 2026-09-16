class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        y, x = 0 ,0
        for c in commands:
            if c =="UP":
                y -= 1
            elif c == "DOWN":
                y += 1
            elif c == "LEFT":
                x -= 1
            elif c =="RIGHT":
                x += 1
        return((y*n)+x)