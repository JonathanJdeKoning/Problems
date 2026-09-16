class Solution:
    def countTime(self, time: str) -> int:
        res = 1
		# split hour and minute digits
        h1, h2, _ ,  m1, m2 = time
        
        if h1 == "?" and h2 == "?":
            res*=24
        elif h1 == "?":
            if int(h2) >=4:
                res*=2
            else:
                res*=3
                
        elif h2 == "?":
            if int(h1) <= 1:
                res*=10
            elif h1 == "2":
                res*=4
                
        if m1 == "?" and m2 == "?":
            res*=60
        elif m1 == "?":
            res*=6
        elif m2 == "?":
            res*=10
        
        return res
        