
from itertools import *
from collections import *
ans = 0
ranges = True
R = []
def merge(intervals):
    intervals.sort()
    ans = [intervals[0]]

    for currStart, currEnd in intervals[1:]:
        prevEnd = ans[-1][-1]
        # If overlap
        if currStart <= prevEnd:
            ans[-1][-1] = max(currEnd, prevEnd)
        else:
            ans.append([currStart, currEnd])

    return ans

#with open("test.in","r") as file:
with open("data.in","r") as file:
    for line in file.readlines():
        x = line.strip()
        if not x: break

        R.append(list(map(int, x.split("-"))))
        A = merge(R)

for s, e in A:
    ans += e-s+1    
print(ans)
        
