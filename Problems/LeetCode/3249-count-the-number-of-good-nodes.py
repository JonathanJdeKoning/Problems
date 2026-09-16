class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for start,end in edges:
            d[start].append(end)
            d[end].append(start)
        out = 0
        old = set()
        @cache
        def getSize(root):
            nonlocal out

            subsizes = []
            ans = 1
            if len(d[root]) == 1 and root != 0:
                out += 1
                return ans
            for edge in d[root]:
                if edge not in old:
                    old.add(root)
                    subsizes.append(getSize(edge))

            ans += sum(subsizes)
            if len(Counter(subsizes)) == 1:
                out = out+1

            return ans

        getSize(0)

        return out