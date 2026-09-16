class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = dict(Counter(text))
        total = 0
        try:
            while count["b"] >0 and count["a"] > 0 and count["l"]>1 and count["o"] > 1 and count["n"]>0:
                total += 1
                count["b"] -=1
                count["a"] -=1
                count["l"] -=2
                count["o"] -= 2
                count["n"] -= 1
        except:pass
        return total