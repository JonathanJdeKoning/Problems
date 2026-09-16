class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        fq = Counter()
        for res in responses:
            for r in set(res):
                fq[r] += 1

        return min(fq.items(), key = lambda x: (-x[1], x[0]))[0]