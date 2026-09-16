l, r = list(map(int, input().split()))
S= input()
l -= 1
r -= 1
print(S[:l] + S[l:r+1][::-1] + S[r+1:])