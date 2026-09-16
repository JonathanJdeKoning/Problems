class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        ans = []
        seen = deque([])
        k = 0
        for num in nums:
            if num > 0:
                k = 0
                seen.appendleft(num)
            elif num == -1:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k-1])
                else:
                    ans.append(-1)
        return ans
