def part1():
    for sy, sx , h, w in P:
        for i in range(h):
            for j in range(w):
                M[sy+i][sx+j] += 1
    ans = 0
    for row in M:
        for x in row:
            if x > 1:
                ans += 1
    return ans
def part2():
    for c, (sy, sx, h,w) in enumerate(P, start=1):
        good = True
        for i in range(h):
            if not good: break
            for j in range(w):
                if M[sy+i][sx+j] != 1:
                    good = False
                    break
        if good: return c
            
if __name__ == "__main__":
    P = []
    M = [[0]*1010 for _ in range(1010)]
    with open("in.txt", "r") as file:
        for line in file.readlines():
            data = line.strip().split()
            sy,sx = map(int, data[2][:-1].split(","))
            h,w = map(int, data[-1].split("x"))
            P.append((sy,sx,h,w))
    print(part1())
    print(part2())