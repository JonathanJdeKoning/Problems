def part1(Q):
    mp= {k:k.swapcase() for k in "qwertyuiopasdfghjklmnbvcxzQWERTYUIOPASDFGHJKLZXCVBNM"}
    stack = []
    for c in Q:
        stack.append(c)
        while len(stack)> 1 and stack[-2] == mp[stack[-1]]:
            stack.pop()
            stack.pop()
    return len(stack)

def part2():
    return part1(min(["".join([c for c in P if c not in (x, x.upper())]) for x in "abcdefghijklmnopqrstuvwxyz"],key=part1))

if __name__ == "__main__":
    P = []

    with open("in.txt", "r") as file:
        P = file.readline().strip()
    N = len(P)
    print(part1(P))
    print(part2())