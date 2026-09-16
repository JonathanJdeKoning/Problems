class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np
        try:
            mat = np.reshape(mat, (r,c))
        except: pass
        return mat