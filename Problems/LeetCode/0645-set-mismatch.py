class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        fq = Counter(nums)
        ans = [None, None]
        for i in range(1,N + 1):
            if i not in fq:
                ans[1] = i
            if fq[i] == 2:
                ans[0] = i
        return ans