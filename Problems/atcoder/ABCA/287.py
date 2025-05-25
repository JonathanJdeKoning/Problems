n = int(input())
q = [input() for _ in range(n)]
if q.count("For")> len(q)//2: print("Yes")
else:print("No")
