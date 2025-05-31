s = input()
from collections import Counter
freq = Counter(s)

freqfreq = Counter(freq.values())
for i in range(len(s)):
    count = freqfreq[i+1]
    if count>0 and count != 2:
        print("No"); exit()
print("Yes")
