class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        fq = Counter(nums)
        ans = set()
        for num in nums:
            if num + k in fq:
                if k == 0 and fq[num] < 2:
                    continue
                
                ans.add(tuple(sorted((num, num+k))))

        return len(ans)