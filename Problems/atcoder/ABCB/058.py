from itertools import zip_longest
o = input()
e = input()
s = []
for a,b in zip_longest(o,e, fillvalue=""):
    s.append(a)
    s.append(b)
print("".join(s))