input()
print(" ".join(map(str, [x for x in list(map(int, input().split())) if x%2==0])))
