class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        start = 0
        end = 3
        for i in range(len(arr)-2):
            if len([x for x in arr[start:end] if x%2 != 0]) == 3:
                return True
            start += 1
            end += 1
        return False 