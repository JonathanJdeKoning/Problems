T = input()
P = input()

def Z(s):
    n = len(s)
    z = [0]*n
    z[0] = n
    l = 0
    r = 0
    for i in range(1, n):
        if (i < r):
            z[i] = min(r-i, z[i-l])
        
        while (i+z[i]<n and s[z[i]] == s[i+z[i]]):
            z[i] += 1

        if (i+z[i]>r):
            l = i
            r = i+z[i]
    return z

ZString = P + ">" + T
z = Z(ZString)
cnt = 0
pos = []
for i in range(len(z)):
    if z[i] == len(P):
        cnt += 1
        pos.append(i-len(P))
print(cnt)
if cnt >0:
    print(" ".join(list(map(str, pos))))