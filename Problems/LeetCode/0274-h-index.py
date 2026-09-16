class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans = 0
        mn = float('inf')
        papers = 0
        while citations:
            curr = citations.pop()
            mn = min(mn, curr)
            papers += 1
            ans = max(ans, min(papers, mn))
        return ans


