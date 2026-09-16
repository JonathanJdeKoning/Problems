def part1(i,j):
    P = Q.copy()
    P[1] = i
    P[2] = j
    curr = 0
    while True:
        op = P[curr]
        if op == 99: return P[0]
        x, y, z = P[curr+1], P[curr+2], P[curr+3]
        a,b = P[x], P[y]
        if op==1:
            P[z] = a+b
        else:
            P[z] = a*b
        curr += 4
def part2():
    for i in range(100):
        for j in range(100):
            if part1(i,j) == 19690720:
                return 100*i+j
if __name__ == "__main__":
    Q = None
    with open("in.txt", "r") as file:
        Q = list(map(int, file.readline().strip().split(",")))
    print(part1(12, 2))
    print(part2())