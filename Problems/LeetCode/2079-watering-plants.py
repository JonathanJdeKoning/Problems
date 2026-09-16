class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 1
        curr = capacity
        def walk(i):
            curr = capacity
            return 2 * (i+1)

        i = 0
        while True:

            need = plants[i]
            waters = ceil(need / capacity)

            if waters == 1:
                curr -= need
            else:
                ans += walk(i) * (waters - 1)
                curr = need % capacity
            
            if i == len(plants) -1: return ans


            while i != len(plants) - 1 and curr >= plants[i + 1]:
                i += 1
                ans += 1
                curr -= plants[i]
            
            if i == len(plants) -1: return ans

            ans += walk(i)
            i += 1
            ans += 1
            curr = capacity




            
           
        return ans




