N = int(input())
s, t= input().split()

new  =[]
for a,b in zip(s,t):
    new.append(a)
    new.append(b)
print("".join(new))