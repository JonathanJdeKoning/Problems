class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        S = "123456789"
        nums = []
        for l in range(1, 10):
            for i in range(9-(l-1)):
                nums.append(int(S[i:i+l]))

        nums.sort()
        ans = []
        for num in nums:
            if num >= low and num <= high:
                ans.append(num)
        return ans
