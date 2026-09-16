class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        fq = Counter(nums)

        for num in nums:
            comp = k - num
            if num == comp:
                if fq[num] >= 2:
                    ans += 1
                    fq[num] -= 2
            elif fq[num] >= 1 and fq[comp] >= 1:
                fq[num] -= 1
                fq[comp] -= 1
                ans += 1
        return ans