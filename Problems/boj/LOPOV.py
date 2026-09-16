from heapq import heappush, heappop
from collections import Counter
numJewels, numBags = list(map(int, input().split()))
jewelArr = []
for _ in range(numJewels):
    jewelMass, jewelValue = list(map(int, input().split()))

bagMultiSet = Counter()
for _ in range(numBags):
    bagMaxMass = int(input())
    bagMultiSet[bagMaxMass] += 1

    
