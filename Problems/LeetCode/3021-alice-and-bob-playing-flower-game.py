class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        mini = min(n,m)
        maxi = max(n,m)
        
        minodds = None
        minevens = None
        maxodds = None
        maxevens = None
        
        if mini %2 ==0:
            minodds = mini//2
            minevens = mini//2
        else:
            minodds = ((mini-1)//2)+1
            minevens = (mini-1)//2
        
        
        if maxi %2 ==0:
            maxodds = maxi//2
            maxevens = maxi//2
        else:
            maxodds = ((maxi-1)//2)+1
            maxevens = (maxi-1)//2
            
        total = 0
        print(minevens)
        print(minodds)

        print(maxevens)

        print(maxodds)

        for num in range(1,mini+1):
            if num%2==0:
                total += maxodds
            else:
                total += maxevens
        return total
            
            
            
            
            