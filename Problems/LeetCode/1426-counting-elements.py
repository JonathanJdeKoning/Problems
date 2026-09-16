class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set(arr)
        ans = 0
        for num in arr:
            if num + 1 in seen:
                ans += 1
        return ans