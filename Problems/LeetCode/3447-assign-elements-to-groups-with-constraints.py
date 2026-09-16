class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        N = len(groups)
        idxLeft = set(list(range(N)))
        
        factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
        ans = [-1]*N

        uniqElems = set(elements)
        uniqGroups = set(groups)
        idxmap = {}
        for i, elem in enumerate(elements):
            if elem in idxmap: continue
            idxmap[elem] = i
            
        mp = defaultdict(list)
        for i, num in enumerate(groups):
            mp[num].append(i)

        for k, v in mp.items():
            f = factors(k)
            goodf = f.intersection(uniqElems)
            if not goodf: continue

            best = min([idxmap[x] for x in goodf])

            for loc in mp[k]:
                ans[loc] = best
            
            



        return ans
        