class Solution:
    def minMaxDifference(self, num: int) -> int:
        mnnum = str(num)
        mxnum = str(num)

        for c in mxnum:
            if c != "9":
                mxnum = mxnum.replace(c,"9")
                break
        for c in mnnum:
            if c != "0":
                mnnum = mnnum.replace(c,"0")
                break
        return int(mxnum) - int(mnnum)