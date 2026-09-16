class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            score = 0
            for j in range(i+1, len(nums)):
                if nums[i]%2 != nums[j]%2:
                    score += 1
            ans.append(score)
        return ans