class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        nums = [x%2 for x in nums]
        numOdd = nums.count(1)
        numEve = nums.count(0)
        swaps = 0
        if abs(numOdd - numEve) > 1: return -1
        edge = 1
        if numEve > numOdd: edge = 0
        ans = inf
        need1 = list(range(0, len(nums), 2))
        need2 = list(range(1, len(nums), 2))
        pos = []
        for i in range(len(nums)):
            if nums[i] == edge:
                pos.append(i)


        ans = sum([abs(b-a) for a, b in zip(pos, need1)])   

        if numEve == numOdd:      
            ans = min(ans, sum([abs(b-a) for a, b in zip(pos, need2)]))
                    
        return ans

            
