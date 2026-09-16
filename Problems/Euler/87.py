class Primes:
    def __init__(self, n):  # O(N)
        self.n = n
        self.primes = primes = []
        self.lp = lp = [0]*(n+1)
        self.phi = phi = [0]*(n+1)

        lp[1] = phi[1] = 1  # sig[1] = 1
        for i in range(2, n+1):
            if lp[i] == 0:
                lp[i] = i
                primes.append(i)
                phi[i] = i-1  # sig[i] = i+1
            for p in primes:
                if i*p > n: break
                lp[i*p] = p
                if lp[i] == p:
                    phi[i*p] = phi[i]*p  # sig[i*p] = sig[i]*(1+p) - sig[i//p]*p
                    break
                phi[i*p] = phi[i]*phi[p]

    def __getitem__(self, x):
        if isinstance(x, slice):  # O((W+sqR)lglgR)
            l, r = x.start or 0, x.stop
            P = [True]*(r-l)
            for i in range(2-l): P[i] = False
            for p in self.primes:
                if p*p > r: break
                for j in range(max(p*p, (l+p-1)//p*p), r, p):
                    P[j-l] = False
            return P
        if x < 2: return False
        if x <= self.n: return self.lp[x] == x  # O(1)
        for p in self.primes:  # O(sqX)
            if p*p > x: break
            if x%p == 0: return False
        return True

    def factorization(self, x):
        for p in self.primes:
            if p*p > x: break
            if x <= self.n: break
            if x%p == 0:
                cnt = 0
                while x%p == 0: cnt += 1; x //= p
                yield p, cnt
        while 1 < x <= self.n:
            p, cnt = self.lp[x], 0
            while x%p == 0: cnt += 1; x //= p
            yield p, cnt
        if x >= self.n and x > 1:
            yield x, 1

    def factors(self, x):
        res = [1]
        for p, b in self.factorization(x):
            n = len(res)
            for j in range(1, b+1):
                for d in res[:n]:
                    res.append(d * p**j)
        return res
p = Primes(85)
P = [i for i in range(86) if p[i]]
ans = set()
for sq in P:
    x = sq**2
    for tri in P:
        y=tri**3
        for fr in P:
            z=fr**4

            a = x+y+z
            ans.add(a)
print(len(ans))
            
