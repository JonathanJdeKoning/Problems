class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        final = []
        for num in range(1, n+1):
            new = ""
            if num % 3 == 0:
                new += "Fizz"
            if num % 5 == 0:
                new += "Buzz"
            if num % 5 != 0 and num % 3 != 0:
                final.append(str(num))
                continue
            final.append(new)
        return final