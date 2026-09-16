class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        ans = 0
        A = [-a,-b,-c]
        heapify(A)

        while True:
            x = abs(heappop(A))
            y = abs(heappop(A))

            if not x or not y:
                break
            ans += 1
            heappush(A, -(x-1))
            heappush(A, -(y-1))
        return ans