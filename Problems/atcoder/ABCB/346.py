s = "wbwbwwbwbwbw"*20

ans = set()

for i in range(len(s)+1):
    for j in range(i+1, len(s)+1):
        ck = s[i:j]
        ans.add((ck.count("w"), ck.count("b")))
w,b = map(int, input().split())

if (w,b) in ans:
    print("Yes")
else:
    print("No")
