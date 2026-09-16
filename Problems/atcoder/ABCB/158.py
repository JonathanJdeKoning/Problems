N, A, B = list(map(int, input().split()))

T = A + B
full = N // T

ans = A * full

left = N - T*full

ans += min(left, A)
print(ans)