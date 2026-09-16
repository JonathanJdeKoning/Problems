class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        k = len(s) // k
        chunks = Counter([s[i:i+k] for i in range(0, len(s), k)])
        tchunks = [t[i:i+k] for i in range(0, len(t), k)]

        for c in tchunks:
            if chunks[c]:
                chunks[c] -= 1
            else:
                return False
        return True
