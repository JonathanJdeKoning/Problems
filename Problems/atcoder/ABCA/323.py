s = input()
for i in range(2, len(s)+1, 2):
    if s[i-1]!="0":print("No");exit(0)
print("Yes")
