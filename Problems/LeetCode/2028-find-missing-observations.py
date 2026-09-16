class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        rollSum = sum(rolls)
        needSum = mean * (len(rolls) + n) - rollSum

        if needSum > n*6: return []
        if needSum < n: return []

        base = [1]*n

        need = needSum - n

        curr = 0
        while need:
            sub = min(5, need)
            base[curr] += sub
            need -= sub
            curr += 1
        return base
