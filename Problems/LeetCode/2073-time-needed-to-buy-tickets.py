class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        while True:
            for i, person in enumerate(tickets):
                
                if person > 0:
                    count += 1
                    tickets[i] -= 1
                    if i ==k :
                        if tickets[i] == 0:
                            return count    
