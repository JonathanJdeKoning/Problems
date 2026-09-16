mp = {
    ">": (0,1),
    "<": (0,-1),
    "v": (1,0),
    "^": (-1,0)
}
def part1():
    seen = set()
    y,x = 0,0
    seen.add((y,x))
    for c in puzzle:
        dy, dx = mp[c]
        y, x = y+dy, x+dx
        seen.add((y,x))
    return len(seen)

def part2():
    seen = set()
    sy,sx = 0,0
    ry, rx = 0,0
    seen.add((0,0))
    for i,c in enumerate(puzzle):
        dy, dx = mp[c]
        if i%2==0:
            sy, sx = sy+dy, sx+dx
            seen.add((sy,sx))
        else:
            ry, rx = ry+dy, rx+dx
            seen.add((ry,rx))
    return len(seen)


if __name__ == "__main__":
    puzzle = None
    with open("in.txt", "r") as file:
        puzzle = file.readline().strip()

    print(part1())
    print(part2())