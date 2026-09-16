from fractions import Fraction
N = 100
e = [2]
k = 1
for i in range(N-1):
    if i%3 == 1:
        e.append(2*k)
        k += 1
    else:
        e.append(1)
start = Fraction(1,e.pop())
for ee in e[::-1]:
    start = Fraction(1, ee+start)
print(sum(int(x) for x in str(start.denominator)))
