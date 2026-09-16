import math
class Solution:
    def myAtoi(self, s: str) -> int:
        bad = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        white = " "
        t = ""
        gotem = False
        for c in s:
            if c == " ":
                if gotem:
                    break
            if c.isdigit() or c=="-" or c == "." or c == "+":
                gotem = True
                t+= c
            elif c in bad:
                if not gotem:
                    return 0
                else:
                    break
                   
                
        u = ""
        print(t)
        grace = True
        for c in t:
            if grace:
                u+=c
                grace = False
            elif not c.isdigit() and not grace:
                break
            elif c.isdigit():
                u+=c
        print(u)
        try:
            num = float(u)
        except: return 0
        
        if num.is_integer():
            num = int(num)
        else:
            num = int(math.floor(num))
        
        
        if num > 2**31 - 1:
            num = 2**31 - 1
        if num < -(2**31):
            num = -(2**31)
        return num