
def Z(s):
    n = len(s)
    z = [0]*n
    l = 0
    r = 0
    for i in range(1, n):
        if (i < r):
            z[i] = min(r-i, z[i-1])
        
        while (i+z[i]<n and s[z[i]] == s[i+z[i]]):
            z[i] += 1

        if (i+z[i]>r):
            l = i
            r = i+z[i]
    return z

S = input()
z = Z(S)
print(" ".join(list(map(str, z))))