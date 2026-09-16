class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        l = 0
        r = k
        threshold *= k
        base = sum(arr[:r]) 
        if base >= threshold: ans += 1
        while r < len(arr):
            base -= arr[l]
            base += arr[r]
            if base >= threshold: ans += 1
            l += 1
            r += 1
        return ans