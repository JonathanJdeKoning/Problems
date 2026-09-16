class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mp = {
            "6": "9",
            "9": "6",
            "0": "0",
            "1": "1",
            "8": "8",
            "2": "5",
            "5": "3"
        }
        new = "".join([mp.get(c, "!") for c in str(num)[::-1]])
        return new == num