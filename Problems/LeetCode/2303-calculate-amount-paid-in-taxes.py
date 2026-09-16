class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total = 0
        init = income
        run = 0
        for bracket in brackets:
            upper = bracket[0] - run
            rate = bracket[1]

            if income <= upper:
                total += income-(income*(rate/100))
                break
            else:
                income -= upper
                total += upper-(upper*(rate/100))
                run=bracket[0]
        return init-total

