mp = {
    "U":(-1,0),
    "D": (1,0),
    "L": (0,-1),
    "R": (0,1)
}
def solve():
    time = {}
    seen = set()
    y,x = 0,0
    t = 0
    for d, n in P:
        dy,dx = mp[d]
        for _ in range(n):
            t += 1
            y += dy
            x += dx
            seen.add((y,x))
            if (y,x) not in time:
                time[(y,x)] = t
    ans1 = int(1e9)
    ans2 = int(1e9)
    y,x = 0,0
    t = 0 
    for d, n in Q:
        dy, dx = mp[d]
        for _ in range(n):
            t += 1
            y += dy
            x += dx
            if (y,x) in seen:
                ans1 = min(ans1, abs(y)+abs(x))
                ans2 = min(ans2, t+time[(y,x)])
    return ans1, ans2

            
if __name__ == "__main__":
    P = []
    Q = []
    with open("in.txt", "r") as file:
        P = [(x[0], int(x[1:])) for x in file.readline().strip().split(",")]
        Q = [(x[0], int(x[1:])) for x in file.readline().strip().split(",")]
    ans1, ans2 = solve()
    print(ans1, ans2, sep="\n")