class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        R, C = len(mat), len(mat[0])

        diags = defaultdict(list)
        for i in range(R):
            for j in range(C):
                diags[i+j].append(mat[i][j])
        ans = []
        for i in range(R+C):
            if i%2==0:
                diags[i] = diags[i][::-1]
            ans.extend(diags[i])
        return ans