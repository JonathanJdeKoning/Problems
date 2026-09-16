K = int(input())
S = input()

if len(S) <= K:
    exit(print(S))

print(f"{S[:K]}...")