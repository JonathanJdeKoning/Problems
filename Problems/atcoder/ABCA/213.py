a,b = map(int, input().split())
for i in range(256):
    if a^i == b: print(i);break
