def part1():
    return sum(row[-1]-row[0] for row in P)
def part2():
    ans = 0
    for row in P:
        for i in range(len(row)-1):
            for j in range(i+1, len(row)):
                if row[j]%row[i] == 0:
                    ans += row[j]//row[i]
    return ans 
if __name__ == "__main__":
    P = []
    with open("in.txt", "r") as file:
        for line in file.readlines():
            P.append(sorted(map(int,line.strip().split())))
    print(part1())
    print(part2())