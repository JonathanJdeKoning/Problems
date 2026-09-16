class Robot:

    def __init__(self, width: int, height: int):
        self.begun = False
        self.W = width
        self.H = height
        W = self.W
        H = self.H
        self.totalCells = 2*(width+height)-4
        self.cell = 0
        self.mp = {}

        for i in range(W):
            self.mp[i] = (i, 0, 0)
        for i in range(W, W+H-1):
            self.mp[i] = (W-1, i-W+1, 1)
        for i in range(W+H-1, W+H-1+W):
            self.mp[i] = ((W+H+W-3)-i, H-1, 2)
        for i in range(1, H-1):
            self.mp[self.totalCells-i] = (0,i, 3)

        self.mp[0] = (0,0,3)
        #print(self.mp)


    def step(self, num: int) -> None:
        self.cell = (self.cell+num) % self.totalCells
        self.begun = True

    def getPos(self) -> List[int]:
        x, y, d = self.mp[self.cell]
        return [x,y]

    def getDir(self) -> str:
        if not self.begun: return "East"
        x,y,d = self.mp[self.cell]
        return {0:"East", 1:"North", 2:"West", 3:"South"}[d]

        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()