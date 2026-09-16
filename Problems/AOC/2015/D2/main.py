def part1():
    totalPaper = 0
    for x,y,z in boxes:
        a,b,c = x*y, y*z, x*z
        totalPaper += 2*(a+b+c) + min(a,b,c)
    return totalPaper

def part2():
    totalRibbon = 0
    for x,y,z in boxes:
        totalRibbon += 2*(x+y)
        totalRibbon += x*y*z
    return totalRibbon


if __name__ == "__main__":
    boxes = []
    with open("in.txt", "r") as file:
        for line in file.readlines():
            boxes.append(sorted(list(map(int, line.split("x")))))

    print(part1())
    print(part2())