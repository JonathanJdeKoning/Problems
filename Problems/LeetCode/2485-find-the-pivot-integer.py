class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = list(range(1,n+1))
        for i, num in enumerate(arr):
            if sum(arr[:i+1]) == sum(arr[i:]):
                return i+1
        return -1