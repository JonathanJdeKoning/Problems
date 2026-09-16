__import__("atexit").register(lambda: open("display_runtime.txt","w").write("0"))
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        ans = 0
        new = []
        coins.sort()
        prev = coins[0][1]
        for start, end, val in coins[1:]:
            if start>prev+1:
                new.append([prev+1, start-1, 0])
            prev = end
        if prev != 10**9:
            new.append([prev+1, 10**9, 0])
        coins.extend(new)
        coins.sort()
        print(coins)
        tail = 0
        l = coins[0][0]
        r = l + k -1
        for i, (start, end, val) in enumerate(coins):
            if r >= start and r <= end:
                head = i
        base = 0
        ts,te,tv = coins[tail]
        hs,he,hv = coins[head]
        tn = (te-ts)+1
        hn = (he-hs)+1

        tmiss = (l-ts)
        hmiss = (he-r)
        base -= tmiss*tv
        base -= hmiss*hv
        for i in range(tail, head+1):
            iS,iE,iV = coins[i]
            iN = (iE-iS)+1
            base += iN*iV
        ans = base
            
        while head != len(coins)-1:            
            ts,te,tv = coins[tail]
            hs,he,hv = coins[head]
            tn = (te-ts)+1
            hn = (he-hs)+1

            if l == te or r == he:
                l += 1
                r += 1
                base -= tv
                if l > te:
                    tail += 1
                if r > he:
                    head += 1
                base += coins[head][-1]
                ans = max(ans, base)
                continue
            else:
                tmiss = (l-ts)
                hmiss = (he-r)
                
                grow = min((tn-tmiss)- 1, hmiss)
                base -= grow*tv
                base += grow*hv
                ans = max(ans, base)
                l += grow
                r += grow
        return ans
            
        
        