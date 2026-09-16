N = int(input())
first = input()
seen = set([first])
need = first[-1]

for _ in range(N-1):
    word = input()
    if word in seen:
        exit(print("No"))
    if word[0] != need:
        exit(print("No"))
    need = word[-1]
    seen.add(word)

print("Yes")