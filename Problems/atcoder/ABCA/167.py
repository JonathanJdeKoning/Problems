s = input()
t = input()

if len(t) == len(s)+1 and t[:-1] == s: print("Yes")
else:
    print("No")
