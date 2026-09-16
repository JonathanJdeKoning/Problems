class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j <= i: continue
                if gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1: 
                    count += 1
                    print(i,j)
        return count 