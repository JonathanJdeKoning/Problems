class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        fq = Counter(nums)
        pairs = 0
        for start, count in fq.items():
            if not target.startswith(start):
                continue
            
            end = target[len(start):]
            if end not in fq:
                continue
            
            pairs += count*fq[end]

            if start == end:
                pairs -= count
        return pairs










        