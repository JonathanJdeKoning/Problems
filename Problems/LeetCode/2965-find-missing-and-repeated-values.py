class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = set(range(1, n**2+1))
        found = []
        for i in range(n):
            for j in range(n):
                found.append(grid[i][j])
        fq = Counter(found)
        double = fq.most_common()[0][0]
        return [double, (nums - set(found)).pop()]

            
