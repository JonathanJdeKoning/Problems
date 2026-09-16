class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0)>=2: return True
        arr = set(arr)
        for num in arr:
            if num*2 in arr and num != 0: return True
        return False