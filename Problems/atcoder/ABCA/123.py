ant = []
for _ in range(5):
    ant.append(int(input()))
ant.sort()
k = int(input())

for i in range(5):
    for j in range(i,5):
        if ant[j] - ant[i] >k:
            print(":("); exit()
print("Yay!")
