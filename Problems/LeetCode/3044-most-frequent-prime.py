class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        allem = []
        directions = [[-1,-1],[-1,1],[1,-1],[1,1],[0,1],[1,0],[0,-1],[-1,0]]
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        for i, row in enumerate(mat):
            for j, pos in enumerate(row):

                for dy, dx in directions:
                    y = i
                    x = j
                    holder = [str(pos)]
                    while True:

                        y += dy
                        x += dx

                        if y <= -1 or x <= -1 or y >= rows or x >= cols:
                            break
                        holder.append(str(mat[y][x]))
                    tot = "".join(holder)
                    for k in range(2,len(tot)+1):
                        try:
                            allem.append(int(tot[:k]))
                        except: pass
        count = dict(Counter(allem))
        mx = -1
        ans = -1
        for k, v in count.items():
            if v > mx:
                if is_prime(k):
                    mx = v
                    ans = k
            if v >= mx:
                if k > ans:
                    if is_prime(k):
                        mx = v
                        ans = k
            else:
                continue
        return ans 


                    
                
                