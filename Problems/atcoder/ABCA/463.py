W, H = map(int, input().split())
for i in range(1000):
    if i*16 == W and i*9 == H:
        exit(print("Yes"))
print("No")
    
