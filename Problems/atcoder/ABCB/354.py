n,t,d=int(input()),0,[]
for _ in range(n):
    a,b=input().split()
    t+=int(b)
    d.append(a)
print(sorted(d)[t%n])
