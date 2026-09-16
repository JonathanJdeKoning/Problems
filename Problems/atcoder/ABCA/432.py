a,b,c = list(map(int, input().split()))


x = sorted([a,b,c], reverse=True)

print("".join(map(str, x)))