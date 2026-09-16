def part1():
    return sum([x//3 - 2 for x in P])
def part2():
    ans = 0
    for p in P:
        while p > 0:
            p = max(0, p//3 -2)
            ans += p
    return ans
if __name__ == "__main__":
    P = []
    with open("in.txt", "r") as file:
        for line in file.readlines():
            P.append(int(line.strip()))
    print(part1())
    print(part2())