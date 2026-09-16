class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        fq = Counter(tasks)
        h = [-x for x in fq.values()]
        heapify(h)
        q = deque()
        t = 0
        while h or q:
            while q and q[0][1] <= t:
                a,b = q.popleft()
                heappush(h, a)
            if h:
                mx = heappop(h)
                if mx != -1: 
                    q.append((mx+1, t+n+1))                         
            t+=1

        return t


