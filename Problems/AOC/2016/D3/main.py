def isTriangle(a,b,c):
    return a+b>c and b+c>a and c+a>b
def part1():
    return sum(isTriangle(a,b,c) for a,b,c in P)
def part2():
    ROT = list(zip(*P))[::-1]
    ans = 0 
    for i in range(len(ROT)):
        for j in range(0,len(ROT[i])-2,3):
            a,b,c = ROT[i][j:j+3]
            if isTriangle(a,b,c):
                ans += 1
    return ans
if __name__ == "__main__":
    P = []
    with open("in.txt", "r") as file:
        for line in file.readlines():
            P.append(list(map(int, line.strip().split())))


    print(part1())
    print(part2())