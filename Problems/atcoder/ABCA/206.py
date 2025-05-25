n = int(input())
from math import floor
price = floor(1.08 * n)

if price == 206:
    print("so-so")
elif price < 206:
    print("Yay!")
else:
    print(":(")
