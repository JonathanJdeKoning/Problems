from fractions import Fraction

n,d = map(int, input().split())

print(str(Fraction(n,d)).replace("/", ":"))
