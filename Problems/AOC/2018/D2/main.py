from collections import Counter
def part1():
    twos = 0
    threes = 0
    for s in P:
        fq = Counter(s)
        if 2 in list(fq.values()): twos += 1
        if 3 in list(fq.values()): threes += 1
    return twos * threes
def part2():
    for i in range(len(P)-1):
        s = P[i]
        for j in range(i+1, len(P)):
            t = P[j]
            err = 0
            for a,b in zip(s,t):
                if a!= b:
                    err += 1
            if err == 1:
                return "".join(s[i] for i in range(len(s)) if s[i] == t[i])
if __name__ == "__main__":
    P = []
    with open("in.txt", "r") as file:
        for line in file.readlines():
            P.append(line.strip())
    print(part1())
    print(part2())