import re
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        ax = [m.start() for m in re.finditer(a, s)]
        bx = [m.start() for m in re.finditer(b, s)]
        print(ax)
        print(bx)
        ans = set()
        for i in ax:
            got = False    
            for j in bx:
                if abs(i - j) <= k:
                    ans.add(i)
                    got = True
                    break
                
        return sorted(list(ans))
                
        