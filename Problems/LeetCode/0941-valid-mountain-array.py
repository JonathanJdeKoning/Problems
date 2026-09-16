class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        
        curr = arr[0]
        up = True
        for i, num in enumerate(arr[1:]):
            if up:
                if num > curr:
                    curr = num
                    continue
                if num == curr:
                    return False
                if num < curr:
                    up = False
                    curr = num
                    if i == 0: return False
                    continue
            if not up:
                if num < curr:
                    curr = num
                    continue
                if num == curr:
                    return False
                if num > curr:
                    return False
        if not up:
            return True
        else: return False
            