from itertools import*
print(len(max([list(v)for k,v in groupby(input())],key=len)))