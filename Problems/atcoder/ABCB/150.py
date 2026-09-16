N = int(input())
S = input()

S = S.replace("ABC", "")

print((N - len(S))//3)