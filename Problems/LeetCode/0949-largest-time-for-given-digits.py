class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def isValid(arr):
            if arr[2] > 5: return False
            if arr[0] > 2: return False
            if arr[0] == 2 and arr[1] > 3: return False
            return True

        def toMinutes(arr):
            return int(str(arr[-2]) + str(arr[-1])) + 60*int(str(arr[0]) + str(arr[1]))
        

        valid = [list(perm) for perm in permutations(arr) if isValid(list(perm))]
        if not valid: return ""
        mx = max(valid, key = lambda arr: toMinutes(arr))
        return f"{mx[0]}{mx[1]}:{mx[2]}{mx[3]}"


