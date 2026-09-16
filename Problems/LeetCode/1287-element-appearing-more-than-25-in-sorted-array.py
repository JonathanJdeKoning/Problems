class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = dict(Counter(arr))
        mx = max(count.values())
        for k, v in count.items():
            if v == mx:
                return k