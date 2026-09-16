N = int(input())


S = input().lower()

print("".join([chr((((ord(c) - 97) + N) % 26) + 97) for c in S]).upper())