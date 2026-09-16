pad1 = ["123","456","789"]
pad2 = ["XX1XX","X234X","56789","XABCX","XXDXX"]
mp={
    "R":(0,1),
    "L":(0,-1),
    "U":(-1,0),
    "D":(1,0)
}

def insertCode(pad, startY, startX):
    cy, cx = startY,startX
    N = len(pad)
    ans = []
    for line in P:
        for c in line:
            dy, dx = mp[c]
            ny,nx = cy+dy, cx+dx
            if ny not in range(N) or nx not in range(N): continue
            if pad[ny][nx] == "X":continue
            
            cy, cx = ny,nx
        ans.append(pad[cy][cx])
    return "".join(ans)


def part1(): return insertCode(pad1, 1, 1)
def part2(): return insertCode(pad2, 2, 0)

if __name__ == "__main__":
    P = []
    with open("in.txt", "r") as file:
        for line in file.readlines():
            P.append(line.strip())

    print(part1())
    print(part2())