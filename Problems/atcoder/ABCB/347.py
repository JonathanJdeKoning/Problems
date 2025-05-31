s = input()
a = set()
for i in range(len(s)+1):
    for j in range(i+1, len(s)+1):
        a.add(s[i:j])
print(len(a))
