class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0]
        xor = 0
        for num in arr:
            xor ^= num
            pref.append(xor)
        ans = []
        for l, r in queries:
            ans.append(pref[r+1] ^ pref[l])
        return ans
        
