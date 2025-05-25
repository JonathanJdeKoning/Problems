s = input()
t = input()

x =  0
for a,b in zip(s,t):
    if a==b: 
        x += 1
print(x)

