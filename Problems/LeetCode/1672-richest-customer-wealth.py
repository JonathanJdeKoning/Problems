class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        total = 0
        for bank in accounts:
            total = 0
            for account in bank:
                total += account
            if total > maximum:
                maximum = total
        return maximum
