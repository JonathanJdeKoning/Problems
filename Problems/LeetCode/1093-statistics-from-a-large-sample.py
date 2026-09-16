class Solution:
    def sampleStats(self, count: List[int]) -> List[float]: 
        total, totalNums = 0, 0
        minimum, maximum = inf, 0
        mode, modeFQ = None, 0

        for num, fq in enumerate(count):
            if fq == 0: continue
            total += num * fq
            totalNums += fq
            minimum = min(minimum, num)
            maximum = max(maximum, num)
            if fq > modeFQ:
                mode = num
                modeFQ = fq

        mean = total / totalNums

        def kth(k):
            curr = 0
            ans = None
            for num, fq in enumerate(count):
                if fq + curr >= k:
                    return num
                curr += fq
        if totalNums%2 ==1:
            median = kth(1+(totalNums//2))
        else:
            median = (kth(totalNums//2) + kth((totalNums//2)+1)) /2
        return [
            float(minimum), float(maximum), float(mean), float(median), float(mode)]
        
            