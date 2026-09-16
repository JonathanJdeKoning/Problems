class Solution:
    def minOperations(self, logs: List[str]) -> int:
        e = 0
        for g in logs:
            if g == "../":
                if e > 0: 
                    e -=1
                else: continue
            elif g == "./": continue
            else: e += 1
        return e
