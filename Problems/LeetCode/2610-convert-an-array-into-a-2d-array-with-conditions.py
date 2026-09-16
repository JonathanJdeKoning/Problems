class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        count = dict(Counter(nums))
        mat = []
        for _ in range(max(count.values())):
            mat.append([])
        for key, val in count.items():
            for i in range(val):
                mat[i-1].append(key)
        return mat