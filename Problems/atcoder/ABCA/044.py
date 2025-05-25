n = int(input())
k = int(input())
x = int(input())
y = int(input())
t = 0

for i in range(n):
    if i <k:
        t +=x
    else:
        t += y
print(t)
