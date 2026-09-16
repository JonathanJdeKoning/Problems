class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        N = len(seats)
        ans = 0

        seats.sort()
        students.sort()

        for i in range(N):
            ans += abs(seats[i] - students[i])
        
        return ans



        