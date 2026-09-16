class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1], [1,1]]
        
    
        startn = 1
        
        for i in range(32):
            start = ans[startn]
            out = [1]
            for j in range(len(start)-1):
                out.append(start[j]+start[j+1])
            out.append(1)
            ans.append(out)
            startn += 1

        return ans[rowIndex]
                