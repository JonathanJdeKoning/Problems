class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        A = []
        B = []
        A.append(nums[0])
        B.append(nums[1])

        for num in nums[2:]:
            if A[-1] > B[-1]:
                A.append(num)
            else:
                B.append(num)
        return A + B