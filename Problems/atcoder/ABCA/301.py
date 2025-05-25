n = int(input())
s = input()
w={"T":"A","A":"T"}
t,a = s.count("T"), s.count("A")
if t>a: print("T")
elif a>t: print("A")
else: print(w[s[-1]])

