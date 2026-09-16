class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        one = 0
        two = 0
        for i, score in enumerate(player1):
            if i == 0 : 
                one += score
                continue
            if i == 1:
                if player1[0] == 10:
                    one += score*2
                    continue
                else: 
                    one += score 
                    continue
            check = [player1[i-1], player1[i-2]]
            if 10 in check: score*=2
            one += score


        for i, score in enumerate(player2):
            if i == 0 : 
                two += score
                continue
            if i == 1:
                if player2[0] == 10:
                    two += score*2
                    continue
                else:
                    two += score
                    continue
            check =[player2[i-1], player2[i-2]]
            if 10 in check: score*=2
            two += score
        if one > two: return 1
        if two > one: return 2
        return 0