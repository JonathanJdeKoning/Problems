from itertools import groupby
def part1():
    ans = 0
    for i in range(P, Q+1):
        s = str(i)
        for c in "1234567890":
            if f"{c}{c}" in s: break
        else:
            continue
        if s == "".join(sorted(s)):
            ans += 1
    return ans
def part2():
    ans = 0
    for i in range(P, Q+1):
        s = str(i)
        g = groupby(s)
        for k, v in g:
            if len(list(v)) == 2: break
        else: continue
        if s == "".join(sorted(s)):
            ans += 1
    return ans

if __name__ == "__main__":
    P = None
    Q = None
    with open("in.txt", "r") as file:
        P, Q = map(int, file.readline().strip().split("-"))
    print(part1())
    print(part2())