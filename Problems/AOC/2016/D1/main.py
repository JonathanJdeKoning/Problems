mpL = {
    (-1,0):(0,-1),
    (0,-1):(1,0),
    (1,0):(0,1),
    (0,1):(-1,0)
}
mpR = {v:k for k,v in mpL.items()}
def part1():
    y, x = 0,0 
    dy, dx = -1,0
    for p in puzzle:
        if p[0] == "R":
            dy, dx = mpR[(dy, dx)]
        elif p[0] == "L":
            dy,dx = mpL[(dy,dx)]
        y += int(p[1:]) * dy
        x += int(p[1:]) * dx
    return (abs(y)+abs(x) )


def part2():
    seen = set([(0,0)])
    y, x = 0,0 
    dy, dx = -1,0
    for p in puzzle:
        if p[0] == "R":
            dy, dx = mpR[(dy, dx)]
        elif p[0] == "L":
            dy,dx = mpL[(dy,dx)]
        if dy != 0:
            for _ in range(int(p[1:])):
                y += dy
                if (y,x) in seen:
                    return abs(y)+abs(x)
                seen.add((y,x))
        if dx != 0:
            for _ in range(int(p[1:])):
                x += dx
                if (y,x) in seen:
                    return abs(y) + abs(x)
                seen.add((y,x))

if __name__ == "__main__":
    puzzle = None
    with open("in.txt", "r") as file:
        for line in file.readlines():
            puzzle = line.strip().split(", ")
    print(part1())
    print(part2())