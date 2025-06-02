s = list(input())

s.pop()

best = 5000
while s:
    if len(s)%2 == 1: 
        s.pop()
        continue
    mid = len(s) //2
    if s[:mid] == s[mid:]:
        exit(print(len(s)))
    s.pop()
print(best)