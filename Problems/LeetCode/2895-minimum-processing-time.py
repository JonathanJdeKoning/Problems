class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        ans = 0
        while processorTime:
            cpu = processorTime.pop()
            for _ in range(4):
                ans = max(ans, cpu + tasks.pop())
        return ans