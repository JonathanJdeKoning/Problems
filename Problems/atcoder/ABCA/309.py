a,b = map(int, input().split())
ans = "No"
if b%3==0:
  if a ==b-1:
    ans = "Yes"
elif a in [1,4,7]:
  if b == a+1:
    ans = "Yes"
print(ans)
