class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        new = arr[:]
    
        for i in range(len(arr)):
            arr.pop()
        for n in new:
            if n == 0:
                arr.append(0)
                arr.append(0)
            else:
                arr.append(n)
        for _ in range(len(arr)-len(new)):
            arr.pop()
        