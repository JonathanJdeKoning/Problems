class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
        facts = factors(len(str1)).intersection(factors(len(str2)))

        mn, mx = sorted([str1, str2], key = lambda x: len(x))
        largest = ""
        for f in facts:
            s = mn[:f]

            str1inv = len(str1)//f
            str2inv = len(str2)//f

            if s*str1inv == str1 and s*str2inv == str2:
                if len(largest) < len(s):
                    largest = s
        return largest
        