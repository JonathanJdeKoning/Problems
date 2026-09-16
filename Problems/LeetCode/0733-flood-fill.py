class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
                    
        def coordCheck(y, x):
            nonlocal R
            nonlocal C
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            validCoords = []
            for dy, dx in directions:
                ny = y + dy
                nx = x + dx
                if ny in range(R) and nx in range(C) and (ny,nx) not in seen:
                    validCoords.append((ny, nx))
                    
            return validCoords
        
        stack = [(sr, sc)]
        currColor = image[sr][sc]
        image[sr][sc] = color
        seen = set()
        while stack:
            currY, currX = stack.pop()
            validCoords = coordCheck(currY, currX)
            seen.add((currY, currX))
            
            for y, x in validCoords:
                if image[y][x] == currColor and (y,x) not in seen: 
                    image[y][x] = color
                    stack.append((y, x))
                
        return image
            
            
