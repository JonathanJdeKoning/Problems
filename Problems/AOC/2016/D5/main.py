from hashlib import md5
def part1():
    ans = ""
    i = 0 
    while len(ans) != 8:
        h = md5(f"{P}{i}".encode()).hexdigest()
        if h[:5] == "00000":
            ans += h[5]
        i += 1
    return ans

def part2():
    ans = ["*","*","*","*","*","*","*","*"]
    i = 0 
    found = 0
    while found < 8:
        h = md5(f"{P}{i}".encode()).hexdigest()
        if h[:5] == "00000":
            if h[5] in "01234567" and ans[int(h[5])] == "*":
                ans[int(h[5])] = h[6]
                found += 1
        i += 1
    return "".join(ans)

if __name__ == "__main__":
    P = ""
    with open("in.txt", "r") as file:
        P = file.readline().strip()
    print(part1())
    print(part2())