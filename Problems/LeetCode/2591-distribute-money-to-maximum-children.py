class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children: return -1
        ans = 0
        while children:
            if money - 8 < children-1: return ans
            money -= 8
            children -= 1
            ans += 1
            if children == 1 and money == 4:
                return ans-1
        if money:
            return ans-1
        else:
            return ans
            
            