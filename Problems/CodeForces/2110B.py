
def solve():
    s = input()
    x = 0
    for c in s[:-1]:
        if c == "(" : x += 1
        if c == ")" : x -= 1
        if x ==  0  : return "YES"
    return "NO"

for _ in range(int(input())): print(solve())
