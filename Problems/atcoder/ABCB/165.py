from math import floor
X = int(input())
bal = 100
years = 0
while True:
    years += 1
    bal = floor(1.01 * bal)

    if bal >= X:
        exit(print(years)) 