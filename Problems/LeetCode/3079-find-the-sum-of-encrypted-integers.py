class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            mx = max([int(x) for x in str(num)])
            new = [str(mx) for x in range(len(str(num)))]
            total += int("".join(new))
        return total