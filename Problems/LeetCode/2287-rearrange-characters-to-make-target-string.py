class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        need = {c:target.count(c) for c in target}
        have = {c:s.count(c) for c in s if c in target}
        return min([v//need[k] for k,v in have.items()]) if len(need) == len(have) else 0
            