class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        low = 1
        high = len(s)

        def can_make(req):
            new =copy.copy(s)
            ops = numOps
            needed = 0
            if mid  == 1:
                for i, c in enumerate(new):
                    if c == str(i%2):
                        needed += 1
                needed = min(needed, len(s) - needed)
                if needed <= ops: return True
                return False
            for k,v in groupby(new):
                n = len(list(v))
                if n <= req: continue
                needed = 0
                count = 0
                while True:
                    count += req
                    if count >= n: break
                    needed += 1
                    count += 1
                    if count >= n: break
                if needed > ops: return False
                ops -= needed
                    
                
            return True

            

        while low < high:
            mid = (low+high)//2

            if can_make(mid):
                high = mid
            else:
                low = mid+1
        return low
        