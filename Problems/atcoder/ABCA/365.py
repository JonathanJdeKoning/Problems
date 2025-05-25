y = int(input())

if y%400==0:print(366);exit()
if y%100==0:print(365);exit()
if y%4==0:print(366);exit()
print(365)
