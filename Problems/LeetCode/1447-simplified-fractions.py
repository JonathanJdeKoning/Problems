class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        frac = set()
        for den in range(1,n+1):
            for num in range(1,den):
                top = num
                bot = den
                g = gcd(top, bot)
                while g != 1:
                    top //= g
                    bot //= g
                    g = gcd(top, bot)

                frac.add(f"{top}/{bot}")
        return list(frac)