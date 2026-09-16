class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append((p,s))
        cars.sort()
        
        fleets = 0
        currentFleetTime = -inf
        while cars:
            p, s = cars.pop()
            distanceRemaining = target - p
            timeToTarget = distanceRemaining / s
            #print(p,s, timeToTarget)
            if timeToTarget > currentFleetTime:
                fleets += 1
                currentFleetTime = timeToTarget
            else:
                continue
        return fleets
