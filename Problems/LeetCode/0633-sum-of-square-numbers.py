class Solution:judgeSquareSum=lambda _,c:any(sqrt(c-x*x)%1==0 for x in range(isqrt(c)+1))
