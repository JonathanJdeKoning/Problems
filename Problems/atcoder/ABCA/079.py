n = input()

for i in range(10):
    if str(i)*3 in n:
        print("Yes")
        break
else:
    print("No")
