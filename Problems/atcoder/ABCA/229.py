mat = []
b = 0
for _ in range(2):
    mat.append(list(input()))

if mat == [[".","#"],["#","."]] or mat == [["#","."],[".","#"]]:
    print("No")
else:
    print("Yes")
