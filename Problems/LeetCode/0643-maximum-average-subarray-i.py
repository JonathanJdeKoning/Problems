class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:     
        left = 0
        right = k-1

        windowSum = sum(nums[left:right+1])
        maxAvg = windowSum / k

        while right < len(nums)-1:
            windowSum -= nums[left]
            left += 1

            right += 1
            windowSum += nums[right]

            maxAvg = max(maxAvg, windowSum / k)
            
        return maxAvg

