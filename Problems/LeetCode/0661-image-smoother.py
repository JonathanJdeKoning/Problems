class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        mat = []
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),(0,0)]
        for _ in range(rows):
            mat.append([None]*cols)

        for i in range(rows):
            for j in range(cols):
                pos = img[i][j]
                numcells = 9
                total = 0
                for dy,dx in directions:
                    y = i+dy
                    x = j+dx
                    if x == -1 or y ==-1 or x == cols or y == rows:
                        numcells-=1
                        continue
                    total += img[y][x]
                mat[i][j] = floor(total/numcells)
        return mat