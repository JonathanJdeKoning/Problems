class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = Counter(s1)
        l,r = 0,0
        window = {}
        while r < len(s2):
            window[s2[r]] = window.get(s2[r],0) + 1
            while (r - l + 1) > len(s1):
                window[s2[l]] -=1 
                if window[s2[l]] <= 0 :
                    del window[s2[l]]
                l += 1
            if window == s1Map:
                return True
            r +=1
        return False 