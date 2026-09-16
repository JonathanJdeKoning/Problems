class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        n = set(nums)
        p = []
        for num in nums:
            if num**2 in n:
                p.append(num**2)

        if not p: return -1
        q = []
        for num in p:
            if num**2 in n:
                q.append(num**2)
        print(q)
        if not q: return 2
        r = []
        for num in q:
            if num**2 in n:
                r.append(num**2)

        if not r: return 3
        s = []
        for num in r:
            if num**2 in n:
                s.append(num**2)

        if not s: return 4
    
        t = []
        for num in s:
            if num**2 in n:
                t.append(num**2)

        if not t: return 5
        u = []
        for num in t:
            if num**2 in n:
                u.append(num**2)

        if not u: return 6

