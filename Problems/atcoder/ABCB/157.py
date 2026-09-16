card = [list(map(int, input().split())) for _ in range(3)]
N = int(input())

for _ in range(N):
    num = int(input())

    for i in range(3):
        for j in range(3):
            if card[i][j] == num:
                card[i][j] = "#"

for row in card:
    if row == ["#", "#", "#"]:
        exit(print("Yes"))

for j in range(3):
    col = [row[j] for row in card]
    if col == ["#","#","#"]:
        exit(print("Yes"))

if [card[0][0], card[1][1], card[2][2]] == ["#","#","#"]:
    exit(print("Yes"))

if [card[0][2], card[1][1], card[2][0]] == ["#","#","#"]:
    exit(print("Yes"))


print("No")