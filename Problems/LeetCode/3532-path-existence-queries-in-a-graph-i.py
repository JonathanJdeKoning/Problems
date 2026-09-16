class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        id = 0
        componentMap = {0:0}
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] + maxDiff:
                id += 1
            componentMap[i] = id
            
        return [componentMap[a] == componentMap[b] for a,b in queries]