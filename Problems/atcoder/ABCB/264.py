R, C=  map(int, input().split())
R -= 1
C -= 1

M = 7

parity = max(abs(M-R), abs(M-C))

if parity%2==0:
    print("white")
else:
    print("black")
