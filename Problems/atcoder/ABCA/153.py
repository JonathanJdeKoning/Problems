h,a = map(int, input().split())
total = 0
wack, left= divmod(h, a)
total +=wack 
if left != 0:
    total += 1
print(total)

