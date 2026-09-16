class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        leftZeros = 0
        rightOnes = nums.count(1)

        mp = defaultdict(list)
        initScore = leftZeros + rightOnes
        mp[initScore].append(0)
        for i in range(1, len(nums)+1):
            if nums[i-1] == 0:
                leftZeros += 1
            else:
                rightOnes -= 1

            score = leftZeros + rightOnes
            mp[score].append(i)

        mx = max(list(mp.keys()))

        return mp[mx]
            
