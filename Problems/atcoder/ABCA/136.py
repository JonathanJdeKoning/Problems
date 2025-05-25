a,b,c = map(int, input().split())


left = a-b

c -=left
print(max(0, c))
