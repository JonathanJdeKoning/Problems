n,m = map(int, input().split())
probs = list(map(int, input().split()))
idxs = list(map(int, input().split()))
t = 0 
for i in idxs:
    t += probs[i-1]
print(t)
