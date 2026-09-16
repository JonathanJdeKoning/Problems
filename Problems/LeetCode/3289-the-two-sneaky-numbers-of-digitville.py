class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        fq = Counter(nums)
        ans = []
        for k,v in fq.items():
            if v == 2:
                ans.append(k)
        return ans