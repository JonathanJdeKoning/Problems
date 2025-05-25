s = ""
n,x = map(int, input().split())
for i in range(26):
    s += chr(i+97)*n
print(s[x-1].upper())
