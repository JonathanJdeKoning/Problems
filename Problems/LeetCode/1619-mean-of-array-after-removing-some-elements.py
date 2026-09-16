class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        chop = ceil(len(arr)*0.05)
        arr = arr[chop:-chop]
        return sum(arr)/len(arr)
