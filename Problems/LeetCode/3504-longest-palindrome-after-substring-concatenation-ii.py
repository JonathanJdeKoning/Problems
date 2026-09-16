class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def longest(x, y):
            return min((-len(x), x), (-len(y), y))[1]
        
        def buildTrie(s):
            trie = {}
            for i in range(len(s)):
                node = trie
                for j in range(i, len(s)):
                    node = node.setdefault(s[j], {})
            return trie
        
        def buildPalindrome(s1, s2):
            palin = ""
            for a, b in ((s1, s2), (s2[::-1], s1[::-1])):
                trie = buildTrie(b)
                n = len(a)
                for center in range(2*n-1, 0, -1):
                    mid1 = (center - 1)//2
                    mid2 = (center + 2)//2
                    left = next((left for left, right in zip(range(mid1, 0, -1), range(mid2, n)) 
                                 if a[left] != a[right]), 
                                max(0, mid1 + mid2 - n))
                    node = trie.get(a[left], None)
                    if node is not None:
                        for left in range(left-1, -1, -1):
                            if a[left] not in node:
                                left += 1
                                break
                            node = node[a[left]]                    
                    else: 
                        left = next((left for left in range(left+1, mid1+1) if a[left] in trie), None)
                        if left is None:
                            continue
                    palin = longest(a[left:mid2] + a[left:mid1+1][::-1], palin)
                        
            return palin or -1










        def longest2(text): 
            N = len(text) 
            if N == 0: 
                return
            if N == 1: return 1
            N = 2*N+1
            L = [0] * N 
            L[0] = 0
            L[1] = 1
            C = 1
            R = 2
            i = 0
            iMirror = 0
            maxLPSLength = 0
            maxLPSCenterPosition = 0
            start = -1
            end = -1
            diff = -1
        
            for i in range(2,N): 
               
                iMirror = 2*C-i 
                L[i] = 0
                diff = R - i 
                if diff > 0: 
                    L[i] = min(L[iMirror], diff) 
           
                try: 
                    while ((i+L[i]) < N and (i-L[i]) > 0) and (((i+L[i]+1) % 2 == 0) or (text[(i+L[i]+1)//2] == text[(i-L[i]-1)//2])): 
                        L[i]+=1
                except Exception as e: 
                    pass
           
                if L[i] > maxLPSLength:
                    maxLPSLength = L[i] 
                    maxLPSCenterPosition = i 
        
                if i + L[i] > R: 
                    C = i 
                    R = i + L[i] 
           
        
            start = (maxLPSCenterPosition - maxLPSLength) // 2
            end = start + maxLPSLength - 1
            return len(text[start:end+1]) 

        
        both = buildPalindrome(s,t)
        if both == -1: both = ""
        return max(len(both),longest2(s), longest2(t) )
        