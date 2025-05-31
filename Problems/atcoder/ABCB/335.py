ans = []
n = int(input())
b = list(range(22))
for i in b:
    for j in b:
        for k in b:
            if i+j+k <= n:
                ans.append(f"{i} {j} {k}")
import sys
for a in ans:
    sys.stdout.write(a+"\n")
