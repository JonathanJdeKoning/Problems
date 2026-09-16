def part1():
    return sum(P)
def part2():
    seen = set([0])
    curr = 0
    while True:
        for x in P:
            curr += x
            if curr in seen: return curr
            seen.add(curr)
if __name__ == "__main__":
    P = []
    with open("in.txt", "r") as file:
        for line in file.readlines():
            P.append(int(line.strip()))
    print(part1())
    print(part2())