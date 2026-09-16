from itertools import groupby
from math import inf
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    bestCost = inf 
    
    itemsToLeft = 0
    itemsToRight = N
    
    for groupNum, groupList in groupby(A):
        groupSize = len(list(groupList))
        itemsToRight -= groupSize

        groupCost = groupNum * (itemsToLeft + itemsToRight)
        bestCost = min(bestCost, groupCost)
        
        itemsToLeft += groupSize
    return bestCost


for _ in range(int(input())):
    print(solve())