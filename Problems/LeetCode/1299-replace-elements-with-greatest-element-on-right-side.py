class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.reverse()
        mx = -1
        for i, num in enumerate(arr):
            arr[i] = mx
            mx = max(mx, num)
        arr.reverse()
        return arr
            
            
            
            