class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        reel =  [list(g) for k, g in groupby(s)]

        mxo = 0
        mxz = 0
        for x in reel:
            if x[0] == "1": mxo = max(mxo,len(x))
            else: mxz = max(mxz,len(x))
        return mxo>mxz