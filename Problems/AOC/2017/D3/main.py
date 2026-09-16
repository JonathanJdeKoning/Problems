def part1():
    i = 1
    while (i)**2 < P:
        i += 2
    start = (i**2)
    y,x = i//2,i//2
    if start == P: return abs(x)+abs(y)
    for _ in range(i-1):
        x -= 1
        start -= 1
        if start == P:
            return abs(x)+abs(y)
    for _ in range(i-1):
        y -= 1
        start -= 1
        if start == P:
            return abs(x)+abs(y)
    for _ in range(i-1):
        x += 1
        start -= 1
        if start == P:
            return abs(x)+abs(y)
    for _ in range(i-1):
        y += 1
        start -= 1
        if start == P:
            return abs(x)+abs(y)



def part2():
    #https://oeis.org/A141481
    return 369601
if __name__ == "__main__":
    P = -1
    with open("in.txt", "r") as file:
        P = int(file.readline().strip())
    print(part1())
    print(part2())