class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        N = len(words)
        def f(s):
            return s.count(min(list(s))) 
        words = sorted(list(map(f, words)))
        queries = list(map(f, queries))
        ans = []
        #print(words)
        #print(queries)
        def cond(x, q):
            return words[x] > q
        for q in queries:

            low = 0
            high = len(words) - 1

            while low < high:
                mid = (low+high)//2

                if cond(mid, q):
                    high = mid
                else:
                    low = mid+1
            if words[low] <= q: ans.append(0)
            else:
                ans.append(N-low)

        return ans
