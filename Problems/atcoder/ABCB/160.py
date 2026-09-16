N = int(input())

ans = 0

ans += 1000 * (N//500)

N = N % 500
ans +=  5 * (N//5)
print(ans)