class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        cols = list(zip(*grid[::-1]))
        for i in range(len(cols)):
            cols[i] = cols[i][::-1]
        ans = 0
        for col in cols:
            print(col)
            base = col[0]
            for num in col[1:]:
                if num <= base:
                    new = base+1
                    ans += abs(num-(base+1))

                else:
                    new = num
                base = new
        return ans