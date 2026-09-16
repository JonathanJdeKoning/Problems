from fractions import Fraction
N = int(input())

tot = Fraction(0,1)
A = list(map(int, input().split()))

for num in A:
    tot += Fraction(1, num)
print(float(Fraction(1, tot)))
