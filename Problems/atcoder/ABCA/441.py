P, Q = map(int, input().split())
X, Y = map(int, input().split())
if X in range(P, P+100) and Y in range(Q, Q+100):
    print("Yes")
else: print("No")
