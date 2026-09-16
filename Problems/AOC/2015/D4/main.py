from hashlib import md5
def part1():
    for i in range(1, int(1e9)):
        h = md5(f"{key}{i}".encode()).hexdigest()
        if h[:5] == "00000":
            return i
def part2():
    for i in range(1, int(1e9)):
        h = md5(f"{key}{i}".encode()).hexdigest()
        if h[:6] == "000000":
            return i

if __name__ == "__main__":
    key = "yzbqklnj"

    print(part1())
    print(part2())