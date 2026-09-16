x = None
with open("in.txt") as file:
    x = file.readline()

mp = {"(":1, ")":-1}

def part1():
    return sum(mp[c] for c in x)

def part2():
    count = 0
    for i,c in enumerate(x, start=1):
        count += mp[c]
        if count == -1:
            return i

print(part1())
print(part2())