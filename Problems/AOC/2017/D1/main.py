def part1():
    return sum(int(P[i]) for i in range(N) if P[i] == P[(i+1)%N])
def part2():
    return sum(int(P[i]) for i in range(N) if P[i] == P[(i+N//2)%N])
if __name__ == "__main__":
    P = ""
    with open("in.txt", "r") as file:
        P = file.readline().strip()
    N = len(P)
    print(part1())
    print(part2())