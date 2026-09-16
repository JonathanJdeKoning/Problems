class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()


        while nums:
            new = [nums.pop(), nums.pop(), nums.pop()]
            if new[0] - new[-1] > k: return []
            ans.append(new)
        return ans