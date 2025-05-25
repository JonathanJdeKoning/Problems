H,W = map(int,input().split())
h, w = map(int, input().split())

total = H*W
total -= h*W
total -= (H-h)*w
print(total)
