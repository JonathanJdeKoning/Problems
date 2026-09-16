S = input()
T = input()

ans = len([a for a,b in zip(S, T) if a != b])
print(ans)