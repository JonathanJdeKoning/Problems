class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas) // 4
        i = 1
        pizzas.sort()
        #print(pizzas)
        ans = 0
        rest = 0
        for k in range(1, n+1):
            if k%2 ==1 :
                ans += pizzas.pop()
            else:
                rest += 1
        for _ in range(rest):
            pizzas.pop()
            ans += pizzas.pop()
        return ans
                
            