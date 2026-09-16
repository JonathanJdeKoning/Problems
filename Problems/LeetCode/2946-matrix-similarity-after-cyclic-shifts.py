class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        M = [deque(row) for row in mat]

        for i in range(len(mat)):
            if i % 2 ==0:
                M[i].rotate(k)
            else:
                M[i].rotate(-k)

        return mat == [list(row) for row in M]