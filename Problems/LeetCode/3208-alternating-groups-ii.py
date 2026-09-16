x=range
class Solution:
    def numberOfAlternatingGroups(_,c,k):
        s=n=len(c);a=r=0
        for i in x(n):s=[i,s][c[i]-c[i-1]]
        for i in x(n):r=[0,r+1][c[(s+i)%n]-c[(s+i-1)%n]];a+=r>k-2
        return[a,n][s==n]