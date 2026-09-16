class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        dirs = [(x,y)for y in (-1,0,1) for x in (-1,0,1) if (x,y)!= (0,0)]
        ox, oy = king
        ans = []
        queens = set([tuple(queen) for queen in queens])
        for dx, dy in dirs:
            x, y = ox, oy
            while True:
                y += dy
                x += dx
                if (x,y) in queens:
                    ans.append([x,y])
                    break
                if y not in range(8): break
                if x not in range(8): break
        return ans
