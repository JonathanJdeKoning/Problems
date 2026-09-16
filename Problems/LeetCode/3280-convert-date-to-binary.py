class Solution:
    def convertDateToBinary(self, date: str) -> str:
        a = map(lambda x: bin(int(x))[2:], date.split("-"))
        return "-".join(a)