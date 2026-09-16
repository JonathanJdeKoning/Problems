class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        def divisors(n):
            divs = [1]
            for i in range(2,int(math.sqrt(n))+1):
                if n%i == 0:
                    divs.extend([i,n/i])
            divs.extend([n])
            return list(set(divs))
        x = divisors(num)
        x.remove(num)
        return sum(x) == num