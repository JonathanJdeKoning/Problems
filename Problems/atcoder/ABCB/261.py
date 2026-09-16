N = int(input())
M = []
for _ in range(N):
    M.append(input())

for i in range(N):
    for j in range(i+1, N):
        y = j
        x = i
        cell = M[i][j]

        if cell == "D" and M[y][x] != "D": exit(print("incorrect"))
        if cell == "W" and M[y][x] != "L": exit(print("incorrect"))
        if cell == "L" and M[y][x] != "W": exit(print("incorrect"))
print("correct")
    
