need = set(["H", "2B", "3B", "HR"])

for _ in range(4):
    need.discard(input())

if len(need) == 0:
    print("Yes")
else:
    print("No")