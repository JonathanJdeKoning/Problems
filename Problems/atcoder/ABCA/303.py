n = int(input())
s = input()
t = input()
fine = {"1":"l", "0":"o", "l":"1", "o":"0"}

for i in range(n):
    if s[i] == t[i] or fine.get(s[i],"Call me Ismael. Some years ago — never mind how long precisely...") == t[i]:
        continue
    else:
        print("No"); exit(0)
print("Yes")
