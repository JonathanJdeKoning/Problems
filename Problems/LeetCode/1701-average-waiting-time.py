class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        fin = []
        curr = 0
        for start, time in customers:
            curr = max(curr, start)
            curr += time
            fin.append(curr)
            
        waits = [b-a for a,b in zip([c[0] for c in customers], fin)]
        return sum(waits) / len(waits)
