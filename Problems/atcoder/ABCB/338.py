from collections import Counter
fq = Counter(input())
print(sorted([x for x in fq.keys() if fq[x] == max(fq.values())])[0])
