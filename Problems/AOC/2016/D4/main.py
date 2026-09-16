from collections import Counter
def part1():
    ans = 0
    for room in P:
        fq = Counter([c for c in room[:room.index("[")] if c.isalpha()])
        check = "".join([x[0] for x in sorted(fq.most_common(), key=lambda y:(-y[1],y[0]))[:5]])
        if check == room[-6:-1]:
            ID = int("".join([c for c in room if c.isdigit()]))
            ans += ID
    return ans
def part2():
    for room in P:
        R = list(room)
        ID = int("".join([c for c in room if c.isdigit()]))
        for i, c in enumerate(R):
            if not c.isalpha(): continue
            newC = chr((((ord(c)-ord("a")) + ID) % 26) + ord("a"))
            R[i]=newC
        if "northpole" in "".join(R):
            return ID

if __name__ == "__main__":
    P = []
    with open("in.txt", "r") as file:
        for line in file.readlines():
            P.append(line.strip())


    print(part1())
    print(part2())