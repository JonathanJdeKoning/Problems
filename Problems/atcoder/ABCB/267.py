S = input()
standing = [1, 1, 2, 2, 2, 1, 1]
mp = {
    7: 0,
    4: 1,
    2: 2,
    8: 2,
    5: 3,
    1: 3,
    9: 4,
    3: 4,
    6: 5,
    10:6
}
if S[0] == "1": exit(print("No"))
for i, c in enumerate(S, start=1):
    if c == "0":
        standing[mp[i]] -= 1

standing = "".join(map(str, standing)).strip("0")
if "0" in standing:
    print("Yes")
else:
    print("No")
