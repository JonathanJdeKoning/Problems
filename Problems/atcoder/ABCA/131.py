s = input()

for i in range(10):
    if str(i)+str(i) in s:
        print("Bad"); exit()
print("Good")
