from itertools import permutations

dishes = [int(input()) for _ in range(5)]
best = int(1e9)
for perm in permutations([0,1,2,3,4]):
    time = 0
    for i, idx in enumerate(perm):
        time += dishes[idx]
        if dishes[idx] % 10 == 0 or i == 4: continue

        time += 10 - dishes[idx]%10
    best = min(time, best)    
print(best)