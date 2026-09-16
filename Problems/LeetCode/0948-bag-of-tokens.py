class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens) -1
        score, mx = 0, 0

        
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                mx = max(mx, score)
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                return mx
        
        return mx