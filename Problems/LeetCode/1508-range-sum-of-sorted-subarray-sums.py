class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        mod = 1e9+7
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                arr.append(sum(nums[i:j]))

        arr.sort()
        print(arr)
        return int(sum(arr[left-1:right])%mod)