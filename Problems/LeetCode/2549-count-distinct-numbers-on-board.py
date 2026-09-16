class Solution:
    def distinctIntegers(self, n: int) -> int:
        old = set()
        old.add(n)
        while True:
            oldlen = len(old)
            for num in list(old):
                for i in range(1,num+1):
                    if num%i == 1:
                        old.add(i)
            if len(old) == oldlen:
                return oldlen
