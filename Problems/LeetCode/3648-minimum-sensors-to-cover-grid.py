class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        spread = 1 + 2 * k

        return  ceil(n / spread) * ceil(m / spread)