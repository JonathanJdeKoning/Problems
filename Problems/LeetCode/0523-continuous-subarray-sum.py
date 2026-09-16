class Solution(object):
    def checkSubarraySum(self, nums, k):
        d = {0: -1}
        s = 0

        for i in range(len(nums)):
            s += nums[i]
            rem = s % k

            if rem in d:
                if i - d[rem] > 1:
                    return True
            else:
                d[rem] = i

        return False