class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        goodTriplets = 0

        for i in range(0, len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    x, y, z = arr[i], arr[j], arr[k]

                    if abs(x-y) > a: continue 
                    if abs(y-z) > b: continue
                    if abs(x-z) > c: continue
                    
                    goodTriplets += 1
        return goodTriplets




