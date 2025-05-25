s = input()
from collections import Counter
c = Counter(s)
print(1+s.index(c.most_common(2)[1][0]))
