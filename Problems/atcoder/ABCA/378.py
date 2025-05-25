from collections import Counter
fq = list(Counter(input().split()).values())
#print(fq)
if 3 in fq: exit(print("1"))
if fq.count(2) == 2:
    exit(print(2))
if fq == [4]:
    exit(print(2))
if fq.count(1) == 4:
    print(0)
else:
    print(1)
    

