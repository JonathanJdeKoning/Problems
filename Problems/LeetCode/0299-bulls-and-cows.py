class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = list(secret)
        guess = list(guess)
        bulls = set()
        for i, (a,b) in enumerate(zip(secret, guess)):
            if a == b: bulls.add(i)

        secret = [x for i, x in enumerate(secret) if i not in bulls]
        guess = [x for i, x in enumerate(guess) if i not in bulls]

        secretFQ = Counter(secret)
        guessFQ = Counter(guess)

        cows = 0
        for k, v in guessFQ.items():
            if k not in secretFQ: continue
            cows += min(secretFQ[k], v)
        return f"{len(bulls)}A{cows}B"
