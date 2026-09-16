class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        taken = [i for i,c in enumerate(seats) if c == 1]
        empties =[]
        if seats[0] == 0:
            empties.append(seats.index(1))
        if seats[-1] == 0:
            empties.append(seats[::-1].index(1))
        
        empties.extend([ceil(((b-a)-1)/2) for a,b in pairwise(taken)])
        
        return max(empties)
