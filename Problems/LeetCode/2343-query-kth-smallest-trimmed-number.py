from heapq import nsmallest

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for k, trim in queries:
            # Create a list of (trimmed number, original index) tuples
            trimmed_nums = [(v[-trim:], i) for i, v in enumerate(nums)]
            
            # Use heapq.nsmallest to find the k smallest trimmed numbers based on the trimmed part
            smallest_k = nsmallest(k, trimmed_nums, key=lambda x: (x[0], x[1]))
            
            # Get the index of the k-th smallest trimmed number
            ans.append(smallest_k[-1][1])
        
        return ans