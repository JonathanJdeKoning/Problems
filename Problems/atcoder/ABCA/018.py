a = int(input())
b = int(input())
c = int(input())

n = sorted([a,b,c], reverse=True)
ans = {}
for i in range(1,4):
    ans[n[i-1]] = i


print(ans[a])
print(ans[b])
print(ans[c])
