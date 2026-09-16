class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d = defaultdict(int)
        for i, num in enumerate(nums[:-1]):
            if num == key:
                d[nums[i+1]] += 1
        mx = max(d.values())
        for k in d.keys():
            if d[k] == mx: return k