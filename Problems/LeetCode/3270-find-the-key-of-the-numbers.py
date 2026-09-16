class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        
        num1 = str(num1).zfill(4)
        num2 = str(num2).zfill(4)
        num3 = str(num3).zfill(4)

        key = []
        print(num1, num2, num3)
        for i in range(4):
            key.append(str(min(int(num1[i]), int(num2[i]), int(num3[i]))))

        return int("".join(key))
