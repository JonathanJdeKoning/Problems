N = input()
ans = 0
for c in N:
    ans += int(c)
if ans%9==0:
    print("Yes")
else:
    print("No")