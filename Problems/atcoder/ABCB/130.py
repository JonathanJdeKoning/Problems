N,X = list(map(int, input().split()))
L = list(map(int, input().split()))
pos = 0
bounces = 0
while pos <= X:
    bounces += 1
    try:
        pos += L[bounces-1]
    except: break
print(bounces) 