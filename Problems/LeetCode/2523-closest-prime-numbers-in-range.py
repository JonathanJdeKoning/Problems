N = 1000000
sieve = [True]*(N+1)
sieve[1] = False
for i in range(2, int(sqrt(N))):
    if not sieve[i]: continue

    for j in range(i*i, N, i):
        sieve[j] = False

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        P = [i for i in range(left, right+1) if sieve[i]]
        start = 0
        best = 9999999
        ans = [-1,-1]
        while True:
            try:
                a,b = P[start], P[start + 1]
            except: break
            if b > right:
                break
            if b-a < best:
                best = b-a
                ans = [a,b]
            start += 1
        return ans
        
        