import math
class Solution:
    def minimumPushes(self, word: str) -> int:
        def frequencySort(s):
            mpp = {}
            min_heap = []

            for ch in s:
                if ch in mpp:
                    mpp[ch] += 1
                else:
                    mpp[ch] = 1

            for m in mpp:
                heapq.heappush(min_heap, (mpp[m], m)) # as freq is 1st , char is 2nd

            ans = ""
            #Now we have in the TOP - Less Freq chars
            while min_heap:
                freq, ch = heapq.heappop(min_heap)
                ans += ch * freq # append as many times of freq
            return ans
        word = frequencySort(word)[::-1]
        total = 0
        seen = set()
        for c in word:
            total += math.floor(len(seen)/8) + 1
            seen.add(c)
        return total
            
        
                
            
            