def part1():
    return sum(1 for p in P if len(set(p)) == len(p))
def part2():
    return sum(1 for p in P if len(set(["".join(sorted(x)) for x in p])) == len(p))
if __name__ == "__main__":
    P = []
    with open("in.txt", "r") as file:
        for line in file.readlines():
            P.append(line.strip().split())
    print(part1())
    print(part2())