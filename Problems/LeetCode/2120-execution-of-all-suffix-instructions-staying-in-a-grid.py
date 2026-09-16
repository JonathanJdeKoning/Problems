class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        dirs = {"L": (0, -1), "U":(-1,0),"R":(0,1),"D":(1,0)}
        for i in range(len(s)):
            good = 0 
            y, x = startPos
            for c in s[i:]:
                dy, dx = dirs[c]
                y += dy
                x += dx
                if y not in range(n) or x not in range(n):
                    break
                good += 1

            ans.append(good)
        return ans
