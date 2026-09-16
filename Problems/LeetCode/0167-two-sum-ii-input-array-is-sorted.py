class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l= 0
        r = len(numbers)-1
        t = numbers[l] + numbers[r]

        while t != target:
            if t > target:
                t -= numbers[r]
                r -= 1
                t += numbers[r]
            elif t < target:
                t -= numbers[l]
                l += 1
                t += numbers[l]
        return [l+1, r+1]
            
                    