class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        line = defaultdict(int)
        for start, end in logs:
            line[start] += 1
            line[end] -=1 
        mx = 0
        ans = None
        count = 0
        for k in sorted(line.keys()):
            count += line[k]
            if count > mx:
                mx = count
                ans = k

        return ans