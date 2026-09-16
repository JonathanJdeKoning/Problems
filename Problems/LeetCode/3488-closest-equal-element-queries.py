class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        N = len(nums)
        dists = defaultdict(list)
        for i, num in enumerate(nums):
            dists[num].append(i)

        
        for q in queries:
            val = nums[q]
            valIndices = dists[val]
            if len(valIndices) <= 1:
                ans.append(-1)
                continue
                
            valIDX = bisect_left(valIndices, q)
            left = None
            right = None
            if valIDX == 0:
                left = valIndices[-1]
                right = valIndices[1]
            elif valIDX == len(valIndices) - 1:
                left = valIndices[valIDX -1]
                right = valIndices[0]
            else:
                left = valIndices[valIDX - 1]
                right = valIndices[valIDX + 1]

            
            mnLeftDist = min(abs(left-q), min(left, q) + (N - max(left, q)))
            mnRightDist = min(abs(right-q), min(right, q) + (N - max(right, q)))
            res = min(mnLeftDist, mnRightDist)
            ans.append(res)
            
        return ans
        