N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = {x: i for i,x in enumerate(A)}
b = {x: i for i,x in enumerate(B)}

same = 0
diff = 0

for k in a:
    if k in b:
        if b[k] == a[k]:
            same += 1
        else:
            diff += 1
print(same) 
print(diff) 