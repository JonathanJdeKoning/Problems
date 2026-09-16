A, B = list(map(int, input().split()))
if B == 1:
    exit(print(0))

socks = A
strips = 1

while socks < B:
    socks += A
    socks -= 1
    strips += 1
print(strips)