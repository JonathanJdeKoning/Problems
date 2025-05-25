s = input()

ans = -1
for i, c in enumerate(s, start=1):
    if c =="a": ans = i
print(ans)
