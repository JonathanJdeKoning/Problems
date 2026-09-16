class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        arr = list(range(1, m+1))
        for q in queries:
            for i, num in enumerate(arr):
                if q == num:
                    ans.append(i)
                    arr.pop(i)
                    arr = [num] + arr
                    break
        return ans