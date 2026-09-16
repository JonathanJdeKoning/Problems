from collections import defaultdict
def part1():
    ans = 0
    for word in words:
        vowelCount = 0
        doubled = False
        if "ab" in word or "cd" in word or "pq" in word or "xy" in word: continue
        if word[-1] in "aeiou": vowelCount += 1
        for i,c in enumerate(word[:-1]):
            if c in "aeiou": vowelCount += 1
            if c == word[i+1]:
                doubled = True
        if doubled and vowelCount >= 3:
            ans += 1
    return ans
def part2():
    ans = 0
    for word in words:
        double = False
        between = False
        pairs = defaultdict(list)
        for i in range(len(word)-2):
            if word[i] == word[i+2]:
                between = True
        for i in range(len(word)-1):
            pair = word[i:i+2]
            pairs[pair].append(i)
            if len(pairs[pair]) != 1:
                if i - pairs[pair][0] > 1:
                    double = True
        if between and double:
            ans += 1
    return ans
if __name__ == "__main__":
    words = []
    with open("in.txt", "r") as file:
        for line in file.readlines():
            words.append(line.strip())
    print(part1())
    print(part2())