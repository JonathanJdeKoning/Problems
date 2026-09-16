class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        out = []
        ends = list(set([x for x in digits if x%2==0]))

        for end in ends:
            used = False
            new = digits[:]
            new.remove(end)
            for i in range(len(new)):
                for j in range(len(new)):
                    if new[i] == 0: continue
                    if i==j: continue

                    out.append(new[i]*100 + new[j]*10 + end)



        return sorted(list(set(out)))
