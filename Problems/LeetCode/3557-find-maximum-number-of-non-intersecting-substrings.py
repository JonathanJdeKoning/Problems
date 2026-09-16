class Solution:
    def maxSubstrings(self, s: str) -> int:
        ans = 0
        
        loc = defaultdict(list)
        for i,c in enumerate(s):
            loc[c].append(i)

        ans = 0
        left_bound = -1
        for j, c in enumerate(s):
            v = loc[c]
            start = bisect_left(v, j)

            for x in range(start-1, -1, -1):
                i = v[x]
                if i <= left_bound: break
                if j-i >= 3:
                    ans += 1
                    left_bound = j
                    break
        return ans
                
            
