class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)
        ans = [-1]*len(nums)
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        
        largerPos = pos[max(nums)]
        for num in sorted(pos.keys(), reverse=True)[1:]:
            for idx in pos[num]:
                nextBest = bisect_left(largerPos,idx)
                if nextBest == len(largerPos):
                    nextBest = 0
                ans[idx] = nums[largerPos[nextBest]]
            largerPos.extend(pos[num])
            largerPos.sort()
        return ans
                