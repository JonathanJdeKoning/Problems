import numpy as np

res = {0: [[0]]}
for n in range(1, 11):
    m = 2 ** (2 * n) // 4
    q1 = np.array(res[n - 1])
    q2 = q1 + m
    q3 = q2 + m
    q4 = q3 + m
    res[n] = np.block([
        [q4, q1],
        [q3, q2]
    ]).tolist()


class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        return res[N]