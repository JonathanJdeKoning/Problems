from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace("-", "+-")
        fractions = expression.split("+")
        fractions = [Fraction(x) for x in fractions if x]
        ans = sum(fractions)
        if ans.denominator == 1:
            return f"{ans}/1"
        else:
            return str(ans)