class Solution:waysToSplitArray = lambda _,n:(p:=list(accumulate(n)))[0]*0 + sum([2*p[i] >= p[len(n)-1] for i in range(len(n)-1)])
