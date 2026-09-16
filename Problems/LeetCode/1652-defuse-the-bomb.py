class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        new = []
        if k == 0: return [0]*len(code)
        if k >0:
            for i,num in enumerate(code):
                tot = 0
                for j in range(i+1,i+1+k):
                    tot += code[j%len(code)]
                new.append(tot)
        elif k <0:
            code = code[::-1]
            for i,num in enumerate(code):
                tot = 0
                for j in range(i+1,i+1+(-k)):
                    tot += code[j%len(code)]
                new.append(tot)
            new.reverse()
        return new
