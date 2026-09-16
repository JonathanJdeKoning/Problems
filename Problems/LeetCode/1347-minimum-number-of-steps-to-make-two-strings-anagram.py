class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = dict(Counter(s))
        countt = dict(Counter(t))
        
        needed = 0
        for key, val in counts.items():
            if key not in countt:
                needed += val
            elif countt[key] < val:
                needed += val - countt[key]
        return needed