class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c = nums
        if not(a+b > c and a+c > b and b+c > a): return "none"
        if a==b==c: return "equilateral"
        if a!=b and b!=c and c!=a: return "scalene"
        return "isosceles"