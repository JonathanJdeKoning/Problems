class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = defaultdict(int)
        for i,c in enumerate(s):
            pos[c] = i
        suck = set()
        ans = []
        run = 0
        for i, c in enumerate(s):
            run += 1
            suck.add((pos[c], c))

            if (i,c) in suck:
                suck.discard((i,c))

            if not suck:
                ans.append(run)
                run = 0
            

        return ans