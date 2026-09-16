from itertools import pairwise
curr = 0
cuts = [0]

N = int(input())

A = list(map(int, input().split()))

for num in A:
    curr = (curr+num) % 360
    cuts.append(curr)
cuts.sort()
print(max(360 - cuts[-1], max([b-a for a,b in pairwise(cuts)])))
