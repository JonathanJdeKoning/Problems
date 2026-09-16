class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ans = []
        if len(currentState) == 1: return []
        for i in range(len(currentState)-1):
            if currentState[i] == "+"  and currentState[i+1] == "+":
                
                ans.append(currentState[:i] + '-'*2 + currentState[i+2:])

        return ans
