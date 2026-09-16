M = 998244353
A, B, C, D, E, F = map(int, input().split())
A, B, C, D, E, F = [x%M for x in [A, B, C, D, E, F]]

X = (A*B*C)%M
Y = (D*E*F)%M

print((X-Y)%M)

