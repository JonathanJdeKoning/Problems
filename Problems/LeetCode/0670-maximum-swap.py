class Solution:
    def maximumSwap(self, num: int) -> int:
        best = "".join([str(x) for x in sorted([int(y) for y in str(num)], reverse=True)])
        num = str(num)
        for i in range(len(num)):
            if not num.startswith(best[:i+1]):
                correct = best[i]
                for j in range(len(num)):
                    if num[j] == correct:
                        swap = j

                num = list(num)
                num[i], num[swap] = num[swap], num[i]
                return int("".join(num))
        return int(num)