def part1():
    Q = P.copy()
    curr = 0
    steps = 0
    while curr in range(N):
        steps += 1
        Q[curr] += 1
        curr += Q[curr]-1
    return steps
def part2():
    Q = P.copy()
    curr = 0
    steps = 0
    while curr in range(N):
        steps += 1
        if Q[curr] >= 3:
            Q[curr] -= 1
            curr += Q[curr]+1
        else:
            Q[curr] += 1
            curr += Q[curr]-1
    return steps

if __name__ == "__main__":
    P = []

    with open("in.txt", "r") as file:
        for line in file.readlines():
            P.append(int(line.strip()))
    N = len(P)
    print(part1())
    print(part2())