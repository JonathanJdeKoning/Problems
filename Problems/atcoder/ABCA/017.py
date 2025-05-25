s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
s3, e3 = map(int, input().split())

ans = s1 * (e1/10)
ans += s2 *(e2/10)
ans += s3 * (e3/10)

print(int(ans))
