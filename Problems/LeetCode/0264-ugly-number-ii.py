nums = []
for i in range(100):
    for j in range(100):
        for k in range(100):
            nums.append(2**i * 3**j * 5**k)
nums.sort()
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        return nums[n-1]