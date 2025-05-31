nums = []
while True:
    num = int(input())
    nums.append(num)
    if num==0: break

print("\n".join(map(str, nums[::-1])))
