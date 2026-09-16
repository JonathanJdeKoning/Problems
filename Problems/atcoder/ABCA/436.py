N = int(input())
S = input()

need = max(0, N - len(S))
print("o"*need + S)
