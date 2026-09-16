G, W, H = map(int, input().split())
wallBlockingHammer = W in range(min(H, 0), max(0, H))
wallBlockingGoal = W in range(min(G, 0), max(0, G))
paritySame = H>0==G>0

if wallBlockingHammer and wallBlockingGoal: exit(print(-1))

if not paritySame and wallBlockingGoal:
    exit(print(abs(H) + abs(H-G)))

print(abs(G))




