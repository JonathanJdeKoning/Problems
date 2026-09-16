class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        graph = defaultdict(list)
        ans = [0]*n
        for i in range(1,n+1):
            for j in range(1, n+1):
                dist = 0
                if i==j:continue
                
                if (i == x and j == y) or (i ==y and j == x):
                    ans[0] += 1
                    continue
                
                if (i<x<y<j) or (i<y<x<j):
                    dist = (abs(i-j) - abs(x-y))

                
                else:
                    
                    dist = abs(j-i)
                    dist = min(dist, abs(i-x)+1+abs(y-j))
                    dist = min(dist, abs(i-y)+1+abs(x-j))
                    dist = min(dist, abs(j-x)+1+abs(y-i))
                    dist = min(dist, abs(j-y)+1+abs(x-i))
                    dist -=1
                    
        
                ans[dist] += 1
                    
                    
        return ans                
            
        
                        
                        
                        
                        
                        
                        
                        
                        
                        