n,m = map(int, input().split())
m-=1
n -= 1
tot = 0

tot += (m*(m+1))//2
tot += (n*(n+1))//2

print(tot)
