class Solution:
    def customSortString(self, order: str, s: str) -> str:
        isIn, isOut = [],[]
        for c in s:
            if c in order:
                isIn.append(c)
            else:
                isOut.append(c)
        
        isIn.sort(key=lambda x: order.index(x))

        return "".join(isIn + isOut)


        