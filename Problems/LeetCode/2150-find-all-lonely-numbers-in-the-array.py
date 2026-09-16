class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        fq = Counter(nums)
        ans = []
        for k,v in fq.items():
            if v != 1 or k+1 in fq or k-1 in fq: continue
            ans.append(k)
        return ans