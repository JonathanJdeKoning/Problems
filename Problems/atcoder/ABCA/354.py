pH = 0
tH = int(input())

days = 0
while True:
    pH += 2**days 
    if pH > tH: print(days+1); break
    days += 1
