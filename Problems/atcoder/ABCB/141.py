S = input()

O = [S[i] for i in range(0, len(S), 2)]
E = [S[i] for i in range(1, len(S), 2)]

if "L" in O or "R" in E:
    print("No")
else:
    print("Yes")