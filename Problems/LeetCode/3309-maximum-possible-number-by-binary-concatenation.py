class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        x,y,z= [bin(x)[2:] for x in nums]
        a = [x,y,z]
        b = [y,z,x]
        c = [x,z,y]
        d = [y,x,z]
        e = [z,x,y]
        f = [z,y,x]

        mx = 0

        for i in [a,b,c,d,e,f]:
            mx = max(mx, int("".join(i),2))
        return mx
