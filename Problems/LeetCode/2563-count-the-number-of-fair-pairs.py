class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums = sorted(nums)
        ans = 0
        print(nums)
        for i, num in enumerate(nums[:-1]):
            if num + nums[i + 1] > upper: return ans
            low = i+1
            high = len(nums) - 1

            while low < high:
                mid = (low + high) // 2

                if nums[mid] + num > upper:
                    high = mid
                else:
                    low = mid + 1
            mx = low
            if num + nums[mx] > upper:
                mx -= 1
            

            low = i+1
            high = len(nums) - 1
            while low < high:
                mid = (low + high) // 2
                if nums[mid] + num >= lower:
                    high = mid
                else:
                    low = mid + 1

            mn = low
            
            if num + nums[mn] < lower: continue
            if num + nums[mx] > upper: continue
            ans += (mx - mn) + 1
            print(i, mn, mx)
        return ans

                



