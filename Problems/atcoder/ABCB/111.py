N = int(input())
for i in range(N, 1112):
    if len(set(list(str(i)))) == 1:
        print(i)
        exit()