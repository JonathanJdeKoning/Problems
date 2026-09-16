class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = []

        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                heapq.heappush(h, (arr[i]/arr[j],(arr[i],arr[j])))
        ans = None
        for i in range(k):
            ans = heapq.heappop(h)
        return list(ans[1])