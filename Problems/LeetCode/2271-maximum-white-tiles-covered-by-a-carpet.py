class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        ans = 0
        new = []
        tiles.sort()
        tiles = [tile + [1] for tile in tiles ]

        prev = tiles[0][1]
        for start, end, val in tiles[1:]:
            if start>prev+1:
                new.append([prev+1, start-1, 0])
            prev = end
        if prev != 10**10:
            new.append([prev+1, 10**10, 0])
        tiles.extend(new)
        tiles.sort()
        tail = 0
        l = tiles[0][0]
        r = l + carpetLen -1
        print(tiles[:10])
        print(r)
        for i, (start, end, val) in enumerate(tiles):
            if r >= start and r <= end:
                head = i
        base = 0
        ts,te,tv = tiles[tail]
        hs,he,hv = tiles[head]
        tn = (te-ts)+1
        hn = (he-hs)+1

        tmiss = (l-ts)
        hmiss = (he-r)
        base -= tmiss*tv
        base -= hmiss*hv
        for i in range(tail, head+1):
            iS,iE,iV = tiles[i]
            iN = (iE-iS)+1
            base += iN*iV
        ans = base
            
        while head != len(tiles)-1:            
            ts,te,tv = tiles[tail]
            hs,he,hv = tiles[head]
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
                base += tiles[head][-1]
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
            