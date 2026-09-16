class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        fq = defaultdict(int)
        
        for startIDX in range(len(s)):
            fq.clear()
            currIDX = startIDX
            while currIDX < len(s):
                char = s[currIDX]
                fq[char] += 1

                if fq[char] == k:
                    ans += len(s) - currIDX
                    break
                
                currIDX += 1
        return ans




