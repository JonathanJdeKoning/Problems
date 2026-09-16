class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        fq = Counter(nums)
        heap = []

        for num, freq in fq.items():
            heappush(heap, (-freq, num))

        for _ in range(k):
            f, n = heappop(heap)
            ans.append(n)
        return ans

