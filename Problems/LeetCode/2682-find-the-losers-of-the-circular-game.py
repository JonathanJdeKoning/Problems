class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        curr = 0
        seen = set([0])
        mul = 1
        while True:
            curr = (curr + k*mul)%n
            if curr in seen: break
            seen.add(curr)
            mul += 1

        losers = [i+1 for i in range(n) if i not in seen]
        return losers
