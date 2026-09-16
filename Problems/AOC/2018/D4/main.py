
guards = {}
def part1():
    currGuard = None
    startSleep = None
    sleepiest = None
    sleepTime = 0
    for i in range(len(P)):
        op = P[i][-2]
        if op == "Guard":
            currGuard = P[i][-1]
            continue
        elif op == "falls":
            startSleep = P[i][4]
        elif op == "wakes":
            if currGuard not in guards:
                guards[currGuard] = [0]*60
            for j in range(startSleep, P[i][4]):
                guards[currGuard][j] += 1
            sleep = sum(guards[currGuard])
            if sleep > sleepTime:
                sleepTime = sleep
                sleepiest = currGuard
    
    mxMinute = max(guards[sleepiest])
    for i in range(60):
        if guards[sleepiest][i] == mxMinute:
            return sleepiest * i 


def part2():
    sleepiestMinute = None
    amt = 0
    guardID = None
    for guard in guards:
        for minute, sleep in enumerate(guards[guard]):
            if sleep > amt:
                amt = sleep
                guardID = guard
                sleepiestMinute = minute

    return sleepiestMinute*guardID
if __name__ == "__main__":
    P = []
    with open("in.txt", "r") as file:
        for line in file.readlines():
            data = line.split()
            date = data[0][1:]
            year,month,day = map(int, date.split("-"))
            time = data[1][:-1]
            hour, minute = map(int, time.split(":"))
            op = data[2]
            guard = None
            if op == "Guard":
                guard = int(data[3][1:])
            P.append((year,month,day,hour,minute, op, guard))
    P.sort()
    print(part1())
    print(part2())