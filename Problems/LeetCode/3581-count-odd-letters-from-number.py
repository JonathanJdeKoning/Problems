class Solution:
    def countOddLetters(self, n: int) -> int:
        s = []
        mp = {
            "0": "zero",
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine"
        }
        for c in str(n):
            s.append(mp[c])
        fq = Counter(list("".join(s)))
        ans = 0
        for k, v in fq.items():
            if v %2 == 1:
                ans += 1
        return ans
