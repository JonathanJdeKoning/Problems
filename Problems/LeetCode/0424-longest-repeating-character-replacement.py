class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        def canMakeLength(length):
            if length > len(s): return False
            if length == 1: return True
            
            l = 0
            r = length - 1
            fq = Counter(s[l:r+1])

            while r <= len(s)-2:
                if length - fq.most_common(1)[0][1] <= k:
                    return True
                
                fq[s[l]] -= 1
                l += 1
                r += 1
                fq[s[r]] += 1
            return length - fq.most_common(1)[0][1] <= k

        low = 1 #good
        high = len(s) + 1 #bad

        while high > low + 1:
            mid = (low + high)//2

            if canMakeLength(mid):
                low = mid
            else:
                high = mid
        return low