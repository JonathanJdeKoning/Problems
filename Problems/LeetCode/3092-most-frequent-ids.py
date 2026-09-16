class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        d = defaultdict(int)
        st = SortedList()
        out = []
        for i in range(len(nums)):
            op = freq[i]
            num = nums[i]
            if d[num]: st.remove(d[num])
            d[num] += op
            if d[num]: st.add(d[num])
            out.append(st[-1] if st else 0)
        return(out)
            
            
        
        