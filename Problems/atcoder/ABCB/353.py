n,k = map(int, input().split())
a = list(map(int, input().split()))[::-1]

spots = k
ans = 0

while a:
    group = a.pop()
    if group <= spots:
        spots -= group
    else:
        a.append(group)
        ans += 1
        spots = k
print(ans+1)

