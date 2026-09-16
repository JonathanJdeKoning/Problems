class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr= sorted(arr)
        mn = inf
        out = []
        for i in range(len(arr)-1):
            pair = (arr[i], arr[i+1])
            mn = min(mn, pair[1]-pair[0])
        for i in range(len(arr)-1):
            pair = [arr[i], arr[i+1]]
            if pair[1] - pair[0] == mn:
                out.append(pair)
        return out
