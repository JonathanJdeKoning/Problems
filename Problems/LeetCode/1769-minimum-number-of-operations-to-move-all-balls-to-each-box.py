class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        pos = [i for i in range(len(boxes)) if boxes[i] == "1"]
        for i in range(len(boxes)):
            tot = 0
            for p in pos:
                tot += abs(i-p)
            ans.append(tot)
        return ans
            
