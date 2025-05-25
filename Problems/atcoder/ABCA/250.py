R,C = map(int, input().split())
i,j = map(int, input().split())
ans = 4
if R==1: ans -=1
if C== 1: ans -= 1
if i==R or i==1:  ans -=1
if j==C or j==1: ans -= 1
print(ans)
