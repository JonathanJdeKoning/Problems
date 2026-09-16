def computer(inputNum):
    P = Q.copy()
    P[1] = inputNum
    curr = 0
    argCount = 4
    while True:
        op = P[curr]
        if op == 99: return P[0]
        if op == 1:
            x, y, z = P[curr+1], P[curr+2], P[curr+3]
            a,b = P[x], P[y]
            P[z] = a+b
            argCount = 3
        elif op == 2:
            x, y, z = P[curr+1], P[curr+2], P[curr+3]
            a,b = P[x], P[y]
            P[z] = a*b
            argCount = 3
        elif op == 3:
            x = P[curr+1]
            
        curr += argCount + 1

def part1():
    return computer(1)
def part2():

if __name__ == "__main__":
    Q = []

    with open("in.txt", "r") as file:
        Q = list(map(int, file.readline().strip().split(",")))
    print(part1())
    print(part2())